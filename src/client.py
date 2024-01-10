import os
import time
import grpc
import librosa
import tempfile
import numpy as np
import soundfile as sf
from logger import Logger
from dotenv import load_dotenv
from request_builder import RequestBuilder
from ai_processing_service_client import AIProcessingServiceClient


# Load environment variables from .env file
load_dotenv()

# Constants for configuration
USER_LOCALE = os.getenv("USER_LOCALE")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
CERT_FILE_PATH = os.getenv("CERT_FILE_PATH")
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")


class Client:
    def __init__(self):
        self.client_token = AUTH_TOKEN
        self.user_locale = USER_LOCALE
        self.client = AIProcessingServiceClient(server_address=SERVER_ADDRESS, cert_file=CERT_FILE_PATH)
        self.log = Logger.get_logger(__name__)

    def read_audio_data_from_file(self, file_path):
        """Read raw audio data from a file."""

        # Load the audio file with librosa, which will normalize the audio data to the range [-1, 1]
        audio_file_path = f"/app/{file_path}"
        audio_data, sr = librosa.load(audio_file_path, sr=8000)

        # Convert the normalized audio data to 16-bit PCM format
        audio_data_16bit = (audio_data * np.iinfo(np.int16).max).astype(np.int16)

        # Use a temporary file to write and then read the audio data
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            sf.write(temp_file.name, audio_data_16bit, sr)
            with open(temp_file.name, "rb") as f:
                return f.read()

    def build_requests(self):
        """Build requests for processing."""
        # Create Initialize request
        initialize_request = RequestBuilder.create_initialize_request(self.client_token)

        # Create AudioChunk requests
        audio_files = ["chunk0.wav", "chunk1.wav", "chunk2.wav", "chunk3.wav", "chunk4.wav"]

        audio_chunk_requests = [
            RequestBuilder.create_audio_chunk_request(self.read_audio_data_from_file(file)) for file in audio_files
        ]

        # Create Finalize request
        finalize_request = RequestBuilder.create_finalize_request(0)

        return [initialize_request] + audio_chunk_requests + [finalize_request]

    def process_requests(self, requests):
        """Process the provided requests and log responses."""
        self.log.info("Processing requests...")
        for response in self.client.process(requests, self.client_token, self.user_locale):
            self.log.info(f"Received response: {response}")
            time.sleep(25)

    def run(self):
        try:
            self.log.info("Initializing AIProcessingServiceClient...")
            requests = self.build_requests()
            self.process_requests(requests)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.UNAUTHENTICATED:
                self.log.error("Authentication failed with the AI Processing Service.")
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                self.log.error("AI Processing Service is currently unavailable.")
            elif e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                self.log.error("Request to the AI Processing Service timed out.")
            else:
                self.log.error(f"gRPC error occurred: {e.details()}")
        except Exception as e:
            self.log.error(f"An unexpected error occurred: {type(e).__name__} - {e}")

        self.log.info("Client run completed.")


if __name__ == "__main__":
    client = Client()
    client.run()
