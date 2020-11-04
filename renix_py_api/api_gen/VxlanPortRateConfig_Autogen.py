"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class VxlanPortRateConfig(ROMObject):
    def __init__(self, ArpTransmitRate=None, **kwargs):
        self._ArpTransmitRate = ArpTransmitRate  # VXLAN ARP transmit rate(packets/second) 

        properties = kwargs.copy()
        if ArpTransmitRate is not None:
            properties['ArpTransmitRate'] = ArpTransmitRate

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ArpTransmitRate=None, **kwargs):
        properties = kwargs.copy()
        if ArpTransmitRate is not None:
            self._ArpTransmitRate = ArpTransmitRate
            properties['ArpTransmitRate'] = ArpTransmitRate

        super(VxlanPortRateConfig, self).edit(**properties)

    @property
    def ArpTransmitRate(self):
        """
        get the value of property _ArpTransmitRate
        """
        if self.force_auto_sync:
            self.get('ArpTransmitRate')
        return self._ArpTransmitRate

    @ArpTransmitRate.setter
    def ArpTransmitRate(self, value):
        self._ArpTransmitRate = value
        self.edit(ArpTransmitRate=value)

    def _set_arptransmitrate_with_str(self, value):
        try:
            self._ArpTransmitRate = int(value)
        except ValueError:
            self._ArpTransmitRate = hex(int(value, 16))

