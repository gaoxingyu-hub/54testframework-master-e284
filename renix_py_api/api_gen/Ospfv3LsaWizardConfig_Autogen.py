"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class Ospfv3LsaWizardConfig(WizardConfigBase):
    def __init__(self, TopologyType=None, SimulatedRoutersCount=None, InterfaceType=None, RouterMaxInterfaceCount=None, TransitNetworkMaxRouterCount=None, UneditableSimulatedRoutersCount=None, EmulatedRouterPossessSimulatedRouterCount=None, RowCount=None, ColumnCount=None, GridEmulatedRouterPosition=None, EmulatedRouterAttachRowIndex=None, EmulatedRouterAttachColumnIndex=None, MeshRouterCount=None, MeshEmulatedRouterPosition=None, RingRouterCount=None, RingEmulatedRouterPosition=None, HubSpokeRouterCount=None, HubSpokeEmulatedRouterPosition=None, StartingPrefixRange=None, EndingPrefixRange=None, AreaType=None, StartingRouterId=None, RouterIdStep=None, IntraAreaEmulated=None, IntraAreaSimulated=None, IntraAreaRoutesCount=None, IntraAreaOverride=None, IntraAreaStartingIpPrefix=None, IntraAreaEndingIpPrefix=None, IntraAreaDistributionType=None, IntraAreaStartPrefixLength=None, IntraAreaEndPrefixLength=None, IntraAreaPrimaryMetric=None, InterAreaEmulated=None, InterAreaSimulated=None, InterAreaRoutesCount=None, InterAreaOverride=None, InterAreaStartingIpPrefix=None, InterAreaEndingIpPrefix=None, InterAreaDistributionType=None, InterAreaStartPrefixLength=None, InterAreaEndPrefixLength=None, InterAreaPrimaryMetric=None, ExternalEmulated=None, ExternalSimulated=None, ExternalRoutesCount=None, ExternalOverride=None, ExternalStartingIpPrefix=None, ExternalEndingIpPrefix=None, ExternalDistributionType=None, ExternalStartPrefixLength=None, ExternalEndPrefixLength=None, ExternalPrimaryMetric=None, **kwargs):
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
        self._StartingRouterId = StartingRouterId  # Staring Route ID
        self._RouterIdStep = RouterIdStep  # Router ID Step
        self._IntraAreaEmulated = IntraAreaEmulated  # Emulated routers
        self._IntraAreaSimulated = IntraAreaSimulated  # Simulated routers
        self._IntraAreaRoutesCount = IntraAreaRoutesCount  # Total number of routes create
        self._IntraAreaOverride = IntraAreaOverride  # Override
        self._IntraAreaStartingIpPrefix = IntraAreaStartingIpPrefix  # Starting IP prefix
        self._IntraAreaEndingIpPrefix = IntraAreaEndingIpPrefix  # Ending IP prefix
        self._IntraAreaDistributionType = IntraAreaDistributionType  # Prefix length distribution type
        self._IntraAreaStartPrefixLength = IntraAreaStartPrefixLength  # Start prefix length:
        self._IntraAreaEndPrefixLength = IntraAreaEndPrefixLength  # End prefix length:
        self._IntraAreaPrimaryMetric = IntraAreaPrimaryMetric  # Primary Metric
        self._InterAreaEmulated = InterAreaEmulated  # Emulated routers
        self._InterAreaSimulated = InterAreaSimulated  # Simulated routers
        self._InterAreaRoutesCount = InterAreaRoutesCount  # Total number of routes create
        self._InterAreaOverride = InterAreaOverride  # Override
        self._InterAreaStartingIpPrefix = InterAreaStartingIpPrefix  # Starting IP prefix
        self._InterAreaEndingIpPrefix = InterAreaEndingIpPrefix  # Ending IP prefix
        self._InterAreaDistributionType = InterAreaDistributionType  # Prefix length distribution type
        self._InterAreaStartPrefixLength = InterAreaStartPrefixLength  # Start prefix length:
        self._InterAreaEndPrefixLength = InterAreaEndPrefixLength  # End prefix length:
        self._InterAreaPrimaryMetric = InterAreaPrimaryMetric  # Metric
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
        if StartingRouterId is not None:
            properties['StartingRouterId'] = StartingRouterId
        if RouterIdStep is not None:
            properties['RouterIdStep'] = RouterIdStep
        if IntraAreaEmulated is not None:
            properties['IntraAreaEmulated'] = IntraAreaEmulated
        if IntraAreaSimulated is not None:
            properties['IntraAreaSimulated'] = IntraAreaSimulated
        if IntraAreaRoutesCount is not None:
            properties['IntraAreaRoutesCount'] = IntraAreaRoutesCount
        if IntraAreaOverride is not None:
            properties['IntraAreaOverride'] = IntraAreaOverride
        if IntraAreaStartingIpPrefix is not None:
            properties['IntraAreaStartingIpPrefix'] = IntraAreaStartingIpPrefix
        if IntraAreaEndingIpPrefix is not None:
            properties['IntraAreaEndingIpPrefix'] = IntraAreaEndingIpPrefix
        if IntraAreaDistributionType is not None:
            properties['IntraAreaDistributionType'] = IntraAreaDistributionType
        if IntraAreaStartPrefixLength is not None:
            properties['IntraAreaStartPrefixLength'] = IntraAreaStartPrefixLength
        if IntraAreaEndPrefixLength is not None:
            properties['IntraAreaEndPrefixLength'] = IntraAreaEndPrefixLength
        if IntraAreaPrimaryMetric is not None:
            properties['IntraAreaPrimaryMetric'] = IntraAreaPrimaryMetric
        if InterAreaEmulated is not None:
            properties['InterAreaEmulated'] = InterAreaEmulated
        if InterAreaSimulated is not None:
            properties['InterAreaSimulated'] = InterAreaSimulated
        if InterAreaRoutesCount is not None:
            properties['InterAreaRoutesCount'] = InterAreaRoutesCount
        if InterAreaOverride is not None:
            properties['InterAreaOverride'] = InterAreaOverride
        if InterAreaStartingIpPrefix is not None:
            properties['InterAreaStartingIpPrefix'] = InterAreaStartingIpPrefix
        if InterAreaEndingIpPrefix is not None:
            properties['InterAreaEndingIpPrefix'] = InterAreaEndingIpPrefix
        if InterAreaDistributionType is not None:
            properties['InterAreaDistributionType'] = InterAreaDistributionType
        if InterAreaStartPrefixLength is not None:
            properties['InterAreaStartPrefixLength'] = InterAreaStartPrefixLength
        if InterAreaEndPrefixLength is not None:
            properties['InterAreaEndPrefixLength'] = InterAreaEndPrefixLength
        if InterAreaPrimaryMetric is not None:
            properties['InterAreaPrimaryMetric'] = InterAreaPrimaryMetric
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
        super(Ospfv3LsaWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TopologyType=None, SimulatedRoutersCount=None, InterfaceType=None, RouterMaxInterfaceCount=None, TransitNetworkMaxRouterCount=None, UneditableSimulatedRoutersCount=None, EmulatedRouterPossessSimulatedRouterCount=None, RowCount=None, ColumnCount=None, GridEmulatedRouterPosition=None, EmulatedRouterAttachRowIndex=None, EmulatedRouterAttachColumnIndex=None, MeshRouterCount=None, MeshEmulatedRouterPosition=None, RingRouterCount=None, RingEmulatedRouterPosition=None, HubSpokeRouterCount=None, HubSpokeEmulatedRouterPosition=None, StartingPrefixRange=None, EndingPrefixRange=None, AreaType=None, StartingRouterId=None, RouterIdStep=None, IntraAreaEmulated=None, IntraAreaSimulated=None, IntraAreaRoutesCount=None, IntraAreaOverride=None, IntraAreaStartingIpPrefix=None, IntraAreaEndingIpPrefix=None, IntraAreaDistributionType=None, IntraAreaStartPrefixLength=None, IntraAreaEndPrefixLength=None, IntraAreaPrimaryMetric=None, InterAreaEmulated=None, InterAreaSimulated=None, InterAreaRoutesCount=None, InterAreaOverride=None, InterAreaStartingIpPrefix=None, InterAreaEndingIpPrefix=None, InterAreaDistributionType=None, InterAreaStartPrefixLength=None, InterAreaEndPrefixLength=None, InterAreaPrimaryMetric=None, ExternalEmulated=None, ExternalSimulated=None, ExternalRoutesCount=None, ExternalOverride=None, ExternalStartingIpPrefix=None, ExternalEndingIpPrefix=None, ExternalDistributionType=None, ExternalStartPrefixLength=None, ExternalEndPrefixLength=None, ExternalPrimaryMetric=None, **kwargs):
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
        if StartingRouterId is not None:
            self._StartingRouterId = StartingRouterId
            properties['StartingRouterId'] = StartingRouterId
        if RouterIdStep is not None:
            self._RouterIdStep = RouterIdStep
            properties['RouterIdStep'] = RouterIdStep
        if IntraAreaEmulated is not None:
            self._IntraAreaEmulated = IntraAreaEmulated
            properties['IntraAreaEmulated'] = IntraAreaEmulated
        if IntraAreaSimulated is not None:
            self._IntraAreaSimulated = IntraAreaSimulated
            properties['IntraAreaSimulated'] = IntraAreaSimulated
        if IntraAreaRoutesCount is not None:
            self._IntraAreaRoutesCount = IntraAreaRoutesCount
            properties['IntraAreaRoutesCount'] = IntraAreaRoutesCount
        if IntraAreaOverride is not None:
            self._IntraAreaOverride = IntraAreaOverride
            properties['IntraAreaOverride'] = IntraAreaOverride
        if IntraAreaStartingIpPrefix is not None:
            self._IntraAreaStartingIpPrefix = IntraAreaStartingIpPrefix
            properties['IntraAreaStartingIpPrefix'] = IntraAreaStartingIpPrefix
        if IntraAreaEndingIpPrefix is not None:
            self._IntraAreaEndingIpPrefix = IntraAreaEndingIpPrefix
            properties['IntraAreaEndingIpPrefix'] = IntraAreaEndingIpPrefix
        if IntraAreaDistributionType is not None:
            self._IntraAreaDistributionType = IntraAreaDistributionType
            properties['IntraAreaDistributionType'] = IntraAreaDistributionType
        if IntraAreaStartPrefixLength is not None:
            self._IntraAreaStartPrefixLength = IntraAreaStartPrefixLength
            properties['IntraAreaStartPrefixLength'] = IntraAreaStartPrefixLength
        if IntraAreaEndPrefixLength is not None:
            self._IntraAreaEndPrefixLength = IntraAreaEndPrefixLength
            properties['IntraAreaEndPrefixLength'] = IntraAreaEndPrefixLength
        if IntraAreaPrimaryMetric is not None:
            self._IntraAreaPrimaryMetric = IntraAreaPrimaryMetric
            properties['IntraAreaPrimaryMetric'] = IntraAreaPrimaryMetric
        if InterAreaEmulated is not None:
            self._InterAreaEmulated = InterAreaEmulated
            properties['InterAreaEmulated'] = InterAreaEmulated
        if InterAreaSimulated is not None:
            self._InterAreaSimulated = InterAreaSimulated
            properties['InterAreaSimulated'] = InterAreaSimulated
        if InterAreaRoutesCount is not None:
            self._InterAreaRoutesCount = InterAreaRoutesCount
            properties['InterAreaRoutesCount'] = InterAreaRoutesCount
        if InterAreaOverride is not None:
            self._InterAreaOverride = InterAreaOverride
            properties['InterAreaOverride'] = InterAreaOverride
        if InterAreaStartingIpPrefix is not None:
            self._InterAreaStartingIpPrefix = InterAreaStartingIpPrefix
            properties['InterAreaStartingIpPrefix'] = InterAreaStartingIpPrefix
        if InterAreaEndingIpPrefix is not None:
            self._InterAreaEndingIpPrefix = InterAreaEndingIpPrefix
            properties['InterAreaEndingIpPrefix'] = InterAreaEndingIpPrefix
        if InterAreaDistributionType is not None:
            self._InterAreaDistributionType = InterAreaDistributionType
            properties['InterAreaDistributionType'] = InterAreaDistributionType
        if InterAreaStartPrefixLength is not None:
            self._InterAreaStartPrefixLength = InterAreaStartPrefixLength
            properties['InterAreaStartPrefixLength'] = InterAreaStartPrefixLength
        if InterAreaEndPrefixLength is not None:
            self._InterAreaEndPrefixLength = InterAreaEndPrefixLength
            properties['InterAreaEndPrefixLength'] = InterAreaEndPrefixLength
        if InterAreaPrimaryMetric is not None:
            self._InterAreaPrimaryMetric = InterAreaPrimaryMetric
            properties['InterAreaPrimaryMetric'] = InterAreaPrimaryMetric
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

        super(Ospfv3LsaWizardConfig, self).edit(**properties)

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
    def IntraAreaEmulated(self):
        """
        get the value of property _IntraAreaEmulated
        """
        if self.force_auto_sync:
            self.get('IntraAreaEmulated')
        return self._IntraAreaEmulated

    @property
    def IntraAreaSimulated(self):
        """
        get the value of property _IntraAreaSimulated
        """
        if self.force_auto_sync:
            self.get('IntraAreaSimulated')
        return self._IntraAreaSimulated

    @property
    def IntraAreaRoutesCount(self):
        """
        get the value of property _IntraAreaRoutesCount
        """
        if self.force_auto_sync:
            self.get('IntraAreaRoutesCount')
        return self._IntraAreaRoutesCount

    @property
    def IntraAreaOverride(self):
        """
        get the value of property _IntraAreaOverride
        """
        if self.force_auto_sync:
            self.get('IntraAreaOverride')
        return self._IntraAreaOverride

    @property
    def IntraAreaStartingIpPrefix(self):
        """
        get the value of property _IntraAreaStartingIpPrefix
        """
        if self.force_auto_sync:
            self.get('IntraAreaStartingIpPrefix')
        return self._IntraAreaStartingIpPrefix

    @property
    def IntraAreaEndingIpPrefix(self):
        """
        get the value of property _IntraAreaEndingIpPrefix
        """
        if self.force_auto_sync:
            self.get('IntraAreaEndingIpPrefix')
        return self._IntraAreaEndingIpPrefix

    @property
    def IntraAreaDistributionType(self):
        """
        get the value of property _IntraAreaDistributionType
        """
        if self.force_auto_sync:
            self.get('IntraAreaDistributionType')
        return self._IntraAreaDistributionType

    @property
    def IntraAreaStartPrefixLength(self):
        """
        get the value of property _IntraAreaStartPrefixLength
        """
        if self.force_auto_sync:
            self.get('IntraAreaStartPrefixLength')
        return self._IntraAreaStartPrefixLength

    @property
    def IntraAreaEndPrefixLength(self):
        """
        get the value of property _IntraAreaEndPrefixLength
        """
        if self.force_auto_sync:
            self.get('IntraAreaEndPrefixLength')
        return self._IntraAreaEndPrefixLength

    @property
    def IntraAreaPrimaryMetric(self):
        """
        get the value of property _IntraAreaPrimaryMetric
        """
        if self.force_auto_sync:
            self.get('IntraAreaPrimaryMetric')
        return self._IntraAreaPrimaryMetric

    @property
    def InterAreaEmulated(self):
        """
        get the value of property _InterAreaEmulated
        """
        if self.force_auto_sync:
            self.get('InterAreaEmulated')
        return self._InterAreaEmulated

    @property
    def InterAreaSimulated(self):
        """
        get the value of property _InterAreaSimulated
        """
        if self.force_auto_sync:
            self.get('InterAreaSimulated')
        return self._InterAreaSimulated

    @property
    def InterAreaRoutesCount(self):
        """
        get the value of property _InterAreaRoutesCount
        """
        if self.force_auto_sync:
            self.get('InterAreaRoutesCount')
        return self._InterAreaRoutesCount

    @property
    def InterAreaOverride(self):
        """
        get the value of property _InterAreaOverride
        """
        if self.force_auto_sync:
            self.get('InterAreaOverride')
        return self._InterAreaOverride

    @property
    def InterAreaStartingIpPrefix(self):
        """
        get the value of property _InterAreaStartingIpPrefix
        """
        if self.force_auto_sync:
            self.get('InterAreaStartingIpPrefix')
        return self._InterAreaStartingIpPrefix

    @property
    def InterAreaEndingIpPrefix(self):
        """
        get the value of property _InterAreaEndingIpPrefix
        """
        if self.force_auto_sync:
            self.get('InterAreaEndingIpPrefix')
        return self._InterAreaEndingIpPrefix

    @property
    def InterAreaDistributionType(self):
        """
        get the value of property _InterAreaDistributionType
        """
        if self.force_auto_sync:
            self.get('InterAreaDistributionType')
        return self._InterAreaDistributionType

    @property
    def InterAreaStartPrefixLength(self):
        """
        get the value of property _InterAreaStartPrefixLength
        """
        if self.force_auto_sync:
            self.get('InterAreaStartPrefixLength')
        return self._InterAreaStartPrefixLength

    @property
    def InterAreaEndPrefixLength(self):
        """
        get the value of property _InterAreaEndPrefixLength
        """
        if self.force_auto_sync:
            self.get('InterAreaEndPrefixLength')
        return self._InterAreaEndPrefixLength

    @property
    def InterAreaPrimaryMetric(self):
        """
        get the value of property _InterAreaPrimaryMetric
        """
        if self.force_auto_sync:
            self.get('InterAreaPrimaryMetric')
        return self._InterAreaPrimaryMetric

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

    @StartingRouterId.setter
    def StartingRouterId(self, value):
        self._StartingRouterId = value
        self.edit(StartingRouterId=value)

    @RouterIdStep.setter
    def RouterIdStep(self, value):
        self._RouterIdStep = value
        self.edit(RouterIdStep=value)

    @IntraAreaEmulated.setter
    def IntraAreaEmulated(self, value):
        self._IntraAreaEmulated = value
        self.edit(IntraAreaEmulated=value)

    @IntraAreaSimulated.setter
    def IntraAreaSimulated(self, value):
        self._IntraAreaSimulated = value
        self.edit(IntraAreaSimulated=value)

    @IntraAreaRoutesCount.setter
    def IntraAreaRoutesCount(self, value):
        self._IntraAreaRoutesCount = value
        self.edit(IntraAreaRoutesCount=value)

    @IntraAreaOverride.setter
    def IntraAreaOverride(self, value):
        self._IntraAreaOverride = value
        self.edit(IntraAreaOverride=value)

    @IntraAreaStartingIpPrefix.setter
    def IntraAreaStartingIpPrefix(self, value):
        self._IntraAreaStartingIpPrefix = value
        self.edit(IntraAreaStartingIpPrefix=value)

    @IntraAreaEndingIpPrefix.setter
    def IntraAreaEndingIpPrefix(self, value):
        self._IntraAreaEndingIpPrefix = value
        self.edit(IntraAreaEndingIpPrefix=value)

    @IntraAreaDistributionType.setter
    def IntraAreaDistributionType(self, value):
        self._IntraAreaDistributionType = value
        self.edit(IntraAreaDistributionType=value)

    @IntraAreaStartPrefixLength.setter
    def IntraAreaStartPrefixLength(self, value):
        self._IntraAreaStartPrefixLength = value
        self.edit(IntraAreaStartPrefixLength=value)

    @IntraAreaEndPrefixLength.setter
    def IntraAreaEndPrefixLength(self, value):
        self._IntraAreaEndPrefixLength = value
        self.edit(IntraAreaEndPrefixLength=value)

    @IntraAreaPrimaryMetric.setter
    def IntraAreaPrimaryMetric(self, value):
        self._IntraAreaPrimaryMetric = value
        self.edit(IntraAreaPrimaryMetric=value)

    @InterAreaEmulated.setter
    def InterAreaEmulated(self, value):
        self._InterAreaEmulated = value
        self.edit(InterAreaEmulated=value)

    @InterAreaSimulated.setter
    def InterAreaSimulated(self, value):
        self._InterAreaSimulated = value
        self.edit(InterAreaSimulated=value)

    @InterAreaRoutesCount.setter
    def InterAreaRoutesCount(self, value):
        self._InterAreaRoutesCount = value
        self.edit(InterAreaRoutesCount=value)

    @InterAreaOverride.setter
    def InterAreaOverride(self, value):
        self._InterAreaOverride = value
        self.edit(InterAreaOverride=value)

    @InterAreaStartingIpPrefix.setter
    def InterAreaStartingIpPrefix(self, value):
        self._InterAreaStartingIpPrefix = value
        self.edit(InterAreaStartingIpPrefix=value)

    @InterAreaEndingIpPrefix.setter
    def InterAreaEndingIpPrefix(self, value):
        self._InterAreaEndingIpPrefix = value
        self.edit(InterAreaEndingIpPrefix=value)

    @InterAreaDistributionType.setter
    def InterAreaDistributionType(self, value):
        self._InterAreaDistributionType = value
        self.edit(InterAreaDistributionType=value)

    @InterAreaStartPrefixLength.setter
    def InterAreaStartPrefixLength(self, value):
        self._InterAreaStartPrefixLength = value
        self.edit(InterAreaStartPrefixLength=value)

    @InterAreaEndPrefixLength.setter
    def InterAreaEndPrefixLength(self, value):
        self._InterAreaEndPrefixLength = value
        self.edit(InterAreaEndPrefixLength=value)

    @InterAreaPrimaryMetric.setter
    def InterAreaPrimaryMetric(self, value):
        self._InterAreaPrimaryMetric = value
        self.edit(InterAreaPrimaryMetric=value)

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
        exec('self._TopologyType = EnumOspfv3WizardTopologyType.%s' % value[:seperate])

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
        exec('self._GridEmulatedRouterPosition = EnumOspfv3WizardGridRouterPositionType.%s' % value[:seperate])

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
        exec('self._MeshEmulatedRouterPosition = EnumOspfv3WizardFullMeshRouterPositionType.%s' % value[:seperate])

    def _set_ringroutercount_with_str(self, value):
        try:
            self._RingRouterCount = int(value)
        except ValueError:
            self._RingRouterCount = hex(int(value, 16))

    def _set_ringemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._RingEmulatedRouterPosition = EnumOspfv3WizardRingRouterPositionType.%s' % value[:seperate])

    def _set_hubspokeroutercount_with_str(self, value):
        try:
            self._HubSpokeRouterCount = int(value)
        except ValueError:
            self._HubSpokeRouterCount = hex(int(value, 16))

    def _set_hubspokeemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._HubSpokeEmulatedRouterPosition = EnumOspfv3WizardHubSpokeRouterPositionType.%s' % value[:seperate])

    def _set_startingprefixrange_with_str(self, value):
        self._StartingPrefixRange = value

    def _set_endingprefixrange_with_str(self, value):
        self._EndingPrefixRange = value

    def _set_areatype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AreaType = EnumOspfv3WizardAreaType.%s' % value[:seperate])

    def _set_startingrouterid_with_str(self, value):
        self._StartingRouterId = value

    def _set_routeridstep_with_str(self, value):
        self._RouterIdStep = value

    def _set_intraareaemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._IntraAreaEmulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

    def _set_intraareasimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._IntraAreaSimulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

    def _set_intraarearoutescount_with_str(self, value):
        try:
            self._IntraAreaRoutesCount = int(value)
        except ValueError:
            self._IntraAreaRoutesCount = hex(int(value, 16))

    def _set_intraareaoverride_with_str(self, value):
        self._IntraAreaOverride = (value == 'True')

    def _set_intraareastartingipprefix_with_str(self, value):
        self._IntraAreaStartingIpPrefix = value

    def _set_intraareaendingipprefix_with_str(self, value):
        self._IntraAreaEndingIpPrefix = value

    def _set_intraareadistributiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._IntraAreaDistributionType = EnumOspfv3WizardDistributionType.%s' % value[:seperate])

    def _set_intraareastartprefixlength_with_str(self, value):
        try:
            self._IntraAreaStartPrefixLength = int(value)
        except ValueError:
            self._IntraAreaStartPrefixLength = hex(int(value, 16))

    def _set_intraareaendprefixlength_with_str(self, value):
        try:
            self._IntraAreaEndPrefixLength = int(value)
        except ValueError:
            self._IntraAreaEndPrefixLength = hex(int(value, 16))

    def _set_intraareaprimarymetric_with_str(self, value):
        try:
            self._IntraAreaPrimaryMetric = int(value)
        except ValueError:
            self._IntraAreaPrimaryMetric = hex(int(value, 16))

    def _set_interareaemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._InterAreaEmulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

    def _set_interareasimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._InterAreaSimulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

    def _set_interarearoutescount_with_str(self, value):
        try:
            self._InterAreaRoutesCount = int(value)
        except ValueError:
            self._InterAreaRoutesCount = hex(int(value, 16))

    def _set_interareaoverride_with_str(self, value):
        self._InterAreaOverride = (value == 'True')

    def _set_interareastartingipprefix_with_str(self, value):
        self._InterAreaStartingIpPrefix = value

    def _set_interareaendingipprefix_with_str(self, value):
        self._InterAreaEndingIpPrefix = value

    def _set_interareadistributiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._InterAreaDistributionType = EnumOspfv3WizardDistributionType.%s' % value[:seperate])

    def _set_interareastartprefixlength_with_str(self, value):
        try:
            self._InterAreaStartPrefixLength = int(value)
        except ValueError:
            self._InterAreaStartPrefixLength = hex(int(value, 16))

    def _set_interareaendprefixlength_with_str(self, value):
        try:
            self._InterAreaEndPrefixLength = int(value)
        except ValueError:
            self._InterAreaEndPrefixLength = hex(int(value, 16))

    def _set_interareaprimarymetric_with_str(self, value):
        try:
            self._InterAreaPrimaryMetric = int(value)
        except ValueError:
            self._InterAreaPrimaryMetric = hex(int(value, 16))

    def _set_externalemulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExternalEmulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

    def _set_externalsimulated_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExternalSimulated = EnumOspfv3WizardRadioType.%s' % value[:seperate])

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
        exec('self._ExternalDistributionType = EnumOspfv3WizardDistributionType.%s' % value[:seperate])

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

