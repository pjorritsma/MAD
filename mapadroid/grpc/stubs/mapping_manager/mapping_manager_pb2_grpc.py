# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from mapadroid.grpc.compiled.mapping_manager import mapping_manager_pb2 as mapping__manager_dot_mapping__manager__pb2


class MappingManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllowedAuthenticationCredentials = channel.unary_unary(
            '/mapadroid.mapping_manager.MappingManager/GetAllowedAuthenticationCredentials',
            request_serializer=mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsRequest.SerializeToString,
            response_deserializer=mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsResponse.FromString,
        )
        self.GetAllLoadedOrigins = channel.unary_unary(
            '/mapadroid.mapping_manager.MappingManager/GetAllLoadedOrigins',
            request_serializer=mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsRequest.SerializeToString,
            response_deserializer=mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsResponse.FromString,
        )
        self.GetSafeItemsNotToDelete = channel.unary_unary(
            '/mapadroid.mapping_manager.MappingManager/GetSafeItemsNotToDelete',
            request_serializer=mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteRequest.SerializeToString,
            response_deserializer=mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteResponse.FromString,
        )
        self.IsRoutemanagerOfOriginLevelmode = channel.unary_unary(
            '/mapadroid.mapping_manager.MappingManager/IsRoutemanagerOfOriginLevelmode',
            request_serializer=mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeRequest.SerializeToString,
            response_deserializer=mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeResponse.FromString,
        )


class MappingManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllowedAuthenticationCredentials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllLoadedOrigins(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSafeItemsNotToDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsRoutemanagerOfOriginLevelmode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MappingManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAllowedAuthenticationCredentials': grpc.unary_unary_rpc_method_handler(
            servicer.GetAllowedAuthenticationCredentials,
            request_deserializer=mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsRequest.FromString,
            response_serializer=mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsResponse.SerializeToString,
        ),
        'GetAllLoadedOrigins': grpc.unary_unary_rpc_method_handler(
            servicer.GetAllLoadedOrigins,
            request_deserializer=mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsRequest.FromString,
            response_serializer=mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsResponse.SerializeToString,
        ),
        'GetSafeItemsNotToDelete': grpc.unary_unary_rpc_method_handler(
            servicer.GetSafeItemsNotToDelete,
            request_deserializer=mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteRequest.FromString,
            response_serializer=mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteResponse.SerializeToString,
        ),
        'IsRoutemanagerOfOriginLevelmode': grpc.unary_unary_rpc_method_handler(
            servicer.IsRoutemanagerOfOriginLevelmode,
            request_deserializer=mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeRequest.FromString,
            response_serializer=mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'mapadroid.mapping_manager.MappingManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MappingManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllowedAuthenticationCredentials(request,
                                            target,
                                            options=(),
                                            channel_credentials=None,
                                            call_credentials=None,
                                            insecure=False,
                                            compression=None,
                                            wait_for_ready=None,
                                            timeout=None,
                                            metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/mapadroid.mapping_manager.MappingManager/GetAllowedAuthenticationCredentials',
                                             mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsRequest.SerializeToString,
                                             mapping__manager_dot_mapping__manager__pb2.GetAllowedAuthenticationCredentialsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllLoadedOrigins(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/mapadroid.mapping_manager.MappingManager/GetAllLoadedOrigins',
                                             mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsRequest.SerializeToString,
                                             mapping__manager_dot_mapping__manager__pb2.GetAllLoadedOriginsResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSafeItemsNotToDelete(request,
                                target,
                                options=(),
                                channel_credentials=None,
                                call_credentials=None,
                                insecure=False,
                                compression=None,
                                wait_for_ready=None,
                                timeout=None,
                                metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/mapadroid.mapping_manager.MappingManager/GetSafeItemsNotToDelete',
                                             mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteRequest.SerializeToString,
                                             mapping__manager_dot_mapping__manager__pb2.GetSafeItemsNotToDeleteResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsRoutemanagerOfOriginLevelmode(request,
                                        target,
                                        options=(),
                                        channel_credentials=None,
                                        call_credentials=None,
                                        insecure=False,
                                        compression=None,
                                        wait_for_ready=None,
                                        timeout=None,
                                        metadata=None):
        return grpc.experimental.unary_unary(request, target,
                                             '/mapadroid.mapping_manager.MappingManager/IsRoutemanagerOfOriginLevelmode',
                                             mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeRequest.SerializeToString,
                                             mapping__manager_dot_mapping__manager__pb2.IsRoutemanagerOfOriginLevelmodeResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
