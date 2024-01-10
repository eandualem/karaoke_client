# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Declarations.Model.AIProcessingService import AIProcessingRequest_pb2 as Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingRequest__pb2
from Declarations.Model.AIProcessingService import AIProcessingResponse_pb2 as Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingResponse__pb2


class AIProcessingServiceStub(object):
    """The service used by clients to connect with the PuglIA-developed back-end.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Process = channel.stream_stream(
                '/AIProcessingService/Process',
                request_serializer=Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingRequest__pb2.AIProcessingRequest.SerializeToString,
                response_deserializer=Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingResponse__pb2.AIProcessingResponse.FromString,
                )


class AIProcessingServiceServicer(object):
    """The service used by clients to connect with the PuglIA-developed back-end.
    """

    def Process(self, request_iterator, context):
        """The function used to process a chunk of audio data. The invocation requires two headers: Authorization, an opaque string provided by Lisari's back-end to the client; and User-Locale, the user's locale in ISO 639-1 Code format.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AIProcessingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Process': grpc.stream_stream_rpc_method_handler(
                    servicer.Process,
                    request_deserializer=Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingRequest__pb2.AIProcessingRequest.FromString,
                    response_serializer=Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingResponse__pb2.AIProcessingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AIProcessingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AIProcessingService(object):
    """The service used by clients to connect with the PuglIA-developed back-end.
    """

    @staticmethod
    def Process(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/AIProcessingService/Process',
            Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingRequest__pb2.AIProcessingRequest.SerializeToString,
            Declarations_dot_Model_dot_AIProcessingService_dot_AIProcessingResponse__pb2.AIProcessingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
