"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpGlobalConfig_Autogen import OfpGlobalConfig


@rom_manager.rom
class OfpQueueConfig(OfpGlobalConfig):
    def __init__(self, ID=None, **kwargs):
        self._ID = ID  # ID

        properties = kwargs.copy()
        if ID is not None:
            properties['ID'] = ID

        # call base class function, and it will send message to renix server to create a class.
        super(OfpQueueConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ID=None, **kwargs):
        properties = kwargs.copy()
        if ID is not None:
            self._ID = ID
            properties['ID'] = ID

        super(OfpQueueConfig, self).edit(**properties)

    @property
    def ID(self):
        """
        get the value of property _ID
        """
        if self.force_auto_sync:
            self.get('ID')
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value
        self.edit(ID=value)

    def _set_id_with_str(self, value):
        try:
            self._ID = int(value)
        except ValueError:
            self._ID = hex(int(value, 16))

