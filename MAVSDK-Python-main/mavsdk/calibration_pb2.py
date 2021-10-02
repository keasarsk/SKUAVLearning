# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calibration/calibration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='calibration/calibration.proto',
  package='mavsdk.rpc.calibration',
  syntax='proto3',
  serialized_options=b'\n\025io.mavsdk.calibrationB\020CalibrationProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x63\x61libration/calibration.proto\x12\x16mavsdk.rpc.calibration\x1a\x14mavsdk_options.proto\"\x1f\n\x1dSubscribeCalibrateGyroRequest\"\x9b\x01\n\x15\x43\x61librateGyroResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"(\n&SubscribeCalibrateAccelerometerRequest\"\xa4\x01\n\x1e\x43\x61librateAccelerometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\'\n%SubscribeCalibrateMagnetometerRequest\"\xa3\x01\n\x1d\x43\x61librateMagnetometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\'\n%SubscribeCalibrateLevelHorizonRequest\"\xa3\x01\n\x1d\x43\x61librateLevelHorizonResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\".\n,SubscribeCalibrateGimbalAccelerometerRequest\"\xaa\x01\n$CalibrateGimbalAccelerometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\x0f\n\rCancelRequest\"W\n\x0e\x43\x61ncelResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\"\xe2\x02\n\x11\x43\x61librationResult\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mavsdk.rpc.calibration.CalibrationResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xf6\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x0f\n\x0bRESULT_NEXT\x10\x02\x12\x11\n\rRESULT_FAILED\x10\x03\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x04\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x05\x12\x0f\n\x0bRESULT_BUSY\x10\x06\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x07\x12\x12\n\x0eRESULT_TIMEOUT\x10\x08\x12\x14\n\x10RESULT_CANCELLED\x10\t\x12\x17\n\x13RESULT_FAILED_ARMED\x10\n\"\x83\x01\n\x0cProgressData\x12\x1f\n\x0chas_progress\x18\x01 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x19\n\x08progress\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\"\n\x0fhas_status_text\x18\x03 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x13\n\x0bstatus_text\x18\x04 \x01(\t2\xac\x07\n\x12\x43\x61librationService\x12\x8a\x01\n\x16SubscribeCalibrateGyro\x12\x35.mavsdk.rpc.calibration.SubscribeCalibrateGyroRequest\x1a-.mavsdk.rpc.calibration.CalibrateGyroResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa5\x01\n\x1fSubscribeCalibrateAccelerometer\x12>.mavsdk.rpc.calibration.SubscribeCalibrateAccelerometerRequest\x1a\x36.mavsdk.rpc.calibration.CalibrateAccelerometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa2\x01\n\x1eSubscribeCalibrateMagnetometer\x12=.mavsdk.rpc.calibration.SubscribeCalibrateMagnetometerRequest\x1a\x35.mavsdk.rpc.calibration.CalibrateMagnetometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa2\x01\n\x1eSubscribeCalibrateLevelHorizon\x12=.mavsdk.rpc.calibration.SubscribeCalibrateLevelHorizonRequest\x1a\x35.mavsdk.rpc.calibration.CalibrateLevelHorizonResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xb7\x01\n%SubscribeCalibrateGimbalAccelerometer\x12\x44.mavsdk.rpc.calibration.SubscribeCalibrateGimbalAccelerometerRequest\x1a<.mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12]\n\x06\x43\x61ncel\x12%.mavsdk.rpc.calibration.CancelRequest\x1a&.mavsdk.rpc.calibration.CancelResponse\"\x04\x80\xb5\x18\x01\x42)\n\x15io.mavsdk.calibrationB\x10\x43\x61librationProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])



_CALIBRATIONRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.calibration.CalibrationResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NEXT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BUSY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_COMMAND_DENIED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CANCELLED', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_FAILED_ARMED', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1329,
  serialized_end=1575,
)
_sym_db.RegisterEnumDescriptor(_CALIBRATIONRESULT_RESULT)


_SUBSCRIBECALIBRATEGYROREQUEST = _descriptor.Descriptor(
  name='SubscribeCalibrateGyroRequest',
  full_name='mavsdk.rpc.calibration.SubscribeCalibrateGyroRequest',
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
  serialized_start=79,
  serialized_end=110,
)


_CALIBRATEGYRORESPONSE = _descriptor.Descriptor(
  name='CalibrateGyroResponse',
  full_name='mavsdk.rpc.calibration.CalibrateGyroResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CalibrateGyroResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_data', full_name='mavsdk.rpc.calibration.CalibrateGyroResponse.progress_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=113,
  serialized_end=268,
)


_SUBSCRIBECALIBRATEACCELEROMETERREQUEST = _descriptor.Descriptor(
  name='SubscribeCalibrateAccelerometerRequest',
  full_name='mavsdk.rpc.calibration.SubscribeCalibrateAccelerometerRequest',
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
  serialized_start=270,
  serialized_end=310,
)


_CALIBRATEACCELEROMETERRESPONSE = _descriptor.Descriptor(
  name='CalibrateAccelerometerResponse',
  full_name='mavsdk.rpc.calibration.CalibrateAccelerometerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CalibrateAccelerometerResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_data', full_name='mavsdk.rpc.calibration.CalibrateAccelerometerResponse.progress_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=313,
  serialized_end=477,
)


_SUBSCRIBECALIBRATEMAGNETOMETERREQUEST = _descriptor.Descriptor(
  name='SubscribeCalibrateMagnetometerRequest',
  full_name='mavsdk.rpc.calibration.SubscribeCalibrateMagnetometerRequest',
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
  serialized_start=479,
  serialized_end=518,
)


_CALIBRATEMAGNETOMETERRESPONSE = _descriptor.Descriptor(
  name='CalibrateMagnetometerResponse',
  full_name='mavsdk.rpc.calibration.CalibrateMagnetometerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CalibrateMagnetometerResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_data', full_name='mavsdk.rpc.calibration.CalibrateMagnetometerResponse.progress_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=521,
  serialized_end=684,
)


_SUBSCRIBECALIBRATELEVELHORIZONREQUEST = _descriptor.Descriptor(
  name='SubscribeCalibrateLevelHorizonRequest',
  full_name='mavsdk.rpc.calibration.SubscribeCalibrateLevelHorizonRequest',
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
  serialized_start=686,
  serialized_end=725,
)


_CALIBRATELEVELHORIZONRESPONSE = _descriptor.Descriptor(
  name='CalibrateLevelHorizonResponse',
  full_name='mavsdk.rpc.calibration.CalibrateLevelHorizonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CalibrateLevelHorizonResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_data', full_name='mavsdk.rpc.calibration.CalibrateLevelHorizonResponse.progress_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=728,
  serialized_end=891,
)


_SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST = _descriptor.Descriptor(
  name='SubscribeCalibrateGimbalAccelerometerRequest',
  full_name='mavsdk.rpc.calibration.SubscribeCalibrateGimbalAccelerometerRequest',
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
  serialized_start=893,
  serialized_end=939,
)


_CALIBRATEGIMBALACCELEROMETERRESPONSE = _descriptor.Descriptor(
  name='CalibrateGimbalAccelerometerResponse',
  full_name='mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress_data', full_name='mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse.progress_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=942,
  serialized_end=1112,
)


_CANCELREQUEST = _descriptor.Descriptor(
  name='CancelRequest',
  full_name='mavsdk.rpc.calibration.CancelRequest',
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
  serialized_start=1114,
  serialized_end=1129,
)


_CANCELRESPONSE = _descriptor.Descriptor(
  name='CancelResponse',
  full_name='mavsdk.rpc.calibration.CancelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibration_result', full_name='mavsdk.rpc.calibration.CancelResponse.calibration_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1131,
  serialized_end=1218,
)


_CALIBRATIONRESULT = _descriptor.Descriptor(
  name='CalibrationResult',
  full_name='mavsdk.rpc.calibration.CalibrationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.calibration.CalibrationResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.calibration.CalibrationResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CALIBRATIONRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1221,
  serialized_end=1575,
)


_PROGRESSDATA = _descriptor.Descriptor(
  name='ProgressData',
  full_name='mavsdk.rpc.calibration.ProgressData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_progress', full_name='mavsdk.rpc.calibration.ProgressData.has_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\005false', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='mavsdk.rpc.calibration.ProgressData.progress', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\003NaN', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_status_text', full_name='mavsdk.rpc.calibration.ProgressData.has_status_text', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\005false', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_text', full_name='mavsdk.rpc.calibration.ProgressData.status_text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1578,
  serialized_end=1709,
)

_CALIBRATEGYRORESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATEGYRORESPONSE.fields_by_name['progress_data'].message_type = _PROGRESSDATA
_CALIBRATEACCELEROMETERRESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATEACCELEROMETERRESPONSE.fields_by_name['progress_data'].message_type = _PROGRESSDATA
_CALIBRATEMAGNETOMETERRESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATEMAGNETOMETERRESPONSE.fields_by_name['progress_data'].message_type = _PROGRESSDATA
_CALIBRATELEVELHORIZONRESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATELEVELHORIZONRESPONSE.fields_by_name['progress_data'].message_type = _PROGRESSDATA
_CALIBRATEGIMBALACCELEROMETERRESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATEGIMBALACCELEROMETERRESPONSE.fields_by_name['progress_data'].message_type = _PROGRESSDATA
_CANCELRESPONSE.fields_by_name['calibration_result'].message_type = _CALIBRATIONRESULT
_CALIBRATIONRESULT.fields_by_name['result'].enum_type = _CALIBRATIONRESULT_RESULT
_CALIBRATIONRESULT_RESULT.containing_type = _CALIBRATIONRESULT
DESCRIPTOR.message_types_by_name['SubscribeCalibrateGyroRequest'] = _SUBSCRIBECALIBRATEGYROREQUEST
DESCRIPTOR.message_types_by_name['CalibrateGyroResponse'] = _CALIBRATEGYRORESPONSE
DESCRIPTOR.message_types_by_name['SubscribeCalibrateAccelerometerRequest'] = _SUBSCRIBECALIBRATEACCELEROMETERREQUEST
DESCRIPTOR.message_types_by_name['CalibrateAccelerometerResponse'] = _CALIBRATEACCELEROMETERRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeCalibrateMagnetometerRequest'] = _SUBSCRIBECALIBRATEMAGNETOMETERREQUEST
DESCRIPTOR.message_types_by_name['CalibrateMagnetometerResponse'] = _CALIBRATEMAGNETOMETERRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeCalibrateLevelHorizonRequest'] = _SUBSCRIBECALIBRATELEVELHORIZONREQUEST
DESCRIPTOR.message_types_by_name['CalibrateLevelHorizonResponse'] = _CALIBRATELEVELHORIZONRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeCalibrateGimbalAccelerometerRequest'] = _SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST
DESCRIPTOR.message_types_by_name['CalibrateGimbalAccelerometerResponse'] = _CALIBRATEGIMBALACCELEROMETERRESPONSE
DESCRIPTOR.message_types_by_name['CancelRequest'] = _CANCELREQUEST
DESCRIPTOR.message_types_by_name['CancelResponse'] = _CANCELRESPONSE
DESCRIPTOR.message_types_by_name['CalibrationResult'] = _CALIBRATIONRESULT
DESCRIPTOR.message_types_by_name['ProgressData'] = _PROGRESSDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeCalibrateGyroRequest = _reflection.GeneratedProtocolMessageType('SubscribeCalibrateGyroRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECALIBRATEGYROREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.SubscribeCalibrateGyroRequest)
  })
_sym_db.RegisterMessage(SubscribeCalibrateGyroRequest)

CalibrateGyroResponse = _reflection.GeneratedProtocolMessageType('CalibrateGyroResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATEGYRORESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrateGyroResponse)
  })
_sym_db.RegisterMessage(CalibrateGyroResponse)

SubscribeCalibrateAccelerometerRequest = _reflection.GeneratedProtocolMessageType('SubscribeCalibrateAccelerometerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECALIBRATEACCELEROMETERREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.SubscribeCalibrateAccelerometerRequest)
  })
_sym_db.RegisterMessage(SubscribeCalibrateAccelerometerRequest)

CalibrateAccelerometerResponse = _reflection.GeneratedProtocolMessageType('CalibrateAccelerometerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATEACCELEROMETERRESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrateAccelerometerResponse)
  })
_sym_db.RegisterMessage(CalibrateAccelerometerResponse)

SubscribeCalibrateMagnetometerRequest = _reflection.GeneratedProtocolMessageType('SubscribeCalibrateMagnetometerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECALIBRATEMAGNETOMETERREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.SubscribeCalibrateMagnetometerRequest)
  })
_sym_db.RegisterMessage(SubscribeCalibrateMagnetometerRequest)

CalibrateMagnetometerResponse = _reflection.GeneratedProtocolMessageType('CalibrateMagnetometerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATEMAGNETOMETERRESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrateMagnetometerResponse)
  })
_sym_db.RegisterMessage(CalibrateMagnetometerResponse)

SubscribeCalibrateLevelHorizonRequest = _reflection.GeneratedProtocolMessageType('SubscribeCalibrateLevelHorizonRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECALIBRATELEVELHORIZONREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.SubscribeCalibrateLevelHorizonRequest)
  })
_sym_db.RegisterMessage(SubscribeCalibrateLevelHorizonRequest)

CalibrateLevelHorizonResponse = _reflection.GeneratedProtocolMessageType('CalibrateLevelHorizonResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATELEVELHORIZONRESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrateLevelHorizonResponse)
  })
_sym_db.RegisterMessage(CalibrateLevelHorizonResponse)

SubscribeCalibrateGimbalAccelerometerRequest = _reflection.GeneratedProtocolMessageType('SubscribeCalibrateGimbalAccelerometerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.SubscribeCalibrateGimbalAccelerometerRequest)
  })
_sym_db.RegisterMessage(SubscribeCalibrateGimbalAccelerometerRequest)

CalibrateGimbalAccelerometerResponse = _reflection.GeneratedProtocolMessageType('CalibrateGimbalAccelerometerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATEGIMBALACCELEROMETERRESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse)
  })
_sym_db.RegisterMessage(CalibrateGimbalAccelerometerResponse)

CancelRequest = _reflection.GeneratedProtocolMessageType('CancelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELREQUEST,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CancelRequest)
  })
_sym_db.RegisterMessage(CancelRequest)

CancelResponse = _reflection.GeneratedProtocolMessageType('CancelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELRESPONSE,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CancelResponse)
  })
_sym_db.RegisterMessage(CancelResponse)

CalibrationResult = _reflection.GeneratedProtocolMessageType('CalibrationResult', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATIONRESULT,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.CalibrationResult)
  })
_sym_db.RegisterMessage(CalibrationResult)

ProgressData = _reflection.GeneratedProtocolMessageType('ProgressData', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSDATA,
  '__module__' : 'calibration.calibration_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.calibration.ProgressData)
  })
_sym_db.RegisterMessage(ProgressData)


DESCRIPTOR._options = None
_PROGRESSDATA.fields_by_name['has_progress']._options = None
_PROGRESSDATA.fields_by_name['progress']._options = None
_PROGRESSDATA.fields_by_name['has_status_text']._options = None

_CALIBRATIONSERVICE = _descriptor.ServiceDescriptor(
  name='CalibrationService',
  full_name='mavsdk.rpc.calibration.CalibrationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1712,
  serialized_end=2652,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeCalibrateGyro',
    full_name='mavsdk.rpc.calibration.CalibrationService.SubscribeCalibrateGyro',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBECALIBRATEGYROREQUEST,
    output_type=_CALIBRATEGYRORESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeCalibrateAccelerometer',
    full_name='mavsdk.rpc.calibration.CalibrationService.SubscribeCalibrateAccelerometer',
    index=1,
    containing_service=None,
    input_type=_SUBSCRIBECALIBRATEACCELEROMETERREQUEST,
    output_type=_CALIBRATEACCELEROMETERRESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeCalibrateMagnetometer',
    full_name='mavsdk.rpc.calibration.CalibrationService.SubscribeCalibrateMagnetometer',
    index=2,
    containing_service=None,
    input_type=_SUBSCRIBECALIBRATEMAGNETOMETERREQUEST,
    output_type=_CALIBRATEMAGNETOMETERRESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeCalibrateLevelHorizon',
    full_name='mavsdk.rpc.calibration.CalibrationService.SubscribeCalibrateLevelHorizon',
    index=3,
    containing_service=None,
    input_type=_SUBSCRIBECALIBRATELEVELHORIZONREQUEST,
    output_type=_CALIBRATELEVELHORIZONRESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeCalibrateGimbalAccelerometer',
    full_name='mavsdk.rpc.calibration.CalibrationService.SubscribeCalibrateGimbalAccelerometer',
    index=4,
    containing_service=None,
    input_type=_SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST,
    output_type=_CALIBRATEGIMBALACCELEROMETERRESPONSE,
    serialized_options=b'\200\265\030\000\210\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Cancel',
    full_name='mavsdk.rpc.calibration.CalibrationService.Cancel',
    index=5,
    containing_service=None,
    input_type=_CANCELREQUEST,
    output_type=_CANCELRESPONSE,
    serialized_options=b'\200\265\030\001',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALIBRATIONSERVICE)

DESCRIPTOR.services_by_name['CalibrationService'] = _CALIBRATIONSERVICE

# @@protoc_insertion_point(module_scope)
