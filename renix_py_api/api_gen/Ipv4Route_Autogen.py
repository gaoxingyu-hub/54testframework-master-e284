"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DynamicNetworkLayer_Autogen import DynamicNetworkLayer


@rom_manager.rom
class Ipv4Route(DynamicNetworkLayer):
    def __init__(self, NetworkAddress=None, Step=None, PrefixLength=None, NetworkList=None, NextHopList=None, PrefixLengthList=None, **kwargs):
        self._NetworkAddress = NetworkAddress  # NetWork Address
        self._Step = Step  # IPv4 Address Step
        self._PrefixLength = PrefixLength  # IPv4 Prefix Length
        self._NetworkList = NetworkList  # NetWork List
        self._NextHopList = NextHopList  # Next Hop List
        self._PrefixLengthList = PrefixLengthList  # IPv4 Prefix Length List

        properties = kwargs.copy()
        if NetworkAddress is not None:
            properties['NetworkAddress'] = NetworkAddress
        if Step is not None:
            properties['Step'] = Step
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if NetworkList is not None:
            properties['NetworkList'] = NetworkList
        if NextHopList is not None:
            properties['NextHopList'] = NextHopList
        if PrefixLengthList is not None:
            properties['PrefixLengthList'] = PrefixLengthList

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv4Route, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NetworkAddress=None, Step=None, PrefixLength=None, NetworkList=None, NextHopList=None, PrefixLengthList=None, **kwargs):
        properties = kwargs.copy()
        if NetworkAddress is not None:
            self._NetworkAddress = NetworkAddress
            properties['NetworkAddress'] = NetworkAddress
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if NetworkList is not None:
            self._NetworkList = NetworkList
            properties['NetworkList'] = NetworkList
        if NextHopList is not None:
            self._NextHopList = NextHopList
            properties['NextHopList'] = NextHopList
        if PrefixLengthList is not None:
            self._PrefixLengthList = PrefixLengthList
            properties['PrefixLengthList'] = PrefixLengthList

        super(Ipv4Route, self).edit(**properties)

    @property
    def NetworkAddress(self):
        """
        get the value of property _NetworkAddress
        """
        if self.force_auto_sync:
            self.get('NetworkAddress')
        return self._NetworkAddress

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def NetworkList(self):
        """
        get the value of property _NetworkList
        """
        if self.force_auto_sync:
            self.get('NetworkList')
        return self._NetworkList

    @property
    def NextHopList(self):
        """
        get the value of property _NextHopList
        """
        if self.force_auto_sync:
            self.get('NextHopList')
        return self._NextHopList

    @property
    def PrefixLengthList(self):
        """
        get the value of property _PrefixLengthList
        """
        if self.force_auto_sync:
            self.get('PrefixLengthList')
        return self._PrefixLengthList

    @NetworkAddress.setter
    def NetworkAddress(self, value):
        self._NetworkAddress = value
        self.edit(NetworkAddress=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @NetworkList.setter
    def NetworkList(self, value):
        self._NetworkList = value
        self.edit(NetworkList=value)

    @NextHopList.setter
    def NextHopList(self, value):
        self._NextHopList = value
        self.edit(NextHopList=value)

    @PrefixLengthList.setter
    def PrefixLengthList(self, value):
        self._PrefixLengthList = value
        self.edit(PrefixLengthList=value)

    def _set_networkaddress_with_str(self, value):
        self._NetworkAddress = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_networklist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._NetworkList = tmp_value.split()

    def _set_nexthoplist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._NextHopList = tmp_value.split()

    def _set_prefixlengthlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PrefixLengthList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._PrefixLengthList.append(int(str_value))
            except ValueError:
                self._PrefixLengthList.append(hex(int(str_value, 16)))

