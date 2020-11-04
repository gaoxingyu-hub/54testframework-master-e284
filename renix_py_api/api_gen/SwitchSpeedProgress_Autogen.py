"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .RenixProgress_Autogen import RenixProgress


@rom_manager.rom
class SwitchSpeedProgress(RenixProgress):
    def __init__(self, **kwargs):
        self._PortGroupIndex = 1  # Port Group Index, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(SwitchSpeedProgress, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(SwitchSpeedProgress, self).edit(**properties)

    @property
    def PortGroupIndex(self):
        """
        get the value of property _PortGroupIndex
        """
        if self.force_auto_sync:
            self.get('PortGroupIndex')
        return self._PortGroupIndex

    def _set_portgroupindex_with_str(self, value):
        try:
            self._PortGroupIndex = int(value)
        except ValueError:
            self._PortGroupIndex = hex(int(value, 16))

