"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L2tpPortConfig(ROMObject):
    def __init__(self, TunnelConnectRate=None, **kwargs):
        self._TunnelConnectRate = TunnelConnectRate  # Tunnel Connect Rate (tunnels/sec)

        properties = kwargs.copy()
        if TunnelConnectRate is not None:
            properties['TunnelConnectRate'] = TunnelConnectRate

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TunnelConnectRate=None, **kwargs):
        properties = kwargs.copy()
        if TunnelConnectRate is not None:
            self._TunnelConnectRate = TunnelConnectRate
            properties['TunnelConnectRate'] = TunnelConnectRate

        super(L2tpPortConfig, self).edit(**properties)

    @property
    def TunnelConnectRate(self):
        """
        get the value of property _TunnelConnectRate
        """
        if self.force_auto_sync:
            self.get('TunnelConnectRate')
        return self._TunnelConnectRate

    @TunnelConnectRate.setter
    def TunnelConnectRate(self, value):
        self._TunnelConnectRate = value
        self.edit(TunnelConnectRate=value)

    def _set_tunnelconnectrate_with_str(self, value):
        try:
            self._TunnelConnectRate = int(value)
        except ValueError:
            self._TunnelConnectRate = hex(int(value, 16))

