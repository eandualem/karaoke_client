# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Declarations/Model/Report.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x44\x65\x63larations/Model/Report.proto\x1a\x1egoogle/protobuf/duration.proto\"\xd7\x01\n\x06Report\x12\x15\n\raverage_score\x18\x01 \x01(\x01\x12\"\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x02 \x03(\x0b\x32\x10.Report.Feedback\x1a\x91\x01\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x15\n\raverage_score\x18\x03 \x01(\x01\x12\x12\n\nai_comment\x18\x04 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Declarations.Model.Report_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPORT._serialized_start=68
  _REPORT._serialized_end=283
  _REPORT_FEEDBACK._serialized_start=138
  _REPORT_FEEDBACK._serialized_end=283
# @@protoc_insertion_point(module_scope)
