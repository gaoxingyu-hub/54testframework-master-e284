"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ProtocolStatusRegistry(ROMObject):
    def __init__(self, **kwargs):
        self._Status = 'None'  # Protocol Status Message, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(ProtocolStatusRegistry, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(ProtocolStatusRegistry, self).edit(**properties)

    @property
    def Status(self):
        """
        get the value of property _Status
        """
        if self.force_auto_sync:
            self.get('Status')
        return self._Status

    def _set_status_with_str(self, value):
        self._Status = value

