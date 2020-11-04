"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SubscribeRealtimeCaptureDataCommand(ROMCommand):
    def __init__(self, CaptureConfig=None, ListenPort=None, ListenIp=None, **kwargs):
        self._CaptureConfig = CaptureConfig  # Capture Handle
        self._ListenPort = ListenPort  # Listen Port
        self._ListenIp = ListenIp  # Listen IP

        properties = kwargs.copy()
        if CaptureConfig is not None:
            properties['CaptureConfig'] = CaptureConfig
        if ListenPort is not None:
            properties['ListenPort'] = ListenPort
        if ListenIp is not None:
            properties['ListenIp'] = ListenIp

        # call base class function, and it will send message to renix server to create a class.
        super(SubscribeRealtimeCaptureDataCommand, self).__init__(**properties)

    @property
    def CaptureConfig(self):
        """
        get the value of property _CaptureConfig
        """
        return self._CaptureConfig

    @property
    def ListenPort(self):
        """
        get the value of property _ListenPort
        """
        return self._ListenPort

    @property
    def ListenIp(self):
        """
        get the value of property _ListenIp
        """
        return self._ListenIp

    @CaptureConfig.setter
    def CaptureConfig(self, value):
        self._CaptureConfig = value

    @ListenPort.setter
    def ListenPort(self, value):
        self._ListenPort = value

    @ListenIp.setter
    def ListenIp(self, value):
        self._ListenIp = value

    def _set_captureconfig_with_str(self, value):
        self._CaptureConfig = value

    def _set_listenport_with_str(self, value):
        try:
            self._ListenPort = int(value)
        except ValueError:
            self._ListenPort = hex(int(value, 16))

    def _set_listenip_with_str(self, value):
        self._ListenIp = value

