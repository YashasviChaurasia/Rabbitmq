# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\"\xc9\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12#\n\x06phones\x18\x04 \x03(\x0b\x32\x13.Person.PhoneNumber\x1a\x44\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x11.Person.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"&\n\x0b\x41\x64\x64ressBook\x12\x17\n\x06people\x18\x01 \x03(\x0b\x32\x07.Person')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSON._serialized_start=15
  _PERSON._serialized_end=216
  _PERSON_PHONENUMBER._serialized_start=103
  _PERSON_PHONENUMBER._serialized_end=171
  _PERSON_PHONETYPE._serialized_start=173
  _PERSON_PHONETYPE._serialized_end=216
  _ADDRESSBOOK._serialized_start=218
  _ADDRESSBOOK._serialized_end=256
# @@protoc_insertion_point(module_scope)
