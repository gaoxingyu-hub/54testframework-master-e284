"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LagPortSelected(ROMObject):
    def __init__(self, PortHandles=None, **kwargs):
        self._PortHandles = PortHandles  # Port Handles

        properties = kwargs.copy()
        if PortHandles is not None:
            properties['PortHandles'] = PortHandles

        # call base class function, and it will send message to renix server to create a class.
        super(LagPortSelected, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PortHandles=None, **kwargs):
        properties = kwargs.copy()
        if PortHandles is not None:
            self._PortHandles = PortHandles
            properties['PortHandles'] = PortHandles

        super(LagPortSelected, self).edit(**properties)

    @property
    def PortHandles(self):
        """
        get the value of property _PortHandles
        """
        if self.force_auto_sync:
            self.get('PortHandles')
        return self._PortHandles

    @PortHandles.setter
    def PortHandles(self, value):
        self._PortHandles = value
        self.edit(PortHandles=value)

    def _set_porthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortHandles = tmp_value.split()

