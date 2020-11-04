"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dhcpv4ClientConfig(L23ProtocolConfig):
    def __init__(self, Mode=None, HostName=None, ParameterRequestList=None, EnableRouterOption=None, VendorClassIdentifier=None, BroadcastFlag=None, RelayAgentIp=None, ServerIp=None, EnableRelayAgentCircuitID=None, RelayAgentCircuitID=None, EnableRelayAgentRemoteID=None, RelayAgentRemoteID=None, **kwargs):
        self._State = EnumDhcpv4ClientState.NOT_READY  # DHCPv4 Block State, not editable
        self._Mode = Mode  # DHCPv4 Client Emulation Mode
        self._HostName = HostName  # Host Name
        self._ParameterRequestList = swap_int_to_enum_flag(ParameterRequestList, EnumRequestParameter)  # Parameter Request List
        self._EnableRouterOption = EnableRouterOption  # Enable Router Option
        self._VendorClassIdentifier = VendorClassIdentifier  # Vendor Class Identifier [60]
        self._BroadcastFlag = BroadcastFlag  # Broadcast Flag
        self._RelayAgentIp = RelayAgentIp  # Relay Agent IP
        self._ServerIp = ServerIp  # Server IP
        self._EnableRelayAgentCircuitID = EnableRelayAgentCircuitID  # Enable Relay Agent Circuit ID
        self._RelayAgentCircuitID = RelayAgentCircuitID  # Relay Agent Circuit ID[82-1]
        self._EnableRelayAgentRemoteID = EnableRelayAgentRemoteID  # Enable Relay Agent Remote ID
        self._RelayAgentRemoteID = RelayAgentRemoteID  # Relay Agent Remote ID[82-2]

        properties = kwargs.copy()
        if Mode is not None:
            properties['Mode'] = Mode
        if HostName is not None:
            properties['HostName'] = HostName
        if ParameterRequestList is not None:
            if isinstance(ParameterRequestList, Flag):
                properties['ParameterRequestList'] = ParameterRequestList.value
            else:
                properties['ParameterRequestList'] = ParameterRequestList
        if EnableRouterOption is not None:
            properties['EnableRouterOption'] = EnableRouterOption
        if VendorClassIdentifier is not None:
            properties['VendorClassIdentifier'] = VendorClassIdentifier
        if BroadcastFlag is not None:
            properties['BroadcastFlag'] = BroadcastFlag
        if RelayAgentIp is not None:
            properties['RelayAgentIp'] = RelayAgentIp
        if ServerIp is not None:
            properties['ServerIp'] = ServerIp
        if EnableRelayAgentCircuitID is not None:
            properties['EnableRelayAgentCircuitID'] = EnableRelayAgentCircuitID
        if RelayAgentCircuitID is not None:
            properties['RelayAgentCircuitID'] = RelayAgentCircuitID
        if EnableRelayAgentRemoteID is not None:
            properties['EnableRelayAgentRemoteID'] = EnableRelayAgentRemoteID
        if RelayAgentRemoteID is not None:
            properties['RelayAgentRemoteID'] = RelayAgentRemoteID

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ClientConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Mode=None, HostName=None, ParameterRequestList=None, EnableRouterOption=None, VendorClassIdentifier=None, BroadcastFlag=None, RelayAgentIp=None, ServerIp=None, EnableRelayAgentCircuitID=None, RelayAgentCircuitID=None, EnableRelayAgentRemoteID=None, RelayAgentRemoteID=None, **kwargs):
        properties = kwargs.copy()
        if Mode is not None:
            self._Mode = Mode
            properties['Mode'] = Mode
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if ParameterRequestList is not None:
            self._ParameterRequestList = swap_int_to_enum_flag(ParameterRequestList, EnumRequestParameter)
            if isinstance(ParameterRequestList, Flag):
                properties['ParameterRequestList'] = ParameterRequestList.value
            else:
                properties['ParameterRequestList'] = ParameterRequestList
        if EnableRouterOption is not None:
            self._EnableRouterOption = EnableRouterOption
            properties['EnableRouterOption'] = EnableRouterOption
        if VendorClassIdentifier is not None:
            self._VendorClassIdentifier = VendorClassIdentifier
            properties['VendorClassIdentifier'] = VendorClassIdentifier
        if BroadcastFlag is not None:
            self._BroadcastFlag = BroadcastFlag
            properties['BroadcastFlag'] = BroadcastFlag
        if RelayAgentIp is not None:
            self._RelayAgentIp = RelayAgentIp
            properties['RelayAgentIp'] = RelayAgentIp
        if ServerIp is not None:
            self._ServerIp = ServerIp
            properties['ServerIp'] = ServerIp
        if EnableRelayAgentCircuitID is not None:
            self._EnableRelayAgentCircuitID = EnableRelayAgentCircuitID
            properties['EnableRelayAgentCircuitID'] = EnableRelayAgentCircuitID
        if RelayAgentCircuitID is not None:
            self._RelayAgentCircuitID = RelayAgentCircuitID
            properties['RelayAgentCircuitID'] = RelayAgentCircuitID
        if EnableRelayAgentRemoteID is not None:
            self._EnableRelayAgentRemoteID = EnableRelayAgentRemoteID
            properties['EnableRelayAgentRemoteID'] = EnableRelayAgentRemoteID
        if RelayAgentRemoteID is not None:
            self._RelayAgentRemoteID = RelayAgentRemoteID
            properties['RelayAgentRemoteID'] = RelayAgentRemoteID

        super(Dhcpv4ClientConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        if self.force_auto_sync:
            self.get('Mode')
        return self._Mode

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def ParameterRequestList(self):
        """
        get the value of property _ParameterRequestList
        """
        if self.force_auto_sync:
            self.get('ParameterRequestList')
        return self._ParameterRequestList

    @property
    def EnableRouterOption(self):
        """
        get the value of property _EnableRouterOption
        """
        if self.force_auto_sync:
            self.get('EnableRouterOption')
        return self._EnableRouterOption

    @property
    def VendorClassIdentifier(self):
        """
        get the value of property _VendorClassIdentifier
        """
        if self.force_auto_sync:
            self.get('VendorClassIdentifier')
        return self._VendorClassIdentifier

    @property
    def BroadcastFlag(self):
        """
        get the value of property _BroadcastFlag
        """
        if self.force_auto_sync:
            self.get('BroadcastFlag')
        return self._BroadcastFlag

    @property
    def RelayAgentIp(self):
        """
        get the value of property _RelayAgentIp
        """
        if self.force_auto_sync:
            self.get('RelayAgentIp')
        return self._RelayAgentIp

    @property
    def ServerIp(self):
        """
        get the value of property _ServerIp
        """
        if self.force_auto_sync:
            self.get('ServerIp')
        return self._ServerIp

    @property
    def EnableRelayAgentCircuitID(self):
        """
        get the value of property _EnableRelayAgentCircuitID
        """
        if self.force_auto_sync:
            self.get('EnableRelayAgentCircuitID')
        return self._EnableRelayAgentCircuitID

    @property
    def RelayAgentCircuitID(self):
        """
        get the value of property _RelayAgentCircuitID
        """
        if self.force_auto_sync:
            self.get('RelayAgentCircuitID')
        return self._RelayAgentCircuitID

    @property
    def EnableRelayAgentRemoteID(self):
        """
        get the value of property _EnableRelayAgentRemoteID
        """
        if self.force_auto_sync:
            self.get('EnableRelayAgentRemoteID')
        return self._EnableRelayAgentRemoteID

    @property
    def RelayAgentRemoteID(self):
        """
        get the value of property _RelayAgentRemoteID
        """
        if self.force_auto_sync:
            self.get('RelayAgentRemoteID')
        return self._RelayAgentRemoteID

    @Mode.setter
    def Mode(self, value):
        self._Mode = value
        self.edit(Mode=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @ParameterRequestList.setter
    def ParameterRequestList(self, value):
        self._ParameterRequestList = swap_int_to_enum_flag(value, EnumRequestParameter)
        if isinstance(value, Flag):
            self.edit(ParameterRequestList=value.value)
        else:
            self.edit(ParameterRequestList=value)

    @EnableRouterOption.setter
    def EnableRouterOption(self, value):
        self._EnableRouterOption = value
        self.edit(EnableRouterOption=value)

    @VendorClassIdentifier.setter
    def VendorClassIdentifier(self, value):
        self._VendorClassIdentifier = value
        self.edit(VendorClassIdentifier=value)

    @BroadcastFlag.setter
    def BroadcastFlag(self, value):
        self._BroadcastFlag = value
        self.edit(BroadcastFlag=value)

    @RelayAgentIp.setter
    def RelayAgentIp(self, value):
        self._RelayAgentIp = value
        self.edit(RelayAgentIp=value)

    @ServerIp.setter
    def ServerIp(self, value):
        self._ServerIp = value
        self.edit(ServerIp=value)

    @EnableRelayAgentCircuitID.setter
    def EnableRelayAgentCircuitID(self, value):
        self._EnableRelayAgentCircuitID = value
        self.edit(EnableRelayAgentCircuitID=value)

    @RelayAgentCircuitID.setter
    def RelayAgentCircuitID(self, value):
        self._RelayAgentCircuitID = value
        self.edit(RelayAgentCircuitID=value)

    @EnableRelayAgentRemoteID.setter
    def EnableRelayAgentRemoteID(self, value):
        self._EnableRelayAgentRemoteID = value
        self.edit(EnableRelayAgentRemoteID=value)

    @RelayAgentRemoteID.setter
    def RelayAgentRemoteID(self, value):
        self._RelayAgentRemoteID = value
        self.edit(RelayAgentRemoteID=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumDhcpv4ClientState.%s' % value[:seperate])

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        exec('self._Mode = EnumDhcpv4ClientMode.%s' % value[:seperate])

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_parameterrequestlist_with_str(self, value):
        seperate = value.find(':')
        self._ParameterRequestList = swap_int_to_enum_flag(int(value[seperate+1:]), EnumRequestParameter)

    def _set_enablerouteroption_with_str(self, value):
        self._EnableRouterOption = (value == 'True')

    def _set_vendorclassidentifier_with_str(self, value):
        self._VendorClassIdentifier = value

    def _set_broadcastflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._BroadcastFlag = EnumDhcpv4BroadcastType.%s' % value[:seperate])

    def _set_relayagentip_with_str(self, value):
        self._RelayAgentIp = value

    def _set_serverip_with_str(self, value):
        self._ServerIp = value

    def _set_enablerelayagentcircuitid_with_str(self, value):
        self._EnableRelayAgentCircuitID = (value == 'True')

    def _set_relayagentcircuitid_with_str(self, value):
        self._RelayAgentCircuitID = value

    def _set_enablerelayagentremoteid_with_str(self, value):
        self._EnableRelayAgentRemoteID = (value == 'True')

    def _set_relayagentremoteid_with_str(self, value):
        self._RelayAgentRemoteID = value

