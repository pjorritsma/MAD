# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shared/Worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='shared/Worker.proto',
    package='mapadroid.shared',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x13shared/Worker.proto\x12\x10mapadroid.shared\"\x16\n\x06Worker\x12\x0c\n\x04name\x18\x01 \x01(\tb\x06proto3'
)

_WORKER = _descriptor.Descriptor(
    name='Worker',
    full_name='mapadroid.shared.Worker',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='mapadroid.shared.Worker.name', index=0,
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
    serialized_start=41,
    serialized_end=63,
)

DESCRIPTOR.message_types_by_name['Worker'] = _WORKER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Worker = _reflection.GeneratedProtocolMessageType('Worker', (_message.Message,), {
    'DESCRIPTOR': _WORKER,
    '__module__': 'shared.Worker_pb2'
    # @@protoc_insertion_point(class_scope:mapadroid.shared.Worker)
})
_sym_db.RegisterMessage(Worker)

# @@protoc_insertion_point(module_scope)
