"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkSpecific_Autogen import NetworkSpecific


@rom_manager.rom
class DynamicNetworkLayer(NetworkSpecific):
    def __init__(self, Count=None, AddressMode=None, **kwargs):
        self._Count = Count  # Address Count
        self._AddressMode = AddressMode  # Address Mode

        properties = kwargs.copy()
        if Count is not None:
            properties['Count'] = Count
        if AddressMode is not None:
            properties['AddressMode'] = AddressMode

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicNetworkLayer, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Count=None, AddressMode=None, **kwargs):
        properties = kwargs.copy()
        if Count is not None:
            self._Count = Count
            properties['Count'] = Count
        if AddressMode is not None:
            self._AddressMode = AddressMode
            properties['AddressMode'] = AddressMode

        super(DynamicNetworkLayer, self).edit(**properties)

    @property
    def Count(self):
        """
        get the value of property _Count
        """
        if self.force_auto_sync:
            self.get('Count')
        return self._Count

    @property
    def AddressMode(self):
        """
        get the value of property _AddressMode
        """
        if self.force_auto_sync:
            self.get('AddressMode')
        return self._AddressMode

    @Count.setter
    def Count(self, value):
        self._Count = value
        self.edit(Count=value)

    @AddressMode.setter
    def AddressMode(self, value):
        self._AddressMode = value
        self.edit(AddressMode=value)

    def _set_count_with_str(self, value):
        try:
            self._Count = int(value)
        except ValueError:
            self._Count = hex(int(value, 16))

    def _set_addressmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressMode = EnumAddressMode.%s' % value[:seperate])

