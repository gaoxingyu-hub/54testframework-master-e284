"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillGroupAddressTLVConfig(ROMObject):
    def __init__(self, **kwargs):

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(TrillGroupAddressTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(TrillGroupAddressTLVConfig, self).edit(**properties)

