"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Y1564SmartScripterCommand_Autogen import Y1564SmartScripterCommand


@rom_manager.rom
class Y1564FrameSizeCommand(Y1564SmartScripterCommand):
    def __init__(self, FrameSize=None, **kwargs):
        self._FrameSize = FrameSize  # Frame Size

        properties = kwargs.copy()
        if FrameSize is not None:
            properties['FrameSize'] = FrameSize

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564FrameSizeCommand, self).__init__(**properties)

    @property
    def FrameSize(self):
        """
        get the value of property _FrameSize
        """
        return self._FrameSize

    @FrameSize.setter
    def FrameSize(self, value):
        self._FrameSize = value

    def _set_framesize_with_str(self, value):
        try:
            self._FrameSize = int(value)
        except ValueError:
            self._FrameSize = hex(int(value, 16))

