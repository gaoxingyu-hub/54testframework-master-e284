"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class Ospfv2LsaWizardConfig(WizardConfigBase):
    def __init__(self, TopologyType=None, SimulatedRoutersCount=None, InterfaceType=None, RouterMaxInterfaceCount=None, TransitNetworkMaxRouterCount=None, UneditableSimulatedRoutersCount=None, EmulatedRouterPossessSimulatedRouterCount=None, RowCount=None, ColumnCount=None, GridEmulatedRouterPosition=None, EmulatedRouterAttachRowIndex=None, EmulatedRouterAttachColumnIndex=None, MeshRouterCount=None, MeshEmulatedRouterPosition=None, RingRouterCount=None, RingEmulatedRouterPosition=None, HubSpokeRouterCount=None, HubSpokeEmulatedRouterPosition=None, StartingPrefixRange=None, EndingPrefixRange=None, AreaType=None, InterfacePrefixLength=None, StartingRouterId=None, RouterIdStep=None, StubEmulated=None, StubSimulated=None, StubRoutesCount=None, StubOverride=None, StubStartingIpPrefix=None, StubEndingIpPrefix=None, StubDistributionType=None, StubStartPrefixLength=None, StubEndPrefixLength=None, StubPrimaryMetric=None, SummaryEmulated=None, SummarySimulated=None, SummaryRoutesCount=None, SummaryOverride=None, SummaryStartingIpPrefix=None, SummaryEndingIpPrefix=None, SummaryDistributionType=None, SummaryStartPrefixLength=None, SummaryEndPrefixLength=None, SummaryPrimaryMetric=None, ExternalEmulated=None, ExternalSimulated=None, ExternalRoutesCount=None, ExternalOverride=None, ExternalStartingIpPrefix=None, ExternalEndingIpPrefix=None, ExternalDistributionType=None, ExternalStartPrefixLength=None, ExternalEndPrefixLength=None, ExternalPrimaryMetric=None, **kwargs):
        self._TopologyType = TopologyType  # Tree
        self._SimulatedRoutersCount = SimulatedRoutersCount  # Total number of simulated routers
        self._InterfaceType = InterfaceType  # Interface type
        self._RouterMaxInterfaceCount = RouterMaxInterfaceCount  # Max interfaces per router
        self._TransitNetworkMaxRouterCount = TransitNetworkMaxRouterCount  # Max routers per transit network
        self._UneditableSimulatedRoutersCount = UneditableSimulatedRoutersCount  # Simulated router per emulated router
        self._EmulatedRouterPossessSimulatedRouterCount = EmulatedRouterPossessSimulatedRouterCount  # Simulated router per emulated router
        self._RowCount = RowCount  # Number of rows
        self._ColumnCount = ColumnCount  # Number of columns
        self._GridEmulatedRouterPosition = GridEmulatedRouterPosition  # Emulated router position
        self._EmulatedRouterAttachRowIndex = EmulatedRouterAttachRowIndex  # Emulated Router Attach Row Index
        self._EmulatedRouterAttachColumnIndex = EmulatedRouterAttachColumnIndex  # Emulated Router Attach Column Index
        self._MeshRouterCount = MeshRouterCount  # Number of routers in mesh
        self._MeshEmulatedRouterPosition = MeshEmulatedRouterPosition  # Emulated router position
        self._RingRouterCount = RingRouterCount  # Number of routers in ring
        self._RingEmulatedRouterPosition = RingEmulatedRouterPosition  # Emulated router position
        self._HubSpokeRouterCount = HubSpokeRouterCount  # Number of hub and spoke routers
        self._HubSpokeEmulatedRouterPosition = HubSpokeEmulatedRouterPosition  # Emulated router position
        self._StartingPrefixRange = StartingPrefixRange  # Starting prefix/interface range
        self._EndingPrefixRange = EndingPrefixRange  # Ending prefix/interface range
        self._AreaType = AreaType  # Area type
        self._InterfacePrefixLength = InterfacePrefixLength  # Interface Prefix Length
        self._StartingRouterId = StartingRouterId  # First IPv4 Route
        self._RouterIdStep = RouterIdStep  # Router ID Step
        self._StubEmulated = StubEmulated  # Emulated routers
        self._StubSimulated = StubSimulated  # Simulated routers
        self._StubRoutesCount = StubRoutesCount  # Total number of routes create
        self._StubOverride = StubOverride  # Override
        self._StubStartingIpPrefix = StubStartingIpPrefix  # Starting IP prefix
        self._StubEndingIpPrefix = StubEndingIpPrefix  # Ending IP prefix
        self._StubDistributionType = StubDistributionType  # Prefix length distribution type
        self._StubStartPrefixLength = StubStartPrefixLength  # Start prefix length:
        self._StubEndPrefixLength = StubEndPrefixLength  # End prefix length:
        self._StubPrimaryMetric = StubPrimaryMetric  # Primary Metric
        self._SummaryEmulated = SummaryEmulated  # Emulated routers
        self._SummarySimulated = SummarySimulated  # Simulated routers
        self._SummaryRoutesCount = SummaryRoutesCount  # Total number of routes create
        self._SummaryOverride = SummaryOverride  # Override
        self._SummaryStartingIpPrefix = SummaryStartingIpPrefix  # Starting IP prefix
        self._SummaryEndingIpPrefix = SummaryEndingIpPrefix  # Ending IP prefix
        self._SummaryDistributionType = SummaryDistributionType  # Prefix length distribution type
        self._SummaryStartPrefixLength = SummaryStartPrefixLength  # Start prefix length:
        self._SummaryEndPrefixLength = SummaryEndPrefixLength  # End prefix length:
        self._SummaryPrimaryMetric = SummaryPrimaryMetric  # Primary Metric
        self._ExternalEmulated = ExternalEmulated  # Emulated routers
        self._ExternalSimulated = ExternalSimulated  # Simulated routers
        self._ExternalRoutesCount = ExternalRoutesCount  # Total number of routes create:
        self._ExternalOverride = ExternalOverride  # Override
        self._ExternalStartingIpPrefix = ExternalStartingIpPrefix  # Starting IP prefix
        self._ExternalEndingIpPrefix = ExternalEndingIpPrefix  # Ending IP prefix
        self._ExternalDistributionType = ExternalDistributionType  # Prefix length distribution type
        self._ExternalStartPrefixLength = ExternalStartPrefixLength  # Start prefix length:
        self._ExternalEndPrefixLength = ExternalEndPrefixLength  # End prefix length:
        self._ExternalPrimaryMetric = ExternalPrimaryMetric  # Primary Metric

        properties = kwargs.copy()
        if TopologyType is not None:
            properties['TopologyType'] = TopologyType
        if SimulatedRoutersCount is not None:
            properties['SimulatedRoutersCount'] = SimulatedRoutersCount
        if InterfaceType is not None:
            properties['InterfaceType'] = InterfaceType
        if RouterMaxInterfaceCount is not None:
            properties['RouterMaxInterfaceCount'] = RouterMaxInterfaceCount
        if TransitNetworkMaxRouterCount is not None:
            properties['TransitNetworkMaxRouterCount'] = TransitNetworkMaxRouterCount
        if UneditableSimulatedRoutersCount is not None:
            properties['UneditableSimulatedRoutersCount'] = UneditableSimulatedRoutersCount
        if EmulatedRouterPossessSimulatedRouterCount is not None:
            properties['EmulatedRouterPossessSimulatedRouterCount'] = EmulatedRouterPossessSimulatedRouterCount
        if RowCount is not None:
            properties['RowCount'] = RowCount
        if ColumnCount is not None:
            properties['ColumnCount'] = ColumnCount
        if GridEmulatedRouterPosition is not None:
            properties['GridEmulatedRouterPosition'] = GridEmulatedRouterPosition
        if EmulatedRouterAttachRowIndex is not None:
            properties['EmulatedRouterAttachRowIndex'] = EmulatedRouterAttachRowIndex
        if EmulatedRouterAttachColumnIndex is not None:
            properties['EmulatedRouterAttachColumnIndex'] = EmulatedRouterAttachColumnIndex
        if MeshRouterCount is not None:
            properties['MeshRouterCount'] = MeshRouterCount
        if MeshEmulatedRouterPosition is not None:
            properties['MeshEmulatedRouterPosition'] = MeshEmulatedRouterPosition
        if RingRouterCount is not None:
            properties['RingRouterCount'] = RingRouterCount
        if RingEmulatedRouterPosition is not None:
            properties['RingEmulatedRouterPosition'] = RingEmulatedRouterPosition
        if HubSpokeRouterCount is not None:
            properties['HubSpokeRouterCount'] = HubSpokeRouterCount
        if HubSpokeEmulatedRouterPosition is not None:
            properties['HubSpokeEmulatedRouterPosition'] = HubSpokeEmulatedRouterPosition
        if StartingPrefixRange is not None:
            properties['StartingPrefixRange'] = StartingPrefixRange
        if EndingPrefixRange is not None:
            properties['EndingPrefixRange'] = EndingPrefixRange
        if AreaType is not None:
            properties['AreaType'] = AreaType
        if InterfacePrefixLength is not None:
            properties['InterfacePrefixLength'] = InterfacePrefixLength
        if StartingRouterId is not None:
            properties['StartingRouterId'] = StartingRouterId
        if RouterIdStep is not None:
            properties['RouterIdStep'] = RouterIdStep
        if StubEmulated is not None:
            properties['StubEmulated'] = StubEmulated
        if StubSimulated is not None:
            properties['StubSimulated'] = StubSimulated
        if StubRoutesCount is not None:
            properties['StubRoutesCount'] = StubRoutesCount
        if StubOverride is not None:
            properties['StubOverride'] = StubOverride
        if StubStartingIpPrefix is not None:
            properties['StubStartingIpPrefix'] = StubStartingIpPrefix
        if StubEndingIpPrefix is not None:
            properties['StubEndingIpPrefix'] = StubEndingIpPrefix
        if StubDistributionType is not None:
            properties['StubDistributionType'] = StubDistributionType
        if StubStartPrefixLength is not None:
            properties['StubStartPrefixLength'] = StubStartPrefixLength
        if StubEndPrefixLength is not None:
            properties['StubEndPrefixLength'] = StubEndPrefixLength
        if StubPrimaryMetric is not None:
            properties['StubPrimaryMetric'] = StubPrimaryMetric
        if SummaryEmulated is not None:
            properties['SummaryEmulated'] = SummaryEmulated
        if SummarySimulated is not None:
            properties['SummarySimulated'] = SummarySimulated
        if SummaryRoutesCount is not None:
            properties['SummaryRoutesCount'] = SummaryRoutesCount
        if SummaryOverride is not None:
            properties['SummaryOverride'] = SummaryOverride
        if SummaryStartingIpPrefix is not None:
            properties['SummaryStartingIpPrefix'] = SummaryStartingIpPrefix
        if SummaryEndingIpPrefix is not None:
            properties['SummaryEndingIpPrefix'] = SummaryEndingIpPrefix
        if SummaryDistributionType is not None:
            properties['SummaryDistributionType'] = SummaryDistributionType
        if SummaryStartPrefixLength is not None:
            properties['SummaryStartPrefixLength'] = SummaryStartPrefixLength
        if SummaryEndPrefixLength is not None:
            properties['SummaryEndPrefixLength'] = SummaryEndPrefixLength
        if SummaryPrimaryMetric is not None:
            properties['SummaryPrimaryMetric'] = SummaryPrimaryMetric
        if ExternalEmulated is not None:
            properties['ExternalEmulated'] = ExternalEmulated
        if ExternalSimulated is not None:
            properties['ExternalSimulated'] = ExternalSimulated
        if ExternalRoutesCount is not None:
            properties['ExternalRoutesCount'] = ExternalRoutesCount
        if ExternalOverride is not None:
            properties['ExternalOverride'] = ExternalOverride
        if ExternalStartingIpPrefix is not None:
            properties['ExternalStartingIpPrefix'] = ExternalStartingIpPrefix
        if ExternalEndingIpPrefix is not None:
            properties['ExternalEndingIpPrefix'] = ExternalEndingIpPrefix
        if ExternalDistributionType is not None:
            properties['ExternalDistributionType'] = ExternalDistributionType
        if ExternalStartPrefixLength is not None:
            properties['ExternalStartPrefixLength'] = ExternalStartPrefixLength
        if ExternalEndPrefixLength is not None:
            properties['ExternalEndPrefixLength'] = ExternalEndPrefixLength
        if ExternalPrimaryMetric is not None:
            properties['ExternalPrimaryMetric'] = ExternalPrimaryMetric

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2LsaWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TopologyType=None, SimulatedRoutersCount=None, InterfaceType=None, RouterMaxInterfaceCount=None, TransitNetworkMaxRouterCount=None, UneditableSimulatedRoutersCount=None, EmulatedRouterPossessSimulatedRouterCount=None, RowCount=None, ColumnCount=None, GridEmulatedRouterPosition=None, EmulatedRouterAttachRowIndex=None, EmulatedRouterAttachColumnIndex=None, MeshRouterCount=None, MeshEmulatedRouterPosition=None, RingRouterCount=None, RingEmulatedRouterPosition=None, HubSpokeRouterCount=None, HubSpokeEmulatedRouterPosition=None, StartingPrefixRange=None, EndingPrefixRange=None, AreaType=None, InterfacePrefixLength=None, StartingRouterId=None, RouterIdStep=None, StubEmulated=None, StubSimulated=None, StubRoutesCount=None, StubOverride=None, StubStartingIpPrefix=None, StubEndingIpPrefix=None, StubDistributionType=None, StubStartPrefixLength=None, StubEndPrefixLength=None, StubPrimaryMetric=None, SummaryEmulated=None, SummarySimulated=None, SummaryRoutesCount=None, SummaryOverride=None, SummaryStartingIpPrefix=None, SummaryEndingIpPrefix=None, SummaryDistributionType=None, SummaryStartPrefixLength=None, SummaryEndPrefixLength=None, SummaryPrimaryMetric=None, ExternalEmulated=None, ExternalSimulated=None, ExternalRoutesCount=None, ExternalOverride=None, ExternalStartingIpPrefix=None, ExternalEndingIpPrefix=None, ExternalDistributionType=None, ExternalStartPrefixLength=None, ExternalEndPrefixLength=None, ExternalPrimaryMetric=None, **kwargs):
        properties = kwargs.copy()
        if TopologyType is not None:
            self._TopologyType = TopologyType
            properties['TopologyType'] = TopologyType
        if SimulatedRoutersCount is not None:
            self._SimulatedRoutersCount = SimulatedRoutersCount
            properties['SimulatedRoutersCount'] = SimulatedRoutersCount
        if InterfaceType is not None:
            self._InterfaceType = InterfaceType
            properties['InterfaceType'] = InterfaceType
        if RouterMaxInterfaceCount is not None:
            self._RouterMaxInterfaceCount = RouterMaxInterfaceCount
            properties['RouterMaxInterfaceCount'] = RouterMaxInterfaceCount
        if TransitNetworkMaxRouterCount is not None:
            self._TransitNetworkMaxRouterCount = TransitNetworkMaxRouterCount
            properties['TransitNetworkMaxRouterCount'] = TransitNetworkMaxRouterCount
        if UneditableSimulatedRoutersCount is not None:
            self._UneditableSimulatedRoutersCount = UneditableSimulatedRoutersCount
            properties['UneditableSimulatedRoutersCount'] = UneditableSimulatedRoutersCount
        if EmulatedRouterPossessSimulatedRouterCount is not None:
            self._EmulatedRouterPossessSimulatedRouterCount = EmulatedRouterPossessSimulatedRouterCount
            properties['EmulatedRouterPossessSimulatedRouterCount'] = EmulatedRouterPossessSimulatedRouterCount
        if RowCount is not None:
            self._RowCount = RowCount
            properties['RowCount'] = RowCount
        if ColumnCount is not None:
            self._ColumnCount = ColumnCount
            properties['ColumnCount'] = ColumnCount
        if GridEmulatedRouterPosition is not None:
            self._GridEmulatedRouterPosition = GridEmulatedRouterPosition
            properties['GridEmulatedRouterPosition'] = GridEmulatedRouterPosition
        if EmulatedRouterAttachRowIndex is not None:
            self._EmulatedRouterAttachRowIndex = EmulatedRouterAttachRowIndex
            properties['EmulatedRouterAttachRowIndex'] = EmulatedRouterAttachRowIndex
        if EmulatedRouterAttachColumnIndex is not None:
            self._EmulatedRouterAttachColumnIndex = EmulatedRouterAttachColumnIndex
            properties['EmulatedRouterAttachColumnIndex'] = EmulatedRouterAttachColumnIndex
        if MeshRouterCount is not None:
            self._MeshRouterCount = MeshRouterCount
            properties['MeshRouterCount'] = MeshRouterCount
        if MeshEmulatedRouterPosition is not None:
            self._MeshEmulatedRouterPosition = MeshEmulatedRouterPosition
            properties['MeshEmulatedRouterPosition'] = MeshEmulatedRouterPosition
        if RingRouterCount is not None:
            self._RingRouterCount = RingRouterCount
            properties['RingRouterCount'] = RingRouterCount
        if RingEmulatedRouterPosition is not None:
            self._RingEmulatedRouterPosition = RingEmulatedRouterPosition
            properties['RingEmulatedRouterPosition'] = RingEmulatedRouterPosition
        if HubSpokeRouterCount is not None:
            self._HubSpokeRouterCount = HubSpokeRouterCount
            properties['HubSpokeRouterCount'] = HubSpokeRouterCount
        if HubSpokeEmulatedRouterPosition is not None:
            self._HubSpokeEmulatedRouterPosition = HubSpokeEmulatedRouterPosition
            properties['HubSpokeEmulatedRouterPosition'] = HubSpokeEmulatedRouterPosition
        if StartingPrefixRange is not None:
            self._StartingPrefixRange = StartingPrefixRange
            properties['StartingPrefixRange'] = StartingPrefixRange
        if EndingPrefixRange is not None:
            self._EndingPrefixRange = EndingPrefixRange
            properties['EndingPrefixRange'] = EndingPrefixRange
        if AreaType is not None:
            self._AreaType = AreaType
            properties['AreaType'] = AreaType
        if InterfacePrefixLength is not None:
            self._InterfacePrefixLength = InterfacePrefixLength
            properties['InterfacePrefixLength'] = InterfacePrefixLength
        if StartingRouterId is not None:
            self._StartingRouterId = StartingRouterId
            properties['StartingRouterId'] = StartingRouterId
        if RouterIdStep is not None:
            self._RouterIdStep = RouterIdStep
            properties['RouterIdStep'] = RouterIdStep
        if StubEmulated is not None:
            self._StubEmulated = StubEmulated
            properties['StubEmulated'] = StubEmulated
        if StubSimulated is not None:
            self._StubSimulated = StubSimulated
            properties['StubSimulated'] = StubSimulated
        if StubRoutesCount is not None:
            self._StubRoutesCount = StubRoutesCount
            properties['StubRoutesCount'] = StubRoutesCount
        if StubOverride is not None:
            self._StubOverride = StubOverride
            properties['StubOverride'] = StubOverride
        if StubStartingIpPrefix is not None:
            self._StubStartingIpPrefix = StubStartingIpPrefix
            properties['StubStartingIpPrefix'] = StubStartingIpPrefix
        if StubEndingIpPrefix is not None:
            self._StubEndingIpPrefix = StubEndingIpPrefix
            properties['StubEndingIpPrefix'] = StubEndingIpPrefix
        if StubDistributionType is not None:
            self._StubDistributionType = StubDistributionType
            properties['StubDistributionType'] = StubDistributionType
        if StubStartPrefixLength is not None:
            self._StubStartPrefixLength = StubStartPrefixLength
            properties['StubStartPrefixLength'] = StubStartPrefixLength
        if StubEndPrefixLength is not None:
            self._StubEndPrefixLength = StubEndPrefixLength
            properties['StubEndPrefixLength'] = StubEndPrefixLength
        if StubPrimaryMetric is not None:
            self._StubPrimaryMetric = StubPrimaryMetric
            properties['StubPrimaryMetric'] = StubPrimaryMetric
        if SummaryEmulated is not None:
            self._SummaryEmulated = SummaryEmulated
            properties['SummaryEmulated'] = SummaryEmulated
        if SummarySimulated is not None:
            self._SummarySimulated = SummarySimulated
            properties['SummarySimulated'] = SummarySimulated
        if SummaryRoutesCount is not None:
            self._SummaryRoutesCount = SummaryRoutesCount
            properties['SummaryRoutesCount'] = SummaryRoutesCount
        if SummaryOverride is not None:
            self._SummaryOverride = SummaryOverride
            properties['SummaryOverride'] = SummaryOverride
        if SummaryStartingIpPrefix is not None:
            self._SummaryStartingIpPrefix = SummaryStartingIpPrefix
            properties['SummaryStartingIpPrefix'] = SummaryStartingIpPrefix
        if SummaryEndingIpPrefix is not None:
            self._SummaryEndingIpPrefix = SummaryEndingIpPrefix
            properties['SummaryEndingIpPrefix'] = SummaryEndingIpPrefix
        if SummaryDistributionType is not None:
            self._SummaryDistributionType = SummaryDistributionType
            properties['SummaryDistributionType'] = SummaryDistributionType
        if SummaryStartPrefixLength is not None:
            self._SummaryStartPrefixLength = SummaryStartPrefixLength
            properties['SummaryStartPrefixLength'] = SummaryStartPrefixLength
        if SummaryEndPrefixLength is not None:
            self._SummaryEndPrefixLength = SummaryEndPrefixLength
            properties['SummaryEndPrefixLength'] = SummaryEndPrefixLength
        if SummaryPrimaryMetric is not None:
            self._SummaryPrimaryMetric = SummaryPrimaryMetric
            properties['SummaryPrimaryMetric'] = SummaryPrimaryMetric
        if ExternalEmulated is not None:
            self._ExternalEmulated = ExternalEmulated
            properties['ExternalEmulated'] = ExternalEmulated
        if ExternalSimulated is not None:
            self._ExternalSimulated = ExternalSimulated
            properties['ExternalSimulated'] = ExternalSimulated
        if ExternalRoutesCount is not None:
            self._ExternalRoutesCount = ExternalRoutesCount
            properties['ExternalRoutesCount'] = ExternalRoutesCount
        if ExternalOverride is not None:
            self._ExternalOverride = ExternalOverride
            properties['ExternalOverride'] = ExternalOverride
        if ExternalStartingIpPrefix is not None:
            self._ExternalStartingIpPrefix = ExternalStartingIpPrefix
            properties['ExternalStartingIpPrefix'] = ExternalStartingIpPrefix
        if ExternalEndingIpPrefix is not None:
            self._ExternalEndingIpPrefix = ExternalEndingIpPrefix
            properties['ExternalEndingIpPrefix'] = ExternalEndingIpPrefix
        if ExternalDistributionType is not None:
            self._ExternalDistributionType = ExternalDistributionType
            properties['ExternalDistributionType'] = ExternalDistributionType
        if ExternalStartPrefixLength is not None:
            self._ExternalStartPrefixLength = ExternalStartPrefixLength
            properties['ExternalStartPrefixLength'] = ExternalStartPrefixLength
        if ExternalEndPrefixLength is not None:
            self._ExternalEndPrefixLength = ExternalEndPrefixLength
            properties['ExternalEndPrefixLength'] = ExternalEndPrefixLength
        if ExternalPrimaryMetric is not None:
            self._ExternalPrimaryMetric = ExternalPrimaryMetric
            properties['ExternalPrimaryMetric'] = ExternalPrimaryMetric

        super(Ospfv2LsaWizardConfig, self).edit(**properties)

    @property
    def TopologyType(self):
        """
        get the value of property _TopologyType
        """
        if self.force_auto_sync:
            self.get('TopologyType')
        return self._TopologyType

    @property
    def SimulatedRoutersCount(self):
        """
        get the value of property _SimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('SimulatedRoutersCount')
        return self._SimulatedRoutersCount

    @property
    def InterfaceType(self):
        """
        get the value of property _InterfaceType
        """
        if self.force_auto_sync:
            self.get('InterfaceType')
        return self._InterfaceType

    @property
    def RouterMaxInterfaceCount(self):
        """
        get the value of property _RouterMaxInterfaceCount
        """
        if self.force_auto_sync:
            self.get('RouterMaxInterfaceCount')
        return self._RouterMaxInterfaceCount

    @property
    def TransitNetworkMaxRouterCount(self):
        """
        get the value of property _TransitNetworkMaxRouterCount
        """
        if self.force_auto_sync:
            self.get('TransitNetworkMaxRouterCount')
        return self._TransitNetworkMaxRouterCount

    @property
    def UneditableSimulatedRoutersCount(self):
        """
        get the value of property _UneditableSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('UneditableSimulatedRoutersCount')
        return self._UneditableSimulatedRoutersCount

    @property
    def EmulatedRouterPossessSimulatedRouterCount(self):
        """
        get the value of property _EmulatedRouterPossessSimulatedRouterCount
        """
        if self.force_auto_sync:
            self.get('EmulatedRouterPossessSimulatedRouterCount')
        return self._EmulatedRouterPossessSimulatedRouterCount

    @property
    def RowCount(self):
        """
        get the value of property _RowCount
        """
        if self.force_auto_sync:
            self.get('RowCount')
        return self._RowCount

    @property
    def ColumnCount(self):
        """
        get the value of property _ColumnCount
        """
        if self.force_auto_sync:
            self.get('ColumnCount')
        return self._ColumnCount

    @property
    def GridEmulatedRouterPosition(self):
        """
        get the value of property _GridEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('GridEmulatedRouterPosition')
        return self._GridEmulatedRouterPosition

    @property
    def EmulatedRouterAttachRowIndex(self):
        """
        get the value of property _EmulatedRouterAttachRowIndex
        """
        if self.force_auto_sync:
            self.get('EmulatedRouterAttachRowIndex')
        return self._EmulatedRouterAttachRowIndex

    @property
    def EmulatedRouterAttachColumnIndex(self):
        """
        get the value of property _EmulatedRouterAttachColumnIndex
        """
        if self.force_auto_sync:
            self.get('EmulatedRouterAttachColumnIndex')
        return self._EmulatedRouterAttachColumnIndex

    @property
    def MeshRouterCount(self):
        """
        get the value of property _MeshRouterCount
        """
        if self.force_auto_sync:
            self.get('MeshRouterCount')
        return self._MeshRouterCount

    @property
    def MeshEmulatedRouterPosition(self):
        """
        get the value of property _MeshEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('MeshEmulatedRouterPosition')
        return self._MeshEmulatedRouterPosition

    @property
    def RingRouterCount(self):
        """
        get the value of property _RingRouterCount
        """
        if self.force_auto_sync:
            self.get('RingRouterCount')
        return self._RingRouterCount

    @property
    def RingEmulatedRouterPosition(self):
        """
        get the value of property _RingEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('RingEmulatedRouterPosition')
        return self._RingEmulatedRouterPosition

    @property
    def HubSpokeRouterCount(self):
        """
        get the value of property _HubSpokeRouterCount
        """
        if self.force_auto_sync:
            self.get('HubSpokeRouterCount')
        return self._HubSpokeRouterCount

    @property
    def HubSpokeEmulatedRouterPosition(self):
        """
        get the value of property _HubSpokeEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('HubSpokeEmulatedRouterPosition')
        return self._HubSpokeEmulatedRouterPosition

    @property
    def StartingPrefixRange(self):
        """
        get the value of property _StartingPrefixRange
        """
        if self.force_auto_sync:
            self.get('StartingPrefixRange')
        return self._StartingPrefixRange

    @property
    def EndingPrefixRange(self):
        """
        get the value of property _EndingPrefixRange
        """
        if self.force_auto_sync:
            self.get('EndingPrefixRange')
        return self._EndingPrefixRange

    @property
    def AreaType(self):
        """
        get the value of property _AreaType
        """
        if self.force_auto_sync:
            self.get('AreaType')
        return self._AreaType

    @property
    def InterfacePrefixLength(self):
        """
        get the value of property _InterfacePrefixLength
        """
        if self.force_auto_sync:
            self.get('InterfacePrefixLength')
        return self._InterfacePrefixLength

    @property
    def StartingRouterId(self):
        """
        get the value of property _StartingRouterId
        """
        if self.force_auto_sync:
            self.get('StartingRouterId')
        return self._StartingRouterId

    @property
    def RouterIdStep(self):
        """
        get the value of property _RouterIdStep
        """
        if self.force_auto_sync:
            self.get('RouterIdStep')
        return self._RouterIdStep

    @property
    def StubEmulated(self):
        """
        get the value of property _StubEmulated
        """
        if self.force_auto_sync:
            self.get('StubEmulated')
        return self._StubEmulated

    @property
    def StubSimulated(self):
        """
        get the value of property _StubSimulated
        """
        if self.force_auto_sync:
            self.get('StubSimulated')
        return self._StubSimulated

    @property
    def StubRoutesCount(self):
        """
        get the value of property _StubRoutesCount
        """
        if self.force_auto_sync:
            self.get('StubRoutesCount')
        return self._StubRoutesCount

    @property
    def StubOverride(self):
        """
        get the value of property _StubOverride
        """
        if self.force_auto_sync:
            self.get('StubOverride')
        return self._StubOverride

    @property
    def StubStartingIpPrefix(self):
        """
        get the value of property _StubStartingIpPrefix
        """
        if self.force_auto_sync:
            self.get('StubStartingIpPrefix')
        return self._StubStartingIpPrefix

    @property
    def StubEndingIpPrefix(self):
        """
        get the value of property _StubEndingIpPrefix
        """
        if self.force_auto_sync:
            self.get('StubEndingIpPrefix')
        return self._StubEndingIpPrefix

    @property
    def StubDistributionType(self):
        """
        get the value of property _StubDistributionType
        """
        if self.force_auto_sync:
            self.get('StubDistributionType')
        return self._StubDistributionType

    @property
    def StubStartPrefixLength(self):
        """
        get the value of property _StubStartPrefixLength
        """
        if self.force_auto_sync:
            self.get('StubStartPrefixLength')
        return self._StubStartPrefixLength

    @property
    def StubEndPrefixLength(self):
        """
        get the value of property _StubEndPrefixLength
        """
        if self.force_auto_sync:
            self.get('StubEndPrefixLength')
        return self._StubEndPrefixLength

    @property
    def StubPrimaryMetric(self):
        """
        get the value of property _StubPrimaryMetric
        """
        if self.force_auto_sync:
            self.get('StubPrimaryMetric')
        return self._StubPrimaryMetric

    @property
    def SummaryEmulated(self):
        """
        get the value of property _SummaryEmulated
        """
        if self.force_auto_sync:
            self.get('SummaryEmulated')
        return self._SummaryEmulated

    @property
    def SummarySimulated(self):
        """
        get the value of property _SummarySimulated
        """
        if self.force_auto_sync:
            self.get('SummarySimulated')
        return self._SummarySimulated

    @property
    def SummaryRoutesCount(self):
        """
        get the value of property _SummaryRoutesCount
        """
        if self.force_auto_sync:
            self.get('SummaryRoutesCount')
        return self._SummaryRoutesCount

    @property
    def SummaryOverride(self):
        """
        get the value of property _SummaryOverride
        """
        if self.force_auto_sync:
            self.get('SummaryOverride')
        return self._SummaryOverride

    @property
    def SummaryStartingIpPrefix(self):
        """
        get the value of property _SummaryStartingIpPrefix
        """
        if self.force_auto_sync:
            self.get('SummaryStartingIpPrefix')
        return self._SummaryStartingIpPrefix

    @property
    def SummaryEndingIpPrefix(self):
        """
        get the value of property _SummaryEndingIpPrefix
        """
        if self.force_auto_sync:
            self.get('SummaryEndingIpPrefix')
        return self._SummaryEndingIpPrefix

    @property
    def SummaryDistributionType(self):
        """
        get the value of property _SummaryDistributionType
        """
        if self.force_auto_sync:
            self.get('SummaryDistributionType')
        return self._SummaryDistributionType

    @property
    def SummaryStartPrefixLength(self):
        """
        get the value of property _SummaryStartPrefixLength
        """
        if self.force_auto_sync:
            self.get('SummaryStartPrefixLength')
        return self._SummaryStartPrefixLength

    @property
    def SummaryEndPrefixLength(self):
        """
        get the value of property _SummaryEndPrefixLength
        """
        if self.force_auto_sync:
            self.get('SummaryEndPrefixLength')
        return self._SummaryEndPrefixLength

    @property
    def SummaryPrimaryMetric(self):
        """
        get the value of property _SummaryPrimaryMetric
        """
        if self.force_auto_sync:
            self.get('SummaryPrimaryMetric')
        return self._SummaryPrimaryMetric

    @property
    def ExternalEmulated(self):
        """
        get the value of property _ExternalEmulated
        """
        if self.force_auto_sync:
            self.get('ExternalEmulated')
        return self._ExternalEmulated

    @property
    def ExternalSimulated(self):
        """
        get the value of property _ExternalSimulated
        """
        if self.force_auto_sync:
            self.get('ExternalSimulated')
        return self._ExternalSimulated

    @property
    def ExternalRoutesCount(self):
        """
        get the value of property _ExternalRoutesCount
        """
        if self.force_auto_sync:
            self.get('ExternalRoutesCount')
        return self._ExternalRoutesCount

    @property
    def ExternalOverride(self):
        """
        get the value of property _ExternalOverride
        """
        if self.force_auto_sync:
            self.get('ExternalOverride')
        return self._ExternalOverride

    @property
    def ExternalStartingIpPrefix(self):
        """
        get the value of property _ExternalStartingIpPrefix
        """
        if self.force_auto_sync:
            self.get('ExternalStartingIpPrefix')
        return self._ExternalStartingIpPrefix

    @property
    def ExternalEndingIpPrefix(self):
        """
        get the value of property _ExternalEndingIpPrefix
        """
        if self.force_auto_sync:
            self.get('ExternalEndingIpPrefix')
        return self._ExternalEndingIpPrefix

    @property
    def ExternalDistributionType(self):
        """
        get the value of property _ExternalDistributionType
        """
        if self.force_auto_sync:
            self.get('ExternalDistributionType')
        return self._ExternalDistributionType

    @property
    def ExternalStartPrefixLength(self):
        """
        get the value of property _ExternalStartPrefixLength
        """
        if self.force_auto_sync:
            self.get('ExternalStartPrefixLength')
        return self._ExternalStartPrefixLength

    @property
    def ExternalEndPrefixLength(self):
        """
        get the value of property _ExternalEndPrefixLength
        """
        if self.force_auto_sync:
            self.get('ExternalEndPrefixLength')
        return self._ExternalEndPrefixLength

    @property
    def ExternalPrimaryMetric(self):
        """
        get the value of property _ExternalPrimaryMetric
        """
        if self.force_auto_sync:
            self.get('ExternalPrimaryMetric')
        return self._ExternalPrimaryMetric

    @TopologyType.setter
    def TopologyType(self, value):
        self._TopologyType = value
        self.edit(TopologyType=value)

    @SimulatedRoutersCount.setter
    def SimulatedRoutersCount(self, value):
        self._SimulatedRoutersCount = value
        self.edit(SimulatedRoutersCount=value)

    @InterfaceType.setter
    def InterfaceType(self, value):
        self._InterfaceType = value
        self.edit(InterfaceType=value)

    @RouterMaxInterfaceCount.setter
    def RouterMaxInterfaceCount(self, value):
        self._RouterMaxInterfaceCount = value
        self.edit(RouterMaxInterfaceCount=value)

    @TransitNetworkMaxRouterCount.setter
    def TransitNetworkMaxRouterCount(self, value):
        self._TransitNetworkMaxRouterCount = value
        self.edit(TransitNetworkMaxRouterCount=value)

    @UneditableSimulatedRoutersCount.setter
    def UneditableSimulatedRoutersCount(self, value):
        self._UneditableSimulatedRoutersCount = value
        self.edit(UneditableSimulatedRoutersCount=value)

    @EmulatedRouterPossessSimulatedRouterCount.setter
    def EmulatedRouterPossessSimulatedRouterCount(self, value):
        self._EmulatedRouterPossessSimulatedRouterCount = value
        self.edit(EmulatedRouterPossessSimulatedRouterCount=value)

    @RowCount.setter
    def RowCount(self, value):
        self._RowCount = value
        self.edit(RowCount=value)

    @ColumnCount.setter
    def ColumnCount(self, value):
        self._ColumnCount = value
        self.edit(ColumnCount=value)

    @GridEmulatedRouterPosition.setter
    def GridEmulatedRouterPosition(self, value):
        self._GridEmulatedRouterPosition = value
        self.edit(GridEmulatedRouterPosition=value)

    @EmulatedRouterAttachRowIndex.setter
    def EmulatedRouterAttachRowIndex(self, value):
        self._EmulatedRouterAttachRowIndex = value
        self.edit(EmulatedRouterAttachRowIndex=value)

    @EmulatedRouterAttachColumnIndex.setter
    def EmulatedRouterAttachColumnIndex(self, value):
        self._EmulatedRouterAttachColumnIndex = value
        self.edit(EmulatedRouterAttachColumnIndex=value)

    @MeshRouterCount.setter
    def MeshRouterCount(self, value):
        self._MeshRouterCount = value
        self.edit(MeshRouterCount=value)

    @MeshEmulatedRouterPosition.setter
    def MeshEmulatedRouterPosition(self, value):
        self._MeshEmulatedRouterPosition = value
        self.edit(MeshEmulatedRouterPosition=value)

    @RingRouterCount.setter
    def RingRouterCount(self, value):
        self._RingRouterCount = value
        self.edit(RingRouterCount=value)

    @RingEmulatedRouterPosition.setter
    def RingEmulatedRouterPosition(self, value):
        self._RingEmulatedRouterPosition = value
        self.edit(RingEmulatedRouterPosition=value)

    @HubSpokeRouterCount.setter
    def HubSpokeRouterCount(self, value):
        self._HubSpokeRouterCount = value
        self.edit(HubSpokeRouterCount=value)

    @HubSpokeEmulatedRouterPosition.setter
    def HubSpokeEmulatedRouterPosition(self, value):
        self._HubSpokeEmulatedRouterPosition = value
        self.edit(HubSpokeEmulatedRouterPosition=value)

    @StartingPrefixRange.setter
    def StartingPrefixRange(self, value):
        self._StartingPrefixRange = value
        self.edit(StartingPrefixRange=value)

    @EndingPrefixRange.setter
    def EndingPrefixRange(self, value):
        self._EndingPrefixRange = value
        self.edit(EndingPrefixRange=value)

    @AreaType.setter
    def AreaType(self, value):
        self._AreaType = value
        self.edit(AreaType=value)

    @InterfacePrefixLength.setter
    def InterfacePrefixLength(self, value):
        self._InterfacePrefixLength = value
        self.edit(InterfacePrefixLength=value)

    @StartingRouterId.setter
    def StartingRouterId(self, value):
        self._StartingRouterId = value
        self.edit(StartingRouterId=value)

    @RouterIdStep.setter
    def RouterIdStep(self, value):
        self._RouterIdStep = value
        self.edit(RouterIdStep=value)

    @StubEmulated.setter
    def StubEmulated(self, value):
        self._StubEmulated = value
        self.edit(StubEmulated=value)

    @StubSimulated.setter
    def StubSimulated(self, value):
        self._StubSimulated = value
        self.edit(StubSimulated=value)

    @StubRoutesCount.setter
    def StubRoutesCount(self, value):
        self._StubRoutesCount = value
        self.edit(StubRoutesCount=value)

    @StubOverride.setter
    def StubOverride(self, value):
        self._StubOverride = value
        self.edit(StubOverride=value)

    @StubStartingIpPrefix.setter
    def StubStartingIpPrefix(self, value):
        self._StubStartingIpPrefix = value
        self.edit(StubStartingIpPrefix=value)

    @StubEndingIpPrefix.setter
    def StubEndingIpPrefix(self, value):
        self._StubEndingIpPrefix = value
        self.edit(StubEndingIpPrefix=value)

    @StubDistributionType.setter
    def StubDistributionType(self, value):
        self._StubDistributionType = value
        self.edit(StubDistributionType=value)

    @StubStartPrefixLength.setter
    def StubStartPrefixLength(self, value):
        self._StubStartPrefixLength = value
        self.edit(StubStartPrefixLength=value)

    @StubEndPrefixLength.setter
    def StubEndPrefixLength(self, value):
        self._StubEndPrefixLength = value
        self.edit(StubEndPrefixLength=value)

    @StubPrimaryMetric.setter
    def StubPrimaryMetric(self, value):
        self._StubPrimaryMetric = value
        self.edit(StubPrimaryMetric=value)

    @SummaryEmulated.setter
    def SummaryEmulated(self, value):
        self._SummaryEmulated = value
        self.edit(SummaryEmulated=value)

    @SummarySimulated.setter
    def SummarySimulated(self, value):
        self._SummarySimulated = value
        self.edit(SummarySimulated=value)

    @SummaryRoutesCount.setter
    def SummaryRoutesCount(self, value):
        self._SummaryRoutesCount = value
        self.edit(SummaryRoutesCount=value)

    @SummaryOverride.setter
    def SummaryOverride(self, value):
        self._SummaryOverride = value
        self.edit(SummaryOverride=value)

    @SummaryStartingIpPrefix.setter
    def SummaryStartingIpPrefix(self, value):
        self._SummaryStartingIpPrefix = value
        self.edit(SummaryStartingIpPrefix=value)

    @SummaryEndingIpPrefix.setter
    def SummaryEndingIpPrefix(self, value):
        self._SummaryEndingIpPrefix = value
        self.edit(SummaryEndingIpPrefix=value)

    @SummaryDistributionType.setter
    def SummaryDistributionType(self, value):
        self._SummaryDistributionType = value
        self.edit(SummaryDistributionType=value)

    @SummaryStartPrefixLength.setter
    def SummaryStartPrefixLength(self, value):
        self._SummaryStartPrefixLength = value
        self.edit(SummaryStartPrefixLength=value)

    @SummaryEndPrefixLength.setter
    def SummaryEndPrefixLength(self, value):
        self._SummaryEndPrefixLength = value
        self.edit(SummaryEndPrefixLength=value)

    @SummaryPrimaryMetric.setter
    def SummaryPrimaryMetric(self, value):
        self._SummaryPrimaryMetric = value
        self.edit(SummaryPrimaryMetric=value)

    @ExternalEmulated.setter
    def ExternalEmulated(self, value):
        self._ExternalEmulated = value
        self.edit(ExternalEmulated=value)

    @ExternalSimulated.setter
    def ExternalSimulated(self, value):
        self._ExternalSimulated = value
        self.edit(ExternalSimulated=value)

    @ExternalRoutesCount.setter
    def ExternalRoutesCount(self, value):
        self._ExternalRoutesCount = value
        self.edit(ExternalRoutesCount=value)

    @ExternalOverride.setter
    def ExternalOverride(self, value):
        self._ExternalOverride = value
        self.edit(ExternalOverride=value)

    @ExternalStartingIpPrefix.setter
    def ExternalStartingIpPrefix(self, value):
        self._ExternalStartingIpPrefix = value
        self.edit(ExternalStartingIpPrefix=value)

    @ExternalEndingIpPrefix.setter
    def ExternalEndingIpPrefix(self, value):
        self._ExternalEndingIpPrefix = value
        self.edit(ExternalEndingIpPrefix=value)

    @ExternalDistributionType.setter
    def ExternalDistributionType(self, value):
        self._ExternalDistributionType = value
        self.edit(ExternalDistributionType=value)

    @ExternalStartPrefixLength.setter
    def ExternalStartPrefixLength(self, value):
        self._ExternalStartPrefixLength = value
        self.edit(ExternalStartPrefixLength=value)

    @ExternalEndPrefixLength.setter
    def ExternalEndPrefixLength(self, value):
        self._ExternalEndPrefixLength = value
        self.edit(ExternalEndPrefixLength=value)

    @ExternalPrimaryMetric.setter
    def ExternalPrimaryMetric(self, value):
        self._ExternalPrimaryMetric = value
        self.edit(ExternalPrimaryMetric=value)

    def _set_topologytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TopologyType = EnumOspfv2WizardTopologyType.%s' % value[:seperate])

    def _set_simulatedrouterscount_with_str(self, value):
        try:
            self._SimulatedRoutersCount = int(value)
        except ValueError:
            self._SimulatedRoutersCount = hex(int(value, 16))

    def _set_interfacetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._InterfaceType = EnumOspfNetworkType.%s' % value[:seperate])

    def _set_routermaxinterfacecount_with_str(self, value):
        try:
            self._RouterMaxInterfaceCount = int(value)
        except ValueError:
            self._RouterMaxInterfaceCount = hex(int(value, 16))

    def _set_transitnetworkmaxroutercount_with_str(self, value):
        try:
            self._TransitNetworkMaxRouterCount = int(value)
        except ValueError:
            self._TransitNetworkMaxRouterCount = hex(int(value, 16))

    def _set_uneditablesimulatedrouterscount_with_str(self, value):
        try:
            self._UneditableSimulatedRoutersCount = int(value)
        except ValueError:
            self._UneditableSimulatedRoutersCount = hex(int(value, 16))

    def _set_emulatedrouterpossesssimulatedroutercount_with_str(self, value):
        try:
            self._EmulatedRouterPossessSimulatedRouterCount = int(value)
        except ValueError:
            self._EmulatedRouterPossessSimulatedRouterCount = hex(int(value, 16))

    def _set_rowcount_with_str(self, value):
        try:
            self._RowCount = int(value)
        except ValueError:
            self._RowCount = hex(int(value, 16))

    def _set_columncount_with_str(self, value):
        try:
            self._ColumnCount = int(value)
        except ValueError:
            self._ColumnCount = hex(int(value, 16))

    def _set_gridemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._GridEmulatedRouterPosition = EnumOspfv2WizardGridRouterPositionType.%s' % value[:seperate])

    def _set_emulatedrouterattachrowindex_with_str(self, value):
        try:
            self._EmulatedRouterAttachRowIndex = int(value)
        except ValueError:
            self._EmulatedRouterAttachRowIndex = hex(int(value, 16))

    def _set_emulatedrouterattachcolumnindex_with_str(self, value):
        try:
            self._EmulatedRouterAttachColumnIndex = int(value)
        except ValueError:
            self._EmulatedRouterAttachColumnIndex = hex(int(value, 16))

    def _set_meshroutercount_with_str(self, value):
        try:
            self._MeshRouterCount = int(value)
        except ValueError:
            self._MeshRouterCount = hex(int(value, 16))

    def _set_meshemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._MeshEmulatedRouterPosition = EnumOspfv2WizardFullMeshRouterPositionType.%s' % value[:seperate])

    def _set_ringroutercount_with_str(self, value):
        try:
            self._RingRouterCount = int(value)
        except ValueError:
            self._RingRouterCount = hex(int(value, 16))

    def _set_ringemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._RingEmulatedRouterPosition = EnumOspfv2WizardRingRouterPositionType.%s' % value[:seperate])

    def _set_hubspokeroutercount_with_str(self, value):
        try:
            self._HubSpokeRouterCount = int(value)
        except ValueError:
            self._HubSpokeRouterCount = hex(int(value, 16))

    def _set_hubspokeemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._HubSpokeEmulatedRouterPosition = EnumOspfv2WizardHubSpokeRouterPositionType.%s' % value[:seperate])

    def _set_startingprefixrange_with_str(self, value):
        self._StartingPrefixRange = value

    def _set_endingprefixrange_with_str(self, value):
        self._EndingPrefixRange = value

    def _set_areatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AreaType = EnumOspfv2WizardAreaType.%s' % value[:seperate])

    def _set_interfaceprefixlength_with_str(self, value):
        try:
            self._InterfacePrefixLength = int(value)
        except ValueError:
            self._InterfacePrefixLength = hex(int(value, 16))

    def _set_startingrouterid_with_str(self, value):
        self._StartingRouterId = value

    def _set_routeridstep_with_str(self, value):
        self._RouterIdStep = value

    def _set_stubemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._StubEmulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_stubsimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._StubSimulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_stubroutescount_with_str(self, value):
        try:
            self._StubRoutesCount = int(value)
        except ValueError:
            self._StubRoutesCount = hex(int(value, 16))

    def _set_stuboverride_with_str(self, value):
        self._StubOverride = (value == 'True')

    def _set_stubstartingipprefix_with_str(self, value):
        self._StubStartingIpPrefix = value

    def _set_stubendingipprefix_with_str(self, value):
        self._StubEndingIpPrefix = value

    def _set_stubdistributiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._StubDistributionType = EnumOspfv2WizardDistributionType.%s' % value[:seperate])

    def _set_stubstartprefixlength_with_str(self, value):
        try:
            self._StubStartPrefixLength = int(value)
        except ValueError:
            self._StubStartPrefixLength = hex(int(value, 16))

    def _set_stubendprefixlength_with_str(self, value):
        try:
            self._StubEndPrefixLength = int(value)
        except ValueError:
            self._StubEndPrefixLength = hex(int(value, 16))

    def _set_stubprimarymetric_with_str(self, value):
        try:
            self._StubPrimaryMetric = int(value)
        except ValueError:
            self._StubPrimaryMetric = hex(int(value, 16))

    def _set_summaryemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._SummaryEmulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_summarysimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._SummarySimulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_summaryroutescount_with_str(self, value):
        try:
            self._SummaryRoutesCount = int(value)
        except ValueError:
            self._SummaryRoutesCount = hex(int(value, 16))

    def _set_summaryoverride_with_str(self, value):
        self._SummaryOverride = (value == 'True')

    def _set_summarystartingipprefix_with_str(self, value):
        self._SummaryStartingIpPrefix = value

    def _set_summaryendingipprefix_with_str(self, value):
        self._SummaryEndingIpPrefix = value

    def _set_summarydistributiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._SummaryDistributionType = EnumOspfv2WizardDistributionType.%s' % value[:seperate])

    def _set_summarystartprefixlength_with_str(self, value):
        try:
            self._SummaryStartPrefixLength = int(value)
        except ValueError:
            self._SummaryStartPrefixLength = hex(int(value, 16))

    def _set_summaryendprefixlength_with_str(self, value):
        try:
            self._SummaryEndPrefixLength = int(value)
        except ValueError:
            self._SummaryEndPrefixLength = hex(int(value, 16))

    def _set_summaryprimarymetric_with_str(self, value):
        try:
            self._SummaryPrimaryMetric = int(value)
        except ValueError:
            self._SummaryPrimaryMetric = hex(int(value, 16))

    def _set_externalemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExternalEmulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_externalsimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExternalSimulated = EnumOspfv2WizardRadioType.%s' % value[:seperate])

    def _set_externalroutescount_with_str(self, value):
        try:
            self._ExternalRoutesCount = int(value)
        except ValueError:
            self._ExternalRoutesCount = hex(int(value, 16))

    def _set_externaloverride_with_str(self, value):
        self._ExternalOverride = (value == 'True')

    def _set_externalstartingipprefix_with_str(self, value):
        self._ExternalStartingIpPrefix = value

    def _set_externalendingipprefix_with_str(self, value):
        self._ExternalEndingIpPrefix = value

    def _set_externaldistributiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExternalDistributionType = EnumOspfv2WizardDistributionType.%s' % value[:seperate])

    def _set_externalstartprefixlength_with_str(self, value):
        try:
            self._ExternalStartPrefixLength = int(value)
        except ValueError:
            self._ExternalStartPrefixLength = hex(int(value, 16))

    def _set_externalendprefixlength_with_str(self, value):
        try:
            self._ExternalEndPrefixLength = int(value)
        except ValueError:
            self._ExternalEndPrefixLength = hex(int(value, 16))

    def _set_externalprimarymetric_with_str(self, value):
        try:
            self._ExternalPrimaryMetric = int(value)
        except ValueError:
            self._ExternalPrimaryMetric = hex(int(value, 16))

