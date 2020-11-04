"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class CommandStatusUpdater(ROMObject):
    def __init__(self, **kwargs):
        self._CommandStatus = None  # Command Status Message, not editable
        self._UnregisteredObjects = None  # Unregistered Objects, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(CommandStatusUpdater, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(CommandStatusUpdater, self).edit(**properties)

    @property
    def CommandStatus(self):
        """
        get the value of property _CommandStatus
        """
        if self.force_auto_sync:
            self.get('CommandStatus')
        return self._CommandStatus

    @property
    def UnregisteredObjects(self):
        """
        get the value of property _UnregisteredObjects
        """
        if self.force_auto_sync:
            self.get('UnregisteredObjects')
        return self._UnregisteredObjects

    def _set_commandstatus_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CommandStatus = tmp_value.split()

    def _set_unregisteredobjects_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._UnregisteredObjects = tmp_value.split()

