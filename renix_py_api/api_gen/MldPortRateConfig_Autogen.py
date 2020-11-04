"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class MldPortRateConfig(ROMObject):
    def __init__(self, MldMaximumOutputRate=None, **kwargs):
        self._MldMaximumOutputRate = MldMaximumOutputRate  # Maximum output rate (packets/sec) 

        properties = kwargs.copy()
        if MldMaximumOutputRate is not None:
            properties['MldMaximumOutputRate'] = MldMaximumOutputRate

        # call base class function, and it will send message to renix server to create a class.
        super(MldPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MldMaximumOutputRate=None, **kwargs):
        properties = kwargs.copy()
        if MldMaximumOutputRate is not None:
            self._MldMaximumOutputRate = MldMaximumOutputRate
            properties['MldMaximumOutputRate'] = MldMaximumOutputRate

        super(MldPortRateConfig, self).edit(**properties)

    @property
    def MldMaximumOutputRate(self):
        """
        get the value of property _MldMaximumOutputRate
        """
        if self.force_auto_sync:
            self.get('MldMaximumOutputRate')
        return self._MldMaximumOutputRate

    @MldMaximumOutputRate.setter
    def MldMaximumOutputRate(self, value):
        self._MldMaximumOutputRate = value
        self.edit(MldMaximumOutputRate=value)

    def _set_mldmaximumoutputrate_with_str(self, value):
        try:
            self._MldMaximumOutputRate = int(value)
        except ValueError:
            self._MldMaximumOutputRate = hex(int(value, 16))

