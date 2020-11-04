"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class DeleteROMCommand(ROMCommand):
    def __init__(self, ToDelete=None, **kwargs):
        self._ToDelete = ToDelete  # Objects to Deleted

        properties = kwargs.copy()
        if ToDelete is not None:
            properties['ToDelete'] = ToDelete

        # call base class function, and it will send message to renix server to create a class.
        super(DeleteROMCommand, self).__init__(**properties)

    @property
    def ToDelete(self):
        """
        get the value of property _ToDelete
        """
        return self._ToDelete

    @ToDelete.setter
    def ToDelete(self, value):
        self._ToDelete = value

    def _set_todelete_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ToDelete = tmp_value.split()

