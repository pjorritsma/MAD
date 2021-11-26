# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mapping_manager/mapping_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='mapping_manager/mapping_manager.proto',
    package='mapadroid.mapping_manager',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%mapping_manager/mapping_manager.proto\x12\x19mapadroid.mapping_manager\"\x16\n\x06Worker\x12\x0c\n\x04name\x18\x01 \x01(\t\"[\n&IsRoutemanagerOfOriginLevelmodeRequest\x12\x31\n\x06worker\x18\x01 \x01(\x0b\x32!.mapadroid.mapping_manager.Worker\"?\n\'IsRoutemanagerOfOriginLevelmodeResponse\x12\x14\n\x0cis_levelmode\x18\x01 \x01(\x08\"S\n\x1eGetSafeItemsNotToDeleteRequest\x12\x31\n\x06worker\x18\x01 \x01(\x0b\x32!.mapadroid.mapping_manager.Worker\"3\n\x1fGetSafeItemsNotToDeleteResponse\x12\x10\n\x08item_ids\x18\x01 \x03(\x05\",\n*GetAllowedAuthenticationCredentialsRequest\"\xe5\x01\n+GetAllowedAuthenticationCredentialsResponse\x12{\n\x13\x61llowed_credentials\x18\x01 \x03(\x0b\x32^.mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry\x1a\x39\n\x17\x41llowedCredentialsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\x1aGetAllLoadedOriginsRequest\"5\n\x1bGetAllLoadedOriginsResponse\x12\x16\n\x0eloaded_origins\x18\x01 \x03(\t2\x8c\x05\n\x0eMappingManager\x12\xb4\x01\n#GetAllowedAuthenticationCredentials\x12\x45.mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsRequest\x1a\x46.mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse\x12\x84\x01\n\x13GetAllLoadedOrigins\x12\x35.mapadroid.mapping_manager.GetAllLoadedOriginsRequest\x1a\x36.mapadroid.mapping_manager.GetAllLoadedOriginsResponse\x12\x90\x01\n\x17GetSafeItemsNotToDelete\x12\x39.mapadroid.mapping_manager.GetSafeItemsNotToDeleteRequest\x1a:.mapadroid.mapping_manager.GetSafeItemsNotToDeleteResponse\x12\xa8\x01\n\x1fIsRoutemanagerOfOriginLevelmode\x12\x41.mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeRequest\x1a\x42.mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeResponseb\x06proto3'
)

_WORKER = _descriptor.Descriptor(
    name='Worker',
    full_name='mapadroid.mapping_manager.Worker',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='mapadroid.mapping_manager.Worker.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=68,
    serialized_end=90,
)

_ISROUTEMANAGEROFORIGINLEVELMODEREQUEST = _descriptor.Descriptor(
    name='IsRoutemanagerOfOriginLevelmodeRequest',
    full_name='mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='worker', full_name='mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeRequest.worker', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=92,
    serialized_end=183,
)

_ISROUTEMANAGEROFORIGINLEVELMODERESPONSE = _descriptor.Descriptor(
    name='IsRoutemanagerOfOriginLevelmodeResponse',
    full_name='mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='is_levelmode',
            full_name='mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeResponse.is_levelmode', index=0,
            number=1, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=185,
    serialized_end=248,
)

_GETSAFEITEMSNOTTODELETEREQUEST = _descriptor.Descriptor(
    name='GetSafeItemsNotToDeleteRequest',
    full_name='mapadroid.mapping_manager.GetSafeItemsNotToDeleteRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='worker', full_name='mapadroid.mapping_manager.GetSafeItemsNotToDeleteRequest.worker', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=250,
    serialized_end=333,
)

_GETSAFEITEMSNOTTODELETERESPONSE = _descriptor.Descriptor(
    name='GetSafeItemsNotToDeleteResponse',
    full_name='mapadroid.mapping_manager.GetSafeItemsNotToDeleteResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='item_ids', full_name='mapadroid.mapping_manager.GetSafeItemsNotToDeleteResponse.item_ids', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=335,
    serialized_end=386,
)

_GETALLOWEDAUTHENTICATIONCREDENTIALSREQUEST = _descriptor.Descriptor(
    name='GetAllowedAuthenticationCredentialsRequest',
    full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=388,
    serialized_end=432,
)

_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY = _descriptor.Descriptor(
    name='AllowedCredentialsEntry',
    full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry.key',
            index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry.value',
            index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=607,
    serialized_end=664,
)

_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE = _descriptor.Descriptor(
    name='GetAllowedAuthenticationCredentialsResponse',
    full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='allowed_credentials',
            full_name='mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.allowed_credentials',
            index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=435,
    serialized_end=664,
)

_GETALLLOADEDORIGINSREQUEST = _descriptor.Descriptor(
    name='GetAllLoadedOriginsRequest',
    full_name='mapadroid.mapping_manager.GetAllLoadedOriginsRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=666,
    serialized_end=694,
)

_GETALLLOADEDORIGINSRESPONSE = _descriptor.Descriptor(
    name='GetAllLoadedOriginsResponse',
    full_name='mapadroid.mapping_manager.GetAllLoadedOriginsResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='loaded_origins', full_name='mapadroid.mapping_manager.GetAllLoadedOriginsResponse.loaded_origins',
            index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=696,
    serialized_end=749,
)

_ISROUTEMANAGEROFORIGINLEVELMODEREQUEST.fields_by_name['worker'].message_type = _WORKER
_GETSAFEITEMSNOTTODELETEREQUEST.fields_by_name['worker'].message_type = _WORKER
_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY.containing_type = _GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE
_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE.fields_by_name[
    'allowed_credentials'].message_type = _GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY
DESCRIPTOR.message_types_by_name['Worker'] = _WORKER
DESCRIPTOR.message_types_by_name['IsRoutemanagerOfOriginLevelmodeRequest'] = _ISROUTEMANAGEROFORIGINLEVELMODEREQUEST
DESCRIPTOR.message_types_by_name['IsRoutemanagerOfOriginLevelmodeResponse'] = _ISROUTEMANAGEROFORIGINLEVELMODERESPONSE
DESCRIPTOR.message_types_by_name['GetSafeItemsNotToDeleteRequest'] = _GETSAFEITEMSNOTTODELETEREQUEST
DESCRIPTOR.message_types_by_name['GetSafeItemsNotToDeleteResponse'] = _GETSAFEITEMSNOTTODELETERESPONSE
DESCRIPTOR.message_types_by_name[
    'GetAllowedAuthenticationCredentialsRequest'] = _GETALLOWEDAUTHENTICATIONCREDENTIALSREQUEST
DESCRIPTOR.message_types_by_name[
    'GetAllowedAuthenticationCredentialsResponse'] = _GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE
DESCRIPTOR.message_types_by_name['GetAllLoadedOriginsRequest'] = _GETALLLOADEDORIGINSREQUEST
DESCRIPTOR.message_types_by_name['GetAllLoadedOriginsResponse'] = _GETALLLOADEDORIGINSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Worker = _reflection.GeneratedProtocolMessageType('Worker', (_message.Message,), {
    'DESCRIPTOR': _WORKER,
    '__module__': 'mapping_manager.mapping_manager_pb2'
    # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.Worker)
})
_sym_db.RegisterMessage(Worker)

IsRoutemanagerOfOriginLevelmodeRequest = _reflection.GeneratedProtocolMessageType(
    'IsRoutemanagerOfOriginLevelmodeRequest', (_message.Message,), {
        'DESCRIPTOR': _ISROUTEMANAGEROFORIGINLEVELMODEREQUEST,
        '__module__': 'mapping_manager.mapping_manager_pb2'
        # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeRequest)
    })
_sym_db.RegisterMessage(IsRoutemanagerOfOriginLevelmodeRequest)

IsRoutemanagerOfOriginLevelmodeResponse = _reflection.GeneratedProtocolMessageType(
    'IsRoutemanagerOfOriginLevelmodeResponse', (_message.Message,), {
        'DESCRIPTOR': _ISROUTEMANAGEROFORIGINLEVELMODERESPONSE,
        '__module__': 'mapping_manager.mapping_manager_pb2'
        # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.IsRoutemanagerOfOriginLevelmodeResponse)
    })
_sym_db.RegisterMessage(IsRoutemanagerOfOriginLevelmodeResponse)

GetSafeItemsNotToDeleteRequest = _reflection.GeneratedProtocolMessageType('GetSafeItemsNotToDeleteRequest',
                                                                          (_message.Message,), {
                                                                              'DESCRIPTOR': _GETSAFEITEMSNOTTODELETEREQUEST,
                                                                              '__module__': 'mapping_manager.mapping_manager_pb2'
                                                                              # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetSafeItemsNotToDeleteRequest)
                                                                          })
_sym_db.RegisterMessage(GetSafeItemsNotToDeleteRequest)

GetSafeItemsNotToDeleteResponse = _reflection.GeneratedProtocolMessageType('GetSafeItemsNotToDeleteResponse',
                                                                           (_message.Message,), {
                                                                               'DESCRIPTOR': _GETSAFEITEMSNOTTODELETERESPONSE,
                                                                               '__module__': 'mapping_manager.mapping_manager_pb2'
                                                                               # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetSafeItemsNotToDeleteResponse)
                                                                           })
_sym_db.RegisterMessage(GetSafeItemsNotToDeleteResponse)

GetAllowedAuthenticationCredentialsRequest = _reflection.GeneratedProtocolMessageType(
    'GetAllowedAuthenticationCredentialsRequest', (_message.Message,), {
        'DESCRIPTOR': _GETALLOWEDAUTHENTICATIONCREDENTIALSREQUEST,
        '__module__': 'mapping_manager.mapping_manager_pb2'
        # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsRequest)
    })
_sym_db.RegisterMessage(GetAllowedAuthenticationCredentialsRequest)

GetAllowedAuthenticationCredentialsResponse = _reflection.GeneratedProtocolMessageType(
    'GetAllowedAuthenticationCredentialsResponse', (_message.Message,), {

        'AllowedCredentialsEntry': _reflection.GeneratedProtocolMessageType('AllowedCredentialsEntry',
                                                                            (_message.Message,), {
                                                                                'DESCRIPTOR': _GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY,
                                                                                '__module__': 'mapping_manager.mapping_manager_pb2'
                                                                                # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry)
                                                                            })
        ,
        'DESCRIPTOR': _GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE,
        '__module__': 'mapping_manager.mapping_manager_pb2'
        # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetAllowedAuthenticationCredentialsResponse)
    })
_sym_db.RegisterMessage(GetAllowedAuthenticationCredentialsResponse)
_sym_db.RegisterMessage(GetAllowedAuthenticationCredentialsResponse.AllowedCredentialsEntry)

GetAllLoadedOriginsRequest = _reflection.GeneratedProtocolMessageType('GetAllLoadedOriginsRequest', (_message.Message,),
                                                                      {
                                                                          'DESCRIPTOR': _GETALLLOADEDORIGINSREQUEST,
                                                                          '__module__': 'mapping_manager.mapping_manager_pb2'
                                                                          # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetAllLoadedOriginsRequest)
                                                                      })
_sym_db.RegisterMessage(GetAllLoadedOriginsRequest)

GetAllLoadedOriginsResponse = _reflection.GeneratedProtocolMessageType('GetAllLoadedOriginsResponse',
                                                                       (_message.Message,), {
                                                                           'DESCRIPTOR': _GETALLLOADEDORIGINSRESPONSE,
                                                                           '__module__': 'mapping_manager.mapping_manager_pb2'
                                                                           # @@protoc_insertion_point(class_scope:mapadroid.mapping_manager.GetAllLoadedOriginsResponse)
                                                                       })
_sym_db.RegisterMessage(GetAllLoadedOriginsResponse)

_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE_ALLOWEDCREDENTIALSENTRY._options = None

_MAPPINGMANAGER = _descriptor.ServiceDescriptor(
    name='MappingManager',
    full_name='mapadroid.mapping_manager.MappingManager',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=752,
    serialized_end=1404,
    methods=[
        _descriptor.MethodDescriptor(
            name='GetAllowedAuthenticationCredentials',
            full_name='mapadroid.mapping_manager.MappingManager.GetAllowedAuthenticationCredentials',
            index=0,
            containing_service=None,
            input_type=_GETALLOWEDAUTHENTICATIONCREDENTIALSREQUEST,
            output_type=_GETALLOWEDAUTHENTICATIONCREDENTIALSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetAllLoadedOrigins',
            full_name='mapadroid.mapping_manager.MappingManager.GetAllLoadedOrigins',
            index=1,
            containing_service=None,
            input_type=_GETALLLOADEDORIGINSREQUEST,
            output_type=_GETALLLOADEDORIGINSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetSafeItemsNotToDelete',
            full_name='mapadroid.mapping_manager.MappingManager.GetSafeItemsNotToDelete',
            index=2,
            containing_service=None,
            input_type=_GETSAFEITEMSNOTTODELETEREQUEST,
            output_type=_GETSAFEITEMSNOTTODELETERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='IsRoutemanagerOfOriginLevelmode',
            full_name='mapadroid.mapping_manager.MappingManager.IsRoutemanagerOfOriginLevelmode',
            index=3,
            containing_service=None,
            input_type=_ISROUTEMANAGEROFORIGINLEVELMODEREQUEST,
            output_type=_ISROUTEMANAGEROFORIGINLEVELMODERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_MAPPINGMANAGER)

DESCRIPTOR.services_by_name['MappingManager'] = _MAPPINGMANAGER

# @@protoc_insertion_point(module_scope)
