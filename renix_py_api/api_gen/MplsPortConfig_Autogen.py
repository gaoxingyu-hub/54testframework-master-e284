"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class MplsPortConfig(ROMObject):
    def __init__(self, EnableInterfaceBlock=None, InterfaceBockCount=None, Encapsulation=None, DutIPAddress=None, DutIPAddressStep=None, PrefixLength=None, IPv6Address=None, IPv6AddressStep=None, IPv6PrefixLength=None, VlanId=None, VlanIdStep=None, **kwargs):
        self._EnableInterfaceBlock = EnableInterfaceBlock  # Enable Interface Block
        self._InterfaceBockCount = InterfaceBockCount  # Interface Block Count
        self._Encapsulation = Encapsulation  # Encapsulation Type
        self._DutIPAddress = DutIPAddress  # DUT IP Address
        self._DutIPAddressStep = DutIPAddressStep  # DUT IP Address Step
        self._PrefixLength = PrefixLength  # Prefix Length
        self._IPv6Address = IPv6Address  # IPv6 Address
        self._IPv6AddressStep = IPv6AddressStep  # IPv6 Address Step
        self._IPv6PrefixLength = IPv6PrefixLength  # IPv6 Prefix Length
        self._VlanId = VlanId  # VLAN ID
        self._VlanIdStep = VlanIdStep  # VLAN ID Step

        properties = kwargs.copy()
        if EnableInterfaceBlock is not None:
            properties['EnableInterfaceBlock'] = EnableInterfaceBlock
        if InterfaceBockCount is not None:
            properties['InterfaceBockCount'] = InterfaceBockCount
        if Encapsulation is not None:
            properties['Encapsulation'] = Encapsulation
        if DutIPAddress is not None:
            properties['DutIPAddress'] = DutIPAddress
        if DutIPAddressStep is not None:
            properties['DutIPAddressStep'] = DutIPAddressStep
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if IPv6Address is not None:
            properties['IPv6Address'] = IPv6Address
        if IPv6AddressStep is not None:
            properties['IPv6AddressStep'] = IPv6AddressStep
        if IPv6PrefixLength is not None:
            properties['IPv6PrefixLength'] = IPv6PrefixLength
        if VlanId is not None:
            properties['VlanId'] = VlanId
        if VlanIdStep is not None:
            properties['VlanIdStep'] = VlanIdStep

        # call base class function, and it will send message to renix server to create a class.
        super(MplsPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableInterfaceBlock=None, InterfaceBockCount=None, Encapsulation=None, DutIPAddress=None, DutIPAddressStep=None, PrefixLength=None, IPv6Address=None, IPv6AddressStep=None, IPv6PrefixLength=None, VlanId=None, VlanIdStep=None, **kwargs):
        properties = kwargs.copy()
        if EnableInterfaceBlock is not None:
            self._EnableInterfaceBlock = EnableInterfaceBlock
            properties['EnableInterfaceBlock'] = EnableInterfaceBlock
        if InterfaceBockCount is not None:
            self._InterfaceBockCount = InterfaceBockCount
            properties['InterfaceBockCount'] = InterfaceBockCount
        if Encapsulation is not None:
            self._Encapsulation = Encapsulation
            properties['Encapsulation'] = Encapsulation
        if DutIPAddress is not None:
            self._DutIPAddress = DutIPAddress
            properties['DutIPAddress'] = DutIPAddress
        if DutIPAddressStep is not None:
            self._DutIPAddressStep = DutIPAddressStep
            properties['DutIPAddressStep'] = DutIPAddressStep
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if IPv6Address is not None:
            self._IPv6Address = IPv6Address
            properties['IPv6Address'] = IPv6Address
        if IPv6AddressStep is not None:
            self._IPv6AddressStep = IPv6AddressStep
            properties['IPv6AddressStep'] = IPv6AddressStep
        if IPv6PrefixLength is not None:
            self._IPv6PrefixLength = IPv6PrefixLength
            properties['IPv6PrefixLength'] = IPv6PrefixLength
        if VlanId is not None:
            self._VlanId = VlanId
            properties['VlanId'] = VlanId
        if VlanIdStep is not None:
            self._VlanIdStep = VlanIdStep
            properties['VlanIdStep'] = VlanIdStep

        super(MplsPortConfig, self).edit(**properties)

    @property
    def EnableInterfaceBlock(self):
        """
        get the value of property _EnableInterfaceBlock
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceBlock')
        return self._EnableInterfaceBlock

    @property
    def InterfaceBockCount(self):
        """
        get the value of property _InterfaceBockCount
        """
        if self.force_auto_sync:
            self.get('InterfaceBockCount')
        return self._InterfaceBockCount

    @property
    def Encapsulation(self):
        """
        get the value of property _Encapsulation
        """
        if self.force_auto_sync:
            self.get('Encapsulation')
        return self._Encapsulation

    @property
    def DutIPAddress(self):
        """
        get the value of property _DutIPAddress
        """
        if self.force_auto_sync:
            self.get('DutIPAddress')
        return self._DutIPAddress

    @property
    def DutIPAddressStep(self):
        """
        get the value of property _DutIPAddressStep
        """
        if self.force_auto_sync:
            self.get('DutIPAddressStep')
        return self._DutIPAddressStep

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

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
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def VlanIdStep(self):
        """
        get the value of property _VlanIdStep
        """
        if self.force_auto_sync:
            self.get('VlanIdStep')
        return self._VlanIdStep

    @EnableInterfaceBlock.setter
    def EnableInterfaceBlock(self, value):
        self._EnableInterfaceBlock = value
        self.edit(EnableInterfaceBlock=value)

    @InterfaceBockCount.setter
    def InterfaceBockCount(self, value):
        self._InterfaceBockCount = value
        self.edit(InterfaceBockCount=value)

    @Encapsulation.setter
    def Encapsulation(self, value):
        self._Encapsulation = value
        self.edit(Encapsulation=value)

    @DutIPAddress.setter
    def DutIPAddress(self, value):
        self._DutIPAddress = value
        self.edit(DutIPAddress=value)

    @DutIPAddressStep.setter
    def DutIPAddressStep(self, value):
        self._DutIPAddressStep = value
        self.edit(DutIPAddressStep=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

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

    @VlanId.setter
    def VlanId(self, value):
        self._VlanId = value
        self.edit(VlanId=value)

    @VlanIdStep.setter
    def VlanIdStep(self, value):
        self._VlanIdStep = value
        self.edit(VlanIdStep=value)

    def _set_enableinterfaceblock_with_str(self, value):
        self._EnableInterfaceBlock = (value == 'True')

    def _set_interfacebockcount_with_str(self, value):
        try:
            self._InterfaceBockCount = int(value)
        except ValueError:
            self._InterfaceBockCount = hex(int(value, 16))

    def _set_encapsulation_with_str(self, value):
        seperate = value.find(':')
        exec('self._Encapsulation = EnumMplsEncapsulationType.%s' % value[:seperate])

    def _set_dutipaddress_with_str(self, value):
        self._DutIPAddress = value

    def _set_dutipaddressstep_with_str(self, value):
        self._DutIPAddressStep = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_ipv6address_with_str(self, value):
        self._IPv6Address = value

    def _set_ipv6addressstep_with_str(self, value):
        self._IPv6AddressStep = value

    def _set_ipv6prefixlength_with_str(self, value):
        try:
            self._IPv6PrefixLength = int(value)
        except ValueError:
            self._IPv6PrefixLength = hex(int(value, 16))

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_vlanidstep_with_str(self, value):
        try:
            self._VlanIdStep = int(value)
        except ValueError:
            self._VlanIdStep = hex(int(value, 16))

