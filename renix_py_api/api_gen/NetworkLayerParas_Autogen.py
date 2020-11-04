"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class NetworkLayerParas(ROMObject):
    def __init__(self, AddressCount=None, **kwargs):
        self._AddressCount = AddressCount  # Number of IPv4 Address Count

        properties = kwargs.copy()
        if AddressCount is not None:
            properties['AddressCount'] = AddressCount

        # call base class function, and it will send message to renix server to create a class.
        super(NetworkLayerParas, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AddressCount=None, **kwargs):
        properties = kwargs.copy()
        if AddressCount is not None:
            self._AddressCount = AddressCount
            properties['AddressCount'] = AddressCount

        super(NetworkLayerParas, self).edit(**properties)

    @property
    def AddressCount(self):
        """
        get the value of property _AddressCount
        """
        if self.force_auto_sync:
            self.get('AddressCount')
        return self._AddressCount

    @AddressCount.setter
    def AddressCount(self, value):
        self._AddressCount = value
        self.edit(AddressCount=value)

    def _set_addresscount_with_str(self, value):
        try:
            self._AddressCount = int(value)
        except ValueError:
            self._AddressCount = hex(int(value, 16))

