"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv4AddressPool(ROMObject):
    def __init__(self, PoolAddressStart=None, PoolAddressStep=None, PrefixLength=None, RouterList=None, LimitPoolCount=None, PoolAddressCount=None, DomainName=None, DnsList=None, **kwargs):
        self._PoolAddressStart = PoolAddressStart  # Pool Address Start
        self._PoolAddressStep = PoolAddressStep  # Pool Address Step
        self._PrefixLength = PrefixLength  # Prefix Length
        self._RouterList = RouterList  # Router List
        self._LimitPoolCount = LimitPoolCount  # Limit Pool Address Count
        self._PoolAddressCount = PoolAddressCount  # Pool Address Count
        self._DomainName = DomainName  # Domain Name
        self._DnsList = DnsList  # Domain Name Server List

        properties = kwargs.copy()
        if PoolAddressStart is not None:
            properties['PoolAddressStart'] = PoolAddressStart
        if PoolAddressStep is not None:
            properties['PoolAddressStep'] = PoolAddressStep
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if RouterList is not None:
            properties['RouterList'] = RouterList
        if LimitPoolCount is not None:
            properties['LimitPoolCount'] = LimitPoolCount
        if PoolAddressCount is not None:
            properties['PoolAddressCount'] = PoolAddressCount
        if DomainName is not None:
            properties['DomainName'] = DomainName
        if DnsList is not None:
            properties['DnsList'] = DnsList

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4AddressPool, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PoolAddressStart=None, PoolAddressStep=None, PrefixLength=None, RouterList=None, LimitPoolCount=None, PoolAddressCount=None, DomainName=None, DnsList=None, **kwargs):
        properties = kwargs.copy()
        if PoolAddressStart is not None:
            self._PoolAddressStart = PoolAddressStart
            properties['PoolAddressStart'] = PoolAddressStart
        if PoolAddressStep is not None:
            self._PoolAddressStep = PoolAddressStep
            properties['PoolAddressStep'] = PoolAddressStep
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if RouterList is not None:
            self._RouterList = RouterList
            properties['RouterList'] = RouterList
        if LimitPoolCount is not None:
            self._LimitPoolCount = LimitPoolCount
            properties['LimitPoolCount'] = LimitPoolCount
        if PoolAddressCount is not None:
            self._PoolAddressCount = PoolAddressCount
            properties['PoolAddressCount'] = PoolAddressCount
        if DomainName is not None:
            self._DomainName = DomainName
            properties['DomainName'] = DomainName
        if DnsList is not None:
            self._DnsList = DnsList
            properties['DnsList'] = DnsList

        super(Dhcpv4AddressPool, self).edit(**properties)

    @property
    def PoolAddressStart(self):
        """
        get the value of property _PoolAddressStart
        """
        if self.force_auto_sync:
            self.get('PoolAddressStart')
        return self._PoolAddressStart

    @property
    def PoolAddressStep(self):
        """
        get the value of property _PoolAddressStep
        """
        if self.force_auto_sync:
            self.get('PoolAddressStep')
        return self._PoolAddressStep

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def RouterList(self):
        """
        get the value of property _RouterList
        """
        if self.force_auto_sync:
            self.get('RouterList')
        return self._RouterList

    @property
    def LimitPoolCount(self):
        """
        get the value of property _LimitPoolCount
        """
        if self.force_auto_sync:
            self.get('LimitPoolCount')
        return self._LimitPoolCount

    @property
    def PoolAddressCount(self):
        """
        get the value of property _PoolAddressCount
        """
        if self.force_auto_sync:
            self.get('PoolAddressCount')
        return self._PoolAddressCount

    @property
    def DomainName(self):
        """
        get the value of property _DomainName
        """
        if self.force_auto_sync:
            self.get('DomainName')
        return self._DomainName

    @property
    def DnsList(self):
        """
        get the value of property _DnsList
        """
        if self.force_auto_sync:
            self.get('DnsList')
        return self._DnsList

    @PoolAddressStart.setter
    def PoolAddressStart(self, value):
        self._PoolAddressStart = value
        self.edit(PoolAddressStart=value)

    @PoolAddressStep.setter
    def PoolAddressStep(self, value):
        self._PoolAddressStep = value
        self.edit(PoolAddressStep=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @RouterList.setter
    def RouterList(self, value):
        self._RouterList = value
        self.edit(RouterList=value)

    @LimitPoolCount.setter
    def LimitPoolCount(self, value):
        self._LimitPoolCount = value
        self.edit(LimitPoolCount=value)

    @PoolAddressCount.setter
    def PoolAddressCount(self, value):
        self._PoolAddressCount = value
        self.edit(PoolAddressCount=value)

    @DomainName.setter
    def DomainName(self, value):
        self._DomainName = value
        self.edit(DomainName=value)

    @DnsList.setter
    def DnsList(self, value):
        self._DnsList = value
        self.edit(DnsList=value)

    def _set_pooladdressstart_with_str(self, value):
        self._PoolAddressStart = value

    def _set_pooladdressstep_with_str(self, value):
        self._PoolAddressStep = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_routerlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RouterList = tmp_value.split()

    def _set_limitpoolcount_with_str(self, value):
        self._LimitPoolCount = (value == 'True')

    def _set_pooladdresscount_with_str(self, value):
        try:
            self._PoolAddressCount = int(value)
        except ValueError:
            self._PoolAddressCount = hex(int(value, 16))

    def _set_domainname_with_str(self, value):
        self._DomainName = value

    def _set_dnslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DnsList = tmp_value.split()

