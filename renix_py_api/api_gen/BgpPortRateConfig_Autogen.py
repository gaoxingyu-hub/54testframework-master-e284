"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BgpPortRateConfig(ROMObject):
    def __init__(self, BgpUpdateMessageRate=None, SessionConnectDelay=None, SessionDisconnectDelay=None, **kwargs):
        self._BgpUpdateMessageRate = BgpUpdateMessageRate  # BGP Update Messages Tx Rate (messages/sec)
        self._SessionConnectDelay = SessionConnectDelay  # BGP Session Connect Delay (ms)
        self._SessionDisconnectDelay = SessionDisconnectDelay  # BGP Session Disconnect Delay (ms)

        properties = kwargs.copy()
        if BgpUpdateMessageRate is not None:
            properties['BgpUpdateMessageRate'] = BgpUpdateMessageRate
        if SessionConnectDelay is not None:
            properties['SessionConnectDelay'] = SessionConnectDelay
        if SessionDisconnectDelay is not None:
            properties['SessionDisconnectDelay'] = SessionDisconnectDelay

        # call base class function, and it will send message to renix server to create a class.
        super(BgpPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, BgpUpdateMessageRate=None, SessionConnectDelay=None, SessionDisconnectDelay=None, **kwargs):
        properties = kwargs.copy()
        if BgpUpdateMessageRate is not None:
            self._BgpUpdateMessageRate = BgpUpdateMessageRate
            properties['BgpUpdateMessageRate'] = BgpUpdateMessageRate
        if SessionConnectDelay is not None:
            self._SessionConnectDelay = SessionConnectDelay
            properties['SessionConnectDelay'] = SessionConnectDelay
        if SessionDisconnectDelay is not None:
            self._SessionDisconnectDelay = SessionDisconnectDelay
            properties['SessionDisconnectDelay'] = SessionDisconnectDelay

        super(BgpPortRateConfig, self).edit(**properties)

    @property
    def BgpUpdateMessageRate(self):
        """
        get the value of property _BgpUpdateMessageRate
        """
        if self.force_auto_sync:
            self.get('BgpUpdateMessageRate')
        return self._BgpUpdateMessageRate

    @property
    def SessionConnectDelay(self):
        """
        get the value of property _SessionConnectDelay
        """
        if self.force_auto_sync:
            self.get('SessionConnectDelay')
        return self._SessionConnectDelay

    @property
    def SessionDisconnectDelay(self):
        """
        get the value of property _SessionDisconnectDelay
        """
        if self.force_auto_sync:
            self.get('SessionDisconnectDelay')
        return self._SessionDisconnectDelay

    @BgpUpdateMessageRate.setter
    def BgpUpdateMessageRate(self, value):
        self._BgpUpdateMessageRate = value
        self.edit(BgpUpdateMessageRate=value)

    @SessionConnectDelay.setter
    def SessionConnectDelay(self, value):
        self._SessionConnectDelay = value
        self.edit(SessionConnectDelay=value)

    @SessionDisconnectDelay.setter
    def SessionDisconnectDelay(self, value):
        self._SessionDisconnectDelay = value
        self.edit(SessionDisconnectDelay=value)

    def _set_bgpupdatemessagerate_with_str(self, value):
        try:
            self._BgpUpdateMessageRate = int(value)
        except ValueError:
            self._BgpUpdateMessageRate = hex(int(value, 16))

    def _set_sessionconnectdelay_with_str(self, value):
        try:
            self._SessionConnectDelay = int(value)
        except ValueError:
            self._SessionConnectDelay = hex(int(value, 16))

    def _set_sessiondisconnectdelay_with_str(self, value):
        try:
            self._SessionDisconnectDelay = int(value)
        except ValueError:
            self._SessionDisconnectDelay = hex(int(value, 16))

