"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class FilesCommand(ROMCommand):
    def __init__(self, PortHandles=None, **kwargs):
        self._PortHandles = PortHandles  # Port

        properties = kwargs.copy()
        if PortHandles is not None:
            properties['PortHandles'] = PortHandles

        # call base class function, and it will send message to renix server to create a class.
        super(FilesCommand, self).__init__(**properties)

    @property
    def PortHandles(self):
        """
        get the value of property _PortHandles
        """
        return self._PortHandles

    @PortHandles.setter
    def PortHandles(self, value):
        self._PortHandles = value

    def _set_porthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortHandles = tmp_value.split()

