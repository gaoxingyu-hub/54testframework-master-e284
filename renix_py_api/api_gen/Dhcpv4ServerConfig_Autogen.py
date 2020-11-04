"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dhcpv4ServerConfig(L23ProtocolConfig):
    def __init__(self, LeaseTime=None, RenewTime=None, RebindTime=None, MinLeaseTime=None, DeclineReserveTime=None, OfferReserveTime=None, ServerHostName=None, **kwargs):
        self._State = EnumDhcpv4ServerState.NOT_READY  # DHCPv4 Server State, not editable
        self._LeaseTime = LeaseTime  # Lease Time (sec)
        self._RenewTime = RenewTime  # Renew Time (%)
        self._RebindTime = RebindTime  # Rebind Time (%)
        self._MinLeaseTime = MinLeaseTime  # Min Allowed Lease Time (sec)
        self._DeclineReserveTime = DeclineReserveTime  # Decline Reserve Time (secs)
        self._OfferReserveTime = OfferReserveTime  # Offer Reserve Time (secs)
        self._ServerHostName = ServerHostName  # Server Host Name

        properties = kwargs.copy()
        if LeaseTime is not None:
            properties['LeaseTime'] = LeaseTime
        if RenewTime is not None:
            properties['RenewTime'] = RenewTime
        if RebindTime is not None:
            properties['RebindTime'] = RebindTime
        if MinLeaseTime is not None:
            properties['MinLeaseTime'] = MinLeaseTime
        if DeclineReserveTime is not None:
            properties['DeclineReserveTime'] = DeclineReserveTime
        if OfferReserveTime is not None:
            properties['OfferReserveTime'] = OfferReserveTime
        if ServerHostName is not None:
            properties['ServerHostName'] = ServerHostName

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LeaseTime=None, RenewTime=None, RebindTime=None, MinLeaseTime=None, DeclineReserveTime=None, OfferReserveTime=None, ServerHostName=None, **kwargs):
        properties = kwargs.copy()
        if LeaseTime is not None:
            self._LeaseTime = LeaseTime
            properties['LeaseTime'] = LeaseTime
        if RenewTime is not None:
            self._RenewTime = RenewTime
            properties['RenewTime'] = RenewTime
        if RebindTime is not None:
            self._RebindTime = RebindTime
            properties['RebindTime'] = RebindTime
        if MinLeaseTime is not None:
            self._MinLeaseTime = MinLeaseTime
            properties['MinLeaseTime'] = MinLeaseTime
        if DeclineReserveTime is not None:
            self._DeclineReserveTime = DeclineReserveTime
            properties['DeclineReserveTime'] = DeclineReserveTime
        if OfferReserveTime is not None:
            self._OfferReserveTime = OfferReserveTime
            properties['OfferReserveTime'] = OfferReserveTime
        if ServerHostName is not None:
            self._ServerHostName = ServerHostName
            properties['ServerHostName'] = ServerHostName

        super(Dhcpv4ServerConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def LeaseTime(self):
        """
        get the value of property _LeaseTime
        """
        if self.force_auto_sync:
            self.get('LeaseTime')
        return self._LeaseTime

    @property
    def RenewTime(self):
        """
        get the value of property _RenewTime
        """
        if self.force_auto_sync:
            self.get('RenewTime')
        return self._RenewTime

    @property
    def RebindTime(self):
        """
        get the value of property _RebindTime
        """
        if self.force_auto_sync:
            self.get('RebindTime')
        return self._RebindTime

    @property
    def MinLeaseTime(self):
        """
        get the value of property _MinLeaseTime
        """
        if self.force_auto_sync:
            self.get('MinLeaseTime')
        return self._MinLeaseTime

    @property
    def DeclineReserveTime(self):
        """
        get the value of property _DeclineReserveTime
        """
        if self.force_auto_sync:
            self.get('DeclineReserveTime')
        return self._DeclineReserveTime

    @property
    def OfferReserveTime(self):
        """
        get the value of property _OfferReserveTime
        """
        if self.force_auto_sync:
            self.get('OfferReserveTime')
        return self._OfferReserveTime

    @property
    def ServerHostName(self):
        """
        get the value of property _ServerHostName
        """
        if self.force_auto_sync:
            self.get('ServerHostName')
        return self._ServerHostName

    @LeaseTime.setter
    def LeaseTime(self, value):
        self._LeaseTime = value
        self.edit(LeaseTime=value)

    @RenewTime.setter
    def RenewTime(self, value):
        self._RenewTime = value
        self.edit(RenewTime=value)

    @RebindTime.setter
    def RebindTime(self, value):
        self._RebindTime = value
        self.edit(RebindTime=value)

    @MinLeaseTime.setter
    def MinLeaseTime(self, value):
        self._MinLeaseTime = value
        self.edit(MinLeaseTime=value)

    @DeclineReserveTime.setter
    def DeclineReserveTime(self, value):
        self._DeclineReserveTime = value
        self.edit(DeclineReserveTime=value)

    @OfferReserveTime.setter
    def OfferReserveTime(self, value):
        self._OfferReserveTime = value
        self.edit(OfferReserveTime=value)

    @ServerHostName.setter
    def ServerHostName(self, value):
        self._ServerHostName = value
        self.edit(ServerHostName=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumDhcpv4ServerState.%s' % value[:seperate])

    def _set_leasetime_with_str(self, value):
        try:
            self._LeaseTime = int(value)
        except ValueError:
            self._LeaseTime = hex(int(value, 16))

    def _set_renewtime_with_str(self, value):
        self._RenewTime = float(value)

    def _set_rebindtime_with_str(self, value):
        self._RebindTime = float(value)

    def _set_minleasetime_with_str(self, value):
        try:
            self._MinLeaseTime = int(value)
        except ValueError:
            self._MinLeaseTime = hex(int(value, 16))

    def _set_declinereservetime_with_str(self, value):
        try:
            self._DeclineReserveTime = int(value)
        except ValueError:
            self._DeclineReserveTime = hex(int(value, 16))

    def _set_offerreservetime_with_str(self, value):
        try:
            self._OfferReserveTime = int(value)
        except ValueError:
            self._OfferReserveTime = hex(int(value, 16))

    def _set_serverhostname_with_str(self, value):
        self._ServerHostName = value

