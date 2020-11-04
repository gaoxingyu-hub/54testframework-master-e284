"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PingCommand(ROMCommand):
    def __init__(self, InterfaceHandle=None, FrameCount=None, TimeInterval=None, **kwargs):
        self._InterfaceHandle = InterfaceHandle  # Ping Interface
        self._FrameCount = FrameCount  # Frame Count
        self._TimeInterval = TimeInterval  # Time Interval (sec)

        properties = kwargs.copy()
        if InterfaceHandle is not None:
            properties['InterfaceHandle'] = InterfaceHandle
        if FrameCount is not None:
            properties['FrameCount'] = FrameCount
        if TimeInterval is not None:
            properties['TimeInterval'] = TimeInterval

        # call base class function, and it will send message to renix server to create a class.
        super(PingCommand, self).__init__(**properties)

    @property
    def InterfaceHandle(self):
        """
        get the value of property _InterfaceHandle
        """
        return self._InterfaceHandle

    @property
    def FrameCount(self):
        """
        get the value of property _FrameCount
        """
        return self._FrameCount

    @property
    def TimeInterval(self):
        """
        get the value of property _TimeInterval
        """
        return self._TimeInterval

    @InterfaceHandle.setter
    def InterfaceHandle(self, value):
        self._InterfaceHandle = value

    @FrameCount.setter
    def FrameCount(self, value):
        self._FrameCount = value

    @TimeInterval.setter
    def TimeInterval(self, value):
        self._TimeInterval = value

    def _set_interfacehandle_with_str(self, value):
        self._InterfaceHandle = value

    def _set_framecount_with_str(self, value):
        try:
            self._FrameCount = int(value)
        except ValueError:
            self._FrameCount = hex(int(value, 16))

    def _set_timeinterval_with_str(self, value):
        try:
            self._TimeInterval = int(value)
        except ValueError:
            self._TimeInterval = hex(int(value, 16))

