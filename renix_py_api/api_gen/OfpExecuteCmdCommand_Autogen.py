"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpCommand_Autogen import OfpCommand


@rom_manager.rom
class OfpExecuteCmdCommand(OfpCommand):
    def __init__(self, CmdHandles=None, SwitchDescHandles=None, **kwargs):
        self._CmdHandles = CmdHandles  # Command Handles
        self._SwitchDescHandles = SwitchDescHandles  # Switch Descriptor Handles

        properties = kwargs.copy()
        if CmdHandles is not None:
            properties['CmdHandles'] = CmdHandles
        if SwitchDescHandles is not None:
            properties['SwitchDescHandles'] = SwitchDescHandles

        # call base class function, and it will send message to renix server to create a class.
        super(OfpExecuteCmdCommand, self).__init__(**properties)

    @property
    def CmdHandles(self):
        """
        get the value of property _CmdHandles
        """
        return self._CmdHandles

    @property
    def SwitchDescHandles(self):
        """
        get the value of property _SwitchDescHandles
        """
        return self._SwitchDescHandles

    @CmdHandles.setter
    def CmdHandles(self, value):
        self._CmdHandles = value

    @SwitchDescHandles.setter
    def SwitchDescHandles(self, value):
        self._SwitchDescHandles = value

    def _set_cmdhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CmdHandles = tmp_value.split()

    def _set_switchdeschandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SwitchDescHandles = tmp_value.split()

