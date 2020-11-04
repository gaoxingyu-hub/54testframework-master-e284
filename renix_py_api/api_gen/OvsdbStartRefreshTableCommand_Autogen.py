"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class OvsdbStartRefreshTableCommand(ROMCommand):
    def __init__(self, OvsdbHandle=None, **kwargs):
        self._OvsdbHandle = OvsdbHandle  # OVSDB Protocol Config

        properties = kwargs.copy()
        if OvsdbHandle is not None:
            properties['OvsdbHandle'] = OvsdbHandle

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbStartRefreshTableCommand, self).__init__(**properties)

    @property
    def OvsdbHandle(self):
        """
        get the value of property _OvsdbHandle
        """
        return self._OvsdbHandle

    @OvsdbHandle.setter
    def OvsdbHandle(self, value):
        self._OvsdbHandle = value

    def _set_ovsdbhandle_with_str(self, value):
        self._OvsdbHandle = value

