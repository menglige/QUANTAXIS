# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock.proto',
  package='stock',
  serialized_pb=_b('\n\x0bstock.proto\x12\x05stock\"\x97\x01\n\tstock_min\x12\x0c\n\x04high\x18\x01 \x02(\x02\x12\x0b\n\x03low\x18\x02 \x02(\x02\x12\x0c\n\x04open\x18\x03 \x02(\x02\x12\r\n\x05\x63lose\x18\x04 \x02(\x02\x12\x0e\n\x06volume\x18\x05 \x02(\x02\x12\x0f\n\x07\x62\x61rtime\x18\x06 \x02(\t\x12\x12\n\nbarendtime\x18\x07 \x02(\t\x12\x10\n\x08turnover\x18\x08 \x02(\x02\x12\x0b\n\x03\x64\x61y\x18\t \x02(\t\"0\n\nstock_info\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x10.stock.market_id:\x02sh*\x1b\n\tmarket_id\x12\x06\n\x02sh\x10\x00\x12\x06\n\x02sz\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MARKET_ID = _descriptor.EnumDescriptor(
  name='market_id',
  full_name='stock.market_id',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='sh', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sz', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=226,
  serialized_end=253,
)
_sym_db.RegisterEnumDescriptor(_MARKET_ID)

market_id = enum_type_wrapper.EnumTypeWrapper(_MARKET_ID)
sh = 0
sz = 1



_STOCK_MIN = _descriptor.Descriptor(
  name='stock_min',
  full_name='stock.stock_min',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='high', full_name='stock.stock_min.high', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='stock.stock_min.low', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='stock.stock_min.open', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='stock.stock_min.close', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='stock.stock_min.volume', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bartime', full_name='stock.stock_min.bartime', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='barendtime', full_name='stock.stock_min.barendtime', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turnover', full_name='stock.stock_min.turnover', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='stock.stock_min.day', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=174,
)


_STOCK_INFO = _descriptor.Descriptor(
  name='stock_info',
  full_name='stock.stock_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='stock.stock_info.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=224,
)

_STOCK_INFO.fields_by_name['type'].enum_type = _MARKET_ID
DESCRIPTOR.message_types_by_name['stock_min'] = _STOCK_MIN
DESCRIPTOR.message_types_by_name['stock_info'] = _STOCK_INFO
DESCRIPTOR.enum_types_by_name['market_id'] = _MARKET_ID

stock_min = _reflection.GeneratedProtocolMessageType('stock_min', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_MIN,
  __module__ = 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.stock_min)
  ))
_sym_db.RegisterMessage(stock_min)

stock_info = _reflection.GeneratedProtocolMessageType('stock_info', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_INFO,
  __module__ = 'stock_pb2'
  # @@protoc_insertion_point(class_scope:stock.stock_info)
  ))
_sym_db.RegisterMessage(stock_info)


# @@protoc_insertion_point(module_scope)
