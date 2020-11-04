"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayer_Autogen import NetworkLayer


@rom_manager.rom
class Ipv4Layer(NetworkLayer):
    def __init__(self, Address=None, Step=None, AddressList=None, PrefixLength=None, Gateway=None, GatewayStep=None, GatewayList=None, GatewayCount=None, GatewayMac=None, **kwargs):
        self._Address = Address  # IPv4 Address
        self._Step = Step  # IPv4 Address Step
        self._AddressList = AddressList  # IPv4 Address List
        self._PrefixLength = PrefixLength  # IPv4 Prefix Length
        self._Gateway = Gateway  # IPv4 Gateway Address
        self._GatewayStep = GatewayStep  # IPv4 Gateway Address Step
        self._GatewayList = GatewayList  # IPv4 Gateway List
        self._GatewayCount = GatewayCount  # IPv4 Gateway Count
        self._GatewayMac = GatewayMac  # IPv4 Gateway MAC Address
        self._ResolvedMacList = None  # Resolved MAC Address List, not editable

        properties = kwargs.copy()
        if Address is not None:
            properties['Address'] = Address
        if Step is not None:
            properties['Step'] = Step
        if AddressList is not None:
            properties['AddressList'] = AddressList
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if Gateway is not None:
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            properties['GatewayStep'] = GatewayStep
        if GatewayList is not None:
            properties['GatewayList'] = GatewayList
        if GatewayCount is not None:
            properties['GatewayCount'] = GatewayCount
        if GatewayMac is not None:
            properties['GatewayMac'] = GatewayMac

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv4Layer, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Address=None, Step=None, AddressList=None, PrefixLength=None, Gateway=None, GatewayStep=None, GatewayList=None, GatewayCount=None, GatewayMac=None, **kwargs):
        properties = kwargs.copy()
        if Address is not None:
            self._Address = Address
            properties['Address'] = Address
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if AddressList is not None:
            self._AddressList = AddressList
            properties['AddressList'] = AddressList
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if Gateway is not None:
            self._Gateway = Gateway
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            self._GatewayStep = GatewayStep
            properties['GatewayStep'] = GatewayStep
        if GatewayList is not None:
            self._GatewayList = GatewayList
            properties['GatewayList'] = GatewayList
        if GatewayCount is not None:
            self._GatewayCount = GatewayCount
            properties['GatewayCount'] = GatewayCount
        if GatewayMac is not None:
            self._GatewayMac = GatewayMac
            properties['GatewayMac'] = GatewayMac

        super(Ipv4Layer, self).edit(**properties)

    @property
    def Address(self):
        """
        get the value of property _Address
        """
        if self.force_auto_sync:
            self.get('Address')
        return self._Address

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def AddressList(self):
        """
        get the value of property _AddressList
        """
        if self.force_auto_sync:
            self.get('AddressList')
        return self._AddressList

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def Gateway(self):
        """
        get the value of property _Gateway
        """
        if self.force_auto_sync:
            self.get('Gateway')
        return self._Gateway

    @property
    def GatewayStep(self):
        """
        get the value of property _GatewayStep
        """
        if self.force_auto_sync:
            self.get('GatewayStep')
        return self._GatewayStep

    @property
    def GatewayList(self):
        """
        get the value of property _GatewayList
        """
        if self.force_auto_sync:
            self.get('GatewayList')
        return self._GatewayList

    @property
    def GatewayCount(self):
        """
        get the value of property _GatewayCount
        """
        if self.force_auto_sync:
            self.get('GatewayCount')
        return self._GatewayCount

    @property
    def GatewayMac(self):
        """
        get the value of property _GatewayMac
        """
        if self.force_auto_sync:
            self.get('GatewayMac')
        return self._GatewayMac

    @property
    def ResolvedMacList(self):
        """
        get the value of property _ResolvedMacList
        """
        if self.force_auto_sync:
            self.get('ResolvedMacList')
        return self._ResolvedMacList

    @Address.setter
    def Address(self, value):
        self._Address = value
        self.edit(Address=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @AddressList.setter
    def AddressList(self, value):
        self._AddressList = value
        self.edit(AddressList=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @Gateway.setter
    def Gateway(self, value):
        self._Gateway = value
        self.edit(Gateway=value)

    @GatewayStep.setter
    def GatewayStep(self, value):
        self._GatewayStep = value
        self.edit(GatewayStep=value)

    @GatewayList.setter
    def GatewayList(self, value):
        self._GatewayList = value
        self.edit(GatewayList=value)

    @GatewayCount.setter
    def GatewayCount(self, value):
        self._GatewayCount = value
        self.edit(GatewayCount=value)

    @GatewayMac.setter
    def GatewayMac(self, value):
        self._GatewayMac = value
        self.edit(GatewayMac=value)

    def _set_address_with_str(self, value):
        self._Address = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_addresslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AddressList = tmp_value.split()

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_gateway_with_str(self, value):
        self._Gateway = value

    def _set_gatewaystep_with_str(self, value):
        self._GatewayStep = value

    def _set_gatewaylist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._GatewayList = tmp_value.split()

    def _set_gatewaycount_with_str(self, value):
        try:
            self._GatewayCount = int(value)
        except ValueError:
            self._GatewayCount = hex(int(value, 16))

    def _set_gatewaymac_with_str(self, value):
        self._GatewayMac = value

    def _set_resolvedmaclist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ResolvedMacList = tmp_value.split()

