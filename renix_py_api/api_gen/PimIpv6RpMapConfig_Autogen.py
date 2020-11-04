"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PimIpv6RpMapConfig(ROMObject):
    def __init__(self, MulticastGroupAddr=None, RpAddr=None, RpPriority=None, RpHoldTime=None, **kwargs):
        self._MulticastGroupAddr = MulticastGroupAddr  # Multicast Group IPv6 Address
        self._RpAddr = RpAddr  # RP Address
        self._RpPriority = RpPriority  # RP Priority
        self._RpHoldTime = RpHoldTime  # RP Hold Time (sec)

        properties = kwargs.copy()
        if MulticastGroupAddr is not None:
            properties['MulticastGroupAddr'] = MulticastGroupAddr
        if RpAddr is not None:
            properties['RpAddr'] = RpAddr
        if RpPriority is not None:
            properties['RpPriority'] = RpPriority
        if RpHoldTime is not None:
            properties['RpHoldTime'] = RpHoldTime

        # call base class function, and it will send message to renix server to create a class.
        super(PimIpv6RpMapConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MulticastGroupAddr=None, RpAddr=None, RpPriority=None, RpHoldTime=None, **kwargs):
        properties = kwargs.copy()
        if MulticastGroupAddr is not None:
            self._MulticastGroupAddr = MulticastGroupAddr
            properties['MulticastGroupAddr'] = MulticastGroupAddr
        if RpAddr is not None:
            self._RpAddr = RpAddr
            properties['RpAddr'] = RpAddr
        if RpPriority is not None:
            self._RpPriority = RpPriority
            properties['RpPriority'] = RpPriority
        if RpHoldTime is not None:
            self._RpHoldTime = RpHoldTime
            properties['RpHoldTime'] = RpHoldTime

        super(PimIpv6RpMapConfig, self).edit(**properties)

    @property
    def MulticastGroupAddr(self):
        """
        get the value of property _MulticastGroupAddr
        """
        if self.force_auto_sync:
            self.get('MulticastGroupAddr')
        return self._MulticastGroupAddr

    @property
    def RpAddr(self):
        """
        get the value of property _RpAddr
        """
        if self.force_auto_sync:
            self.get('RpAddr')
        return self._RpAddr

    @property
    def RpPriority(self):
        """
        get the value of property _RpPriority
        """
        if self.force_auto_sync:
            self.get('RpPriority')
        return self._RpPriority

    @property
    def RpHoldTime(self):
        """
        get the value of property _RpHoldTime
        """
        if self.force_auto_sync:
            self.get('RpHoldTime')
        return self._RpHoldTime

    @MulticastGroupAddr.setter
    def MulticastGroupAddr(self, value):
        self._MulticastGroupAddr = value
        self.edit(MulticastGroupAddr=value)

    @RpAddr.setter
    def RpAddr(self, value):
        self._RpAddr = value
        self.edit(RpAddr=value)

    @RpPriority.setter
    def RpPriority(self, value):
        self._RpPriority = value
        self.edit(RpPriority=value)

    @RpHoldTime.setter
    def RpHoldTime(self, value):
        self._RpHoldTime = value
        self.edit(RpHoldTime=value)

    def _set_multicastgroupaddr_with_str(self, value):
        self._MulticastGroupAddr = value

    def _set_rpaddr_with_str(self, value):
        self._RpAddr = value

    def _set_rppriority_with_str(self, value):
        try:
            self._RpPriority = int(value)
        except ValueError:
            self._RpPriority = hex(int(value, 16))

    def _set_rpholdtime_with_str(self, value):
        try:
            self._RpHoldTime = int(value)
        except ValueError:
            self._RpHoldTime = hex(int(value, 16))

