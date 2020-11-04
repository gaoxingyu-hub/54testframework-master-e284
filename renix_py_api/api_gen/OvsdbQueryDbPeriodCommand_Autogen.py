"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OvsdbQueryDbCommand_Autogen import OvsdbQueryDbCommand


@rom_manager.rom
class OvsdbQueryDbPeriodCommand(OvsdbQueryDbCommand):
    def __init__(self, OvsdbHandle=None, OvsdbTimer=None, **kwargs):
        self._OvsdbHandle = OvsdbHandle  # OVSDB Protocol Config
        self._OvsdbTimer = OvsdbTimer  # 

        properties = kwargs.copy()
        if OvsdbHandle is not None:
            properties['OvsdbHandle'] = OvsdbHandle
        if OvsdbTimer is not None:
            properties['OvsdbTimer'] = OvsdbTimer

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbQueryDbPeriodCommand, self).__init__(**properties)

    @property
    def OvsdbHandle(self):
        """
        get the value of property _OvsdbHandle
        """
        return self._OvsdbHandle

    @property
    def OvsdbTimer(self):
        """
        get the value of property _OvsdbTimer
        """
        return self._OvsdbTimer

    @OvsdbHandle.setter
    def OvsdbHandle(self, value):
        self._OvsdbHandle = value

    @OvsdbTimer.setter
    def OvsdbTimer(self, value):
        self._OvsdbTimer = value

    def _set_ovsdbhandle_with_str(self, value):
        self._OvsdbHandle = value

    def _set_ovsdbtimer_with_str(self, value):
        try:
            self._OvsdbTimer = int(value)
        except ValueError:
            self._OvsdbTimer = hex(int(value, 16))

