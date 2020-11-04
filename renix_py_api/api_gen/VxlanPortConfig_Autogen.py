"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class VxlanPortConfig(ROMObject):
    def __init__(self, PrefixLength=None, VtepIPAddress=None, VtepIPAddressStep=None, IPv4RouterId=None, IPv4RouterIdStep=None, GatewayIPAddress=None, GatewayIPAddressStep=None, EnableVlan=None, VlanId=None, VlanCount=None, VlanIdStep=None, MacAddress=None, MacStep=None, HostsPerSegment=None, AddressMode=None, IPv6Address=None, IPv6AddressStep=None, IPv6PrefixLength=None, GatewayIPv6Address=None, GatewayStepIPv6Address=None, AttachedVtepIPAddress=None, TunnelIpMode=None, **kwargs):
        self._PrefixLength = PrefixLength  # Prefix Length
        self._VtepIPAddress = VtepIPAddress  # VTEP IP Address
        self._VtepIPAddressStep = VtepIPAddressStep  # VTEP IP Address Step
        self._IPv4RouterId = IPv4RouterId  # IPv4 Router ID
        self._IPv4RouterIdStep = IPv4RouterIdStep  # IPv4 Router ID Step
        self._GatewayIPAddress = GatewayIPAddress  # Gateway IP Address
        self._GatewayIPAddressStep = GatewayIPAddressStep  # Gateway IP Address Step
        self._EnableVlan = EnableVlan  # Enable VLAN
        self._VlanId = VlanId  # VLAN ID
        self._VlanCount = VlanCount  # VLAN Count
        self._VlanIdStep = VlanIdStep  # VLAN ID Step
        self._MacAddress = MacAddress  # MAC Address
        self._MacStep = MacStep  # MAC Address Step
        self._HostsPerSegment = HostsPerSegment  # Hosts per Segment
        self._AddressMode = AddressMode  # Address Mode
        self._IPv6Address = IPv6Address  # IPv6 Address
        self._IPv6AddressStep = IPv6AddressStep  # IPv6 Address Step
        self._IPv6PrefixLength = IPv6PrefixLength  # IPv6 Prefix Length
        self._GatewayIPv6Address = GatewayIPv6Address  # IPv6 Gateway Address
        self._GatewayStepIPv6Address = GatewayStepIPv6Address  # IPv6 Gateway Address Step
        self._AttachedVtepIPAddress = AttachedVtepIPAddress  # Attached VTEP IP Address
        self._TunnelIpMode = TunnelIpMode  # Tunnel Ip Mode

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if VtepIPAddress is not None:
            properties['VtepIPAddress'] = VtepIPAddress
        if VtepIPAddressStep is not None:
            properties['VtepIPAddressStep'] = VtepIPAddressStep
        if IPv4RouterId is not None:
            properties['IPv4RouterId'] = IPv4RouterId
        if IPv4RouterIdStep is not None:
            properties['IPv4RouterIdStep'] = IPv4RouterIdStep
        if GatewayIPAddress is not None:
            properties['GatewayIPAddress'] = GatewayIPAddress
        if GatewayIPAddressStep is not None:
            properties['GatewayIPAddressStep'] = GatewayIPAddressStep
        if EnableVlan is not None:
            properties['EnableVlan'] = EnableVlan
        if VlanId is not None:
            properties['VlanId'] = VlanId
        if VlanCount is not None:
            properties['VlanCount'] = VlanCount
        if VlanIdStep is not None:
            properties['VlanIdStep'] = VlanIdStep
        if MacAddress is not None:
            properties['MacAddress'] = MacAddress
        if MacStep is not None:
            properties['MacStep'] = MacStep
        if HostsPerSegment is not None:
            properties['HostsPerSegment'] = HostsPerSegment
        if AddressMode is not None:
            properties['AddressMode'] = AddressMode
        if IPv6Address is not None:
            properties['IPv6Address'] = IPv6Address
        if IPv6AddressStep is not None:
            properties['IPv6AddressStep'] = IPv6AddressStep
        if IPv6PrefixLength is not None:
            properties['IPv6PrefixLength'] = IPv6PrefixLength
        if GatewayIPv6Address is not None:
            properties['GatewayIPv6Address'] = GatewayIPv6Address
        if GatewayStepIPv6Address is not None:
            properties['GatewayStepIPv6Address'] = GatewayStepIPv6Address
        if AttachedVtepIPAddress is not None:
            properties['AttachedVtepIPAddress'] = AttachedVtepIPAddress
        if TunnelIpMode is not None:
            properties['TunnelIpMode'] = TunnelIpMode

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, VtepIPAddress=None, VtepIPAddressStep=None, IPv4RouterId=None, IPv4RouterIdStep=None, GatewayIPAddress=None, GatewayIPAddressStep=None, EnableVlan=None, VlanId=None, VlanCount=None, VlanIdStep=None, MacAddress=None, MacStep=None, HostsPerSegment=None, AddressMode=None, IPv6Address=None, IPv6AddressStep=None, IPv6PrefixLength=None, GatewayIPv6Address=None, GatewayStepIPv6Address=None, AttachedVtepIPAddress=None, TunnelIpMode=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if VtepIPAddress is not None:
            self._VtepIPAddress = VtepIPAddress
            properties['VtepIPAddress'] = VtepIPAddress
        if VtepIPAddressStep is not None:
            self._VtepIPAddressStep = VtepIPAddressStep
            properties['VtepIPAddressStep'] = VtepIPAddressStep
        if IPv4RouterId is not None:
            self._IPv4RouterId = IPv4RouterId
            properties['IPv4RouterId'] = IPv4RouterId
        if IPv4RouterIdStep is not None:
            self._IPv4RouterIdStep = IPv4RouterIdStep
            properties['IPv4RouterIdStep'] = IPv4RouterIdStep
        if GatewayIPAddress is not None:
            self._GatewayIPAddress = GatewayIPAddress
            properties['GatewayIPAddress'] = GatewayIPAddress
        if GatewayIPAddressStep is not None:
            self._GatewayIPAddressStep = GatewayIPAddressStep
            properties['GatewayIPAddressStep'] = GatewayIPAddressStep
        if EnableVlan is not None:
            self._EnableVlan = EnableVlan
            properties['EnableVlan'] = EnableVlan
        if VlanId is not None:
            self._VlanId = VlanId
            properties['VlanId'] = VlanId
        if VlanCount is not None:
            self._VlanCount = VlanCount
            properties['VlanCount'] = VlanCount
        if VlanIdStep is not None:
            self._VlanIdStep = VlanIdStep
            properties['VlanIdStep'] = VlanIdStep
        if MacAddress is not None:
            self._MacAddress = MacAddress
            properties['MacAddress'] = MacAddress
        if MacStep is not None:
            self._MacStep = MacStep
            properties['MacStep'] = MacStep
        if HostsPerSegment is not None:
            self._HostsPerSegment = HostsPerSegment
            properties['HostsPerSegment'] = HostsPerSegment
        if AddressMode is not None:
            self._AddressMode = AddressMode
            properties['AddressMode'] = AddressMode
        if IPv6Address is not None:
            self._IPv6Address = IPv6Address
            properties['IPv6Address'] = IPv6Address
        if IPv6AddressStep is not None:
            self._IPv6AddressStep = IPv6AddressStep
            properties['IPv6AddressStep'] = IPv6AddressStep
        if IPv6PrefixLength is not None:
            self._IPv6PrefixLength = IPv6PrefixLength
            properties['IPv6PrefixLength'] = IPv6PrefixLength
        if GatewayIPv6Address is not None:
            self._GatewayIPv6Address = GatewayIPv6Address
            properties['GatewayIPv6Address'] = GatewayIPv6Address
        if GatewayStepIPv6Address is not None:
            self._GatewayStepIPv6Address = GatewayStepIPv6Address
            properties['GatewayStepIPv6Address'] = GatewayStepIPv6Address
        if AttachedVtepIPAddress is not None:
            self._AttachedVtepIPAddress = AttachedVtepIPAddress
            properties['AttachedVtepIPAddress'] = AttachedVtepIPAddress
        if TunnelIpMode is not None:
            self._TunnelIpMode = TunnelIpMode
            properties['TunnelIpMode'] = TunnelIpMode

        super(VxlanPortConfig, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def VtepIPAddress(self):
        """
        get the value of property _VtepIPAddress
        """
        if self.force_auto_sync:
            self.get('VtepIPAddress')
        return self._VtepIPAddress

    @property
    def VtepIPAddressStep(self):
        """
        get the value of property _VtepIPAddressStep
        """
        if self.force_auto_sync:
            self.get('VtepIPAddressStep')
        return self._VtepIPAddressStep

    @property
    def IPv4RouterId(self):
        """
        get the value of property _IPv4RouterId
        """
        if self.force_auto_sync:
            self.get('IPv4RouterId')
        return self._IPv4RouterId

    @property
    def IPv4RouterIdStep(self):
        """
        get the value of property _IPv4RouterIdStep
        """
        if self.force_auto_sync:
            self.get('IPv4RouterIdStep')
        return self._IPv4RouterIdStep

    @property
    def GatewayIPAddress(self):
        """
        get the value of property _GatewayIPAddress
        """
        if self.force_auto_sync:
            self.get('GatewayIPAddress')
        return self._GatewayIPAddress

    @property
    def GatewayIPAddressStep(self):
        """
        get the value of property _GatewayIPAddressStep
        """
        if self.force_auto_sync:
            self.get('GatewayIPAddressStep')
        return self._GatewayIPAddressStep

    @property
    def EnableVlan(self):
        """
        get the value of property _EnableVlan
        """
        if self.force_auto_sync:
            self.get('EnableVlan')
        return self._EnableVlan

    @property
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def VlanCount(self):
        """
        get the value of property _VlanCount
        """
        if self.force_auto_sync:
            self.get('VlanCount')
        return self._VlanCount

    @property
    def VlanIdStep(self):
        """
        get the value of property _VlanIdStep
        """
        if self.force_auto_sync:
            self.get('VlanIdStep')
        return self._VlanIdStep

    @property
    def MacAddress(self):
        """
        get the value of property _MacAddress
        """
        if self.force_auto_sync:
            self.get('MacAddress')
        return self._MacAddress

    @property
    def MacStep(self):
        """
        get the value of property _MacStep
        """
        if self.force_auto_sync:
            self.get('MacStep')
        return self._MacStep

    @property
    def HostsPerSegment(self):
        """
        get the value of property _HostsPerSegment
        """
        if self.force_auto_sync:
            self.get('HostsPerSegment')
        return self._HostsPerSegment

    @property
    def AddressMode(self):
        """
        get the value of property _AddressMode
        """
        if self.force_auto_sync:
            self.get('AddressMode')
        return self._AddressMode

    @property
    def IPv6Address(self):
        """
        get the value of property _IPv6Address
        """
        if self.force_auto_sync:
            self.get('IPv6Address')
        return self._IPv6Address

    @property
    def IPv6AddressStep(self):
        """
        get the value of property _IPv6AddressStep
        """
        if self.force_auto_sync:
            self.get('IPv6AddressStep')
        return self._IPv6AddressStep

    @property
    def IPv6PrefixLength(self):
        """
        get the value of property _IPv6PrefixLength
        """
        if self.force_auto_sync:
            self.get('IPv6PrefixLength')
        return self._IPv6PrefixLength

    @property
    def GatewayIPv6Address(self):
        """
        get the value of property _GatewayIPv6Address
        """
        if self.force_auto_sync:
            self.get('GatewayIPv6Address')
        return self._GatewayIPv6Address

    @property
    def GatewayStepIPv6Address(self):
        """
        get the value of property _GatewayStepIPv6Address
        """
        if self.force_auto_sync:
            self.get('GatewayStepIPv6Address')
        return self._GatewayStepIPv6Address

    @property
    def AttachedVtepIPAddress(self):
        """
        get the value of property _AttachedVtepIPAddress
        """
        if self.force_auto_sync:
            self.get('AttachedVtepIPAddress')
        return self._AttachedVtepIPAddress

    @property
    def TunnelIpMode(self):
        """
        get the value of property _TunnelIpMode
        """
        if self.force_auto_sync:
            self.get('TunnelIpMode')
        return self._TunnelIpMode

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @VtepIPAddress.setter
    def VtepIPAddress(self, value):
        self._VtepIPAddress = value
        self.edit(VtepIPAddress=value)

    @VtepIPAddressStep.setter
    def VtepIPAddressStep(self, value):
        self._VtepIPAddressStep = value
        self.edit(VtepIPAddressStep=value)

    @IPv4RouterId.setter
    def IPv4RouterId(self, value):
        self._IPv4RouterId = value
        self.edit(IPv4RouterId=value)

    @IPv4RouterIdStep.setter
    def IPv4RouterIdStep(self, value):
        self._IPv4RouterIdStep = value
        self.edit(IPv4RouterIdStep=value)

    @GatewayIPAddress.setter
    def GatewayIPAddress(self, value):
        self._GatewayIPAddress = value
        self.edit(GatewayIPAddress=value)

    @GatewayIPAddressStep.setter
    def GatewayIPAddressStep(self, value):
        self._GatewayIPAddressStep = value
        self.edit(GatewayIPAddressStep=value)

    @EnableVlan.setter
    def EnableVlan(self, value):
        self._EnableVlan = value
        self.edit(EnableVlan=value)

    @VlanId.setter
    def VlanId(self, value):
        self._VlanId = value
        self.edit(VlanId=value)

    @VlanCount.setter
    def VlanCount(self, value):
        self._VlanCount = value
        self.edit(VlanCount=value)

    @VlanIdStep.setter
    def VlanIdStep(self, value):
        self._VlanIdStep = value
        self.edit(VlanIdStep=value)

    @MacAddress.setter
    def MacAddress(self, value):
        self._MacAddress = value
        self.edit(MacAddress=value)

    @MacStep.setter
    def MacStep(self, value):
        self._MacStep = value
        self.edit(MacStep=value)

    @HostsPerSegment.setter
    def HostsPerSegment(self, value):
        self._HostsPerSegment = value
        self.edit(HostsPerSegment=value)

    @AddressMode.setter
    def AddressMode(self, value):
        self._AddressMode = value
        self.edit(AddressMode=value)

    @IPv6Address.setter
    def IPv6Address(self, value):
        self._IPv6Address = value
        self.edit(IPv6Address=value)

    @IPv6AddressStep.setter
    def IPv6AddressStep(self, value):
        self._IPv6AddressStep = value
        self.edit(IPv6AddressStep=value)

    @IPv6PrefixLength.setter
    def IPv6PrefixLength(self, value):
        self._IPv6PrefixLength = value
        self.edit(IPv6PrefixLength=value)

    @GatewayIPv6Address.setter
    def GatewayIPv6Address(self, value):
        self._GatewayIPv6Address = value
        self.edit(GatewayIPv6Address=value)

    @GatewayStepIPv6Address.setter
    def GatewayStepIPv6Address(self, value):
        self._GatewayStepIPv6Address = value
        self.edit(GatewayStepIPv6Address=value)

    @AttachedVtepIPAddress.setter
    def AttachedVtepIPAddress(self, value):
        self._AttachedVtepIPAddress = value
        self.edit(AttachedVtepIPAddress=value)

    @TunnelIpMode.setter
    def TunnelIpMode(self, value):
        self._TunnelIpMode = value
        self.edit(TunnelIpMode=value)

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_vtepipaddress_with_str(self, value):
        self._VtepIPAddress = value

    def _set_vtepipaddressstep_with_str(self, value):
        self._VtepIPAddressStep = value

    def _set_ipv4routerid_with_str(self, value):
        self._IPv4RouterId = value

    def _set_ipv4routeridstep_with_str(self, value):
        self._IPv4RouterIdStep = value

    def _set_gatewayipaddress_with_str(self, value):
        self._GatewayIPAddress = value

    def _set_gatewayipaddressstep_with_str(self, value):
        self._GatewayIPAddressStep = value

    def _set_enablevlan_with_str(self, value):
        self._EnableVlan = (value == 'True')

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_vlancount_with_str(self, value):
        try:
            self._VlanCount = int(value)
        except ValueError:
            self._VlanCount = hex(int(value, 16))

    def _set_vlanidstep_with_str(self, value):
        try:
            self._VlanIdStep = int(value)
        except ValueError:
            self._VlanIdStep = hex(int(value, 16))

    def _set_macaddress_with_str(self, value):
        self._MacAddress = value

    def _set_macstep_with_str(self, value):
        self._MacStep = value

    def _set_hostspersegment_with_str(self, value):
        try:
            self._HostsPerSegment = int(value)
        except ValueError:
            self._HostsPerSegment = hex(int(value, 16))

    def _set_addressmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddressMode = EnumVxlanAddressMode.%s' % value[:seperate])

    def _set_ipv6address_with_str(self, value):
        self._IPv6Address = value

    def _set_ipv6addressstep_with_str(self, value):
        self._IPv6AddressStep = value

    def _set_ipv6prefixlength_with_str(self, value):
        try:
            self._IPv6PrefixLength = int(value)
        except ValueError:
            self._IPv6PrefixLength = hex(int(value, 16))

    def _set_gatewayipv6address_with_str(self, value):
        self._GatewayIPv6Address = value

    def _set_gatewaystepipv6address_with_str(self, value):
        self._GatewayStepIPv6Address = value

    def _set_attachedvtepipaddress_with_str(self, value):
        self._AttachedVtepIPAddress = value

    def _set_tunnelipmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TunnelIpMode = EnumTunnelIpAddress.%s' % value[:seperate])

