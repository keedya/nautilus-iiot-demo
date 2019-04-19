# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pravega/pravega.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pravega/pravega.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\"io.pravega.example.pravega_gatewayP\001'),
  serialized_pb=_b('\n\x15pravega/pravega.proto\"#\n\x12\x43reateScopeRequest\x12\r\n\x05scope\x18\x01 \x01(\t\"&\n\x13\x43reateScopeResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"4\n\x13\x43reateStreamRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\"\'\n\x14\x43reateStreamResponse\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"F\n\x11ReadEventsRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0e\n\x06stream\x18\x02 \x01(\t\x12\x12\n\ntimeout_ms\x18\x03 \x01(\x03\"e\n\x12ReadEventsResponse\x12\r\n\x05\x65vent\x18\x01 \x01(\x0c\x12\x10\n\x08position\x18\x02 \x01(\t\x12\x15\n\revent_pointer\x18\x03 \x01(\t\x12\x17\n\x0f\x63heckpoint_name\x18\x04 \x01(\t\"\x80\x01\n\x12WriteEventsRequest\x12\r\n\x05\x65vent\x18\x01 \x01(\x0c\x12\x13\n\x0brouting_key\x18\x02 \x01(\t\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x0e\n\x06stream\x18\x04 \x01(\t\x12\x17\n\x0fuse_transaction\x18\x05 \x01(\x08\x12\x0e\n\x06\x63ommit\x18\x06 \x01(\x08\"\x15\n\x13WriteEventsResponse2\x84\x02\n\x0ePravegaGateway\x12:\n\x0b\x43reateScope\x12\x13.CreateScopeRequest\x1a\x14.CreateScopeResponse\"\x00\x12=\n\x0c\x43reateStream\x12\x14.CreateStreamRequest\x1a\x15.CreateStreamResponse\"\x00\x12\x39\n\nReadEvents\x12\x12.ReadEventsRequest\x1a\x13.ReadEventsResponse\"\x00\x30\x01\x12<\n\x0bWriteEvents\x12\x13.WriteEventsRequest\x1a\x14.WriteEventsResponse\"\x00(\x01\x42&\n\"io.pravega.example.pravega_gatewayP\x01\x62\x06proto3')
)




_CREATESCOPEREQUEST = _descriptor.Descriptor(
  name='CreateScopeRequest',
  full_name='CreateScopeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='CreateScopeRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=25,
  serialized_end=60,
)


_CREATESCOPERESPONSE = _descriptor.Descriptor(
  name='CreateScopeResponse',
  full_name='CreateScopeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='CreateScopeResponse.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=62,
  serialized_end=100,
)


_CREATESTREAMREQUEST = _descriptor.Descriptor(
  name='CreateStreamRequest',
  full_name='CreateStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='CreateStreamRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='CreateStreamRequest.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=102,
  serialized_end=154,
)


_CREATESTREAMRESPONSE = _descriptor.Descriptor(
  name='CreateStreamResponse',
  full_name='CreateStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='CreateStreamResponse.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=156,
  serialized_end=195,
)


_READEVENTSREQUEST = _descriptor.Descriptor(
  name='ReadEventsRequest',
  full_name='ReadEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='ReadEventsRequest.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='ReadEventsRequest.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_ms', full_name='ReadEventsRequest.timeout_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=267,
)


_READEVENTSRESPONSE = _descriptor.Descriptor(
  name='ReadEventsResponse',
  full_name='ReadEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='ReadEventsResponse.event', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='ReadEventsResponse.position', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_pointer', full_name='ReadEventsResponse.event_pointer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_name', full_name='ReadEventsResponse.checkpoint_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=269,
  serialized_end=370,
)


_WRITEEVENTSREQUEST = _descriptor.Descriptor(
  name='WriteEventsRequest',
  full_name='WriteEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='WriteEventsRequest.event', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routing_key', full_name='WriteEventsRequest.routing_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='WriteEventsRequest.scope', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='WriteEventsRequest.stream', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_transaction', full_name='WriteEventsRequest.use_transaction', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit', full_name='WriteEventsRequest.commit', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=373,
  serialized_end=501,
)


_WRITEEVENTSRESPONSE = _descriptor.Descriptor(
  name='WriteEventsResponse',
  full_name='WriteEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=503,
  serialized_end=524,
)

DESCRIPTOR.message_types_by_name['CreateScopeRequest'] = _CREATESCOPEREQUEST
DESCRIPTOR.message_types_by_name['CreateScopeResponse'] = _CREATESCOPERESPONSE
DESCRIPTOR.message_types_by_name['CreateStreamRequest'] = _CREATESTREAMREQUEST
DESCRIPTOR.message_types_by_name['CreateStreamResponse'] = _CREATESTREAMRESPONSE
DESCRIPTOR.message_types_by_name['ReadEventsRequest'] = _READEVENTSREQUEST
DESCRIPTOR.message_types_by_name['ReadEventsResponse'] = _READEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['WriteEventsRequest'] = _WRITEEVENTSREQUEST
DESCRIPTOR.message_types_by_name['WriteEventsResponse'] = _WRITEEVENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateScopeRequest = _reflection.GeneratedProtocolMessageType('CreateScopeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESCOPEREQUEST,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:CreateScopeRequest)
  ))
_sym_db.RegisterMessage(CreateScopeRequest)

CreateScopeResponse = _reflection.GeneratedProtocolMessageType('CreateScopeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESCOPERESPONSE,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:CreateScopeResponse)
  ))
_sym_db.RegisterMessage(CreateScopeResponse)

CreateStreamRequest = _reflection.GeneratedProtocolMessageType('CreateStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTREAMREQUEST,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:CreateStreamRequest)
  ))
_sym_db.RegisterMessage(CreateStreamRequest)

CreateStreamResponse = _reflection.GeneratedProtocolMessageType('CreateStreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTREAMRESPONSE,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:CreateStreamResponse)
  ))
_sym_db.RegisterMessage(CreateStreamResponse)

ReadEventsRequest = _reflection.GeneratedProtocolMessageType('ReadEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _READEVENTSREQUEST,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:ReadEventsRequest)
  ))
_sym_db.RegisterMessage(ReadEventsRequest)

ReadEventsResponse = _reflection.GeneratedProtocolMessageType('ReadEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _READEVENTSRESPONSE,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:ReadEventsResponse)
  ))
_sym_db.RegisterMessage(ReadEventsResponse)

WriteEventsRequest = _reflection.GeneratedProtocolMessageType('WriteEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEEVENTSREQUEST,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:WriteEventsRequest)
  ))
_sym_db.RegisterMessage(WriteEventsRequest)

WriteEventsResponse = _reflection.GeneratedProtocolMessageType('WriteEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITEEVENTSRESPONSE,
  __module__ = 'pravega.pravega_pb2'
  # @@protoc_insertion_point(class_scope:WriteEventsResponse)
  ))
_sym_db.RegisterMessage(WriteEventsResponse)


DESCRIPTOR._options = None

_PRAVEGAGATEWAY = _descriptor.ServiceDescriptor(
  name='PravegaGateway',
  full_name='PravegaGateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=527,
  serialized_end=787,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateScope',
    full_name='PravegaGateway.CreateScope',
    index=0,
    containing_service=None,
    input_type=_CREATESCOPEREQUEST,
    output_type=_CREATESCOPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateStream',
    full_name='PravegaGateway.CreateStream',
    index=1,
    containing_service=None,
    input_type=_CREATESTREAMREQUEST,
    output_type=_CREATESTREAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadEvents',
    full_name='PravegaGateway.ReadEvents',
    index=2,
    containing_service=None,
    input_type=_READEVENTSREQUEST,
    output_type=_READEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteEvents',
    full_name='PravegaGateway.WriteEvents',
    index=3,
    containing_service=None,
    input_type=_WRITEEVENTSREQUEST,
    output_type=_WRITEEVENTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRAVEGAGATEWAY)

DESCRIPTOR.services_by_name['PravegaGateway'] = _PRAVEGAGATEWAY

# @@protoc_insertion_point(module_scope)
