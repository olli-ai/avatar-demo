# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixing_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14mixing_service.proto\x12\x06mixing\"\xdb\x01\n\rMixingRequest\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x14\n\x0cvoice_gender\x18\x04 \x01(\t\x12\x12\n\nvoice_name\x18\x05 \x01(\t\x12\x15\n\rdriving_style\x18\x06 \x01(\t\x12\x14\n\x0cuse_enhancer\x18\x07 \x01(\x08\x12\x15\n\rtarget_height\x18\x08 \x01(\x05\x12\x14\n\x0ctarget_width\x18\t \x01(\x05\x12\x13\n\x0btarget_size\x18\n \x01(\x05\"?\n\x0eMixingResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05video\x18\x02 \x01(\x0c\x12\x10\n\x08is_final\x18\x03 \x01(\x08\x32L\n\rMixingService\x12;\n\x08Generate\x12\x15.mixing.MixingRequest\x1a\x16.mixing.MixingResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mixing_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MIXINGREQUEST']._serialized_start=33
  _globals['_MIXINGREQUEST']._serialized_end=252
  _globals['_MIXINGRESPONSE']._serialized_start=254
  _globals['_MIXINGRESPONSE']._serialized_end=317
  _globals['_MIXINGSERVICE']._serialized_start=319
  _globals['_MIXINGSERVICE']._serialized_end=395
# @@protoc_insertion_point(module_scope)
