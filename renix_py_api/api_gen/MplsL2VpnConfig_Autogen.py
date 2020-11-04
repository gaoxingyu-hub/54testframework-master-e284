"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsVpnConfig_Autogen import MplsVpnConfig


@rom_manager.rom
class MplsL2VpnConfig(MplsVpnConfig):
    def __init__(self, HostMacStart=None, HostMacStep=None, OverlapHosts=None, EnableHostVlan=None, NumberOfCustomerSideVlanHeaders=None, NumberOfProviderSideVlanHeaders=None, VlanIdStart=None, VlanIdStepPerLsp=None, VlanIdStepPerHost=None, TotalHosts=None, HostsPerCustomerCe=None, HostsPerProviderCe=None, HostsPerLsp=None, CustomerHostPercent=None, ProviderHostPercent=None, **kwargs):
        self._HostMacStart = HostMacStart  # Start
        self._HostMacStep = HostMacStep  # Step
        self._OverlapHosts = OverlapHosts  # Overlap Hosts
        self._EnableHostVlan = EnableHostVlan  # Enable Host VLAN
        self._NumberOfCustomerSideVlanHeaders = NumberOfCustomerSideVlanHeaders  # Number of Customer Side VLAN Headers
        self._NumberOfProviderSideVlanHeaders = NumberOfProviderSideVlanHeaders  # Number of Provider Side VLAN Headers
        self._VlanIdStart = VlanIdStart  # VLAN ID Start
        self._VlanIdStepPerLsp = VlanIdStepPerLsp  # VLAN ID Step per LSP
        self._VlanIdStepPerHost = VlanIdStepPerHost  # VLAN ID Step per Host
        self._HostAssignment = EnumMplsHostAssignment.HostsOrMacsPerCe  # Assignment, not editable
        self._TotalHosts = TotalHosts  # Total Hosts
        self._HostsPerCustomerCe = HostsPerCustomerCe  # Hosts per Customer CE
        self._HostsPerProviderCe = HostsPerProviderCe  # Hosts per Provider CE
        self._HostsPerLsp = HostsPerLsp  # Hosts per LSP
        self._CustomerHostPercent = CustomerHostPercent  # Customer Host %
        self._ProviderHostPercent = ProviderHostPercent  # Provider Host %

        properties = kwargs.copy()
        if HostMacStart is not None:
            properties['HostMacStart'] = HostMacStart
        if HostMacStep is not None:
            properties['HostMacStep'] = HostMacStep
        if OverlapHosts is not None:
            properties['OverlapHosts'] = OverlapHosts
        if EnableHostVlan is not None:
            properties['EnableHostVlan'] = EnableHostVlan
        if NumberOfCustomerSideVlanHeaders is not None:
            properties['NumberOfCustomerSideVlanHeaders'] = NumberOfCustomerSideVlanHeaders
        if NumberOfProviderSideVlanHeaders is not None:
            properties['NumberOfProviderSideVlanHeaders'] = NumberOfProviderSideVlanHeaders
        if VlanIdStart is not None:
            properties['VlanIdStart'] = VlanIdStart
        if VlanIdStepPerLsp is not None:
            properties['VlanIdStepPerLsp'] = VlanIdStepPerLsp
        if VlanIdStepPerHost is not None:
            properties['VlanIdStepPerHost'] = VlanIdStepPerHost
        if TotalHosts is not None:
            properties['TotalHosts'] = TotalHosts
        if HostsPerCustomerCe is not None:
            properties['HostsPerCustomerCe'] = HostsPerCustomerCe
        if HostsPerProviderCe is not None:
            properties['HostsPerProviderCe'] = HostsPerProviderCe
        if HostsPerLsp is not None:
            properties['HostsPerLsp'] = HostsPerLsp
        if CustomerHostPercent is not None:
            properties['CustomerHostPercent'] = CustomerHostPercent
        if ProviderHostPercent is not None:
            properties['ProviderHostPercent'] = ProviderHostPercent

        # call base class function, and it will send message to renix server to create a class.
        super(MplsL2VpnConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HostMacStart=None, HostMacStep=None, OverlapHosts=None, EnableHostVlan=None, NumberOfCustomerSideVlanHeaders=None, NumberOfProviderSideVlanHeaders=None, VlanIdStart=None, VlanIdStepPerLsp=None, VlanIdStepPerHost=None, TotalHosts=None, HostsPerCustomerCe=None, HostsPerProviderCe=None, HostsPerLsp=None, CustomerHostPercent=None, ProviderHostPercent=None, **kwargs):
        properties = kwargs.copy()
        if HostMacStart is not None:
            self._HostMacStart = HostMacStart
            properties['HostMacStart'] = HostMacStart
        if HostMacStep is not None:
            self._HostMacStep = HostMacStep
            properties['HostMacStep'] = HostMacStep
        if OverlapHosts is not None:
            self._OverlapHosts = OverlapHosts
            properties['OverlapHosts'] = OverlapHosts
        if EnableHostVlan is not None:
            self._EnableHostVlan = EnableHostVlan
            properties['EnableHostVlan'] = EnableHostVlan
        if NumberOfCustomerSideVlanHeaders is not None:
            self._NumberOfCustomerSideVlanHeaders = NumberOfCustomerSideVlanHeaders
            properties['NumberOfCustomerSideVlanHeaders'] = NumberOfCustomerSideVlanHeaders
        if NumberOfProviderSideVlanHeaders is not None:
            self._NumberOfProviderSideVlanHeaders = NumberOfProviderSideVlanHeaders
            properties['NumberOfProviderSideVlanHeaders'] = NumberOfProviderSideVlanHeaders
        if VlanIdStart is not None:
            self._VlanIdStart = VlanIdStart
            properties['VlanIdStart'] = VlanIdStart
        if VlanIdStepPerLsp is not None:
            self._VlanIdStepPerLsp = VlanIdStepPerLsp
            properties['VlanIdStepPerLsp'] = VlanIdStepPerLsp
        if VlanIdStepPerHost is not None:
            self._VlanIdStepPerHost = VlanIdStepPerHost
            properties['VlanIdStepPerHost'] = VlanIdStepPerHost
        if TotalHosts is not None:
            self._TotalHosts = TotalHosts
            properties['TotalHosts'] = TotalHosts
        if HostsPerCustomerCe is not None:
            self._HostsPerCustomerCe = HostsPerCustomerCe
            properties['HostsPerCustomerCe'] = HostsPerCustomerCe
        if HostsPerProviderCe is not None:
            self._HostsPerProviderCe = HostsPerProviderCe
            properties['HostsPerProviderCe'] = HostsPerProviderCe
        if HostsPerLsp is not None:
            self._HostsPerLsp = HostsPerLsp
            properties['HostsPerLsp'] = HostsPerLsp
        if CustomerHostPercent is not None:
            self._CustomerHostPercent = CustomerHostPercent
            properties['CustomerHostPercent'] = CustomerHostPercent
        if ProviderHostPercent is not None:
            self._ProviderHostPercent = ProviderHostPercent
            properties['ProviderHostPercent'] = ProviderHostPercent

        super(MplsL2VpnConfig, self).edit(**properties)

    @property
    def HostMacStart(self):
        """
        get the value of property _HostMacStart
        """
        if self.force_auto_sync:
            self.get('HostMacStart')
        return self._HostMacStart

    @property
    def HostMacStep(self):
        """
        get the value of property _HostMacStep
        """
        if self.force_auto_sync:
            self.get('HostMacStep')
        return self._HostMacStep

    @property
    def OverlapHosts(self):
        """
        get the value of property _OverlapHosts
        """
        if self.force_auto_sync:
            self.get('OverlapHosts')
        return self._OverlapHosts

    @property
    def EnableHostVlan(self):
        """
        get the value of property _EnableHostVlan
        """
        if self.force_auto_sync:
            self.get('EnableHostVlan')
        return self._EnableHostVlan

    @property
    def NumberOfCustomerSideVlanHeaders(self):
        """
        get the value of property _NumberOfCustomerSideVlanHeaders
        """
        if self.force_auto_sync:
            self.get('NumberOfCustomerSideVlanHeaders')
        return self._NumberOfCustomerSideVlanHeaders

    @property
    def NumberOfProviderSideVlanHeaders(self):
        """
        get the value of property _NumberOfProviderSideVlanHeaders
        """
        if self.force_auto_sync:
            self.get('NumberOfProviderSideVlanHeaders')
        return self._NumberOfProviderSideVlanHeaders

    @property
    def VlanIdStart(self):
        """
        get the value of property _VlanIdStart
        """
        if self.force_auto_sync:
            self.get('VlanIdStart')
        return self._VlanIdStart

    @property
    def VlanIdStepPerLsp(self):
        """
        get the value of property _VlanIdStepPerLsp
        """
        if self.force_auto_sync:
            self.get('VlanIdStepPerLsp')
        return self._VlanIdStepPerLsp

    @property
    def VlanIdStepPerHost(self):
        """
        get the value of property _VlanIdStepPerHost
        """
        if self.force_auto_sync:
            self.get('VlanIdStepPerHost')
        return self._VlanIdStepPerHost

    @property
    def HostAssignment(self):
        """
        get the value of property _HostAssignment
        """
        if self.force_auto_sync:
            self.get('HostAssignment')
        return self._HostAssignment

    @property
    def TotalHosts(self):
        """
        get the value of property _TotalHosts
        """
        if self.force_auto_sync:
            self.get('TotalHosts')
        return self._TotalHosts

    @property
    def HostsPerCustomerCe(self):
        """
        get the value of property _HostsPerCustomerCe
        """
        if self.force_auto_sync:
            self.get('HostsPerCustomerCe')
        return self._HostsPerCustomerCe

    @property
    def HostsPerProviderCe(self):
        """
        get the value of property _HostsPerProviderCe
        """
        if self.force_auto_sync:
            self.get('HostsPerProviderCe')
        return self._HostsPerProviderCe

    @property
    def HostsPerLsp(self):
        """
        get the value of property _HostsPerLsp
        """
        if self.force_auto_sync:
            self.get('HostsPerLsp')
        return self._HostsPerLsp

    @property
    def CustomerHostPercent(self):
        """
        get the value of property _CustomerHostPercent
        """
        if self.force_auto_sync:
            self.get('CustomerHostPercent')
        return self._CustomerHostPercent

    @property
    def ProviderHostPercent(self):
        """
        get the value of property _ProviderHostPercent
        """
        if self.force_auto_sync:
            self.get('ProviderHostPercent')
        return self._ProviderHostPercent

    @HostMacStart.setter
    def HostMacStart(self, value):
        self._HostMacStart = value
        self.edit(HostMacStart=value)

    @HostMacStep.setter
    def HostMacStep(self, value):
        self._HostMacStep = value
        self.edit(HostMacStep=value)

    @OverlapHosts.setter
    def OverlapHosts(self, value):
        self._OverlapHosts = value
        self.edit(OverlapHosts=value)

    @EnableHostVlan.setter
    def EnableHostVlan(self, value):
        self._EnableHostVlan = value
        self.edit(EnableHostVlan=value)

    @NumberOfCustomerSideVlanHeaders.setter
    def NumberOfCustomerSideVlanHeaders(self, value):
        self._NumberOfCustomerSideVlanHeaders = value
        self.edit(NumberOfCustomerSideVlanHeaders=value)

    @NumberOfProviderSideVlanHeaders.setter
    def NumberOfProviderSideVlanHeaders(self, value):
        self._NumberOfProviderSideVlanHeaders = value
        self.edit(NumberOfProviderSideVlanHeaders=value)

    @VlanIdStart.setter
    def VlanIdStart(self, value):
        self._VlanIdStart = value
        self.edit(VlanIdStart=value)

    @VlanIdStepPerLsp.setter
    def VlanIdStepPerLsp(self, value):
        self._VlanIdStepPerLsp = value
        self.edit(VlanIdStepPerLsp=value)

    @VlanIdStepPerHost.setter
    def VlanIdStepPerHost(self, value):
        self._VlanIdStepPerHost = value
        self.edit(VlanIdStepPerHost=value)

    @TotalHosts.setter
    def TotalHosts(self, value):
        self._TotalHosts = value
        self.edit(TotalHosts=value)

    @HostsPerCustomerCe.setter
    def HostsPerCustomerCe(self, value):
        self._HostsPerCustomerCe = value
        self.edit(HostsPerCustomerCe=value)

    @HostsPerProviderCe.setter
    def HostsPerProviderCe(self, value):
        self._HostsPerProviderCe = value
        self.edit(HostsPerProviderCe=value)

    @HostsPerLsp.setter
    def HostsPerLsp(self, value):
        self._HostsPerLsp = value
        self.edit(HostsPerLsp=value)

    @CustomerHostPercent.setter
    def CustomerHostPercent(self, value):
        self._CustomerHostPercent = value
        self.edit(CustomerHostPercent=value)

    @ProviderHostPercent.setter
    def ProviderHostPercent(self, value):
        self._ProviderHostPercent = value
        self.edit(ProviderHostPercent=value)

    def _set_hostmacstart_with_str(self, value):
        self._HostMacStart = value

    def _set_hostmacstep_with_str(self, value):
        self._HostMacStep = value

    def _set_overlaphosts_with_str(self, value):
        self._OverlapHosts = (value == 'True')

    def _set_enablehostvlan_with_str(self, value):
        self._EnableHostVlan = (value == 'True')

    def _set_numberofcustomersidevlanheaders_with_str(self, value):
        try:
            self._NumberOfCustomerSideVlanHeaders = int(value)
        except ValueError:
            self._NumberOfCustomerSideVlanHeaders = hex(int(value, 16))

    def _set_numberofprovidersidevlanheaders_with_str(self, value):
        try:
            self._NumberOfProviderSideVlanHeaders = int(value)
        except ValueError:
            self._NumberOfProviderSideVlanHeaders = hex(int(value, 16))

    def _set_vlanidstart_with_str(self, value):
        try:
            self._VlanIdStart = int(value)
        except ValueError:
            self._VlanIdStart = hex(int(value, 16))

    def _set_vlanidstepperlsp_with_str(self, value):
        try:
            self._VlanIdStepPerLsp = int(value)
        except ValueError:
            self._VlanIdStepPerLsp = hex(int(value, 16))

    def _set_vlanidstepperhost_with_str(self, value):
        try:
            self._VlanIdStepPerHost = int(value)
        except ValueError:
            self._VlanIdStepPerHost = hex(int(value, 16))

    def _set_hostassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._HostAssignment = EnumMplsHostAssignment.%s' % value[:seperate])

    def _set_totalhosts_with_str(self, value):
        try:
            self._TotalHosts = int(value)
        except ValueError:
            self._TotalHosts = hex(int(value, 16))

    def _set_hostspercustomerce_with_str(self, value):
        try:
            self._HostsPerCustomerCe = int(value)
        except ValueError:
            self._HostsPerCustomerCe = hex(int(value, 16))

    def _set_hostsperproviderce_with_str(self, value):
        try:
            self._HostsPerProviderCe = int(value)
        except ValueError:
            self._HostsPerProviderCe = hex(int(value, 16))

    def _set_hostsperlsp_with_str(self, value):
        try:
            self._HostsPerLsp = int(value)
        except ValueError:
            self._HostsPerLsp = hex(int(value, 16))

    def _set_customerhostpercent_with_str(self, value):
        try:
            self._CustomerHostPercent = int(value)
        except ValueError:
            self._CustomerHostPercent = hex(int(value, 16))

    def _set_providerhostpercent_with_str(self, value):
        try:
            self._ProviderHostPercent = int(value)
        except ValueError:
            self._ProviderHostPercent = hex(int(value, 16))

