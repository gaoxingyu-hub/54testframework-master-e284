"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisPortRateConfig(ROMObject):
    def __init__(self, UpdateRoutesTransmitRate=None, **kwargs):
        self._UpdateRoutesTransmitRate = UpdateRoutesTransmitRate  # IS-IS Tx Hello Rate(messages/second) 

        properties = kwargs.copy()
        if UpdateRoutesTransmitRate is not None:
            properties['UpdateRoutesTransmitRate'] = UpdateRoutesTransmitRate

        # call base class function, and it will send message to renix server to create a class.
        super(IsisPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, UpdateRoutesTransmitRate=None, **kwargs):
        properties = kwargs.copy()
        if UpdateRoutesTransmitRate is not None:
            self._UpdateRoutesTransmitRate = UpdateRoutesTransmitRate
            properties['UpdateRoutesTransmitRate'] = UpdateRoutesTransmitRate

        super(IsisPortRateConfig, self).edit(**properties)

    @property
    def UpdateRoutesTransmitRate(self):
        """
        get the value of property _UpdateRoutesTransmitRate
        """
        if self.force_auto_sync:
            self.get('UpdateRoutesTransmitRate')
        return self._UpdateRoutesTransmitRate

    @UpdateRoutesTransmitRate.setter
    def UpdateRoutesTransmitRate(self, value):
        self._UpdateRoutesTransmitRate = value
        self.edit(UpdateRoutesTransmitRate=value)

    def _set_updateroutestransmitrate_with_str(self, value):
        try:
            self._UpdateRoutesTransmitRate = int(value)
        except ValueError:
            self._UpdateRoutesTransmitRate = hex(int(value, 16))

