"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WaitForTrafficStopCommand_Autogen import WaitForTrafficStopCommand


@rom_manager.rom
class Y1564WaitForFrameSentOverCommand(WaitForTrafficStopCommand):
    def __init__(self, FrameSentNumber=None, **kwargs):
        self._FrameSentNumber = FrameSentNumber  # Frame Sent Number

        properties = kwargs.copy()
        if FrameSentNumber is not None:
            properties['FrameSentNumber'] = FrameSentNumber

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564WaitForFrameSentOverCommand, self).__init__(**properties)

    @property
    def FrameSentNumber(self):
        """
        get the value of property _FrameSentNumber
        """
        return self._FrameSentNumber

    @FrameSentNumber.setter
    def FrameSentNumber(self, value):
        self._FrameSentNumber = value

    def _set_framesentnumber_with_str(self, value):
        try:
            self._FrameSentNumber = int(value)
        except ValueError:
            self._FrameSentNumber = hex(int(value, 16))

