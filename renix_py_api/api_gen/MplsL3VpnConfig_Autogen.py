"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsVpnConfig_Autogen import MplsVpnConfig


@rom_manager.rom
class MplsL3VpnConfig(MplsVpnConfig):
    def __init__(self, NumberOfVpns=None, RouteTargetStart=None, RouteTargetStep=None, CeProtocolAssignment=None, CustomerRdStart=None, CustomerRdStepPerVpnEnabled=None, CustomerRdStepPerVpn=None, CustomerRdStepPerCeEnabled=None, CustomerRdStepPerCe=None, CustomerEnable4ByteAsNumber=None, CustomerCeAsNumberStart=None, CustomerCeAsNumberStepPerVpnEnabled=None, CustomerCeAsNumberStepPerVpn=None, CustomerCeAsNumberStepPerCeEnabled=None, CustomerCeAsNumberStepPerCe=None, CustomerCe4ByteAsNumberStart=None, CustomerCe4ByteAsNumberStepPerVpnEnabled=None, CustomerCe4ByteAsNumberStepPerVpn=None, CustomerCe4ByteAsNumberStepPerCeEnabled=None, CustomerCe4ByteAsNumberStepPerCe=None, ProviderDistributionSelectorCount=None, ProviderMeshed=None, ProviderRdStart=None, ProviderRdStepPerVpnEnabled=None, ProviderRdStepPerVpn=None, ProviderRdStepPerCeEnabled=None, ProviderRdStepPerCe=None, ProviderAppendCeAsToPath=None, ProviderEnable4ByteAsNumber=None, ProviderCeAsNumberStart=None, ProviderCeAsNumberStepPerVpnEnabled=None, ProviderCeAsNumberStepPerVpn=None, ProviderCeAsNumberStepPerCeEnabled=None, ProviderCeAsNumberStepPerCe=None, ProviderCe4ByteAsNumberStart=None, ProviderCe4ByteAsNumberStepPerVpnEnabled=None, ProviderCe4ByteAsNumberStepPerVpn=None, ProviderCe4ByteAsNumberStepPerCeEnabled=None, ProviderCe4ByteAsNumberStepPerCe=None, CustomerPrefixLength=None, CustomerRoutesPerPe=None, CustomerOverlapRoutes=None, ProviderPrefixLength=None, ProviderRoutesPerPe=None, ProviderOverlapRoutes=None, ProviderStartLabel=None, **kwargs):
        self._NumberOfVpns = NumberOfVpns  # Number of VPNs
        self._RouteTargetStart = RouteTargetStart  # Route Target Start
        self._RouteTargetStep = RouteTargetStep  # Route Target Step
        self._RdAssignment = EnumMplsRdAssignment.UseRT  # RD Assignment, not editable
        self._VpnAssignment = EnumMplsAssignment.RoundRobin  # VPN Assignment, not editable
        self._CeProtocol = EnumMplsCeProtocol.BGP  # CE Protocol, not editable
        self._CeProtocolAssignment = CeProtocolAssignment  # CE Protocol Assignment
        self._CustomerRdStart = CustomerRdStart  # Start
        self._CustomerRdStepPerVpnEnabled = CustomerRdStepPerVpnEnabled  # Step per VPN Enabled
        self._CustomerRdStepPerVpn = CustomerRdStepPerVpn  # Step per VPN
        self._CustomerRdStepPerCeEnabled = CustomerRdStepPerCeEnabled  # Step per CE Enabled
        self._CustomerRdStepPerCe = CustomerRdStepPerCe  # Step per CE
        self._CustomerEnable4ByteAsNumber = CustomerEnable4ByteAsNumber  # Enable 4-Byte AS Number
        self._CustomerCeAsNumberStart = CustomerCeAsNumberStart  # Start
        self._CustomerCeAsNumberStepPerVpnEnabled = CustomerCeAsNumberStepPerVpnEnabled  # Step per VPN Enabled
        self._CustomerCeAsNumberStepPerVpn = CustomerCeAsNumberStepPerVpn  # Step per VPN
        self._CustomerCeAsNumberStepPerCeEnabled = CustomerCeAsNumberStepPerCeEnabled  # Step per CE Enabled
        self._CustomerCeAsNumberStepPerCe = CustomerCeAsNumberStepPerCe  # Step per CE
        self._CustomerCe4ByteAsNumberStart = CustomerCe4ByteAsNumberStart  # Start
        self._CustomerCe4ByteAsNumberStepPerVpnEnabled = CustomerCe4ByteAsNumberStepPerVpnEnabled  # Step per VPN Enabled
        self._CustomerCe4ByteAsNumberStepPerVpn = CustomerCe4ByteAsNumberStepPerVpn  # Step per VPN
        self._CustomerCe4ByteAsNumberStepPerCeEnabled = CustomerCe4ByteAsNumberStepPerCeEnabled  # Step per CE Enabled
        self._CustomerCe4ByteAsNumberStepPerCe = CustomerCe4ByteAsNumberStepPerCe  # Step per CE
        self._ProviderDistributionSelector = EnumMplsDistributionSelector.PEsPerVPN  # Distribution Selector, not editable
        self._ProviderDistributionSelectorCount = ProviderDistributionSelectorCount  # Distribution Selector Count
        self._ProviderMeshed = ProviderMeshed  # Meshed
        self._ProviderRdStart = ProviderRdStart  # Start
        self._ProviderRdStepPerVpnEnabled = ProviderRdStepPerVpnEnabled  # Step per VPN Enabled
        self._ProviderRdStepPerVpn = ProviderRdStepPerVpn  # Step per VPN
        self._ProviderRdStepPerCeEnabled = ProviderRdStepPerCeEnabled  # Step per CE Enabled
        self._ProviderRdStepPerCe = ProviderRdStepPerCe  # Step per CE
        self._ProviderAppendCeAsToPath = ProviderAppendCeAsToPath  # Append CE AS to path
        self._ProviderEnable4ByteAsNumber = ProviderEnable4ByteAsNumber  # Enable 4-Byte AS Number
        self._ProviderCeAsNumberStart = ProviderCeAsNumberStart  # Start
        self._ProviderCeAsNumberStepPerVpnEnabled = ProviderCeAsNumberStepPerVpnEnabled  # Step per VPN Enabled
        self._ProviderCeAsNumberStepPerVpn = ProviderCeAsNumberStepPerVpn  # Step per VPN
        self._ProviderCeAsNumberStepPerCeEnabled = ProviderCeAsNumberStepPerCeEnabled  # Step per CE Enabled
        self._ProviderCeAsNumberStepPerCe = ProviderCeAsNumberStepPerCe  # Step per CE
        self._ProviderCe4ByteAsNumberStart = ProviderCe4ByteAsNumberStart  # Start
        self._ProviderCe4ByteAsNumberStepPerVpnEnabled = ProviderCe4ByteAsNumberStepPerVpnEnabled  # Step per VPN Enabled
        self._ProviderCe4ByteAsNumberStepPerVpn = ProviderCe4ByteAsNumberStepPerVpn  # Step per VPN
        self._ProviderCe4ByteAsNumberStepPerCeEnabled = ProviderCe4ByteAsNumberStepPerCeEnabled  # Step per CE Enabled
        self._ProviderCe4ByteAsNumberStepPerCe = ProviderCe4ByteAsNumberStepPerCe  # Step per CE
        self._CustomerPrefixLength = CustomerPrefixLength  # Prefix Length
        self._CustomerRoutesPerPe = CustomerRoutesPerPe  # Routes per CE
        self._CustomerOverlapRoutes = CustomerOverlapRoutes  # Overlap Routes
        self._CustomerRouteType = EnumMplsRouteType.Internal  # Route Type, not editable
        self._ProviderPrefixLength = ProviderPrefixLength  # Prefix Length
        self._ProviderRoutesPerPe = ProviderRoutesPerPe  # Routes per CE
        self._ProviderOverlapRoutes = ProviderOverlapRoutes  # Overlap Routes
        self._ProviderLabelMethod = EnumMplsLabelMethod.LabelPerSite  # Label Method, not editable
        self._ProviderStartLabel = ProviderStartLabel  # Start Label

        properties = kwargs.copy()
        if NumberOfVpns is not None:
            properties['NumberOfVpns'] = NumberOfVpns
        if RouteTargetStart is not None:
            properties['RouteTargetStart'] = RouteTargetStart
        if RouteTargetStep is not None:
            properties['RouteTargetStep'] = RouteTargetStep
        if CeProtocolAssignment is not None:
            properties['CeProtocolAssignment'] = CeProtocolAssignment
        if CustomerRdStart is not None:
            properties['CustomerRdStart'] = CustomerRdStart
        if CustomerRdStepPerVpnEnabled is not None:
            properties['CustomerRdStepPerVpnEnabled'] = CustomerRdStepPerVpnEnabled
        if CustomerRdStepPerVpn is not None:
            properties['CustomerRdStepPerVpn'] = CustomerRdStepPerVpn
        if CustomerRdStepPerCeEnabled is not None:
            properties['CustomerRdStepPerCeEnabled'] = CustomerRdStepPerCeEnabled
        if CustomerRdStepPerCe is not None:
            properties['CustomerRdStepPerCe'] = CustomerRdStepPerCe
        if CustomerEnable4ByteAsNumber is not None:
            properties['CustomerEnable4ByteAsNumber'] = CustomerEnable4ByteAsNumber
        if CustomerCeAsNumberStart is not None:
            properties['CustomerCeAsNumberStart'] = CustomerCeAsNumberStart
        if CustomerCeAsNumberStepPerVpnEnabled is not None:
            properties['CustomerCeAsNumberStepPerVpnEnabled'] = CustomerCeAsNumberStepPerVpnEnabled
        if CustomerCeAsNumberStepPerVpn is not None:
            properties['CustomerCeAsNumberStepPerVpn'] = CustomerCeAsNumberStepPerVpn
        if CustomerCeAsNumberStepPerCeEnabled is not None:
            properties['CustomerCeAsNumberStepPerCeEnabled'] = CustomerCeAsNumberStepPerCeEnabled
        if CustomerCeAsNumberStepPerCe is not None:
            properties['CustomerCeAsNumberStepPerCe'] = CustomerCeAsNumberStepPerCe
        if CustomerCe4ByteAsNumberStart is not None:
            properties['CustomerCe4ByteAsNumberStart'] = CustomerCe4ByteAsNumberStart
        if CustomerCe4ByteAsNumberStepPerVpnEnabled is not None:
            properties['CustomerCe4ByteAsNumberStepPerVpnEnabled'] = CustomerCe4ByteAsNumberStepPerVpnEnabled
        if CustomerCe4ByteAsNumberStepPerVpn is not None:
            properties['CustomerCe4ByteAsNumberStepPerVpn'] = CustomerCe4ByteAsNumberStepPerVpn
        if CustomerCe4ByteAsNumberStepPerCeEnabled is not None:
            properties['CustomerCe4ByteAsNumberStepPerCeEnabled'] = CustomerCe4ByteAsNumberStepPerCeEnabled
        if CustomerCe4ByteAsNumberStepPerCe is not None:
            properties['CustomerCe4ByteAsNumberStepPerCe'] = CustomerCe4ByteAsNumberStepPerCe
        if ProviderDistributionSelectorCount is not None:
            properties['ProviderDistributionSelectorCount'] = ProviderDistributionSelectorCount
        if ProviderMeshed is not None:
            properties['ProviderMeshed'] = ProviderMeshed
        if ProviderRdStart is not None:
            properties['ProviderRdStart'] = ProviderRdStart
        if ProviderRdStepPerVpnEnabled is not None:
            properties['ProviderRdStepPerVpnEnabled'] = ProviderRdStepPerVpnEnabled
        if ProviderRdStepPerVpn is not None:
            properties['ProviderRdStepPerVpn'] = ProviderRdStepPerVpn
        if ProviderRdStepPerCeEnabled is not None:
            properties['ProviderRdStepPerCeEnabled'] = ProviderRdStepPerCeEnabled
        if ProviderRdStepPerCe is not None:
            properties['ProviderRdStepPerCe'] = ProviderRdStepPerCe
        if ProviderAppendCeAsToPath is not None:
            properties['ProviderAppendCeAsToPath'] = ProviderAppendCeAsToPath
        if ProviderEnable4ByteAsNumber is not None:
            properties['ProviderEnable4ByteAsNumber'] = ProviderEnable4ByteAsNumber
        if ProviderCeAsNumberStart is not None:
            properties['ProviderCeAsNumberStart'] = ProviderCeAsNumberStart
        if ProviderCeAsNumberStepPerVpnEnabled is not None:
            properties['ProviderCeAsNumberStepPerVpnEnabled'] = ProviderCeAsNumberStepPerVpnEnabled
        if ProviderCeAsNumberStepPerVpn is not None:
            properties['ProviderCeAsNumberStepPerVpn'] = ProviderCeAsNumberStepPerVpn
        if ProviderCeAsNumberStepPerCeEnabled is not None:
            properties['ProviderCeAsNumberStepPerCeEnabled'] = ProviderCeAsNumberStepPerCeEnabled
        if ProviderCeAsNumberStepPerCe is not None:
            properties['ProviderCeAsNumberStepPerCe'] = ProviderCeAsNumberStepPerCe
        if ProviderCe4ByteAsNumberStart is not None:
            properties['ProviderCe4ByteAsNumberStart'] = ProviderCe4ByteAsNumberStart
        if ProviderCe4ByteAsNumberStepPerVpnEnabled is not None:
            properties['ProviderCe4ByteAsNumberStepPerVpnEnabled'] = ProviderCe4ByteAsNumberStepPerVpnEnabled
        if ProviderCe4ByteAsNumberStepPerVpn is not None:
            properties['ProviderCe4ByteAsNumberStepPerVpn'] = ProviderCe4ByteAsNumberStepPerVpn
        if ProviderCe4ByteAsNumberStepPerCeEnabled is not None:
            properties['ProviderCe4ByteAsNumberStepPerCeEnabled'] = ProviderCe4ByteAsNumberStepPerCeEnabled
        if ProviderCe4ByteAsNumberStepPerCe is not None:
            properties['ProviderCe4ByteAsNumberStepPerCe'] = ProviderCe4ByteAsNumberStepPerCe
        if CustomerPrefixLength is not None:
            properties['CustomerPrefixLength'] = CustomerPrefixLength
        if CustomerRoutesPerPe is not None:
            properties['CustomerRoutesPerPe'] = CustomerRoutesPerPe
        if CustomerOverlapRoutes is not None:
            properties['CustomerOverlapRoutes'] = CustomerOverlapRoutes
        if ProviderPrefixLength is not None:
            properties['ProviderPrefixLength'] = ProviderPrefixLength
        if ProviderRoutesPerPe is not None:
            properties['ProviderRoutesPerPe'] = ProviderRoutesPerPe
        if ProviderOverlapRoutes is not None:
            properties['ProviderOverlapRoutes'] = ProviderOverlapRoutes
        if ProviderStartLabel is not None:
            properties['ProviderStartLabel'] = ProviderStartLabel

        # call base class function, and it will send message to renix server to create a class.
        super(MplsL3VpnConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NumberOfVpns=None, RouteTargetStart=None, RouteTargetStep=None, CeProtocolAssignment=None, CustomerRdStart=None, CustomerRdStepPerVpnEnabled=None, CustomerRdStepPerVpn=None, CustomerRdStepPerCeEnabled=None, CustomerRdStepPerCe=None, CustomerEnable4ByteAsNumber=None, CustomerCeAsNumberStart=None, CustomerCeAsNumberStepPerVpnEnabled=None, CustomerCeAsNumberStepPerVpn=None, CustomerCeAsNumberStepPerCeEnabled=None, CustomerCeAsNumberStepPerCe=None, CustomerCe4ByteAsNumberStart=None, CustomerCe4ByteAsNumberStepPerVpnEnabled=None, CustomerCe4ByteAsNumberStepPerVpn=None, CustomerCe4ByteAsNumberStepPerCeEnabled=None, CustomerCe4ByteAsNumberStepPerCe=None, ProviderDistributionSelectorCount=None, ProviderMeshed=None, ProviderRdStart=None, ProviderRdStepPerVpnEnabled=None, ProviderRdStepPerVpn=None, ProviderRdStepPerCeEnabled=None, ProviderRdStepPerCe=None, ProviderAppendCeAsToPath=None, ProviderEnable4ByteAsNumber=None, ProviderCeAsNumberStart=None, ProviderCeAsNumberStepPerVpnEnabled=None, ProviderCeAsNumberStepPerVpn=None, ProviderCeAsNumberStepPerCeEnabled=None, ProviderCeAsNumberStepPerCe=None, ProviderCe4ByteAsNumberStart=None, ProviderCe4ByteAsNumberStepPerVpnEnabled=None, ProviderCe4ByteAsNumberStepPerVpn=None, ProviderCe4ByteAsNumberStepPerCeEnabled=None, ProviderCe4ByteAsNumberStepPerCe=None, CustomerPrefixLength=None, CustomerRoutesPerPe=None, CustomerOverlapRoutes=None, ProviderPrefixLength=None, ProviderRoutesPerPe=None, ProviderOverlapRoutes=None, ProviderStartLabel=None, **kwargs):
        properties = kwargs.copy()
        if NumberOfVpns is not None:
            self._NumberOfVpns = NumberOfVpns
            properties['NumberOfVpns'] = NumberOfVpns
        if RouteTargetStart is not None:
            self._RouteTargetStart = RouteTargetStart
            properties['RouteTargetStart'] = RouteTargetStart
        if RouteTargetStep is not None:
            self._RouteTargetStep = RouteTargetStep
            properties['RouteTargetStep'] = RouteTargetStep
        if CeProtocolAssignment is not None:
            self._CeProtocolAssignment = CeProtocolAssignment
            properties['CeProtocolAssignment'] = CeProtocolAssignment
        if CustomerRdStart is not None:
            self._CustomerRdStart = CustomerRdStart
            properties['CustomerRdStart'] = CustomerRdStart
        if CustomerRdStepPerVpnEnabled is not None:
            self._CustomerRdStepPerVpnEnabled = CustomerRdStepPerVpnEnabled
            properties['CustomerRdStepPerVpnEnabled'] = CustomerRdStepPerVpnEnabled
        if CustomerRdStepPerVpn is not None:
            self._CustomerRdStepPerVpn = CustomerRdStepPerVpn
            properties['CustomerRdStepPerVpn'] = CustomerRdStepPerVpn
        if CustomerRdStepPerCeEnabled is not None:
            self._CustomerRdStepPerCeEnabled = CustomerRdStepPerCeEnabled
            properties['CustomerRdStepPerCeEnabled'] = CustomerRdStepPerCeEnabled
        if CustomerRdStepPerCe is not None:
            self._CustomerRdStepPerCe = CustomerRdStepPerCe
            properties['CustomerRdStepPerCe'] = CustomerRdStepPerCe
        if CustomerEnable4ByteAsNumber is not None:
            self._CustomerEnable4ByteAsNumber = CustomerEnable4ByteAsNumber
            properties['CustomerEnable4ByteAsNumber'] = CustomerEnable4ByteAsNumber
        if CustomerCeAsNumberStart is not None:
            self._CustomerCeAsNumberStart = CustomerCeAsNumberStart
            properties['CustomerCeAsNumberStart'] = CustomerCeAsNumberStart
        if CustomerCeAsNumberStepPerVpnEnabled is not None:
            self._CustomerCeAsNumberStepPerVpnEnabled = CustomerCeAsNumberStepPerVpnEnabled
            properties['CustomerCeAsNumberStepPerVpnEnabled'] = CustomerCeAsNumberStepPerVpnEnabled
        if CustomerCeAsNumberStepPerVpn is not None:
            self._CustomerCeAsNumberStepPerVpn = CustomerCeAsNumberStepPerVpn
            properties['CustomerCeAsNumberStepPerVpn'] = CustomerCeAsNumberStepPerVpn
        if CustomerCeAsNumberStepPerCeEnabled is not None:
            self._CustomerCeAsNumberStepPerCeEnabled = CustomerCeAsNumberStepPerCeEnabled
            properties['CustomerCeAsNumberStepPerCeEnabled'] = CustomerCeAsNumberStepPerCeEnabled
        if CustomerCeAsNumberStepPerCe is not None:
            self._CustomerCeAsNumberStepPerCe = CustomerCeAsNumberStepPerCe
            properties['CustomerCeAsNumberStepPerCe'] = CustomerCeAsNumberStepPerCe
        if CustomerCe4ByteAsNumberStart is not None:
            self._CustomerCe4ByteAsNumberStart = CustomerCe4ByteAsNumberStart
            properties['CustomerCe4ByteAsNumberStart'] = CustomerCe4ByteAsNumberStart
        if CustomerCe4ByteAsNumberStepPerVpnEnabled is not None:
            self._CustomerCe4ByteAsNumberStepPerVpnEnabled = CustomerCe4ByteAsNumberStepPerVpnEnabled
            properties['CustomerCe4ByteAsNumberStepPerVpnEnabled'] = CustomerCe4ByteAsNumberStepPerVpnEnabled
        if CustomerCe4ByteAsNumberStepPerVpn is not None:
            self._CustomerCe4ByteAsNumberStepPerVpn = CustomerCe4ByteAsNumberStepPerVpn
            properties['CustomerCe4ByteAsNumberStepPerVpn'] = CustomerCe4ByteAsNumberStepPerVpn
        if CustomerCe4ByteAsNumberStepPerCeEnabled is not None:
            self._CustomerCe4ByteAsNumberStepPerCeEnabled = CustomerCe4ByteAsNumberStepPerCeEnabled
            properties['CustomerCe4ByteAsNumberStepPerCeEnabled'] = CustomerCe4ByteAsNumberStepPerCeEnabled
        if CustomerCe4ByteAsNumberStepPerCe is not None:
            self._CustomerCe4ByteAsNumberStepPerCe = CustomerCe4ByteAsNumberStepPerCe
            properties['CustomerCe4ByteAsNumberStepPerCe'] = CustomerCe4ByteAsNumberStepPerCe
        if ProviderDistributionSelectorCount is not None:
            self._ProviderDistributionSelectorCount = ProviderDistributionSelectorCount
            properties['ProviderDistributionSelectorCount'] = ProviderDistributionSelectorCount
        if ProviderMeshed is not None:
            self._ProviderMeshed = ProviderMeshed
            properties['ProviderMeshed'] = ProviderMeshed
        if ProviderRdStart is not None:
            self._ProviderRdStart = ProviderRdStart
            properties['ProviderRdStart'] = ProviderRdStart
        if ProviderRdStepPerVpnEnabled is not None:
            self._ProviderRdStepPerVpnEnabled = ProviderRdStepPerVpnEnabled
            properties['ProviderRdStepPerVpnEnabled'] = ProviderRdStepPerVpnEnabled
        if ProviderRdStepPerVpn is not None:
            self._ProviderRdStepPerVpn = ProviderRdStepPerVpn
            properties['ProviderRdStepPerVpn'] = ProviderRdStepPerVpn
        if ProviderRdStepPerCeEnabled is not None:
            self._ProviderRdStepPerCeEnabled = ProviderRdStepPerCeEnabled
            properties['ProviderRdStepPerCeEnabled'] = ProviderRdStepPerCeEnabled
        if ProviderRdStepPerCe is not None:
            self._ProviderRdStepPerCe = ProviderRdStepPerCe
            properties['ProviderRdStepPerCe'] = ProviderRdStepPerCe
        if ProviderAppendCeAsToPath is not None:
            self._ProviderAppendCeAsToPath = ProviderAppendCeAsToPath
            properties['ProviderAppendCeAsToPath'] = ProviderAppendCeAsToPath
        if ProviderEnable4ByteAsNumber is not None:
            self._ProviderEnable4ByteAsNumber = ProviderEnable4ByteAsNumber
            properties['ProviderEnable4ByteAsNumber'] = ProviderEnable4ByteAsNumber
        if ProviderCeAsNumberStart is not None:
            self._ProviderCeAsNumberStart = ProviderCeAsNumberStart
            properties['ProviderCeAsNumberStart'] = ProviderCeAsNumberStart
        if ProviderCeAsNumberStepPerVpnEnabled is not None:
            self._ProviderCeAsNumberStepPerVpnEnabled = ProviderCeAsNumberStepPerVpnEnabled
            properties['ProviderCeAsNumberStepPerVpnEnabled'] = ProviderCeAsNumberStepPerVpnEnabled
        if ProviderCeAsNumberStepPerVpn is not None:
            self._ProviderCeAsNumberStepPerVpn = ProviderCeAsNumberStepPerVpn
            properties['ProviderCeAsNumberStepPerVpn'] = ProviderCeAsNumberStepPerVpn
        if ProviderCeAsNumberStepPerCeEnabled is not None:
            self._ProviderCeAsNumberStepPerCeEnabled = ProviderCeAsNumberStepPerCeEnabled
            properties['ProviderCeAsNumberStepPerCeEnabled'] = ProviderCeAsNumberStepPerCeEnabled
        if ProviderCeAsNumberStepPerCe is not None:
            self._ProviderCeAsNumberStepPerCe = ProviderCeAsNumberStepPerCe
            properties['ProviderCeAsNumberStepPerCe'] = ProviderCeAsNumberStepPerCe
        if ProviderCe4ByteAsNumberStart is not None:
            self._ProviderCe4ByteAsNumberStart = ProviderCe4ByteAsNumberStart
            properties['ProviderCe4ByteAsNumberStart'] = ProviderCe4ByteAsNumberStart
        if ProviderCe4ByteAsNumberStepPerVpnEnabled is not None:
            self._ProviderCe4ByteAsNumberStepPerVpnEnabled = ProviderCe4ByteAsNumberStepPerVpnEnabled
            properties['ProviderCe4ByteAsNumberStepPerVpnEnabled'] = ProviderCe4ByteAsNumberStepPerVpnEnabled
        if ProviderCe4ByteAsNumberStepPerVpn is not None:
            self._ProviderCe4ByteAsNumberStepPerVpn = ProviderCe4ByteAsNumberStepPerVpn
            properties['ProviderCe4ByteAsNumberStepPerVpn'] = ProviderCe4ByteAsNumberStepPerVpn
        if ProviderCe4ByteAsNumberStepPerCeEnabled is not None:
            self._ProviderCe4ByteAsNumberStepPerCeEnabled = ProviderCe4ByteAsNumberStepPerCeEnabled
            properties['ProviderCe4ByteAsNumberStepPerCeEnabled'] = ProviderCe4ByteAsNumberStepPerCeEnabled
        if ProviderCe4ByteAsNumberStepPerCe is not None:
            self._ProviderCe4ByteAsNumberStepPerCe = ProviderCe4ByteAsNumberStepPerCe
            properties['ProviderCe4ByteAsNumberStepPerCe'] = ProviderCe4ByteAsNumberStepPerCe
        if CustomerPrefixLength is not None:
            self._CustomerPrefixLength = CustomerPrefixLength
            properties['CustomerPrefixLength'] = CustomerPrefixLength
        if CustomerRoutesPerPe is not None:
            self._CustomerRoutesPerPe = CustomerRoutesPerPe
            properties['CustomerRoutesPerPe'] = CustomerRoutesPerPe
        if CustomerOverlapRoutes is not None:
            self._CustomerOverlapRoutes = CustomerOverlapRoutes
            properties['CustomerOverlapRoutes'] = CustomerOverlapRoutes
        if ProviderPrefixLength is not None:
            self._ProviderPrefixLength = ProviderPrefixLength
            properties['ProviderPrefixLength'] = ProviderPrefixLength
        if ProviderRoutesPerPe is not None:
            self._ProviderRoutesPerPe = ProviderRoutesPerPe
            properties['ProviderRoutesPerPe'] = ProviderRoutesPerPe
        if ProviderOverlapRoutes is not None:
            self._ProviderOverlapRoutes = ProviderOverlapRoutes
            properties['ProviderOverlapRoutes'] = ProviderOverlapRoutes
        if ProviderStartLabel is not None:
            self._ProviderStartLabel = ProviderStartLabel
            properties['ProviderStartLabel'] = ProviderStartLabel

        super(MplsL3VpnConfig, self).edit(**properties)

    @property
    def NumberOfVpns(self):
        """
        get the value of property _NumberOfVpns
        """
        if self.force_auto_sync:
            self.get('NumberOfVpns')
        return self._NumberOfVpns

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
    def VpnAssignment(self):
        """
        get the value of property _VpnAssignment
        """
        if self.force_auto_sync:
            self.get('VpnAssignment')
        return self._VpnAssignment

    @property
    def CeProtocol(self):
        """
        get the value of property _CeProtocol
        """
        if self.force_auto_sync:
            self.get('CeProtocol')
        return self._CeProtocol

    @property
    def CeProtocolAssignment(self):
        """
        get the value of property _CeProtocolAssignment
        """
        if self.force_auto_sync:
            self.get('CeProtocolAssignment')
        return self._CeProtocolAssignment

    @property
    def CustomerRdStart(self):
        """
        get the value of property _CustomerRdStart
        """
        if self.force_auto_sync:
            self.get('CustomerRdStart')
        return self._CustomerRdStart

    @property
    def CustomerRdStepPerVpnEnabled(self):
        """
        get the value of property _CustomerRdStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerVpnEnabled')
        return self._CustomerRdStepPerVpnEnabled

    @property
    def CustomerRdStepPerVpn(self):
        """
        get the value of property _CustomerRdStepPerVpn
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerVpn')
        return self._CustomerRdStepPerVpn

    @property
    def CustomerRdStepPerCeEnabled(self):
        """
        get the value of property _CustomerRdStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerCeEnabled')
        return self._CustomerRdStepPerCeEnabled

    @property
    def CustomerRdStepPerCe(self):
        """
        get the value of property _CustomerRdStepPerCe
        """
        if self.force_auto_sync:
            self.get('CustomerRdStepPerCe')
        return self._CustomerRdStepPerCe

    @property
    def CustomerEnable4ByteAsNumber(self):
        """
        get the value of property _CustomerEnable4ByteAsNumber
        """
        if self.force_auto_sync:
            self.get('CustomerEnable4ByteAsNumber')
        return self._CustomerEnable4ByteAsNumber

    @property
    def CustomerCeAsNumberStart(self):
        """
        get the value of property _CustomerCeAsNumberStart
        """
        if self.force_auto_sync:
            self.get('CustomerCeAsNumberStart')
        return self._CustomerCeAsNumberStart

    @property
    def CustomerCeAsNumberStepPerVpnEnabled(self):
        """
        get the value of property _CustomerCeAsNumberStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerCeAsNumberStepPerVpnEnabled')
        return self._CustomerCeAsNumberStepPerVpnEnabled

    @property
    def CustomerCeAsNumberStepPerVpn(self):
        """
        get the value of property _CustomerCeAsNumberStepPerVpn
        """
        if self.force_auto_sync:
            self.get('CustomerCeAsNumberStepPerVpn')
        return self._CustomerCeAsNumberStepPerVpn

    @property
    def CustomerCeAsNumberStepPerCeEnabled(self):
        """
        get the value of property _CustomerCeAsNumberStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerCeAsNumberStepPerCeEnabled')
        return self._CustomerCeAsNumberStepPerCeEnabled

    @property
    def CustomerCeAsNumberStepPerCe(self):
        """
        get the value of property _CustomerCeAsNumberStepPerCe
        """
        if self.force_auto_sync:
            self.get('CustomerCeAsNumberStepPerCe')
        return self._CustomerCeAsNumberStepPerCe

    @property
    def CustomerCe4ByteAsNumberStart(self):
        """
        get the value of property _CustomerCe4ByteAsNumberStart
        """
        if self.force_auto_sync:
            self.get('CustomerCe4ByteAsNumberStart')
        return self._CustomerCe4ByteAsNumberStart

    @property
    def CustomerCe4ByteAsNumberStepPerVpnEnabled(self):
        """
        get the value of property _CustomerCe4ByteAsNumberStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerCe4ByteAsNumberStepPerVpnEnabled')
        return self._CustomerCe4ByteAsNumberStepPerVpnEnabled

    @property
    def CustomerCe4ByteAsNumberStepPerVpn(self):
        """
        get the value of property _CustomerCe4ByteAsNumberStepPerVpn
        """
        if self.force_auto_sync:
            self.get('CustomerCe4ByteAsNumberStepPerVpn')
        return self._CustomerCe4ByteAsNumberStepPerVpn

    @property
    def CustomerCe4ByteAsNumberStepPerCeEnabled(self):
        """
        get the value of property _CustomerCe4ByteAsNumberStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('CustomerCe4ByteAsNumberStepPerCeEnabled')
        return self._CustomerCe4ByteAsNumberStepPerCeEnabled

    @property
    def CustomerCe4ByteAsNumberStepPerCe(self):
        """
        get the value of property _CustomerCe4ByteAsNumberStepPerCe
        """
        if self.force_auto_sync:
            self.get('CustomerCe4ByteAsNumberStepPerCe')
        return self._CustomerCe4ByteAsNumberStepPerCe

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
    def ProviderMeshed(self):
        """
        get the value of property _ProviderMeshed
        """
        if self.force_auto_sync:
            self.get('ProviderMeshed')
        return self._ProviderMeshed

    @property
    def ProviderRdStart(self):
        """
        get the value of property _ProviderRdStart
        """
        if self.force_auto_sync:
            self.get('ProviderRdStart')
        return self._ProviderRdStart

    @property
    def ProviderRdStepPerVpnEnabled(self):
        """
        get the value of property _ProviderRdStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerVpnEnabled')
        return self._ProviderRdStepPerVpnEnabled

    @property
    def ProviderRdStepPerVpn(self):
        """
        get the value of property _ProviderRdStepPerVpn
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerVpn')
        return self._ProviderRdStepPerVpn

    @property
    def ProviderRdStepPerCeEnabled(self):
        """
        get the value of property _ProviderRdStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerCeEnabled')
        return self._ProviderRdStepPerCeEnabled

    @property
    def ProviderRdStepPerCe(self):
        """
        get the value of property _ProviderRdStepPerCe
        """
        if self.force_auto_sync:
            self.get('ProviderRdStepPerCe')
        return self._ProviderRdStepPerCe

    @property
    def ProviderAppendCeAsToPath(self):
        """
        get the value of property _ProviderAppendCeAsToPath
        """
        if self.force_auto_sync:
            self.get('ProviderAppendCeAsToPath')
        return self._ProviderAppendCeAsToPath

    @property
    def ProviderEnable4ByteAsNumber(self):
        """
        get the value of property _ProviderEnable4ByteAsNumber
        """
        if self.force_auto_sync:
            self.get('ProviderEnable4ByteAsNumber')
        return self._ProviderEnable4ByteAsNumber

    @property
    def ProviderCeAsNumberStart(self):
        """
        get the value of property _ProviderCeAsNumberStart
        """
        if self.force_auto_sync:
            self.get('ProviderCeAsNumberStart')
        return self._ProviderCeAsNumberStart

    @property
    def ProviderCeAsNumberStepPerVpnEnabled(self):
        """
        get the value of property _ProviderCeAsNumberStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderCeAsNumberStepPerVpnEnabled')
        return self._ProviderCeAsNumberStepPerVpnEnabled

    @property
    def ProviderCeAsNumberStepPerVpn(self):
        """
        get the value of property _ProviderCeAsNumberStepPerVpn
        """
        if self.force_auto_sync:
            self.get('ProviderCeAsNumberStepPerVpn')
        return self._ProviderCeAsNumberStepPerVpn

    @property
    def ProviderCeAsNumberStepPerCeEnabled(self):
        """
        get the value of property _ProviderCeAsNumberStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderCeAsNumberStepPerCeEnabled')
        return self._ProviderCeAsNumberStepPerCeEnabled

    @property
    def ProviderCeAsNumberStepPerCe(self):
        """
        get the value of property _ProviderCeAsNumberStepPerCe
        """
        if self.force_auto_sync:
            self.get('ProviderCeAsNumberStepPerCe')
        return self._ProviderCeAsNumberStepPerCe

    @property
    def ProviderCe4ByteAsNumberStart(self):
        """
        get the value of property _ProviderCe4ByteAsNumberStart
        """
        if self.force_auto_sync:
            self.get('ProviderCe4ByteAsNumberStart')
        return self._ProviderCe4ByteAsNumberStart

    @property
    def ProviderCe4ByteAsNumberStepPerVpnEnabled(self):
        """
        get the value of property _ProviderCe4ByteAsNumberStepPerVpnEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderCe4ByteAsNumberStepPerVpnEnabled')
        return self._ProviderCe4ByteAsNumberStepPerVpnEnabled

    @property
    def ProviderCe4ByteAsNumberStepPerVpn(self):
        """
        get the value of property _ProviderCe4ByteAsNumberStepPerVpn
        """
        if self.force_auto_sync:
            self.get('ProviderCe4ByteAsNumberStepPerVpn')
        return self._ProviderCe4ByteAsNumberStepPerVpn

    @property
    def ProviderCe4ByteAsNumberStepPerCeEnabled(self):
        """
        get the value of property _ProviderCe4ByteAsNumberStepPerCeEnabled
        """
        if self.force_auto_sync:
            self.get('ProviderCe4ByteAsNumberStepPerCeEnabled')
        return self._ProviderCe4ByteAsNumberStepPerCeEnabled

    @property
    def ProviderCe4ByteAsNumberStepPerCe(self):
        """
        get the value of property _ProviderCe4ByteAsNumberStepPerCe
        """
        if self.force_auto_sync:
            self.get('ProviderCe4ByteAsNumberStepPerCe')
        return self._ProviderCe4ByteAsNumberStepPerCe

    @property
    def CustomerPrefixLength(self):
        """
        get the value of property _CustomerPrefixLength
        """
        if self.force_auto_sync:
            self.get('CustomerPrefixLength')
        return self._CustomerPrefixLength

    @property
    def CustomerRoutesPerPe(self):
        """
        get the value of property _CustomerRoutesPerPe
        """
        if self.force_auto_sync:
            self.get('CustomerRoutesPerPe')
        return self._CustomerRoutesPerPe

    @property
    def CustomerOverlapRoutes(self):
        """
        get the value of property _CustomerOverlapRoutes
        """
        if self.force_auto_sync:
            self.get('CustomerOverlapRoutes')
        return self._CustomerOverlapRoutes

    @property
    def CustomerRouteType(self):
        """
        get the value of property _CustomerRouteType
        """
        if self.force_auto_sync:
            self.get('CustomerRouteType')
        return self._CustomerRouteType

    @property
    def ProviderPrefixLength(self):
        """
        get the value of property _ProviderPrefixLength
        """
        if self.force_auto_sync:
            self.get('ProviderPrefixLength')
        return self._ProviderPrefixLength

    @property
    def ProviderRoutesPerPe(self):
        """
        get the value of property _ProviderRoutesPerPe
        """
        if self.force_auto_sync:
            self.get('ProviderRoutesPerPe')
        return self._ProviderRoutesPerPe

    @property
    def ProviderOverlapRoutes(self):
        """
        get the value of property _ProviderOverlapRoutes
        """
        if self.force_auto_sync:
            self.get('ProviderOverlapRoutes')
        return self._ProviderOverlapRoutes

    @property
    def ProviderLabelMethod(self):
        """
        get the value of property _ProviderLabelMethod
        """
        if self.force_auto_sync:
            self.get('ProviderLabelMethod')
        return self._ProviderLabelMethod

    @property
    def ProviderStartLabel(self):
        """
        get the value of property _ProviderStartLabel
        """
        if self.force_auto_sync:
            self.get('ProviderStartLabel')
        return self._ProviderStartLabel

    @NumberOfVpns.setter
    def NumberOfVpns(self, value):
        self._NumberOfVpns = value
        self.edit(NumberOfVpns=value)

    @RouteTargetStart.setter
    def RouteTargetStart(self, value):
        self._RouteTargetStart = value
        self.edit(RouteTargetStart=value)

    @RouteTargetStep.setter
    def RouteTargetStep(self, value):
        self._RouteTargetStep = value
        self.edit(RouteTargetStep=value)

    @CeProtocolAssignment.setter
    def CeProtocolAssignment(self, value):
        self._CeProtocolAssignment = value
        self.edit(CeProtocolAssignment=value)

    @CustomerRdStart.setter
    def CustomerRdStart(self, value):
        self._CustomerRdStart = value
        self.edit(CustomerRdStart=value)

    @CustomerRdStepPerVpnEnabled.setter
    def CustomerRdStepPerVpnEnabled(self, value):
        self._CustomerRdStepPerVpnEnabled = value
        self.edit(CustomerRdStepPerVpnEnabled=value)

    @CustomerRdStepPerVpn.setter
    def CustomerRdStepPerVpn(self, value):
        self._CustomerRdStepPerVpn = value
        self.edit(CustomerRdStepPerVpn=value)

    @CustomerRdStepPerCeEnabled.setter
    def CustomerRdStepPerCeEnabled(self, value):
        self._CustomerRdStepPerCeEnabled = value
        self.edit(CustomerRdStepPerCeEnabled=value)

    @CustomerRdStepPerCe.setter
    def CustomerRdStepPerCe(self, value):
        self._CustomerRdStepPerCe = value
        self.edit(CustomerRdStepPerCe=value)

    @CustomerEnable4ByteAsNumber.setter
    def CustomerEnable4ByteAsNumber(self, value):
        self._CustomerEnable4ByteAsNumber = value
        self.edit(CustomerEnable4ByteAsNumber=value)

    @CustomerCeAsNumberStart.setter
    def CustomerCeAsNumberStart(self, value):
        self._CustomerCeAsNumberStart = value
        self.edit(CustomerCeAsNumberStart=value)

    @CustomerCeAsNumberStepPerVpnEnabled.setter
    def CustomerCeAsNumberStepPerVpnEnabled(self, value):
        self._CustomerCeAsNumberStepPerVpnEnabled = value
        self.edit(CustomerCeAsNumberStepPerVpnEnabled=value)

    @CustomerCeAsNumberStepPerVpn.setter
    def CustomerCeAsNumberStepPerVpn(self, value):
        self._CustomerCeAsNumberStepPerVpn = value
        self.edit(CustomerCeAsNumberStepPerVpn=value)

    @CustomerCeAsNumberStepPerCeEnabled.setter
    def CustomerCeAsNumberStepPerCeEnabled(self, value):
        self._CustomerCeAsNumberStepPerCeEnabled = value
        self.edit(CustomerCeAsNumberStepPerCeEnabled=value)

    @CustomerCeAsNumberStepPerCe.setter
    def CustomerCeAsNumberStepPerCe(self, value):
        self._CustomerCeAsNumberStepPerCe = value
        self.edit(CustomerCeAsNumberStepPerCe=value)

    @CustomerCe4ByteAsNumberStart.setter
    def CustomerCe4ByteAsNumberStart(self, value):
        self._CustomerCe4ByteAsNumberStart = value
        self.edit(CustomerCe4ByteAsNumberStart=value)

    @CustomerCe4ByteAsNumberStepPerVpnEnabled.setter
    def CustomerCe4ByteAsNumberStepPerVpnEnabled(self, value):
        self._CustomerCe4ByteAsNumberStepPerVpnEnabled = value
        self.edit(CustomerCe4ByteAsNumberStepPerVpnEnabled=value)

    @CustomerCe4ByteAsNumberStepPerVpn.setter
    def CustomerCe4ByteAsNumberStepPerVpn(self, value):
        self._CustomerCe4ByteAsNumberStepPerVpn = value
        self.edit(CustomerCe4ByteAsNumberStepPerVpn=value)

    @CustomerCe4ByteAsNumberStepPerCeEnabled.setter
    def CustomerCe4ByteAsNumberStepPerCeEnabled(self, value):
        self._CustomerCe4ByteAsNumberStepPerCeEnabled = value
        self.edit(CustomerCe4ByteAsNumberStepPerCeEnabled=value)

    @CustomerCe4ByteAsNumberStepPerCe.setter
    def CustomerCe4ByteAsNumberStepPerCe(self, value):
        self._CustomerCe4ByteAsNumberStepPerCe = value
        self.edit(CustomerCe4ByteAsNumberStepPerCe=value)

    @ProviderDistributionSelectorCount.setter
    def ProviderDistributionSelectorCount(self, value):
        self._ProviderDistributionSelectorCount = value
        self.edit(ProviderDistributionSelectorCount=value)

    @ProviderMeshed.setter
    def ProviderMeshed(self, value):
        self._ProviderMeshed = value
        self.edit(ProviderMeshed=value)

    @ProviderRdStart.setter
    def ProviderRdStart(self, value):
        self._ProviderRdStart = value
        self.edit(ProviderRdStart=value)

    @ProviderRdStepPerVpnEnabled.setter
    def ProviderRdStepPerVpnEnabled(self, value):
        self._ProviderRdStepPerVpnEnabled = value
        self.edit(ProviderRdStepPerVpnEnabled=value)

    @ProviderRdStepPerVpn.setter
    def ProviderRdStepPerVpn(self, value):
        self._ProviderRdStepPerVpn = value
        self.edit(ProviderRdStepPerVpn=value)

    @ProviderRdStepPerCeEnabled.setter
    def ProviderRdStepPerCeEnabled(self, value):
        self._ProviderRdStepPerCeEnabled = value
        self.edit(ProviderRdStepPerCeEnabled=value)

    @ProviderRdStepPerCe.setter
    def ProviderRdStepPerCe(self, value):
        self._ProviderRdStepPerCe = value
        self.edit(ProviderRdStepPerCe=value)

    @ProviderAppendCeAsToPath.setter
    def ProviderAppendCeAsToPath(self, value):
        self._ProviderAppendCeAsToPath = value
        self.edit(ProviderAppendCeAsToPath=value)

    @ProviderEnable4ByteAsNumber.setter
    def ProviderEnable4ByteAsNumber(self, value):
        self._ProviderEnable4ByteAsNumber = value
        self.edit(ProviderEnable4ByteAsNumber=value)

    @ProviderCeAsNumberStart.setter
    def ProviderCeAsNumberStart(self, value):
        self._ProviderCeAsNumberStart = value
        self.edit(ProviderCeAsNumberStart=value)

    @ProviderCeAsNumberStepPerVpnEnabled.setter
    def ProviderCeAsNumberStepPerVpnEnabled(self, value):
        self._ProviderCeAsNumberStepPerVpnEnabled = value
        self.edit(ProviderCeAsNumberStepPerVpnEnabled=value)

    @ProviderCeAsNumberStepPerVpn.setter
    def ProviderCeAsNumberStepPerVpn(self, value):
        self._ProviderCeAsNumberStepPerVpn = value
        self.edit(ProviderCeAsNumberStepPerVpn=value)

    @ProviderCeAsNumberStepPerCeEnabled.setter
    def ProviderCeAsNumberStepPerCeEnabled(self, value):
        self._ProviderCeAsNumberStepPerCeEnabled = value
        self.edit(ProviderCeAsNumberStepPerCeEnabled=value)

    @ProviderCeAsNumberStepPerCe.setter
    def ProviderCeAsNumberStepPerCe(self, value):
        self._ProviderCeAsNumberStepPerCe = value
        self.edit(ProviderCeAsNumberStepPerCe=value)

    @ProviderCe4ByteAsNumberStart.setter
    def ProviderCe4ByteAsNumberStart(self, value):
        self._ProviderCe4ByteAsNumberStart = value
        self.edit(ProviderCe4ByteAsNumberStart=value)

    @ProviderCe4ByteAsNumberStepPerVpnEnabled.setter
    def ProviderCe4ByteAsNumberStepPerVpnEnabled(self, value):
        self._ProviderCe4ByteAsNumberStepPerVpnEnabled = value
        self.edit(ProviderCe4ByteAsNumberStepPerVpnEnabled=value)

    @ProviderCe4ByteAsNumberStepPerVpn.setter
    def ProviderCe4ByteAsNumberStepPerVpn(self, value):
        self._ProviderCe4ByteAsNumberStepPerVpn = value
        self.edit(ProviderCe4ByteAsNumberStepPerVpn=value)

    @ProviderCe4ByteAsNumberStepPerCeEnabled.setter
    def ProviderCe4ByteAsNumberStepPerCeEnabled(self, value):
        self._ProviderCe4ByteAsNumberStepPerCeEnabled = value
        self.edit(ProviderCe4ByteAsNumberStepPerCeEnabled=value)

    @ProviderCe4ByteAsNumberStepPerCe.setter
    def ProviderCe4ByteAsNumberStepPerCe(self, value):
        self._ProviderCe4ByteAsNumberStepPerCe = value
        self.edit(ProviderCe4ByteAsNumberStepPerCe=value)

    @CustomerPrefixLength.setter
    def CustomerPrefixLength(self, value):
        self._CustomerPrefixLength = value
        self.edit(CustomerPrefixLength=value)

    @CustomerRoutesPerPe.setter
    def CustomerRoutesPerPe(self, value):
        self._CustomerRoutesPerPe = value
        self.edit(CustomerRoutesPerPe=value)

    @CustomerOverlapRoutes.setter
    def CustomerOverlapRoutes(self, value):
        self._CustomerOverlapRoutes = value
        self.edit(CustomerOverlapRoutes=value)

    @ProviderPrefixLength.setter
    def ProviderPrefixLength(self, value):
        self._ProviderPrefixLength = value
        self.edit(ProviderPrefixLength=value)

    @ProviderRoutesPerPe.setter
    def ProviderRoutesPerPe(self, value):
        self._ProviderRoutesPerPe = value
        self.edit(ProviderRoutesPerPe=value)

    @ProviderOverlapRoutes.setter
    def ProviderOverlapRoutes(self, value):
        self._ProviderOverlapRoutes = value
        self.edit(ProviderOverlapRoutes=value)

    @ProviderStartLabel.setter
    def ProviderStartLabel(self, value):
        self._ProviderStartLabel = value
        self.edit(ProviderStartLabel=value)

    def _set_numberofvpns_with_str(self, value):
        try:
            self._NumberOfVpns = int(value)
        except ValueError:
            self._NumberOfVpns = hex(int(value, 16))

    def _set_routetargetstart_with_str(self, value):
        self._RouteTargetStart = value

    def _set_routetargetstep_with_str(self, value):
        self._RouteTargetStep = value

    def _set_rdassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._RdAssignment = EnumMplsRdAssignment.%s' % value[:seperate])

    def _set_vpnassignment_with_str(self, value):
        seperate = value.find(':')
        exec('self._VpnAssignment = EnumMplsAssignment.%s' % value[:seperate])

    def _set_ceprotocol_with_str(self, value):
        seperate = value.find(':')
        exec('self._CeProtocol = EnumMplsCeProtocol.%s' % value[:seperate])

    def _set_ceprotocolassignment_with_str(self, value):
        self._CeProtocolAssignment = value

    def _set_customerrdstart_with_str(self, value):
        self._CustomerRdStart = value

    def _set_customerrdsteppervpnenabled_with_str(self, value):
        self._CustomerRdStepPerVpnEnabled = (value == 'True')

    def _set_customerrdsteppervpn_with_str(self, value):
        self._CustomerRdStepPerVpn = value

    def _set_customerrdstepperceenabled_with_str(self, value):
        self._CustomerRdStepPerCeEnabled = (value == 'True')

    def _set_customerrdstepperce_with_str(self, value):
        self._CustomerRdStepPerCe = value

    def _set_customerenable4byteasnumber_with_str(self, value):
        self._CustomerEnable4ByteAsNumber = (value == 'True')

    def _set_customerceasnumberstart_with_str(self, value):
        try:
            self._CustomerCeAsNumberStart = int(value)
        except ValueError:
            self._CustomerCeAsNumberStart = hex(int(value, 16))

    def _set_customerceasnumbersteppervpnenabled_with_str(self, value):
        self._CustomerCeAsNumberStepPerVpnEnabled = (value == 'True')

    def _set_customerceasnumbersteppervpn_with_str(self, value):
        try:
            self._CustomerCeAsNumberStepPerVpn = int(value)
        except ValueError:
            self._CustomerCeAsNumberStepPerVpn = hex(int(value, 16))

    def _set_customerceasnumberstepperceenabled_with_str(self, value):
        self._CustomerCeAsNumberStepPerCeEnabled = (value == 'True')

    def _set_customerceasnumberstepperce_with_str(self, value):
        try:
            self._CustomerCeAsNumberStepPerCe = int(value)
        except ValueError:
            self._CustomerCeAsNumberStepPerCe = hex(int(value, 16))

    def _set_customerce4byteasnumberstart_with_str(self, value):
        try:
            self._CustomerCe4ByteAsNumberStart = int(value)
        except ValueError:
            self._CustomerCe4ByteAsNumberStart = hex(int(value, 16))

    def _set_customerce4byteasnumbersteppervpnenabled_with_str(self, value):
        self._CustomerCe4ByteAsNumberStepPerVpnEnabled = (value == 'True')

    def _set_customerce4byteasnumbersteppervpn_with_str(self, value):
        try:
            self._CustomerCe4ByteAsNumberStepPerVpn = int(value)
        except ValueError:
            self._CustomerCe4ByteAsNumberStepPerVpn = hex(int(value, 16))

    def _set_customerce4byteasnumberstepperceenabled_with_str(self, value):
        self._CustomerCe4ByteAsNumberStepPerCeEnabled = (value == 'True')

    def _set_customerce4byteasnumberstepperce_with_str(self, value):
        try:
            self._CustomerCe4ByteAsNumberStepPerCe = int(value)
        except ValueError:
            self._CustomerCe4ByteAsNumberStepPerCe = hex(int(value, 16))

    def _set_providerdistributionselector_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProviderDistributionSelector = EnumMplsDistributionSelector.%s' % value[:seperate])

    def _set_providerdistributionselectorcount_with_str(self, value):
        try:
            self._ProviderDistributionSelectorCount = int(value)
        except ValueError:
            self._ProviderDistributionSelectorCount = hex(int(value, 16))

    def _set_providermeshed_with_str(self, value):
        self._ProviderMeshed = (value == 'True')

    def _set_providerrdstart_with_str(self, value):
        self._ProviderRdStart = value

    def _set_providerrdsteppervpnenabled_with_str(self, value):
        self._ProviderRdStepPerVpnEnabled = (value == 'True')

    def _set_providerrdsteppervpn_with_str(self, value):
        self._ProviderRdStepPerVpn = value

    def _set_providerrdstepperceenabled_with_str(self, value):
        self._ProviderRdStepPerCeEnabled = (value == 'True')

    def _set_providerrdstepperce_with_str(self, value):
        self._ProviderRdStepPerCe = value

    def _set_providerappendceastopath_with_str(self, value):
        self._ProviderAppendCeAsToPath = (value == 'True')

    def _set_providerenable4byteasnumber_with_str(self, value):
        self._ProviderEnable4ByteAsNumber = (value == 'True')

    def _set_providerceasnumberstart_with_str(self, value):
        try:
            self._ProviderCeAsNumberStart = int(value)
        except ValueError:
            self._ProviderCeAsNumberStart = hex(int(value, 16))

    def _set_providerceasnumbersteppervpnenabled_with_str(self, value):
        self._ProviderCeAsNumberStepPerVpnEnabled = (value == 'True')

    def _set_providerceasnumbersteppervpn_with_str(self, value):
        try:
            self._ProviderCeAsNumberStepPerVpn = int(value)
        except ValueError:
            self._ProviderCeAsNumberStepPerVpn = hex(int(value, 16))

    def _set_providerceasnumberstepperceenabled_with_str(self, value):
        self._ProviderCeAsNumberStepPerCeEnabled = (value == 'True')

    def _set_providerceasnumberstepperce_with_str(self, value):
        try:
            self._ProviderCeAsNumberStepPerCe = int(value)
        except ValueError:
            self._ProviderCeAsNumberStepPerCe = hex(int(value, 16))

    def _set_providerce4byteasnumberstart_with_str(self, value):
        try:
            self._ProviderCe4ByteAsNumberStart = int(value)
        except ValueError:
            self._ProviderCe4ByteAsNumberStart = hex(int(value, 16))

    def _set_providerce4byteasnumbersteppervpnenabled_with_str(self, value):
        self._ProviderCe4ByteAsNumberStepPerVpnEnabled = (value == 'True')

    def _set_providerce4byteasnumbersteppervpn_with_str(self, value):
        try:
            self._ProviderCe4ByteAsNumberStepPerVpn = int(value)
        except ValueError:
            self._ProviderCe4ByteAsNumberStepPerVpn = hex(int(value, 16))

    def _set_providerce4byteasnumberstepperceenabled_with_str(self, value):
        self._ProviderCe4ByteAsNumberStepPerCeEnabled = (value == 'True')

    def _set_providerce4byteasnumberstepperce_with_str(self, value):
        try:
            self._ProviderCe4ByteAsNumberStepPerCe = int(value)
        except ValueError:
            self._ProviderCe4ByteAsNumberStepPerCe = hex(int(value, 16))

    def _set_customerprefixlength_with_str(self, value):
        try:
            self._CustomerPrefixLength = int(value)
        except ValueError:
            self._CustomerPrefixLength = hex(int(value, 16))

    def _set_customerroutesperpe_with_str(self, value):
        try:
            self._CustomerRoutesPerPe = int(value)
        except ValueError:
            self._CustomerRoutesPerPe = hex(int(value, 16))

    def _set_customeroverlaproutes_with_str(self, value):
        self._CustomerOverlapRoutes = (value == 'True')

    def _set_customerroutetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CustomerRouteType = EnumMplsRouteType.%s' % value[:seperate])

    def _set_providerprefixlength_with_str(self, value):
        try:
            self._ProviderPrefixLength = int(value)
        except ValueError:
            self._ProviderPrefixLength = hex(int(value, 16))

    def _set_providerroutesperpe_with_str(self, value):
        try:
            self._ProviderRoutesPerPe = int(value)
        except ValueError:
            self._ProviderRoutesPerPe = hex(int(value, 16))

    def _set_provideroverlaproutes_with_str(self, value):
        self._ProviderOverlapRoutes = (value == 'True')

    def _set_providerlabelmethod_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProviderLabelMethod = EnumMplsLabelMethod.%s' % value[:seperate])

    def _set_providerstartlabel_with_str(self, value):
        try:
            self._ProviderStartLabel = int(value)
        except ValueError:
            self._ProviderStartLabel = hex(int(value, 16))

