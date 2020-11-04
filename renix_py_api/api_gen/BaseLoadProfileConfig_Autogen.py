"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BaseLoadProfileConfig(ROMObject):
    def __init__(self, **kwargs):
        self._LoadMode = EnumProfileAllocation.PER_SIDE  # Profile Allocation, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BaseLoadProfileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(BaseLoadProfileConfig, self).edit(**properties)

    @property
    def LoadMode(self):
        """
        get the value of property _LoadMode
        """
        if self.force_auto_sync:
            self.get('LoadMode')
        return self._LoadMode

    def _set_loadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadMode = EnumProfileAllocation.%s' % value[:seperate])

