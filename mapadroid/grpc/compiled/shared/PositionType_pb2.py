# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shared/PositionType.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='shared/PositionType.proto',
    package='mapadroid.shared',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19shared/PositionType.proto\x12\x10mapadroid.shared*K\n\x0cPositionType\x12\n\n\x06NORMAL\x10\x00\x12\t\n\x05PRIOQ\x10\x01\x12\x0b\n\x07STARTUP\x10\x02\x12\n\n\x06REBOOT\x10\x03\x12\x0b\n\x07RESTART\x10\x04\x62\x06proto3'
)

_POSITIONTYPE = _descriptor.EnumDescriptor(
    name='PositionType',
    full_name='mapadroid.shared.PositionType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NORMAL', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='PRIOQ', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STARTUP', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='REBOOT', index=3, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='RESTART', index=4, number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=47,
    serialized_end=122,
)
_sym_db.RegisterEnumDescriptor(_POSITIONTYPE)

PositionType = enum_type_wrapper.EnumTypeWrapper(_POSITIONTYPE)
NORMAL = 0
PRIOQ = 1
STARTUP = 2
REBOOT = 3
RESTART = 4

DESCRIPTOR.enum_types_by_name['PositionType'] = _POSITIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

# @@protoc_insertion_point(module_scope)
