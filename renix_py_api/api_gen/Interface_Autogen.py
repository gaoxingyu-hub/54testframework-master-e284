"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Interface(ROMObject):
    def __init__(self, EnableLearningGatewayMac=None, Count=None, EnableInterfaceCount=None, RouterIdMode=None, RouterId=None, RouterIdStep=None, RouterIdList=None, Ipv6RouterId=None, Ipv6RouterIdStep=None, Ipv6RouterIdList=None, **kwargs):
        self._EnableLearningGatewayMac = EnableLearningGatewayMac  # Enable Learning Gateway MAC
        self._Count = Count  # Address Count
        self._EnableInterfaceCount = EnableInterfaceCount  # Enable Interface Count
        self._RouterIdMode = RouterIdMode  # RouterId Mode
        self._RouterId = RouterId  # IPv4 Router ID
        self._RouterIdStep = RouterIdStep  # IPv4 Router ID Step
        self._RouterIdList = RouterIdList  # IPv4 Router ID List
        self._Ipv6RouterId = Ipv6RouterId  # IPv6 Router ID
        self._Ipv6RouterIdStep = Ipv6RouterIdStep  # IPv6 Router ID Step
        self._Ipv6RouterIdList = Ipv6RouterIdList  # IPv6 Router ID List

        properties = kwargs.copy()
        if EnableLearningGatewayMac is not None:
            properties['EnableLearningGatewayMac'] = EnableLearningGatewayMac
        if Count is not None:
            properties['Count'] = Count
        if EnableInterfaceCount is not None:
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if RouterIdMode is not None:
            properties['RouterIdMode'] = RouterIdMode
        if RouterId is not None:
            properties['RouterId'] = RouterId
        if RouterIdStep is not None:
            properties['RouterIdStep'] = RouterIdStep
        if RouterIdList is not None:
            properties['RouterIdList'] = RouterIdList
        if Ipv6RouterId is not None:
            properties['Ipv6RouterId'] = Ipv6RouterId
        if Ipv6RouterIdStep is not None:
            properties['Ipv6RouterIdStep'] = Ipv6RouterIdStep
        if Ipv6RouterIdList is not None:
            properties['Ipv6RouterIdList'] = Ipv6RouterIdList

        # call base class function, and it will send message to renix server to create a class.
        super(Interface, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableLearningGatewayMac=None, Count=None, EnableInterfaceCount=None, RouterIdMode=None, RouterId=None, RouterIdStep=None, RouterIdList=None, Ipv6RouterId=None, Ipv6RouterIdStep=None, Ipv6RouterIdList=None, **kwargs):
        properties = kwargs.copy()
        if EnableLearningGatewayMac is not None:
            self._EnableLearningGatewayMac = EnableLearningGatewayMac
            properties['EnableLearningGatewayMac'] = EnableLearningGatewayMac
        if Count is not None:
            self._Count = Count
            properties['Count'] = Count
        if EnableInterfaceCount is not None:
            self._EnableInterfaceCount = EnableInterfaceCount
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if RouterIdMode is not None:
            self._RouterIdMode = RouterIdMode
            properties['RouterIdMode'] = RouterIdMode
        if RouterId is not None:
            self._RouterId = RouterId
            properties['RouterId'] = RouterId
        if RouterIdStep is not None:
            self._RouterIdStep = RouterIdStep
            properties['RouterIdStep'] = RouterIdStep
        if RouterIdList is not None:
            self._RouterIdList = RouterIdList
            properties['RouterIdList'] = RouterIdList
        if Ipv6RouterId is not None:
            self._Ipv6RouterId = Ipv6RouterId
            properties['Ipv6RouterId'] = Ipv6RouterId
        if Ipv6RouterIdStep is not None:
            self._Ipv6RouterIdStep = Ipv6RouterIdStep
            properties['Ipv6RouterIdStep'] = Ipv6RouterIdStep
        if Ipv6RouterIdList is not None:
            self._Ipv6RouterIdList = Ipv6RouterIdList
            properties['Ipv6RouterIdList'] = Ipv6RouterIdList

        super(Interface, self).edit(**properties)

    @property
    def EnableLearningGatewayMac(self):
        """
        get the value of property _EnableLearningGatewayMac
        """
        if self.force_auto_sync:
            self.get('EnableLearningGatewayMac')
        return self._EnableLearningGatewayMac

    @property
    def Count(self):
        """
        get the value of property _Count
        """
        if self.force_auto_sync:
            self.get('Count')
        return self._Count

    @property
    def EnableInterfaceCount(self):
        """
        get the value of property _EnableInterfaceCount
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceCount')
        return self._EnableInterfaceCount

    @property
    def RouterIdMode(self):
        """
        get the value of property _RouterIdMode
        """
        if self.force_auto_sync:
            self.get('RouterIdMode')
        return self._RouterIdMode

    @property
    def RouterId(self):
        """
        get the value of property _RouterId
        """
        if self.force_auto_sync:
            self.get('RouterId')
        return self._RouterId

    @property
    def RouterIdStep(self):
        """
        get the value of property _RouterIdStep
        """
        if self.force_auto_sync:
            self.get('RouterIdStep')
        return self._RouterIdStep

    @property
    def RouterIdList(self):
        """
        get the value of property _RouterIdList
        """
        if self.force_auto_sync:
            self.get('RouterIdList')
        return self._RouterIdList

    @property
    def Ipv6RouterId(self):
        """
        get the value of property _Ipv6RouterId
        """
        if self.force_auto_sync:
            self.get('Ipv6RouterId')
        return self._Ipv6RouterId

    @property
    def Ipv6RouterIdStep(self):
        """
        get the value of property _Ipv6RouterIdStep
        """
        if self.force_auto_sync:
            self.get('Ipv6RouterIdStep')
        return self._Ipv6RouterIdStep

    @property
    def Ipv6RouterIdList(self):
        """
        get the value of property _Ipv6RouterIdList
        """
        if self.force_auto_sync:
            self.get('Ipv6RouterIdList')
        return self._Ipv6RouterIdList

    @EnableLearningGatewayMac.setter
    def EnableLearningGatewayMac(self, value):
        self._EnableLearningGatewayMac = value
        self.edit(EnableLearningGatewayMac=value)

    @Count.setter
    def Count(self, value):
        self._Count = value
        self.edit(Count=value)

    @EnableInterfaceCount.setter
    def EnableInterfaceCount(self, value):
        self._EnableInterfaceCount = value
        self.edit(EnableInterfaceCount=value)

    @RouterIdMode.setter
    def RouterIdMode(self, value):
        self._RouterIdMode = value
        self.edit(RouterIdMode=value)

    @RouterId.setter
    def RouterId(self, value):
        self._RouterId = value
        self.edit(RouterId=value)

    @RouterIdStep.setter
    def RouterIdStep(self, value):
        self._RouterIdStep = value
        self.edit(RouterIdStep=value)

    @RouterIdList.setter
    def RouterIdList(self, value):
        self._RouterIdList = value
        self.edit(RouterIdList=value)

    @Ipv6RouterId.setter
    def Ipv6RouterId(self, value):
        self._Ipv6RouterId = value
        self.edit(Ipv6RouterId=value)

    @Ipv6RouterIdStep.setter
    def Ipv6RouterIdStep(self, value):
        self._Ipv6RouterIdStep = value
        self.edit(Ipv6RouterIdStep=value)

    @Ipv6RouterIdList.setter
    def Ipv6RouterIdList(self, value):
        self._Ipv6RouterIdList = value
        self.edit(Ipv6RouterIdList=value)

    def _set_enablelearninggatewaymac_with_str(self, value):
        self._EnableLearningGatewayMac = (value == 'True')

    def _set_count_with_str(self, value):
        try:
            self._Count = int(value)
        except ValueError:
            self._Count = hex(int(value, 16))

    def _set_enableinterfacecount_with_str(self, value):
        self._EnableInterfaceCount = (value == 'True')

    def _set_routeridmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterIdMode = EnumAddressMode.%s' % value[:seperate])

    def _set_routerid_with_str(self, value):
        self._RouterId = value

    def _set_routeridstep_with_str(self, value):
        self._RouterIdStep = value

    def _set_routeridlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RouterIdList = tmp_value.split()

    def _set_ipv6routerid_with_str(self, value):
        self._Ipv6RouterId = value

    def _set_ipv6routeridstep_with_str(self, value):
        self._Ipv6RouterIdStep = value

    def _set_ipv6routeridlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ipv6RouterIdList = tmp_value.split()

