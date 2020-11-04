"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Result(ROMObject):
    def __init__(self, **kwargs):
        self._InternalPrimaryKey = ''  # , not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Result, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def InternalPrimaryKey(self):
        """
        get the value of property _InternalPrimaryKey
        """
        if self.force_auto_sync:
            self.get('InternalPrimaryKey')
        return self._InternalPrimaryKey

    def _set_internalprimarykey_with_str(self, value):
        self._InternalPrimaryKey = value

