"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class InterfaceWizardConfig(WizardConfigBase):
    def __init__(self, CountPerPort=None, CountPerInterfaceBlcok=None, EnableEthernet=None, EnableVlan=None, VlanHeaderCount=None, EnableIPv4=None, EnableIPv6=None, EnablePppoe=None, EnableInterfaceCount=None, EnableLearningGatewayMac=None, RouterId=None, RouterIdStep=None, Ipv6RouterId=None, Ipv6RouterIdStep=None, **kwargs):
        self._CountPerPort = CountPerPort  # Number of Interfaces Per Port
        self._CountPerInterfaceBlcok = CountPerInterfaceBlcok  # Address Count
        self._EnableEthernet = EnableEthernet  # Enable Ethernet
        self._EnableVlan = EnableVlan  # Enable VLAN
        self._VlanHeaderCount = VlanHeaderCount  # VLAN Header Count
        self._EnableIPv4 = EnableIPv4  # Enable IPv4
        self._EnableIPv6 = EnableIPv6  # Enable IPv6
        self._EnablePppoe = EnablePppoe  # Enable PPPoE
        self._EnableInterfaceCount = EnableInterfaceCount  # Enable Interface Count
        self._EnableLearningGatewayMac = EnableLearningGatewayMac  # Enable Learning Gateway MAC
        self._RouterId = RouterId  # IPv4 Router ID
        self._RouterIdStep = RouterIdStep  # IPv4 Router ID Step
        self._Ipv6RouterId = Ipv6RouterId  # IPv6 Router ID
        self._Ipv6RouterIdStep = Ipv6RouterIdStep  # IPv6 Router ID Step

        properties = kwargs.copy()
        if CountPerPort is not None:
            properties['CountPerPort'] = CountPerPort
        if CountPerInterfaceBlcok is not None:
            properties['CountPerInterfaceBlcok'] = CountPerInterfaceBlcok
        if EnableEthernet is not None:
            properties['EnableEthernet'] = EnableEthernet
        if EnableVlan is not None:
            properties['EnableVlan'] = EnableVlan
        if VlanHeaderCount is not None:
            properties['VlanHeaderCount'] = VlanHeaderCount
        if EnableIPv4 is not None:
            properties['EnableIPv4'] = EnableIPv4
        if EnableIPv6 is not None:
            properties['EnableIPv6'] = EnableIPv6
        if EnablePppoe is not None:
            properties['EnablePppoe'] = EnablePppoe
        if EnableInterfaceCount is not None:
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if EnableLearningGatewayMac is not None:
            properties['EnableLearningGatewayMac'] = EnableLearningGatewayMac
        if RouterId is not None:
            properties['RouterId'] = RouterId
        if RouterIdStep is not None:
            properties['RouterIdStep'] = RouterIdStep
        if Ipv6RouterId is not None:
            properties['Ipv6RouterId'] = Ipv6RouterId
        if Ipv6RouterIdStep is not None:
            properties['Ipv6RouterIdStep'] = Ipv6RouterIdStep

        # call base class function, and it will send message to renix server to create a class.
        super(InterfaceWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CountPerPort=None, CountPerInterfaceBlcok=None, EnableEthernet=None, EnableVlan=None, VlanHeaderCount=None, EnableIPv4=None, EnableIPv6=None, EnablePppoe=None, EnableInterfaceCount=None, EnableLearningGatewayMac=None, RouterId=None, RouterIdStep=None, Ipv6RouterId=None, Ipv6RouterIdStep=None, **kwargs):
        properties = kwargs.copy()
        if CountPerPort is not None:
            self._CountPerPort = CountPerPort
            properties['CountPerPort'] = CountPerPort
        if CountPerInterfaceBlcok is not None:
            self._CountPerInterfaceBlcok = CountPerInterfaceBlcok
            properties['CountPerInterfaceBlcok'] = CountPerInterfaceBlcok
        if EnableEthernet is not None:
            self._EnableEthernet = EnableEthernet
            properties['EnableEthernet'] = EnableEthernet
        if EnableVlan is not None:
            self._EnableVlan = EnableVlan
            properties['EnableVlan'] = EnableVlan
        if VlanHeaderCount is not None:
            self._VlanHeaderCount = VlanHeaderCount
            properties['VlanHeaderCount'] = VlanHeaderCount
        if EnableIPv4 is not None:
            self._EnableIPv4 = EnableIPv4
            properties['EnableIPv4'] = EnableIPv4
        if EnableIPv6 is not None:
            self._EnableIPv6 = EnableIPv6
            properties['EnableIPv6'] = EnableIPv6
        if EnablePppoe is not None:
            self._EnablePppoe = EnablePppoe
            properties['EnablePppoe'] = EnablePppoe
        if EnableInterfaceCount is not None:
            self._EnableInterfaceCount = EnableInterfaceCount
            properties['EnableInterfaceCount'] = EnableInterfaceCount
        if EnableLearningGatewayMac is not None:
            self._EnableLearningGatewayMac = EnableLearningGatewayMac
            properties['EnableLearningGatewayMac'] = EnableLearningGatewayMac
        if RouterId is not None:
            self._RouterId = RouterId
            properties['RouterId'] = RouterId
        if RouterIdStep is not None:
            self._RouterIdStep = RouterIdStep
            properties['RouterIdStep'] = RouterIdStep
        if Ipv6RouterId is not None:
            self._Ipv6RouterId = Ipv6RouterId
            properties['Ipv6RouterId'] = Ipv6RouterId
        if Ipv6RouterIdStep is not None:
            self._Ipv6RouterIdStep = Ipv6RouterIdStep
            properties['Ipv6RouterIdStep'] = Ipv6RouterIdStep

        super(InterfaceWizardConfig, self).edit(**properties)

    @property
    def CountPerPort(self):
        """
        get the value of property _CountPerPort
        """
        if self.force_auto_sync:
            self.get('CountPerPort')
        return self._CountPerPort

    @property
    def CountPerInterfaceBlcok(self):
        """
        get the value of property _CountPerInterfaceBlcok
        """
        if self.force_auto_sync:
            self.get('CountPerInterfaceBlcok')
        return self._CountPerInterfaceBlcok

    @property
    def EnableEthernet(self):
        """
        get the value of property _EnableEthernet
        """
        if self.force_auto_sync:
            self.get('EnableEthernet')
        return self._EnableEthernet

    @property
    def EnableVlan(self):
        """
        get the value of property _EnableVlan
        """
        if self.force_auto_sync:
            self.get('EnableVlan')
        return self._EnableVlan

    @property
    def VlanHeaderCount(self):
        """
        get the value of property _VlanHeaderCount
        """
        if self.force_auto_sync:
            self.get('VlanHeaderCount')
        return self._VlanHeaderCount

    @property
    def EnableIPv4(self):
        """
        get the value of property _EnableIPv4
        """
        if self.force_auto_sync:
            self.get('EnableIPv4')
        return self._EnableIPv4

    @property
    def EnableIPv6(self):
        """
        get the value of property _EnableIPv6
        """
        if self.force_auto_sync:
            self.get('EnableIPv6')
        return self._EnableIPv6

    @property
    def EnablePppoe(self):
        """
        get the value of property _EnablePppoe
        """
        if self.force_auto_sync:
            self.get('EnablePppoe')
        return self._EnablePppoe

    @property
    def EnableInterfaceCount(self):
        """
        get the value of property _EnableInterfaceCount
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceCount')
        return self._EnableInterfaceCount

    @property
    def EnableLearningGatewayMac(self):
        """
        get the value of property _EnableLearningGatewayMac
        """
        if self.force_auto_sync:
            self.get('EnableLearningGatewayMac')
        return self._EnableLearningGatewayMac

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

    @CountPerPort.setter
    def CountPerPort(self, value):
        self._CountPerPort = value
        self.edit(CountPerPort=value)

    @CountPerInterfaceBlcok.setter
    def CountPerInterfaceBlcok(self, value):
        self._CountPerInterfaceBlcok = value
        self.edit(CountPerInterfaceBlcok=value)

    @EnableEthernet.setter
    def EnableEthernet(self, value):
        self._EnableEthernet = value
        self.edit(EnableEthernet=value)

    @EnableVlan.setter
    def EnableVlan(self, value):
        self._EnableVlan = value
        self.edit(EnableVlan=value)

    @VlanHeaderCount.setter
    def VlanHeaderCount(self, value):
        self._VlanHeaderCount = value
        self.edit(VlanHeaderCount=value)

    @EnableIPv4.setter
    def EnableIPv4(self, value):
        self._EnableIPv4 = value
        self.edit(EnableIPv4=value)

    @EnableIPv6.setter
    def EnableIPv6(self, value):
        self._EnableIPv6 = value
        self.edit(EnableIPv6=value)

    @EnablePppoe.setter
    def EnablePppoe(self, value):
        self._EnablePppoe = value
        self.edit(EnablePppoe=value)

    @EnableInterfaceCount.setter
    def EnableInterfaceCount(self, value):
        self._EnableInterfaceCount = value
        self.edit(EnableInterfaceCount=value)

    @EnableLearningGatewayMac.setter
    def EnableLearningGatewayMac(self, value):
        self._EnableLearningGatewayMac = value
        self.edit(EnableLearningGatewayMac=value)

    @RouterId.setter
    def RouterId(self, value):
        self._RouterId = value
        self.edit(RouterId=value)

    @RouterIdStep.setter
    def RouterIdStep(self, value):
        self._RouterIdStep = value
        self.edit(RouterIdStep=value)

    @Ipv6RouterId.setter
    def Ipv6RouterId(self, value):
        self._Ipv6RouterId = value
        self.edit(Ipv6RouterId=value)

    @Ipv6RouterIdStep.setter
    def Ipv6RouterIdStep(self, value):
        self._Ipv6RouterIdStep = value
        self.edit(Ipv6RouterIdStep=value)

    def _set_countperport_with_str(self, value):
        try:
            self._CountPerPort = int(value)
        except ValueError:
            self._CountPerPort = hex(int(value, 16))

    def _set_countperinterfaceblcok_with_str(self, value):
        try:
            self._CountPerInterfaceBlcok = int(value)
        except ValueError:
            self._CountPerInterfaceBlcok = hex(int(value, 16))

    def _set_enableethernet_with_str(self, value):
        self._EnableEthernet = (value == 'True')

    def _set_enablevlan_with_str(self, value):
        self._EnableVlan = (value == 'True')

    def _set_vlanheadercount_with_str(self, value):
        try:
            self._VlanHeaderCount = int(value)
        except ValueError:
            self._VlanHeaderCount = hex(int(value, 16))

    def _set_enableipv4_with_str(self, value):
        self._EnableIPv4 = (value == 'True')

    def _set_enableipv6_with_str(self, value):
        self._EnableIPv6 = (value == 'True')

    def _set_enablepppoe_with_str(self, value):
        self._EnablePppoe = (value == 'True')

    def _set_enableinterfacecount_with_str(self, value):
        self._EnableInterfaceCount = (value == 'True')

    def _set_enablelearninggatewaymac_with_str(self, value):
        self._EnableLearningGatewayMac = (value == 'True')

    def _set_routerid_with_str(self, value):
        self._RouterId = value

    def _set_routeridstep_with_str(self, value):
        self._RouterIdStep = value

    def _set_ipv6routerid_with_str(self, value):
        self._Ipv6RouterId = value

    def _set_ipv6routeridstep_with_str(self, value):
        self._Ipv6RouterIdStep = value

