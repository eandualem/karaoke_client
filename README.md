# karaoke_client

## Overview 🌐

The `karaoke_client` is designed to interact with the `AIProcessingService` of the Karaoke Scoring System, simulating real-time karaoke performance scoring. This client helps in testing the system by sending audio chunks and receiving scores.

## Getting Started 🚀

### Prerequisites 📋

- Docker installed on your machine.
- Access to the AWS EC2 instance with the Karaoke Scoring System deployed.
- `.pem` file for secure connection to the AWS EC2 instance.

### Installation and Setup 🛠️

#### 1. Clone the Repository:

```bash
git clone [repository-url]
cd karaoke_client
```

#### 2. Certificate Setup:

- Place your `certificate.pem` file in the root directory of `karaoke_client`.
- Ensure the certificate file name matches the one specified in your `.env` file.

The error you're encountering is due to a syntax issue in the Docker run command. It's attempting to find an image named 'proto', which doesn't exist. To resolve this, we should revert to the previous method you mentioned, which correctly uses the `grpc-builder` image to generate the protocol files. Here's the updated instruction for that part:

#### 3. Building Protocol Files:

1. **Clean the Generated Folder (if necessary):**

   Remove the existing `Generated` directory within the `proto` folder to ensure fresh generation of protocol files:

   ```bash
   rm -r ./proto/Generated
   ```

2. **Build the Docker Image for gRPC Generation:**

   Build the `grpc-builder` image using the `Dockerfile.grpcgen`:

   ```bash
   docker build -t grpc-builder -f Dockerfile.grpcgen .
   ```

3. **Generate Protocol Files:**

   Run a temporary container to generate the protocol files and copy them back to the host:

   ```bash
   docker run --name grpc-temp grpc-builder /bin/true
   docker cp grpc-temp:/app/Generated ./proto
   docker rm grpc-temp
   ```

#### 4. Build the Docker Image for the Client:

```bash
docker build -t karaoke-client -f Dockerfile.client .
```

#### 5. Configure Environment Variables:

Update the `.env` file with the appropriate values, especially the `SERVER_ADDRESS`.

Example `.env` content:

```
USER_LOCALE = "en"
AUTH_TOKEN = "token_placeholder"
CERT_FILE_PATH = "certificate.pem"
SERVER_ADDRESS = "ec2-16-171-36-141.eu-north-1.compute.amazonaws.com:50051"
```

### Running the Client 🔨

To run the client and connect it to the `AIProcessingService`:

```bash
docker run -it --rm --name karaoke-client karaoke-client
```

The client will start sending audio chunks and display the scoring results in real-time.

## Folder Structure 📂

```
karaoke_client/
├── Dockerfile.client
├── Dockerfile.grpcgen
├── README.md
├── certificate.pem
├── proto/
│   ├── Declarations/
│   ├── Generated/
│   ├── generate.sh
│   └── requirements_grpcgen.txt
├── requirements.txt
└── src/
    ├── __init__.py
    ├── ai_processing_service_client.py
    ├── client.py
    ├── logger.py
    └── request_builder.py
```
