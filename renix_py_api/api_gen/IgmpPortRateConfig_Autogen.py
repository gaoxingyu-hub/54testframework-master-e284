"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IgmpPortRateConfig(ROMObject):
    def __init__(self, IgmpMaximumOutputRate=None, **kwargs):
        self._IgmpMaximumOutputRate = IgmpMaximumOutputRate  # Maximum output rate (packets/sec) 

        properties = kwargs.copy()
        if IgmpMaximumOutputRate is not None:
            properties['IgmpMaximumOutputRate'] = IgmpMaximumOutputRate

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IgmpMaximumOutputRate=None, **kwargs):
        properties = kwargs.copy()
        if IgmpMaximumOutputRate is not None:
            self._IgmpMaximumOutputRate = IgmpMaximumOutputRate
            properties['IgmpMaximumOutputRate'] = IgmpMaximumOutputRate

        super(IgmpPortRateConfig, self).edit(**properties)

    @property
    def IgmpMaximumOutputRate(self):
        """
        get the value of property _IgmpMaximumOutputRate
        """
        if self.force_auto_sync:
            self.get('IgmpMaximumOutputRate')
        return self._IgmpMaximumOutputRate

    @IgmpMaximumOutputRate.setter
    def IgmpMaximumOutputRate(self, value):
        self._IgmpMaximumOutputRate = value
        self.edit(IgmpMaximumOutputRate=value)

    def _set_igmpmaximumoutputrate_with_str(self, value):
        try:
            self._IgmpMaximumOutputRate = int(value)
        except ValueError:
            self._IgmpMaximumOutputRate = hex(int(value, 16))

