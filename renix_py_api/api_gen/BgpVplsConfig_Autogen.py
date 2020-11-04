"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsL2VpnConfig_Autogen import MplsL2VpnConfig


@rom_manager.rom
class BgpVplsConfig(MplsL2VpnConfig):
    def __init__(self, EnableVplsScalability=None, NumberOfVplss=None, RouteTargetStart=None, RouteTargetStep=None, VplsMtu=None, CustomerRdStart=None, CustomerVeIdStart=None, CustomerStepPerVplsEnabled=None, CustomerRdStepPerVpls=None, CustomerStepPerCeEnabled=None, CustomerRdStepPerCe=None, CustomerVeIdStepPerCe=None, CustomerOverlapEnabled=None, ProviderDistributionSelectorCount=None, ProviderRdStart=None, ProviderVeIdStart=None, ProviderStepPerVplsEnabled=None, ProviderRdStepPerVpls=None, ProviderStepPerCeEnabled=None, ProviderRdStepPerCe=None, ProviderVeIdStepPerCe=None, ProviderOverlapEnabled=None, **kwargs):
        self._EnableVplsScalability = EnableVplsScalability  # Enable VPLS Scalability
        self._NumberOfVplss = NumberOfVplss  # Number of VPLSs
        self._RouteTargetStart = RouteTargetStart  # Route Target Start
        self._RouteTargetStep = RouteTargetStep  # Route Target Step
        self._RdAssignment = EnumMplsRdAssignment.UseRT  # RD Assignment, not editable
        self._VplsMtu = VplsMtu  # VPLS MTU
        self._VplsVersion = EnumMplsVplsVersion.Rfc4761  # VPLS Version, not editable
        self._VplsAssignment = EnumMplsAssignment.RoundRobin  # VPLS Assignment, not editable
        self._CustomerRdStart = CustomerRdStart  # Start
        self._CustomerVeIdStart = CustomerVeIdStart  # Start
        self._CustomerStepPerVplsEnabled = CustomerStepPerVplsEnabled  # Step per VPLS Enabled
        self._CustomerRdStepPerVpls = CustomerRdStepPerVpls  # Step per VPLS
        self._CustomerStepPerCeEnabled = CustomerStepPerCeEnabled  # Step per CE Enabled
        self._CustomerRdStepPerCe = CustomerRdStepPerCe  # Step per CE
        self._CustomerVeIdStepPerCe = CustomerVeIdStepPerCe  # Step per CE
        self._CustomerOverlapEnabled = CustomerOverlapEnabled  # Overlap VE IDs on different VPLSs
        self._ProviderDistributionSelector = EnumMplsDistributionSelector.PEsPerVPN  # Distribution Selector, not editable
        self._ProviderDistributionSelectorCount = ProviderDistributionSelectorCount  # Distribution Selector Count
        self._ProviderRdStart = ProviderRdStart  # Start
        self._ProviderVeIdStart = ProviderVeIdStart  # Start
        self._ProviderStepPerVplsEnabled = ProviderStepPerVplsEnabled  # Step per VPLS Enabled
        self._ProviderRdStepPerVpls = ProviderRdStepPerVpls  # Step per VPLS
        self._ProviderStepPerCeEnabled = ProviderStepPerCeEnabled  # Step per CE Enabled
        self._ProviderRdStepPerCe = ProviderRdStepPerCe  # Step per CE
        self._ProviderVeIdStepPerCe = ProviderVeIdStepPerCe  # Step per CE
        self._ProviderOverlapEnabled = ProviderOverlapEnabled  # Overlap VE IDs on different VPLSs

        properties = kwargs.copy()
        if EnableVplsScalability is not None:
            properties['EnableVplsScalability'] = EnableVplsScalability
        if NumberOfVplss is not None:
            properties['NumberOfVplss'] = NumberOfVplss
        if RouteTargetStart is not None:
            properties['RouteTargetStart'] = RouteTargetStart
        if RouteTargetStep is not None:
            properties['RouteTargetStep'] = RouteTargetStep
        if VplsMtu is not None:
            properties['VplsMtu'] = VplsMtu
        if CustomerRdStart is not None:
            properties['CustomerRdStart'] = CustomerRdStart
        if CustomerVeIdStart is not None:
            properties['CustomerVeIdStart'] = CustomerVeIdStart
        if CustomerStepPerVplsEnabled is not None:
            properties['CustomerStepPerVplsEnabled'] = CustomerStepPerVplsEnabled
        if CustomerRdStepPerVpls is not None:
            properties['CustomerRdStepPerVpls'] = CustomerRdStepPerVpls
        if CustomerStepPerCeEnabled is not None:
            properties['CustomerStepPerCeEnabled'] = CustomerStepPerCeEnabled
        if CustomerRdStepPerCe is not None:
            properties['CustomerRdStepPerCe'] = CustomerRdStepPerCe
        if CustomerVeIdStepPerCe is not None:
            properties['CustomerVeIdStepPerCe'] = CustomerVeIdStepPerCe
        if CustomerOverlapEnabled is not None:
            properties['CustomerOverlapEnabled'] = CustomerOverlapEnabled
        if ProviderDistributionSelectorCount is not None:
            properties['ProviderDistributionSelectorCount'] = ProviderDistributionSelectorCount
        if ProviderRdStart is not None:
            properties['ProviderRdStart'] = ProviderRdStart
        if ProviderVeIdStart is not None:
            properties['ProviderVeIdStart'] = ProviderVeIdStart
        if ProviderStepPerVplsEnabled is not None:
            properties['ProviderStepPerVplsEnabled'] = ProviderStepPerVplsEnabled
        if ProviderRdStepPerVpls is not None:
            properties['ProviderRdStepPerVpls'] = ProviderRdStepPerVpls
        if ProviderStepPerCeEnabled is not None:
            properties['ProviderStepPerCeEnabled'] = ProviderStepPerCeEnabled
        if ProviderRdStepPerCe is not None:
            properties['ProviderRdStepPerCe'] = ProviderRdStepPerCe
        if ProviderVeIdStepPerCe is not None:
            properties['ProviderVeIdStepPerCe'] = ProviderVeIdStepPerCe
        if ProviderOverlapEnabled is not None:
            properties['ProviderOverlapEnabled'] = ProviderOverlapEnabled

        # call base class function, and it will send message to renix server to create a class.
        super(BgpVplsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableVplsScalability=None, NumberOfVplss=None, RouteTargetStart=None, RouteTargetStep=None, VplsMtu=None, CustomerRdStart=None, CustomerVeIdStart=None, CustomerStepPerVplsEnabled=None, CustomerRdStepPerVpls=None, CustomerStepPerCeEnabled=None, CustomerRdStepPerCe=None, CustomerVeIdStepPerCe=None, CustomerOverlapEnabled=None, ProviderDistributionSelectorCount=None, ProviderRdStart=None, ProviderVeIdStart=None, ProviderStepPerVplsEnabled=None, ProviderRdStepPerVpls=None, ProviderStepPerCeEnabled=None, ProviderRdStepPerCe=None, ProviderVeIdStepPerCe=None, ProviderOverlapEnabled=None, **kwargs):
        properties = kwargs.copy()
        if EnableVplsScalability is not None:
            self._EnableVplsScalability = EnableVplsScalability
            properties['EnableVplsScalability'] = EnableVplsScalability
        if NumberOfVplss is not None:
            self._NumberOfVplss = NumberOfVplss
            properties['NumberOfVplss'] = NumberOfVplss
        if RouteTargetStart is not None:
            self._RouteTargetStart = RouteTargetStart
            properties['RouteTargetStart'] = RouteTargetStart
        if RouteTargetStep is not None:
            self._RouteTargetStep = RouteTargetStep
            properties['RouteTargetStep'] = RouteTargetStep
        if VplsMtu is not None:
            self._VplsMtu = VplsMtu
            properties['VplsMtu'] = VplsMtu
        if CustomerRdStart is not None:
            self._CustomerRdStart = CustomerRdStart
            properties['CustomerRdStart'] = CustomerRdStart
        if CustomerVeIdStart is not None:
            self._CustomerVeIdStart = CustomerVeIdStart
            properties['CustomerVeIdStart'] = CustomerVeIdStart
        if CustomerStepPerVplsEnabled is not None:
            self._CustomerStepPerVplsEnabled = CustomerStepPerVplsEnabled
            properties['CustomerStepPerVplsEnabled'] = CustomerStepPerVplsEnabled
        if CustomerRdStepPerVpls is not None:
            self._CustomerRdStepPerVpls = CustomerRdStepPerVpls
            properties['CustomerRdStepPerVpls'] = CustomerRdStepPerVpls
        if CustomerStepPerCeEnabled is not None:
            self._CustomerStepPerCeEnabled = CustomerStepPerCeEnabled
            properties['CustomerStepPerCeEnabled'] = CustomerStepPerCeEnabled
        if CustomerRdStepPerCe is not None:
            self._CustomerRdStepPerCe = CustomerRdStepPerCe
            properties['CustomerRdStepPerCe'] = CustomerRdStepPerCe
        if CustomerVeIdStepPerCe is not None:
            self._CustomerVeIdStepPerCe = CustomerVeIdStepPerCe
            properties['CustomerVeIdStepPerCe'] = CustomerVeIdStepPerCe
        if CustomerOverlapEnabled is not None:
            self._CustomerOverlapEnabled = CustomerOverlapEnabled
            properties['CustomerOverlapEnabled'] = CustomerOverlapEnabled
        if ProviderDistributionSelectorCount is not None:
            self._ProviderDistributionSelectorCount = ProviderDistributionSelectorCount
            properties['ProviderDistributionSelectorCount'] = ProviderDistributionSelectorCount
        if ProviderRdStart is not None:
            self._ProviderRdStart = ProviderRdStart
            properties['ProviderRdStart'] = ProviderRdStart
        if ProviderVeIdStart is not None:
            self._ProviderVeIdStart = ProviderVeIdStart
            properties['ProviderVeIdStart'] = ProviderVeIdStart
        if ProviderStepPerVplsEnabled is not None:
            self._ProviderStepPerVplsEnabled = ProviderStepPerVplsEnabled
            properties['ProviderStepPerVplsEnabled'] = ProviderStepPerVplsEnabled
        if ProviderRdStepPerVpls is not None:
            self._ProviderRdStepPerVpls = ProviderRdStepPerVpls
            properties['ProviderRdStepPerVpls'] = ProviderRdStepPerVpls
        if ProviderStepPerCeEnabled is not None:
            self._ProviderStepPerCeEnabled = ProviderStepPerCeEnabled
            properties['ProviderStepPerCeEnabled'] = ProviderStepPerCeEnabled
        if ProviderRdStepPerCe is not None:
            self._ProviderRdStepPerCe = ProviderRdStepPerCe
            properties['ProviderRdStepPerCe'] = ProviderRdStepPerCe
        if ProviderVeIdStepPerCe is not None:
            self._ProviderVeIdStepPerCe = ProviderVeIdStepPerCe
            properties['ProviderVeIdStepPerCe'] = ProviderVeIdStepPerCe
        if ProviderOverlapEnabled is not None:
            self._ProviderOverlapEnabled = ProviderOverlapEnabled
            properties['ProviderOverlapEnabled'] = ProviderOverlapEnabled

        super(BgpVplsConfig, self).edit(**properties)

    @property
    def EnableVplsScalability(self):
        """
        get the value of property _EnableVplsScalability
        """
        if self.force_auto_sync:
            self.get('EnableVplsScalability')
        return self._EnableVplsScalability

    @property
    def NumberOfVplss(self):
        """
        get the value of property _NumberOfVplss
        """
        if self.force_auto_sync:
            self.get('NumberOfVplss')
        return self._NumberOfVplss

    @property
    def RouteTargetStart(self):
        """
        get the value of property _RouteTargetStart
        """
        if self.force_auto_sync:
            self.get('RouteTargetStart')
        return self._RouteTargetStart

    @property
    def RouteTargetStep(self):
        """
        get the value of property _RouteTargetStep
        """
        if self.force_auto_sync:
            self.get('RouteTargetStep')
        return self._RouteTargetStep

    @property
    def RdAssignment(self):
        """
        get the value of property _RdAssignment
        """
        if self.force_auto_sync:
            self.get('RdAssignment')
        return self._RdAssignment

    @property
    def VplsMtu(self):
        """
        get the value of property _VplsMtu
        """
        if self.force_auto_sync:
            self.get('VplsMtu')
        return self._VplsMtu

    @property
    def VplsVersion(self):
        """
        get the value of property _VplsVersion
        """
        if self.force_auto_sync:
            self.get('VplsVersion')
        return self._VplsVersion

    @property
    def VplsAssignment(self):
        """
        get the value of property _VplsAssignment
        """
        if self.force_auto_sync:
            self.get('VplsAssignment')
        return self._VplsAssignment

    @property
    def CustomerRdStart(self):
        """
        get the value of property _CustomerRdStart
        """
        if self.force_auto_sync:
            self.get('CustomerRdStart')
        return self._CustomerRdStart

    @property
    def CustomerVeIdStart(self):
        """
        get the value of property _CustomerVeIdStart
        """
        if self.force_auto_sync:
            self.get('CustomerVeIdStart')
        return self._CustomerVeIdStart

    @property
    def CustomerStepPerVplsEnabled(self):
        """
        get the value of property _CustomerStepPerVplsEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerStepPerVplsEnabled')
        return self._CustomerStepPerVplsEnabled

    @property
    def CustomerRdStepPerVpls(self):
        """
        get the value of property _CustomerRdStepPerVpls
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerVpls')
        return self._CustomerRdStepPerVpls

    @property
    def CustomerStepPerCeEnabled(self):
        """
        get the value of property _CustomerStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerStepPerCeEnabled')
        return self._CustomerStepPerCeEnabled

    @property
    def CustomerRdStepPerCe(self):
        """
        get the value of property _CustomerRdStepPerCe
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerCe')
        return self._CustomerRdStepPerCe

    @property
    def CustomerVeIdStepPerCe(self):
        """
        get the value of property _CustomerVeIdStepPerCe
        """
        if self.force_auto_sync:
            self.get('CustomerVeIdStepPerCe')
        return self._CustomerVeIdStepPerCe

    @property
    def CustomerOverlapEnabled(self):
        """
        get the value of property _CustomerOverlapEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerOverlapEnabled')
        return self._CustomerOverlapEnabled

    @property
    def ProviderDistributionSelector(self):
        """
        get the value of property _ProviderDistributionSelector
        """
        if self.force_auto_sync:
            self.get('ProviderDistributionSelector')
        return self._ProviderDistributionSelector

    @property
    def ProviderDistributionSelectorCount(self):
        """
        get the value of property _ProviderDistributionSelectorCount
        """
        if self.force_auto_sync:
            self.get('ProviderDistributionSelectorCount')
        return self._ProviderDistributionSelectorCount

    @property
    def ProviderRdStart(self):
        """
        get the value of property _ProviderRdStart
        """
        if self.force_auto_sync:
            self.get('ProviderRdStart')
        return self._ProviderRdStart

    @property
    def ProviderVeIdStart(self):
        """
        get the value of property _ProviderVeIdStart
        """
        if self.force_auto_sync:
            self.get('ProviderVeIdStart')
        return self._ProviderVeIdStart

    @property
    def ProviderStepPerVplsEnabled(self):
        """
        get the value of property _ProviderStepPerVplsEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderStepPerVplsEnabled')
        return self._ProviderStepPerVplsEnabled

    @property
    def ProviderRdStepPerVpls(self):
        """
        get the value of property _ProviderRdStepPerVpls
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerVpls')
        return self._ProviderRdStepPerVpls

    @property
    def ProviderStepPerCeEnabled(self):
        """
        get the value of property _ProviderStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderStepPerCeEnabled')
        return self._ProviderStepPerCeEnabled

    @property
    def ProviderRdStepPerCe(self):
        """
        get the value of property _ProviderRdStepPerCe
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerCe')
        return self._ProviderRdStepPerCe

    @property
    def ProviderVeIdStepPerCe(self):
        """
        get the value of property _ProviderVeIdStepPerCe
        """
        if self.force_auto_sync:
            self.get('ProviderVeIdStepPerCe')
        return self._ProviderVeIdStepPerCe

    @property
    def ProviderOverlapEnabled(self):
        """
        get the value of property _ProviderOverlapEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderOverlapEnabled')
        return self._ProviderOverlapEnabled

    @EnableVplsScalability.setter
    def EnableVplsScalability(self, value):
        self._EnableVplsScalability = value
        self.edit(EnableVplsScalability=value)

    @NumberOfVplss.setter
    def NumberOfVplss(self, value):
        self._NumberOfVplss = value
        self.edit(NumberOfVplss=value)

    @RouteTargetStart.setter
    def RouteTargetStart(self, value):
        self._RouteTargetStart = value
        self.edit(RouteTargetStart=value)

    @RouteTargetStep.setter
    def RouteTargetStep(self, value):
        self._RouteTargetStep = value
        self.edit(RouteTargetStep=value)

    @VplsMtu.setter
    def VplsMtu(self, value):
        self._VplsMtu = value
        self.edit(VplsMtu=value)

    @CustomerRdStart.setter
    def CustomerRdStart(self, value):
        self._CustomerRdStart = value
        self.edit(CustomerRdStart=value)

    @CustomerVeIdStart.setter
    def CustomerVeIdStart(self, value):
        self._CustomerVeIdStart = value
        self.edit(CustomerVeIdStart=value)

    @CustomerStepPerVplsEnabled.setter
    def CustomerStepPerVplsEnabled(self, value):
        self._CustomerStepPerVplsEnabled = value
        self.edit(CustomerStepPerVplsEnabled=value)

    @CustomerRdStepPerVpls.setter
    def CustomerRdStepPerVpls(self, value):
        self._CustomerRdStepPerVpls = value
        self.edit(CustomerRdStepPerVpls=value)

    @CustomerStepPerCeEnabled.setter
    def CustomerStepPerCeEnabled(self, value):
        self._CustomerStepPerCeEnabled = value
        self.edit(CustomerStepPerCeEnabled=value)

    @CustomerRdStepPerCe.setter
    def CustomerRdStepPerCe(self, value):
        self._CustomerRdStepPerCe = value
        self.edit(CustomerRdStepPerCe=value)

    @CustomerVeIdStepPerCe.setter
    def CustomerVeIdStepPerCe(self, value):
        self._CustomerVeIdStepPerCe = value
        self.edit(CustomerVeIdStepPerCe=value)

    @CustomerOverlapEnabled.setter
    def CustomerOverlapEnabled(self, value):
        self._CustomerOverlapEnabled = value
        self.edit(CustomerOverlapEnabled=value)

    @ProviderDistributionSelectorCount.setter
    def ProviderDistributionSelectorCount(self, value):
        self._ProviderDistributionSelectorCount = value
        self.edit(ProviderDistributionSelectorCount=value)

    @ProviderRdStart.setter
    def ProviderRdStart(self, value):
        self._ProviderRdStart = value
        self.edit(ProviderRdStart=value)

    @ProviderVeIdStart.setter
    def ProviderVeIdStart(self, value):
        self._ProviderVeIdStart = value
        self.edit(ProviderVeIdStart=value)

    @ProviderStepPerVplsEnabled.setter
    def ProviderStepPerVplsEnabled(self, value):
        self._ProviderStepPerVplsEnabled = value
        self.edit(ProviderStepPerVplsEnabled=value)

    @ProviderRdStepPerVpls.setter
    def ProviderRdStepPerVpls(self, value):
        self._ProviderRdStepPerVpls = value
        self.edit(ProviderRdStepPerVpls=value)

    @ProviderStepPerCeEnabled.setter
    def ProviderStepPerCeEnabled(self, value):
        self._ProviderStepPerCeEnabled = value
        self.edit(ProviderStepPerCeEnabled=value)

    @ProviderRdStepPerCe.setter
    def ProviderRdStepPerCe(self, value):
        self._ProviderRdStepPerCe = value
        self.edit(ProviderRdStepPerCe=value)

    @ProviderVeIdStepPerCe.setter
    def ProviderVeIdStepPerCe(self, value):
        self._ProviderVeIdStepPerCe = value
        self.edit(ProviderVeIdStepPerCe=value)

    @ProviderOverlapEnabled.setter
    def ProviderOverlapEnabled(self, value):
        self._ProviderOverlapEnabled = value
        self.edit(ProviderOverlapEnabled=value)

    def _set_enablevplsscalability_with_str(self, value):
        self._EnableVplsScalability = (value == 'True')

    def _set_numberofvplss_with_str(self, value):
        try:
            self._NumberOfVplss = int(value)
        except ValueError:
            self._NumberOfVplss = hex(int(value, 16))

    def _set_routetargetstart_with_str(self, value):
        self._RouteTargetStart = value

    def _set_routetargetstep_with_str(self, value):
        self._RouteTargetStep = value

    def _set_rdassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._RdAssignment = EnumMplsRdAssignment.%s' % value[:seperate])

    def _set_vplsmtu_with_str(self, value):
        try:
            self._VplsMtu = int(value)
        except ValueError:
            self._VplsMtu = hex(int(value, 16))

    def _set_vplsversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._VplsVersion = EnumMplsVplsVersion.%s' % value[:seperate])

    def _set_vplsassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._VplsAssignment = EnumMplsAssignment.%s' % value[:seperate])

    def _set_customerrdstart_with_str(self, value):
        self._CustomerRdStart = value

    def _set_customerveidstart_with_str(self, value):
        try:
            self._CustomerVeIdStart = int(value)
        except ValueError:
            self._CustomerVeIdStart = hex(int(value, 16))

    def _set_customersteppervplsenabled_with_str(self, value):
        self._CustomerStepPerVplsEnabled = (value == 'True')

    def _set_customerrdsteppervpls_with_str(self, value):
        self._CustomerRdStepPerVpls = value

    def _set_customerstepperceenabled_with_str(self, value):
        self._CustomerStepPerCeEnabled = (value == 'True')

    def _set_customerrdstepperce_with_str(self, value):
        self._CustomerRdStepPerCe = value

    def _set_customerveidstepperce_with_str(self, value):
        try:
            self._CustomerVeIdStepPerCe = int(value)
        except ValueError:
            self._CustomerVeIdStepPerCe = hex(int(value, 16))

    def _set_customeroverlapenabled_with_str(self, value):
        self._CustomerOverlapEnabled = (value == 'True')

    def _set_providerdistributionselector_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProviderDistributionSelector = EnumMplsDistributionSelector.%s' % value[:seperate])

    def _set_providerdistributionselectorcount_with_str(self, value):
        try:
            self._ProviderDistributionSelectorCount = int(value)
        except ValueError:
            self._ProviderDistributionSelectorCount = hex(int(value, 16))

    def _set_providerrdstart_with_str(self, value):
        self._ProviderRdStart = value

    def _set_providerveidstart_with_str(self, value):
        try:
            self._ProviderVeIdStart = int(value)
        except ValueError:
            self._ProviderVeIdStart = hex(int(value, 16))

    def _set_providersteppervplsenabled_with_str(self, value):
        self._ProviderStepPerVplsEnabled = (value == 'True')

    def _set_providerrdsteppervpls_with_str(self, value):
        self._ProviderRdStepPerVpls = value

    def _set_providerstepperceenabled_with_str(self, value):
        self._ProviderStepPerCeEnabled = (value == 'True')

    def _set_providerrdstepperce_with_str(self, value):
        self._ProviderRdStepPerCe = value

    def _set_providerveidstepperce_with_str(self, value):
        try:
            self._ProviderVeIdStepPerCe = int(value)
        except ValueError:
            self._ProviderVeIdStepPerCe = hex(int(value, 16))

    def _set_provideroverlapenabled_with_str(self, value):
        self._ProviderOverlapEnabled = (value == 'True')

