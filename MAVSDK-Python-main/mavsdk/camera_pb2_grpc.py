# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import camera_pb2 as camera_dot_camera__pb2


class CameraServiceStub(object):
    """
    Can be used to manage cameras that implement the MAVLink
    Camera Protocol: https://mavlink.io/en/protocol/camera.html.

    Currently only a single camera is supported.
    When multiple cameras are supported the plugin will need to be
    instantiated separately for every camera and the camera selected using
    `select_camera`.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TakePhoto = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/TakePhoto',
                request_serializer=camera_dot_camera__pb2.TakePhotoRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.TakePhotoResponse.FromString,
                )
        self.StartPhotoInterval = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StartPhotoInterval',
                request_serializer=camera_dot_camera__pb2.StartPhotoIntervalRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StartPhotoIntervalResponse.FromString,
                )
        self.StopPhotoInterval = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StopPhotoInterval',
                request_serializer=camera_dot_camera__pb2.StopPhotoIntervalRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StopPhotoIntervalResponse.FromString,
                )
        self.StartVideo = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StartVideo',
                request_serializer=camera_dot_camera__pb2.StartVideoRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StartVideoResponse.FromString,
                )
        self.StopVideo = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StopVideo',
                request_serializer=camera_dot_camera__pb2.StopVideoRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StopVideoResponse.FromString,
                )
        self.StartVideoStreaming = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StartVideoStreaming',
                request_serializer=camera_dot_camera__pb2.StartVideoStreamingRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StartVideoStreamingResponse.FromString,
                )
        self.StopVideoStreaming = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/StopVideoStreaming',
                request_serializer=camera_dot_camera__pb2.StopVideoStreamingRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StopVideoStreamingResponse.FromString,
                )
        self.SetMode = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/SetMode',
                request_serializer=camera_dot_camera__pb2.SetModeRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.SetModeResponse.FromString,
                )
        self.ListPhotos = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/ListPhotos',
                request_serializer=camera_dot_camera__pb2.ListPhotosRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.ListPhotosResponse.FromString,
                )
        self.SubscribeMode = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeMode',
                request_serializer=camera_dot_camera__pb2.SubscribeModeRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.ModeResponse.FromString,
                )
        self.SubscribeInformation = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeInformation',
                request_serializer=camera_dot_camera__pb2.SubscribeInformationRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.InformationResponse.FromString,
                )
        self.SubscribeVideoStreamInfo = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeVideoStreamInfo',
                request_serializer=camera_dot_camera__pb2.SubscribeVideoStreamInfoRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.VideoStreamInfoResponse.FromString,
                )
        self.SubscribeCaptureInfo = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeCaptureInfo',
                request_serializer=camera_dot_camera__pb2.SubscribeCaptureInfoRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.CaptureInfoResponse.FromString,
                )
        self.SubscribeStatus = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeStatus',
                request_serializer=camera_dot_camera__pb2.SubscribeStatusRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.StatusResponse.FromString,
                )
        self.SubscribeCurrentSettings = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribeCurrentSettings',
                request_serializer=camera_dot_camera__pb2.SubscribeCurrentSettingsRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.CurrentSettingsResponse.FromString,
                )
        self.SubscribePossibleSettingOptions = channel.unary_stream(
                '/mavsdk.rpc.camera.CameraService/SubscribePossibleSettingOptions',
                request_serializer=camera_dot_camera__pb2.SubscribePossibleSettingOptionsRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.PossibleSettingOptionsResponse.FromString,
                )
        self.SetSetting = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/SetSetting',
                request_serializer=camera_dot_camera__pb2.SetSettingRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.SetSettingResponse.FromString,
                )
        self.GetSetting = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/GetSetting',
                request_serializer=camera_dot_camera__pb2.GetSettingRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.GetSettingResponse.FromString,
                )
        self.FormatStorage = channel.unary_unary(
                '/mavsdk.rpc.camera.CameraService/FormatStorage',
                request_serializer=camera_dot_camera__pb2.FormatStorageRequest.SerializeToString,
                response_deserializer=camera_dot_camera__pb2.FormatStorageResponse.FromString,
                )


class CameraServiceServicer(object):
    """
    Can be used to manage cameras that implement the MAVLink
    Camera Protocol: https://mavlink.io/en/protocol/camera.html.

    Currently only a single camera is supported.
    When multiple cameras are supported the plugin will need to be
    instantiated separately for every camera and the camera selected using
    `select_camera`.
    """

    def TakePhoto(self, request, context):
        """
        Take one photo.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPhotoInterval(self, request, context):
        """
        Start photo timelapse with a given interval.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPhotoInterval(self, request, context):
        """
        Stop a running photo timelapse.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartVideo(self, request, context):
        """
        Start a video recording.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopVideo(self, request, context):
        """
        Stop a running video recording.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartVideoStreaming(self, request, context):
        """
        Start video streaming.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopVideoStreaming(self, request, context):
        """
        Stop current video streaming.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMode(self, request, context):
        """
        Set camera mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPhotos(self, request, context):
        """
        List photos available on the camera.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeMode(self, request, context):
        """
        Subscribe to camera mode updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeInformation(self, request, context):
        """
        Subscribe to camera information updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeVideoStreamInfo(self, request, context):
        """
        Subscribe to video stream info updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCaptureInfo(self, request, context):
        """
        Subscribe to capture info updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStatus(self, request, context):
        """
        Subscribe to camera status updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCurrentSettings(self, request, context):
        """
        Get the list of current camera settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribePossibleSettingOptions(self, request, context):
        """
        Get the list of settings that can be changed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSetting(self, request, context):
        """
        Set a setting to some value.

        Only setting_id of setting and option_id of option needs to be set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSetting(self, request, context):
        """
        Get a setting.

        Only setting_id of setting needs to be set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FormatStorage(self, request, context):
        """
        Format storage (e.g. SD card) in camera.

        This will delete all content of the camera storage!
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CameraServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TakePhoto': grpc.unary_unary_rpc_method_handler(
                    servicer.TakePhoto,
                    request_deserializer=camera_dot_camera__pb2.TakePhotoRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.TakePhotoResponse.SerializeToString,
            ),
            'StartPhotoInterval': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPhotoInterval,
                    request_deserializer=camera_dot_camera__pb2.StartPhotoIntervalRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StartPhotoIntervalResponse.SerializeToString,
            ),
            'StopPhotoInterval': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPhotoInterval,
                    request_deserializer=camera_dot_camera__pb2.StopPhotoIntervalRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StopPhotoIntervalResponse.SerializeToString,
            ),
            'StartVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StartVideo,
                    request_deserializer=camera_dot_camera__pb2.StartVideoRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StartVideoResponse.SerializeToString,
            ),
            'StopVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.StopVideo,
                    request_deserializer=camera_dot_camera__pb2.StopVideoRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StopVideoResponse.SerializeToString,
            ),
            'StartVideoStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.StartVideoStreaming,
                    request_deserializer=camera_dot_camera__pb2.StartVideoStreamingRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StartVideoStreamingResponse.SerializeToString,
            ),
            'StopVideoStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.StopVideoStreaming,
                    request_deserializer=camera_dot_camera__pb2.StopVideoStreamingRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StopVideoStreamingResponse.SerializeToString,
            ),
            'SetMode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMode,
                    request_deserializer=camera_dot_camera__pb2.SetModeRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.SetModeResponse.SerializeToString,
            ),
            'ListPhotos': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPhotos,
                    request_deserializer=camera_dot_camera__pb2.ListPhotosRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.ListPhotosResponse.SerializeToString,
            ),
            'SubscribeMode': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeMode,
                    request_deserializer=camera_dot_camera__pb2.SubscribeModeRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.ModeResponse.SerializeToString,
            ),
            'SubscribeInformation': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeInformation,
                    request_deserializer=camera_dot_camera__pb2.SubscribeInformationRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.InformationResponse.SerializeToString,
            ),
            'SubscribeVideoStreamInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeVideoStreamInfo,
                    request_deserializer=camera_dot_camera__pb2.SubscribeVideoStreamInfoRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.VideoStreamInfoResponse.SerializeToString,
            ),
            'SubscribeCaptureInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCaptureInfo,
                    request_deserializer=camera_dot_camera__pb2.SubscribeCaptureInfoRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.CaptureInfoResponse.SerializeToString,
            ),
            'SubscribeStatus': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeStatus,
                    request_deserializer=camera_dot_camera__pb2.SubscribeStatusRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.StatusResponse.SerializeToString,
            ),
            'SubscribeCurrentSettings': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCurrentSettings,
                    request_deserializer=camera_dot_camera__pb2.SubscribeCurrentSettingsRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.CurrentSettingsResponse.SerializeToString,
            ),
            'SubscribePossibleSettingOptions': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribePossibleSettingOptions,
                    request_deserializer=camera_dot_camera__pb2.SubscribePossibleSettingOptionsRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.PossibleSettingOptionsResponse.SerializeToString,
            ),
            'SetSetting': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSetting,
                    request_deserializer=camera_dot_camera__pb2.SetSettingRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.SetSettingResponse.SerializeToString,
            ),
            'GetSetting': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSetting,
                    request_deserializer=camera_dot_camera__pb2.GetSettingRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.GetSettingResponse.SerializeToString,
            ),
            'FormatStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.FormatStorage,
                    request_deserializer=camera_dot_camera__pb2.FormatStorageRequest.FromString,
                    response_serializer=camera_dot_camera__pb2.FormatStorageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.camera.CameraService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CameraService(object):
    """
    Can be used to manage cameras that implement the MAVLink
    Camera Protocol: https://mavlink.io/en/protocol/camera.html.

    Currently only a single camera is supported.
    When multiple cameras are supported the plugin will need to be
    instantiated separately for every camera and the camera selected using
    `select_camera`.
    """

    @staticmethod
    def TakePhoto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/TakePhoto',
            camera_dot_camera__pb2.TakePhotoRequest.SerializeToString,
            camera_dot_camera__pb2.TakePhotoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartPhotoInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StartPhotoInterval',
            camera_dot_camera__pb2.StartPhotoIntervalRequest.SerializeToString,
            camera_dot_camera__pb2.StartPhotoIntervalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopPhotoInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StopPhotoInterval',
            camera_dot_camera__pb2.StopPhotoIntervalRequest.SerializeToString,
            camera_dot_camera__pb2.StopPhotoIntervalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StartVideo',
            camera_dot_camera__pb2.StartVideoRequest.SerializeToString,
            camera_dot_camera__pb2.StartVideoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StopVideo',
            camera_dot_camera__pb2.StopVideoRequest.SerializeToString,
            camera_dot_camera__pb2.StopVideoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartVideoStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StartVideoStreaming',
            camera_dot_camera__pb2.StartVideoStreamingRequest.SerializeToString,
            camera_dot_camera__pb2.StartVideoStreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopVideoStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/StopVideoStreaming',
            camera_dot_camera__pb2.StopVideoStreamingRequest.SerializeToString,
            camera_dot_camera__pb2.StopVideoStreamingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/SetMode',
            camera_dot_camera__pb2.SetModeRequest.SerializeToString,
            camera_dot_camera__pb2.SetModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPhotos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/ListPhotos',
            camera_dot_camera__pb2.ListPhotosRequest.SerializeToString,
            camera_dot_camera__pb2.ListPhotosResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeMode',
            camera_dot_camera__pb2.SubscribeModeRequest.SerializeToString,
            camera_dot_camera__pb2.ModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeInformation',
            camera_dot_camera__pb2.SubscribeInformationRequest.SerializeToString,
            camera_dot_camera__pb2.InformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeVideoStreamInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeVideoStreamInfo',
            camera_dot_camera__pb2.SubscribeVideoStreamInfoRequest.SerializeToString,
            camera_dot_camera__pb2.VideoStreamInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeCaptureInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeCaptureInfo',
            camera_dot_camera__pb2.SubscribeCaptureInfoRequest.SerializeToString,
            camera_dot_camera__pb2.CaptureInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeStatus',
            camera_dot_camera__pb2.SubscribeStatusRequest.SerializeToString,
            camera_dot_camera__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeCurrentSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribeCurrentSettings',
            camera_dot_camera__pb2.SubscribeCurrentSettingsRequest.SerializeToString,
            camera_dot_camera__pb2.CurrentSettingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribePossibleSettingOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.camera.CameraService/SubscribePossibleSettingOptions',
            camera_dot_camera__pb2.SubscribePossibleSettingOptionsRequest.SerializeToString,
            camera_dot_camera__pb2.PossibleSettingOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSetting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/SetSetting',
            camera_dot_camera__pb2.SetSettingRequest.SerializeToString,
            camera_dot_camera__pb2.SetSettingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSetting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/GetSetting',
            camera_dot_camera__pb2.GetSettingRequest.SerializeToString,
            camera_dot_camera__pb2.GetSettingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FormatStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.camera.CameraService/FormatStorage',
            camera_dot_camera__pb2.FormatStorageRequest.SerializeToString,
            camera_dot_camera__pb2.FormatStorageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
