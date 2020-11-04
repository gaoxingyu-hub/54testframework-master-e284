"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamModifierRondomListSaveClass(ROMObject):
    def __init__(self, **kwargs):
        self._RandomList = None  # Random Mask, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(StreamModifierRondomListSaveClass, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(StreamModifierRondomListSaveClass, self).edit(**properties)

    @property
    def RandomList(self):
        """
        get the value of property _RandomList
        """
        if self.force_auto_sync:
            self.get('RandomList')
        return self._RandomList

    def _set_randomlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RandomList = tmp_value.split()

