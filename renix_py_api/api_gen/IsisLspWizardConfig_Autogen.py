"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class IsisLspWizardConfig(WizardConfigBase):
    def __init__(self, CreateLspLevel=None, TopologyType=None, TreeSimulatedRoutersCount=None, TreeInterfaceType=None, TreeMaxInterfacesPerRouter=None, TreeMaxRoutersPerTransitNetwork=None, GridSimulatedRoutersCount=None, GridSimulatedRoutersPerEmulatedRouter=None, GridNumberOfRows=None, GridNumberOfColumns=None, GridEmulatedRouterPosition=None, GridEmulatedRouterRowIndex=None, GridEmulatedRouterColumnIndex=None, MeshSimulatedRoutersCount=None, MeshSimulatedRoutersPerEmulatedRouter=None, MeshNumberOfRouters=None, MeshEmulatedRouterPosition=None, RingSimulatedRoutersCount=None, RingSimulatedRoutersPerEmulatedRouter=None, RingNumberOfRouters=None, RingEmulatedRouterPosition=None, HubSimulatedRoutersCount=None, HubSimulatedRoutersPerEmulatedRouter=None, HubNumberOfRouters=None, HubEmulatedRouterPosition=None, InterfaceStartIpv4Prefix=None, InterfaceEndIpv4Prefix=None, InterfaceStartIpv6Prefix=None, InterfaceEndIpv6Prefix=None, AdvertiseLoopbackAddress=None, EnableTrafficEngine=None, StartSystemId=None, SystemIdStep=None, StartRouterId=None, RouterIdStep=None, Ipv4InternalAdvEmulatedRouters=None, Ipv4InternalAdvSimulatedRouter=None, Ipv4InternalTotalNumberOfRoutes=None, Ipv4InternalRoutesOverride=None, Ipv4InternalStartRoutesPrefix=None, Ipv4InternalEndRoutesPrefix=None, Ipv4InternalRoutesNoneSeq=None, Ipv4InternalRoutesPrefixLenType=None, Ipv4InternalRoutesPrefixLenStart=None, Ipv4InternalRoutesPrefixLenEnd=None, Ipv4InternalNarrowMetric=None, Ipv4InternalWideMetric=None, Ipv4ExternalAdvEmulatedRouters=None, Ipv4ExternalAdvSimulatedRouter=None, Ipv4ExternalTotalNumberOfRoutes=None, Ipv4ExternalRoutesOverride=None, Ipv4ExternalStartRoutesPrefix=None, Ipv4ExternalEndRoutesPrefix=None, Ipv4ExternalRoutesNoneSeq=None, Ipv4ExternalRoutesPrefixLenType=None, Ipv4ExternalRoutesPrefixLenStart=None, Ipv4ExternalRoutesPrefixLenEnd=None, Ipv4ExternalNarrowMetric=None, Ipv4ExternalWideMetric=None, Ipv6InternalAdvEmulatedRouters=None, Ipv6InternalAdvSimulatedRouter=None, Ipv6InternalTotalNumberOfRoutes=None, Ipv6InternalRoutesOverride=None, Ipv6InternalStartRoutesPrefix=None, Ipv6InternalEndRoutesPrefix=None, Ipv6InternalRoutesNoneSeq=None, Ipv6InternalRoutesPrefixLenType=None, Ipv6InternalRoutesPrefixLenStart=None, Ipv6InternalRoutesPrefixLenEnd=None, Ipv6InternalWideMetric=None, Ipv6ExternalAdvEmulatedRouters=None, Ipv6ExternalAdvSimulatedRouter=None, Ipv6ExternalTotalNumberOfRoutes=None, Ipv6ExternalRoutesOverride=None, Ipv6ExternalStartRoutesPrefix=None, Ipv6ExternalEndRoutesPrefix=None, Ipv6ExternalRoutesNoneSeq=None, Ipv6ExternalRoutesPrefixLenType=None, Ipv6ExternalRoutesPrefixLenStart=None, Ipv6ExternalRoutesPrefixLenEnd=None, Ipv6ExternalWideMetric=None, **kwargs):
        self._CreateLspLevel = CreateLspLevel  # Create Lsp Level
        self._TopologyType = TopologyType  # Topology Type
        self._TreeSimulatedRoutersCount = TreeSimulatedRoutersCount  # Total number of Simulated routers
        self._TreeInterfaceType = TreeInterfaceType  # Interface type
        self._TreeMaxInterfacesPerRouter = TreeMaxInterfacesPerRouter  # Max interfaces per router
        self._TreeMaxRoutersPerTransitNetwork = TreeMaxRoutersPerTransitNetwork  # Max routers per transit network
        self._GridSimulatedRoutersCount = GridSimulatedRoutersCount  # Total number of simulated routers
        self._GridSimulatedRoutersPerEmulatedRouter = GridSimulatedRoutersPerEmulatedRouter  # Simulated Router Per Emulated Router
        self._GridNumberOfRows = GridNumberOfRows  # Number of Rows
        self._GridNumberOfColumns = GridNumberOfColumns  # Number of Columns
        self._GridEmulatedRouterPosition = GridEmulatedRouterPosition  # Emulated Router Position
        self._GridEmulatedRouterRowIndex = GridEmulatedRouterRowIndex  # Emulated Router Row Index
        self._GridEmulatedRouterColumnIndex = GridEmulatedRouterColumnIndex  # Emulated Router Column Index
        self._MeshSimulatedRoutersCount = MeshSimulatedRoutersCount  # Total number of simulated routers
        self._MeshSimulatedRoutersPerEmulatedRouter = MeshSimulatedRoutersPerEmulatedRouter  # Simulated Router Per Emulated Router
        self._MeshNumberOfRouters = MeshNumberOfRouters  # Number Of Routers in Mesh
        self._MeshEmulatedRouterPosition = MeshEmulatedRouterPosition  # Emulated Router Position
        self._RingSimulatedRoutersCount = RingSimulatedRoutersCount  # Total number of simulated routers
        self._RingSimulatedRoutersPerEmulatedRouter = RingSimulatedRoutersPerEmulatedRouter  # Simulated Router Per Emulated Router
        self._RingNumberOfRouters = RingNumberOfRouters  # Number Of Routers in Ring
        self._RingEmulatedRouterPosition = RingEmulatedRouterPosition  # Emulated Router Position
        self._HubSimulatedRoutersCount = HubSimulatedRoutersCount  # Total number of simulated routers
        self._HubSimulatedRoutersPerEmulatedRouter = HubSimulatedRoutersPerEmulatedRouter  # Simulated Router Per Emulated Router
        self._HubNumberOfRouters = HubNumberOfRouters  # Number Of Routers in Hub
        self._HubEmulatedRouterPosition = HubEmulatedRouterPosition  # Emulated Router Position
        self._InterfaceStartIpv4Prefix = InterfaceStartIpv4Prefix  # Starting IPv4 Prefixes
        self._InterfaceEndIpv4Prefix = InterfaceEndIpv4Prefix  # Ending IPv4 Prefixed
        self._InterfaceStartIpv6Prefix = InterfaceStartIpv6Prefix  # Starting IPv6 Prefixes
        self._InterfaceEndIpv6Prefix = InterfaceEndIpv6Prefix  # Starting IPv6 Prefixes
        self._AdvertiseLoopbackAddress = AdvertiseLoopbackAddress  # Advertise Loopback Address
        self._EnableTrafficEngine = EnableTrafficEngine  # Enable Traffic Engine
        self._StartSystemId = StartSystemId  # Starting System ID
        self._SystemIdStep = SystemIdStep  # Ending System ID
        self._StartRouterId = StartRouterId  # Starting Router ID
        self._RouterIdStep = RouterIdStep  # Router ID Step
        self._Ipv4InternalAdvEmulatedRouters = Ipv4InternalAdvEmulatedRouters  # Advertise Routes for Emulated Routers
        self._Ipv4InternalAdvSimulatedRouter = Ipv4InternalAdvSimulatedRouter  # Advertise Routes for Simulated Routers
        self._Ipv4InternalTotalNumberOfRoutes = Ipv4InternalTotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv4InternalRoutesOverride = Ipv4InternalRoutesOverride  # Override
        self._Ipv4InternalStartRoutesPrefix = Ipv4InternalStartRoutesPrefix  # Starting IP Prefix
        self._Ipv4InternalEndRoutesPrefix = Ipv4InternalEndRoutesPrefix  # Ending IP Prefix
        self._Ipv4InternalRoutesNoneSeq = Ipv4InternalRoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv4InternalRoutesPrefixLenType = Ipv4InternalRoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv4InternalRoutesPrefixLenStart = Ipv4InternalRoutesPrefixLenStart  # Start Prefix Length
        self._Ipv4InternalRoutesPrefixLenEnd = Ipv4InternalRoutesPrefixLenEnd  # End Prefix Length
        self._Ipv4InternalNarrowMetric = Ipv4InternalNarrowMetric  # Narrow Metric
        self._Ipv4InternalWideMetric = Ipv4InternalWideMetric  # Wide Metric
        self._Ipv4ExternalAdvEmulatedRouters = Ipv4ExternalAdvEmulatedRouters  # Advertise Routes for Emulated Routers
        self._Ipv4ExternalAdvSimulatedRouter = Ipv4ExternalAdvSimulatedRouter  # Advertise Routes for Simulated Routers
        self._Ipv4ExternalTotalNumberOfRoutes = Ipv4ExternalTotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv4ExternalRoutesOverride = Ipv4ExternalRoutesOverride  # Override
        self._Ipv4ExternalStartRoutesPrefix = Ipv4ExternalStartRoutesPrefix  # Starting IP Prefix
        self._Ipv4ExternalEndRoutesPrefix = Ipv4ExternalEndRoutesPrefix  # Ending IP Prefix
        self._Ipv4ExternalRoutesNoneSeq = Ipv4ExternalRoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv4ExternalRoutesPrefixLenType = Ipv4ExternalRoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv4ExternalRoutesPrefixLenStart = Ipv4ExternalRoutesPrefixLenStart  # Start Prefix Length
        self._Ipv4ExternalRoutesPrefixLenEnd = Ipv4ExternalRoutesPrefixLenEnd  # End Prefix Length
        self._Ipv4ExternalNarrowMetric = Ipv4ExternalNarrowMetric  # Narrow Metric
        self._Ipv4ExternalWideMetric = Ipv4ExternalWideMetric  # Wide Metric
        self._Ipv6InternalAdvEmulatedRouters = Ipv6InternalAdvEmulatedRouters  # Advertise Routes for Emulated Routers
        self._Ipv6InternalAdvSimulatedRouter = Ipv6InternalAdvSimulatedRouter  # Advertise Routes for Simulated Routers
        self._Ipv6InternalTotalNumberOfRoutes = Ipv6InternalTotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv6InternalRoutesOverride = Ipv6InternalRoutesOverride  # Override
        self._Ipv6InternalStartRoutesPrefix = Ipv6InternalStartRoutesPrefix  # Starting IP Prefix
        self._Ipv6InternalEndRoutesPrefix = Ipv6InternalEndRoutesPrefix  # Ending IP Prefix
        self._Ipv6InternalRoutesNoneSeq = Ipv6InternalRoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv6InternalRoutesPrefixLenType = Ipv6InternalRoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv6InternalRoutesPrefixLenStart = Ipv6InternalRoutesPrefixLenStart  # Start Prefix Length
        self._Ipv6InternalRoutesPrefixLenEnd = Ipv6InternalRoutesPrefixLenEnd  # End Prefix Length
        self._Ipv6InternalWideMetric = Ipv6InternalWideMetric  # Wide Metric
        self._Ipv6ExternalAdvEmulatedRouters = Ipv6ExternalAdvEmulatedRouters  # Advertise Routes for Emulated Routers
        self._Ipv6ExternalAdvSimulatedRouter = Ipv6ExternalAdvSimulatedRouter  # Advertise Routes for Simulated Routers
        self._Ipv6ExternalTotalNumberOfRoutes = Ipv6ExternalTotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv6ExternalRoutesOverride = Ipv6ExternalRoutesOverride  # Override
        self._Ipv6ExternalStartRoutesPrefix = Ipv6ExternalStartRoutesPrefix  # Starting IP Prefix
        self._Ipv6ExternalEndRoutesPrefix = Ipv6ExternalEndRoutesPrefix  # Ending IP Prefix
        self._Ipv6ExternalRoutesNoneSeq = Ipv6ExternalRoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv6ExternalRoutesPrefixLenType = Ipv6ExternalRoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv6ExternalRoutesPrefixLenStart = Ipv6ExternalRoutesPrefixLenStart  # Start Prefix Length
        self._Ipv6ExternalRoutesPrefixLenEnd = Ipv6ExternalRoutesPrefixLenEnd  # End Prefix Length
        self._Ipv6ExternalWideMetric = Ipv6ExternalWideMetric  # Wide Metric

        properties = kwargs.copy()
        if CreateLspLevel is not None:
            properties['CreateLspLevel'] = CreateLspLevel
        if TopologyType is not None:
            properties['TopologyType'] = TopologyType
        if TreeSimulatedRoutersCount is not None:
            properties['TreeSimulatedRoutersCount'] = TreeSimulatedRoutersCount
        if TreeInterfaceType is not None:
            properties['TreeInterfaceType'] = TreeInterfaceType
        if TreeMaxInterfacesPerRouter is not None:
            properties['TreeMaxInterfacesPerRouter'] = TreeMaxInterfacesPerRouter
        if TreeMaxRoutersPerTransitNetwork is not None:
            properties['TreeMaxRoutersPerTransitNetwork'] = TreeMaxRoutersPerTransitNetwork
        if GridSimulatedRoutersCount is not None:
            properties['GridSimulatedRoutersCount'] = GridSimulatedRoutersCount
        if GridSimulatedRoutersPerEmulatedRouter is not None:
            properties['GridSimulatedRoutersPerEmulatedRouter'] = GridSimulatedRoutersPerEmulatedRouter
        if GridNumberOfRows is not None:
            properties['GridNumberOfRows'] = GridNumberOfRows
        if GridNumberOfColumns is not None:
            properties['GridNumberOfColumns'] = GridNumberOfColumns
        if GridEmulatedRouterPosition is not None:
            properties['GridEmulatedRouterPosition'] = GridEmulatedRouterPosition
        if GridEmulatedRouterRowIndex is not None:
            properties['GridEmulatedRouterRowIndex'] = GridEmulatedRouterRowIndex
        if GridEmulatedRouterColumnIndex is not None:
            properties['GridEmulatedRouterColumnIndex'] = GridEmulatedRouterColumnIndex
        if MeshSimulatedRoutersCount is not None:
            properties['MeshSimulatedRoutersCount'] = MeshSimulatedRoutersCount
        if MeshSimulatedRoutersPerEmulatedRouter is not None:
            properties['MeshSimulatedRoutersPerEmulatedRouter'] = MeshSimulatedRoutersPerEmulatedRouter
        if MeshNumberOfRouters is not None:
            properties['MeshNumberOfRouters'] = MeshNumberOfRouters
        if MeshEmulatedRouterPosition is not None:
            properties['MeshEmulatedRouterPosition'] = MeshEmulatedRouterPosition
        if RingSimulatedRoutersCount is not None:
            properties['RingSimulatedRoutersCount'] = RingSimulatedRoutersCount
        if RingSimulatedRoutersPerEmulatedRouter is not None:
            properties['RingSimulatedRoutersPerEmulatedRouter'] = RingSimulatedRoutersPerEmulatedRouter
        if RingNumberOfRouters is not None:
            properties['RingNumberOfRouters'] = RingNumberOfRouters
        if RingEmulatedRouterPosition is not None:
            properties['RingEmulatedRouterPosition'] = RingEmulatedRouterPosition
        if HubSimulatedRoutersCount is not None:
            properties['HubSimulatedRoutersCount'] = HubSimulatedRoutersCount
        if HubSimulatedRoutersPerEmulatedRouter is not None:
            properties['HubSimulatedRoutersPerEmulatedRouter'] = HubSimulatedRoutersPerEmulatedRouter
        if HubNumberOfRouters is not None:
            properties['HubNumberOfRouters'] = HubNumberOfRouters
        if HubEmulatedRouterPosition is not None:
            properties['HubEmulatedRouterPosition'] = HubEmulatedRouterPosition
        if InterfaceStartIpv4Prefix is not None:
            properties['InterfaceStartIpv4Prefix'] = InterfaceStartIpv4Prefix
        if InterfaceEndIpv4Prefix is not None:
            properties['InterfaceEndIpv4Prefix'] = InterfaceEndIpv4Prefix
        if InterfaceStartIpv6Prefix is not None:
            properties['InterfaceStartIpv6Prefix'] = InterfaceStartIpv6Prefix
        if InterfaceEndIpv6Prefix is not None:
            properties['InterfaceEndIpv6Prefix'] = InterfaceEndIpv6Prefix
        if AdvertiseLoopbackAddress is not None:
            properties['AdvertiseLoopbackAddress'] = AdvertiseLoopbackAddress
        if EnableTrafficEngine is not None:
            properties['EnableTrafficEngine'] = EnableTrafficEngine
        if StartSystemId is not None:
            properties['StartSystemId'] = StartSystemId
        if SystemIdStep is not None:
            properties['SystemIdStep'] = SystemIdStep
        if StartRouterId is not None:
            properties['StartRouterId'] = StartRouterId
        if RouterIdStep is not None:
            properties['RouterIdStep'] = RouterIdStep
        if Ipv4InternalAdvEmulatedRouters is not None:
            properties['Ipv4InternalAdvEmulatedRouters'] = Ipv4InternalAdvEmulatedRouters
        if Ipv4InternalAdvSimulatedRouter is not None:
            properties['Ipv4InternalAdvSimulatedRouter'] = Ipv4InternalAdvSimulatedRouter
        if Ipv4InternalTotalNumberOfRoutes is not None:
            properties['Ipv4InternalTotalNumberOfRoutes'] = Ipv4InternalTotalNumberOfRoutes
        if Ipv4InternalRoutesOverride is not None:
            properties['Ipv4InternalRoutesOverride'] = Ipv4InternalRoutesOverride
        if Ipv4InternalStartRoutesPrefix is not None:
            properties['Ipv4InternalStartRoutesPrefix'] = Ipv4InternalStartRoutesPrefix
        if Ipv4InternalEndRoutesPrefix is not None:
            properties['Ipv4InternalEndRoutesPrefix'] = Ipv4InternalEndRoutesPrefix
        if Ipv4InternalRoutesNoneSeq is not None:
            properties['Ipv4InternalRoutesNoneSeq'] = Ipv4InternalRoutesNoneSeq
        if Ipv4InternalRoutesPrefixLenType is not None:
            properties['Ipv4InternalRoutesPrefixLenType'] = Ipv4InternalRoutesPrefixLenType
        if Ipv4InternalRoutesPrefixLenStart is not None:
            properties['Ipv4InternalRoutesPrefixLenStart'] = Ipv4InternalRoutesPrefixLenStart
        if Ipv4InternalRoutesPrefixLenEnd is not None:
            properties['Ipv4InternalRoutesPrefixLenEnd'] = Ipv4InternalRoutesPrefixLenEnd
        if Ipv4InternalNarrowMetric is not None:
            properties['Ipv4InternalNarrowMetric'] = Ipv4InternalNarrowMetric
        if Ipv4InternalWideMetric is not None:
            properties['Ipv4InternalWideMetric'] = Ipv4InternalWideMetric
        if Ipv4ExternalAdvEmulatedRouters is not None:
            properties['Ipv4ExternalAdvEmulatedRouters'] = Ipv4ExternalAdvEmulatedRouters
        if Ipv4ExternalAdvSimulatedRouter is not None:
            properties['Ipv4ExternalAdvSimulatedRouter'] = Ipv4ExternalAdvSimulatedRouter
        if Ipv4ExternalTotalNumberOfRoutes is not None:
            properties['Ipv4ExternalTotalNumberOfRoutes'] = Ipv4ExternalTotalNumberOfRoutes
        if Ipv4ExternalRoutesOverride is not None:
            properties['Ipv4ExternalRoutesOverride'] = Ipv4ExternalRoutesOverride
        if Ipv4ExternalStartRoutesPrefix is not None:
            properties['Ipv4ExternalStartRoutesPrefix'] = Ipv4ExternalStartRoutesPrefix
        if Ipv4ExternalEndRoutesPrefix is not None:
            properties['Ipv4ExternalEndRoutesPrefix'] = Ipv4ExternalEndRoutesPrefix
        if Ipv4ExternalRoutesNoneSeq is not None:
            properties['Ipv4ExternalRoutesNoneSeq'] = Ipv4ExternalRoutesNoneSeq
        if Ipv4ExternalRoutesPrefixLenType is not None:
            properties['Ipv4ExternalRoutesPrefixLenType'] = Ipv4ExternalRoutesPrefixLenType
        if Ipv4ExternalRoutesPrefixLenStart is not None:
            properties['Ipv4ExternalRoutesPrefixLenStart'] = Ipv4ExternalRoutesPrefixLenStart
        if Ipv4ExternalRoutesPrefixLenEnd is not None:
            properties['Ipv4ExternalRoutesPrefixLenEnd'] = Ipv4ExternalRoutesPrefixLenEnd
        if Ipv4ExternalNarrowMetric is not None:
            properties['Ipv4ExternalNarrowMetric'] = Ipv4ExternalNarrowMetric
        if Ipv4ExternalWideMetric is not None:
            properties['Ipv4ExternalWideMetric'] = Ipv4ExternalWideMetric
        if Ipv6InternalAdvEmulatedRouters is not None:
            properties['Ipv6InternalAdvEmulatedRouters'] = Ipv6InternalAdvEmulatedRouters
        if Ipv6InternalAdvSimulatedRouter is not None:
            properties['Ipv6InternalAdvSimulatedRouter'] = Ipv6InternalAdvSimulatedRouter
        if Ipv6InternalTotalNumberOfRoutes is not None:
            properties['Ipv6InternalTotalNumberOfRoutes'] = Ipv6InternalTotalNumberOfRoutes
        if Ipv6InternalRoutesOverride is not None:
            properties['Ipv6InternalRoutesOverride'] = Ipv6InternalRoutesOverride
        if Ipv6InternalStartRoutesPrefix is not None:
            properties['Ipv6InternalStartRoutesPrefix'] = Ipv6InternalStartRoutesPrefix
        if Ipv6InternalEndRoutesPrefix is not None:
            properties['Ipv6InternalEndRoutesPrefix'] = Ipv6InternalEndRoutesPrefix
        if Ipv6InternalRoutesNoneSeq is not None:
            properties['Ipv6InternalRoutesNoneSeq'] = Ipv6InternalRoutesNoneSeq
        if Ipv6InternalRoutesPrefixLenType is not None:
            properties['Ipv6InternalRoutesPrefixLenType'] = Ipv6InternalRoutesPrefixLenType
        if Ipv6InternalRoutesPrefixLenStart is not None:
            properties['Ipv6InternalRoutesPrefixLenStart'] = Ipv6InternalRoutesPrefixLenStart
        if Ipv6InternalRoutesPrefixLenEnd is not None:
            properties['Ipv6InternalRoutesPrefixLenEnd'] = Ipv6InternalRoutesPrefixLenEnd
        if Ipv6InternalWideMetric is not None:
            properties['Ipv6InternalWideMetric'] = Ipv6InternalWideMetric
        if Ipv6ExternalAdvEmulatedRouters is not None:
            properties['Ipv6ExternalAdvEmulatedRouters'] = Ipv6ExternalAdvEmulatedRouters
        if Ipv6ExternalAdvSimulatedRouter is not None:
            properties['Ipv6ExternalAdvSimulatedRouter'] = Ipv6ExternalAdvSimulatedRouter
        if Ipv6ExternalTotalNumberOfRoutes is not None:
            properties['Ipv6ExternalTotalNumberOfRoutes'] = Ipv6ExternalTotalNumberOfRoutes
        if Ipv6ExternalRoutesOverride is not None:
            properties['Ipv6ExternalRoutesOverride'] = Ipv6ExternalRoutesOverride
        if Ipv6ExternalStartRoutesPrefix is not None:
            properties['Ipv6ExternalStartRoutesPrefix'] = Ipv6ExternalStartRoutesPrefix
        if Ipv6ExternalEndRoutesPrefix is not None:
            properties['Ipv6ExternalEndRoutesPrefix'] = Ipv6ExternalEndRoutesPrefix
        if Ipv6ExternalRoutesNoneSeq is not None:
            properties['Ipv6ExternalRoutesNoneSeq'] = Ipv6ExternalRoutesNoneSeq
        if Ipv6ExternalRoutesPrefixLenType is not None:
            properties['Ipv6ExternalRoutesPrefixLenType'] = Ipv6ExternalRoutesPrefixLenType
        if Ipv6ExternalRoutesPrefixLenStart is not None:
            properties['Ipv6ExternalRoutesPrefixLenStart'] = Ipv6ExternalRoutesPrefixLenStart
        if Ipv6ExternalRoutesPrefixLenEnd is not None:
            properties['Ipv6ExternalRoutesPrefixLenEnd'] = Ipv6ExternalRoutesPrefixLenEnd
        if Ipv6ExternalWideMetric is not None:
            properties['Ipv6ExternalWideMetric'] = Ipv6ExternalWideMetric

        # call base class function, and it will send message to renix server to create a class.
        super(IsisLspWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CreateLspLevel=None, TopologyType=None, TreeSimulatedRoutersCount=None, TreeInterfaceType=None, TreeMaxInterfacesPerRouter=None, TreeMaxRoutersPerTransitNetwork=None, GridSimulatedRoutersCount=None, GridSimulatedRoutersPerEmulatedRouter=None, GridNumberOfRows=None, GridNumberOfColumns=None, GridEmulatedRouterPosition=None, GridEmulatedRouterRowIndex=None, GridEmulatedRouterColumnIndex=None, MeshSimulatedRoutersCount=None, MeshSimulatedRoutersPerEmulatedRouter=None, MeshNumberOfRouters=None, MeshEmulatedRouterPosition=None, RingSimulatedRoutersCount=None, RingSimulatedRoutersPerEmulatedRouter=None, RingNumberOfRouters=None, RingEmulatedRouterPosition=None, HubSimulatedRoutersCount=None, HubSimulatedRoutersPerEmulatedRouter=None, HubNumberOfRouters=None, HubEmulatedRouterPosition=None, InterfaceStartIpv4Prefix=None, InterfaceEndIpv4Prefix=None, InterfaceStartIpv6Prefix=None, InterfaceEndIpv6Prefix=None, AdvertiseLoopbackAddress=None, EnableTrafficEngine=None, StartSystemId=None, SystemIdStep=None, StartRouterId=None, RouterIdStep=None, Ipv4InternalAdvEmulatedRouters=None, Ipv4InternalAdvSimulatedRouter=None, Ipv4InternalTotalNumberOfRoutes=None, Ipv4InternalRoutesOverride=None, Ipv4InternalStartRoutesPrefix=None, Ipv4InternalEndRoutesPrefix=None, Ipv4InternalRoutesNoneSeq=None, Ipv4InternalRoutesPrefixLenType=None, Ipv4InternalRoutesPrefixLenStart=None, Ipv4InternalRoutesPrefixLenEnd=None, Ipv4InternalNarrowMetric=None, Ipv4InternalWideMetric=None, Ipv4ExternalAdvEmulatedRouters=None, Ipv4ExternalAdvSimulatedRouter=None, Ipv4ExternalTotalNumberOfRoutes=None, Ipv4ExternalRoutesOverride=None, Ipv4ExternalStartRoutesPrefix=None, Ipv4ExternalEndRoutesPrefix=None, Ipv4ExternalRoutesNoneSeq=None, Ipv4ExternalRoutesPrefixLenType=None, Ipv4ExternalRoutesPrefixLenStart=None, Ipv4ExternalRoutesPrefixLenEnd=None, Ipv4ExternalNarrowMetric=None, Ipv4ExternalWideMetric=None, Ipv6InternalAdvEmulatedRouters=None, Ipv6InternalAdvSimulatedRouter=None, Ipv6InternalTotalNumberOfRoutes=None, Ipv6InternalRoutesOverride=None, Ipv6InternalStartRoutesPrefix=None, Ipv6InternalEndRoutesPrefix=None, Ipv6InternalRoutesNoneSeq=None, Ipv6InternalRoutesPrefixLenType=None, Ipv6InternalRoutesPrefixLenStart=None, Ipv6InternalRoutesPrefixLenEnd=None, Ipv6InternalWideMetric=None, Ipv6ExternalAdvEmulatedRouters=None, Ipv6ExternalAdvSimulatedRouter=None, Ipv6ExternalTotalNumberOfRoutes=None, Ipv6ExternalRoutesOverride=None, Ipv6ExternalStartRoutesPrefix=None, Ipv6ExternalEndRoutesPrefix=None, Ipv6ExternalRoutesNoneSeq=None, Ipv6ExternalRoutesPrefixLenType=None, Ipv6ExternalRoutesPrefixLenStart=None, Ipv6ExternalRoutesPrefixLenEnd=None, Ipv6ExternalWideMetric=None, **kwargs):
        properties = kwargs.copy()
        if CreateLspLevel is not None:
            self._CreateLspLevel = CreateLspLevel
            properties['CreateLspLevel'] = CreateLspLevel
        if TopologyType is not None:
            self._TopologyType = TopologyType
            properties['TopologyType'] = TopologyType
        if TreeSimulatedRoutersCount is not None:
            self._TreeSimulatedRoutersCount = TreeSimulatedRoutersCount
            properties['TreeSimulatedRoutersCount'] = TreeSimulatedRoutersCount
        if TreeInterfaceType is not None:
            self._TreeInterfaceType = TreeInterfaceType
            properties['TreeInterfaceType'] = TreeInterfaceType
        if TreeMaxInterfacesPerRouter is not None:
            self._TreeMaxInterfacesPerRouter = TreeMaxInterfacesPerRouter
            properties['TreeMaxInterfacesPerRouter'] = TreeMaxInterfacesPerRouter
        if TreeMaxRoutersPerTransitNetwork is not None:
            self._TreeMaxRoutersPerTransitNetwork = TreeMaxRoutersPerTransitNetwork
            properties['TreeMaxRoutersPerTransitNetwork'] = TreeMaxRoutersPerTransitNetwork
        if GridSimulatedRoutersCount is not None:
            self._GridSimulatedRoutersCount = GridSimulatedRoutersCount
            properties['GridSimulatedRoutersCount'] = GridSimulatedRoutersCount
        if GridSimulatedRoutersPerEmulatedRouter is not None:
            self._GridSimulatedRoutersPerEmulatedRouter = GridSimulatedRoutersPerEmulatedRouter
            properties['GridSimulatedRoutersPerEmulatedRouter'] = GridSimulatedRoutersPerEmulatedRouter
        if GridNumberOfRows is not None:
            self._GridNumberOfRows = GridNumberOfRows
            properties['GridNumberOfRows'] = GridNumberOfRows
        if GridNumberOfColumns is not None:
            self._GridNumberOfColumns = GridNumberOfColumns
            properties['GridNumberOfColumns'] = GridNumberOfColumns
        if GridEmulatedRouterPosition is not None:
            self._GridEmulatedRouterPosition = GridEmulatedRouterPosition
            properties['GridEmulatedRouterPosition'] = GridEmulatedRouterPosition
        if GridEmulatedRouterRowIndex is not None:
            self._GridEmulatedRouterRowIndex = GridEmulatedRouterRowIndex
            properties['GridEmulatedRouterRowIndex'] = GridEmulatedRouterRowIndex
        if GridEmulatedRouterColumnIndex is not None:
            self._GridEmulatedRouterColumnIndex = GridEmulatedRouterColumnIndex
            properties['GridEmulatedRouterColumnIndex'] = GridEmulatedRouterColumnIndex
        if MeshSimulatedRoutersCount is not None:
            self._MeshSimulatedRoutersCount = MeshSimulatedRoutersCount
            properties['MeshSimulatedRoutersCount'] = MeshSimulatedRoutersCount
        if MeshSimulatedRoutersPerEmulatedRouter is not None:
            self._MeshSimulatedRoutersPerEmulatedRouter = MeshSimulatedRoutersPerEmulatedRouter
            properties['MeshSimulatedRoutersPerEmulatedRouter'] = MeshSimulatedRoutersPerEmulatedRouter
        if MeshNumberOfRouters is not None:
            self._MeshNumberOfRouters = MeshNumberOfRouters
            properties['MeshNumberOfRouters'] = MeshNumberOfRouters
        if MeshEmulatedRouterPosition is not None:
            self._MeshEmulatedRouterPosition = MeshEmulatedRouterPosition
            properties['MeshEmulatedRouterPosition'] = MeshEmulatedRouterPosition
        if RingSimulatedRoutersCount is not None:
            self._RingSimulatedRoutersCount = RingSimulatedRoutersCount
            properties['RingSimulatedRoutersCount'] = RingSimulatedRoutersCount
        if RingSimulatedRoutersPerEmulatedRouter is not None:
            self._RingSimulatedRoutersPerEmulatedRouter = RingSimulatedRoutersPerEmulatedRouter
            properties['RingSimulatedRoutersPerEmulatedRouter'] = RingSimulatedRoutersPerEmulatedRouter
        if RingNumberOfRouters is not None:
            self._RingNumberOfRouters = RingNumberOfRouters
            properties['RingNumberOfRouters'] = RingNumberOfRouters
        if RingEmulatedRouterPosition is not None:
            self._RingEmulatedRouterPosition = RingEmulatedRouterPosition
            properties['RingEmulatedRouterPosition'] = RingEmulatedRouterPosition
        if HubSimulatedRoutersCount is not None:
            self._HubSimulatedRoutersCount = HubSimulatedRoutersCount
            properties['HubSimulatedRoutersCount'] = HubSimulatedRoutersCount
        if HubSimulatedRoutersPerEmulatedRouter is not None:
            self._HubSimulatedRoutersPerEmulatedRouter = HubSimulatedRoutersPerEmulatedRouter
            properties['HubSimulatedRoutersPerEmulatedRouter'] = HubSimulatedRoutersPerEmulatedRouter
        if HubNumberOfRouters is not None:
            self._HubNumberOfRouters = HubNumberOfRouters
            properties['HubNumberOfRouters'] = HubNumberOfRouters
        if HubEmulatedRouterPosition is not None:
            self._HubEmulatedRouterPosition = HubEmulatedRouterPosition
            properties['HubEmulatedRouterPosition'] = HubEmulatedRouterPosition
        if InterfaceStartIpv4Prefix is not None:
            self._InterfaceStartIpv4Prefix = InterfaceStartIpv4Prefix
            properties['InterfaceStartIpv4Prefix'] = InterfaceStartIpv4Prefix
        if InterfaceEndIpv4Prefix is not None:
            self._InterfaceEndIpv4Prefix = InterfaceEndIpv4Prefix
            properties['InterfaceEndIpv4Prefix'] = InterfaceEndIpv4Prefix
        if InterfaceStartIpv6Prefix is not None:
            self._InterfaceStartIpv6Prefix = InterfaceStartIpv6Prefix
            properties['InterfaceStartIpv6Prefix'] = InterfaceStartIpv6Prefix
        if InterfaceEndIpv6Prefix is not None:
            self._InterfaceEndIpv6Prefix = InterfaceEndIpv6Prefix
            properties['InterfaceEndIpv6Prefix'] = InterfaceEndIpv6Prefix
        if AdvertiseLoopbackAddress is not None:
            self._AdvertiseLoopbackAddress = AdvertiseLoopbackAddress
            properties['AdvertiseLoopbackAddress'] = AdvertiseLoopbackAddress
        if EnableTrafficEngine is not None:
            self._EnableTrafficEngine = EnableTrafficEngine
            properties['EnableTrafficEngine'] = EnableTrafficEngine
        if StartSystemId is not None:
            self._StartSystemId = StartSystemId
            properties['StartSystemId'] = StartSystemId
        if SystemIdStep is not None:
            self._SystemIdStep = SystemIdStep
            properties['SystemIdStep'] = SystemIdStep
        if StartRouterId is not None:
            self._StartRouterId = StartRouterId
            properties['StartRouterId'] = StartRouterId
        if RouterIdStep is not None:
            self._RouterIdStep = RouterIdStep
            properties['RouterIdStep'] = RouterIdStep
        if Ipv4InternalAdvEmulatedRouters is not None:
            self._Ipv4InternalAdvEmulatedRouters = Ipv4InternalAdvEmulatedRouters
            properties['Ipv4InternalAdvEmulatedRouters'] = Ipv4InternalAdvEmulatedRouters
        if Ipv4InternalAdvSimulatedRouter is not None:
            self._Ipv4InternalAdvSimulatedRouter = Ipv4InternalAdvSimulatedRouter
            properties['Ipv4InternalAdvSimulatedRouter'] = Ipv4InternalAdvSimulatedRouter
        if Ipv4InternalTotalNumberOfRoutes is not None:
            self._Ipv4InternalTotalNumberOfRoutes = Ipv4InternalTotalNumberOfRoutes
            properties['Ipv4InternalTotalNumberOfRoutes'] = Ipv4InternalTotalNumberOfRoutes
        if Ipv4InternalRoutesOverride is not None:
            self._Ipv4InternalRoutesOverride = Ipv4InternalRoutesOverride
            properties['Ipv4InternalRoutesOverride'] = Ipv4InternalRoutesOverride
        if Ipv4InternalStartRoutesPrefix is not None:
            self._Ipv4InternalStartRoutesPrefix = Ipv4InternalStartRoutesPrefix
            properties['Ipv4InternalStartRoutesPrefix'] = Ipv4InternalStartRoutesPrefix
        if Ipv4InternalEndRoutesPrefix is not None:
            self._Ipv4InternalEndRoutesPrefix = Ipv4InternalEndRoutesPrefix
            properties['Ipv4InternalEndRoutesPrefix'] = Ipv4InternalEndRoutesPrefix
        if Ipv4InternalRoutesNoneSeq is not None:
            self._Ipv4InternalRoutesNoneSeq = Ipv4InternalRoutesNoneSeq
            properties['Ipv4InternalRoutesNoneSeq'] = Ipv4InternalRoutesNoneSeq
        if Ipv4InternalRoutesPrefixLenType is not None:
            self._Ipv4InternalRoutesPrefixLenType = Ipv4InternalRoutesPrefixLenType
            properties['Ipv4InternalRoutesPrefixLenType'] = Ipv4InternalRoutesPrefixLenType
        if Ipv4InternalRoutesPrefixLenStart is not None:
            self._Ipv4InternalRoutesPrefixLenStart = Ipv4InternalRoutesPrefixLenStart
            properties['Ipv4InternalRoutesPrefixLenStart'] = Ipv4InternalRoutesPrefixLenStart
        if Ipv4InternalRoutesPrefixLenEnd is not None:
            self._Ipv4InternalRoutesPrefixLenEnd = Ipv4InternalRoutesPrefixLenEnd
            properties['Ipv4InternalRoutesPrefixLenEnd'] = Ipv4InternalRoutesPrefixLenEnd
        if Ipv4InternalNarrowMetric is not None:
            self._Ipv4InternalNarrowMetric = Ipv4InternalNarrowMetric
            properties['Ipv4InternalNarrowMetric'] = Ipv4InternalNarrowMetric
        if Ipv4InternalWideMetric is not None:
            self._Ipv4InternalWideMetric = Ipv4InternalWideMetric
            properties['Ipv4InternalWideMetric'] = Ipv4InternalWideMetric
        if Ipv4ExternalAdvEmulatedRouters is not None:
            self._Ipv4ExternalAdvEmulatedRouters = Ipv4ExternalAdvEmulatedRouters
            properties['Ipv4ExternalAdvEmulatedRouters'] = Ipv4ExternalAdvEmulatedRouters
        if Ipv4ExternalAdvSimulatedRouter is not None:
            self._Ipv4ExternalAdvSimulatedRouter = Ipv4ExternalAdvSimulatedRouter
            properties['Ipv4ExternalAdvSimulatedRouter'] = Ipv4ExternalAdvSimulatedRouter
        if Ipv4ExternalTotalNumberOfRoutes is not None:
            self._Ipv4ExternalTotalNumberOfRoutes = Ipv4ExternalTotalNumberOfRoutes
            properties['Ipv4ExternalTotalNumberOfRoutes'] = Ipv4ExternalTotalNumberOfRoutes
        if Ipv4ExternalRoutesOverride is not None:
            self._Ipv4ExternalRoutesOverride = Ipv4ExternalRoutesOverride
            properties['Ipv4ExternalRoutesOverride'] = Ipv4ExternalRoutesOverride
        if Ipv4ExternalStartRoutesPrefix is not None:
            self._Ipv4ExternalStartRoutesPrefix = Ipv4ExternalStartRoutesPrefix
            properties['Ipv4ExternalStartRoutesPrefix'] = Ipv4ExternalStartRoutesPrefix
        if Ipv4ExternalEndRoutesPrefix is not None:
            self._Ipv4ExternalEndRoutesPrefix = Ipv4ExternalEndRoutesPrefix
            properties['Ipv4ExternalEndRoutesPrefix'] = Ipv4ExternalEndRoutesPrefix
        if Ipv4ExternalRoutesNoneSeq is not None:
            self._Ipv4ExternalRoutesNoneSeq = Ipv4ExternalRoutesNoneSeq
            properties['Ipv4ExternalRoutesNoneSeq'] = Ipv4ExternalRoutesNoneSeq
        if Ipv4ExternalRoutesPrefixLenType is not None:
            self._Ipv4ExternalRoutesPrefixLenType = Ipv4ExternalRoutesPrefixLenType
            properties['Ipv4ExternalRoutesPrefixLenType'] = Ipv4ExternalRoutesPrefixLenType
        if Ipv4ExternalRoutesPrefixLenStart is not None:
            self._Ipv4ExternalRoutesPrefixLenStart = Ipv4ExternalRoutesPrefixLenStart
            properties['Ipv4ExternalRoutesPrefixLenStart'] = Ipv4ExternalRoutesPrefixLenStart
        if Ipv4ExternalRoutesPrefixLenEnd is not None:
            self._Ipv4ExternalRoutesPrefixLenEnd = Ipv4ExternalRoutesPrefixLenEnd
            properties['Ipv4ExternalRoutesPrefixLenEnd'] = Ipv4ExternalRoutesPrefixLenEnd
        if Ipv4ExternalNarrowMetric is not None:
            self._Ipv4ExternalNarrowMetric = Ipv4ExternalNarrowMetric
            properties['Ipv4ExternalNarrowMetric'] = Ipv4ExternalNarrowMetric
        if Ipv4ExternalWideMetric is not None:
            self._Ipv4ExternalWideMetric = Ipv4ExternalWideMetric
            properties['Ipv4ExternalWideMetric'] = Ipv4ExternalWideMetric
        if Ipv6InternalAdvEmulatedRouters is not None:
            self._Ipv6InternalAdvEmulatedRouters = Ipv6InternalAdvEmulatedRouters
            properties['Ipv6InternalAdvEmulatedRouters'] = Ipv6InternalAdvEmulatedRouters
        if Ipv6InternalAdvSimulatedRouter is not None:
            self._Ipv6InternalAdvSimulatedRouter = Ipv6InternalAdvSimulatedRouter
            properties['Ipv6InternalAdvSimulatedRouter'] = Ipv6InternalAdvSimulatedRouter
        if Ipv6InternalTotalNumberOfRoutes is not None:
            self._Ipv6InternalTotalNumberOfRoutes = Ipv6InternalTotalNumberOfRoutes
            properties['Ipv6InternalTotalNumberOfRoutes'] = Ipv6InternalTotalNumberOfRoutes
        if Ipv6InternalRoutesOverride is not None:
            self._Ipv6InternalRoutesOverride = Ipv6InternalRoutesOverride
            properties['Ipv6InternalRoutesOverride'] = Ipv6InternalRoutesOverride
        if Ipv6InternalStartRoutesPrefix is not None:
            self._Ipv6InternalStartRoutesPrefix = Ipv6InternalStartRoutesPrefix
            properties['Ipv6InternalStartRoutesPrefix'] = Ipv6InternalStartRoutesPrefix
        if Ipv6InternalEndRoutesPrefix is not None:
            self._Ipv6InternalEndRoutesPrefix = Ipv6InternalEndRoutesPrefix
            properties['Ipv6InternalEndRoutesPrefix'] = Ipv6InternalEndRoutesPrefix
        if Ipv6InternalRoutesNoneSeq is not None:
            self._Ipv6InternalRoutesNoneSeq = Ipv6InternalRoutesNoneSeq
            properties['Ipv6InternalRoutesNoneSeq'] = Ipv6InternalRoutesNoneSeq
        if Ipv6InternalRoutesPrefixLenType is not None:
            self._Ipv6InternalRoutesPrefixLenType = Ipv6InternalRoutesPrefixLenType
            properties['Ipv6InternalRoutesPrefixLenType'] = Ipv6InternalRoutesPrefixLenType
        if Ipv6InternalRoutesPrefixLenStart is not None:
            self._Ipv6InternalRoutesPrefixLenStart = Ipv6InternalRoutesPrefixLenStart
            properties['Ipv6InternalRoutesPrefixLenStart'] = Ipv6InternalRoutesPrefixLenStart
        if Ipv6InternalRoutesPrefixLenEnd is not None:
            self._Ipv6InternalRoutesPrefixLenEnd = Ipv6InternalRoutesPrefixLenEnd
            properties['Ipv6InternalRoutesPrefixLenEnd'] = Ipv6InternalRoutesPrefixLenEnd
        if Ipv6InternalWideMetric is not None:
            self._Ipv6InternalWideMetric = Ipv6InternalWideMetric
            properties['Ipv6InternalWideMetric'] = Ipv6InternalWideMetric
        if Ipv6ExternalAdvEmulatedRouters is not None:
            self._Ipv6ExternalAdvEmulatedRouters = Ipv6ExternalAdvEmulatedRouters
            properties['Ipv6ExternalAdvEmulatedRouters'] = Ipv6ExternalAdvEmulatedRouters
        if Ipv6ExternalAdvSimulatedRouter is not None:
            self._Ipv6ExternalAdvSimulatedRouter = Ipv6ExternalAdvSimulatedRouter
            properties['Ipv6ExternalAdvSimulatedRouter'] = Ipv6ExternalAdvSimulatedRouter
        if Ipv6ExternalTotalNumberOfRoutes is not None:
            self._Ipv6ExternalTotalNumberOfRoutes = Ipv6ExternalTotalNumberOfRoutes
            properties['Ipv6ExternalTotalNumberOfRoutes'] = Ipv6ExternalTotalNumberOfRoutes
        if Ipv6ExternalRoutesOverride is not None:
            self._Ipv6ExternalRoutesOverride = Ipv6ExternalRoutesOverride
            properties['Ipv6ExternalRoutesOverride'] = Ipv6ExternalRoutesOverride
        if Ipv6ExternalStartRoutesPrefix is not None:
            self._Ipv6ExternalStartRoutesPrefix = Ipv6ExternalStartRoutesPrefix
            properties['Ipv6ExternalStartRoutesPrefix'] = Ipv6ExternalStartRoutesPrefix
        if Ipv6ExternalEndRoutesPrefix is not None:
            self._Ipv6ExternalEndRoutesPrefix = Ipv6ExternalEndRoutesPrefix
            properties['Ipv6ExternalEndRoutesPrefix'] = Ipv6ExternalEndRoutesPrefix
        if Ipv6ExternalRoutesNoneSeq is not None:
            self._Ipv6ExternalRoutesNoneSeq = Ipv6ExternalRoutesNoneSeq
            properties['Ipv6ExternalRoutesNoneSeq'] = Ipv6ExternalRoutesNoneSeq
        if Ipv6ExternalRoutesPrefixLenType is not None:
            self._Ipv6ExternalRoutesPrefixLenType = Ipv6ExternalRoutesPrefixLenType
            properties['Ipv6ExternalRoutesPrefixLenType'] = Ipv6ExternalRoutesPrefixLenType
        if Ipv6ExternalRoutesPrefixLenStart is not None:
            self._Ipv6ExternalRoutesPrefixLenStart = Ipv6ExternalRoutesPrefixLenStart
            properties['Ipv6ExternalRoutesPrefixLenStart'] = Ipv6ExternalRoutesPrefixLenStart
        if Ipv6ExternalRoutesPrefixLenEnd is not None:
            self._Ipv6ExternalRoutesPrefixLenEnd = Ipv6ExternalRoutesPrefixLenEnd
            properties['Ipv6ExternalRoutesPrefixLenEnd'] = Ipv6ExternalRoutesPrefixLenEnd
        if Ipv6ExternalWideMetric is not None:
            self._Ipv6ExternalWideMetric = Ipv6ExternalWideMetric
            properties['Ipv6ExternalWideMetric'] = Ipv6ExternalWideMetric

        super(IsisLspWizardConfig, self).edit(**properties)

    @property
    def CreateLspLevel(self):
        """
        get the value of property _CreateLspLevel
        """
        if self.force_auto_sync:
            self.get('CreateLspLevel')
        return self._CreateLspLevel

    @property
    def TopologyType(self):
        """
        get the value of property _TopologyType
        """
        if self.force_auto_sync:
            self.get('TopologyType')
        return self._TopologyType

    @property
    def TreeSimulatedRoutersCount(self):
        """
        get the value of property _TreeSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('TreeSimulatedRoutersCount')
        return self._TreeSimulatedRoutersCount

    @property
    def TreeInterfaceType(self):
        """
        get the value of property _TreeInterfaceType
        """
        if self.force_auto_sync:
            self.get('TreeInterfaceType')
        return self._TreeInterfaceType

    @property
    def TreeMaxInterfacesPerRouter(self):
        """
        get the value of property _TreeMaxInterfacesPerRouter
        """
        if self.force_auto_sync:
            self.get('TreeMaxInterfacesPerRouter')
        return self._TreeMaxInterfacesPerRouter

    @property
    def TreeMaxRoutersPerTransitNetwork(self):
        """
        get the value of property _TreeMaxRoutersPerTransitNetwork
        """
        if self.force_auto_sync:
            self.get('TreeMaxRoutersPerTransitNetwork')
        return self._TreeMaxRoutersPerTransitNetwork

    @property
    def GridSimulatedRoutersCount(self):
        """
        get the value of property _GridSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('GridSimulatedRoutersCount')
        return self._GridSimulatedRoutersCount

    @property
    def GridSimulatedRoutersPerEmulatedRouter(self):
        """
        get the value of property _GridSimulatedRoutersPerEmulatedRouter
        """
        if self.force_auto_sync:
            self.get('GridSimulatedRoutersPerEmulatedRouter')
        return self._GridSimulatedRoutersPerEmulatedRouter

    @property
    def GridNumberOfRows(self):
        """
        get the value of property _GridNumberOfRows
        """
        if self.force_auto_sync:
            self.get('GridNumberOfRows')
        return self._GridNumberOfRows

    @property
    def GridNumberOfColumns(self):
        """
        get the value of property _GridNumberOfColumns
        """
        if self.force_auto_sync:
            self.get('GridNumberOfColumns')
        return self._GridNumberOfColumns

    @property
    def GridEmulatedRouterPosition(self):
        """
        get the value of property _GridEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('GridEmulatedRouterPosition')
        return self._GridEmulatedRouterPosition

    @property
    def GridEmulatedRouterRowIndex(self):
        """
        get the value of property _GridEmulatedRouterRowIndex
        """
        if self.force_auto_sync:
            self.get('GridEmulatedRouterRowIndex')
        return self._GridEmulatedRouterRowIndex

    @property
    def GridEmulatedRouterColumnIndex(self):
        """
        get the value of property _GridEmulatedRouterColumnIndex
        """
        if self.force_auto_sync:
            self.get('GridEmulatedRouterColumnIndex')
        return self._GridEmulatedRouterColumnIndex

    @property
    def MeshSimulatedRoutersCount(self):
        """
        get the value of property _MeshSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('MeshSimulatedRoutersCount')
        return self._MeshSimulatedRoutersCount

    @property
    def MeshSimulatedRoutersPerEmulatedRouter(self):
        """
        get the value of property _MeshSimulatedRoutersPerEmulatedRouter
        """
        if self.force_auto_sync:
            self.get('MeshSimulatedRoutersPerEmulatedRouter')
        return self._MeshSimulatedRoutersPerEmulatedRouter

    @property
    def MeshNumberOfRouters(self):
        """
        get the value of property _MeshNumberOfRouters
        """
        if self.force_auto_sync:
            self.get('MeshNumberOfRouters')
        return self._MeshNumberOfRouters

    @property
    def MeshEmulatedRouterPosition(self):
        """
        get the value of property _MeshEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('MeshEmulatedRouterPosition')
        return self._MeshEmulatedRouterPosition

    @property
    def RingSimulatedRoutersCount(self):
        """
        get the value of property _RingSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('RingSimulatedRoutersCount')
        return self._RingSimulatedRoutersCount

    @property
    def RingSimulatedRoutersPerEmulatedRouter(self):
        """
        get the value of property _RingSimulatedRoutersPerEmulatedRouter
        """
        if self.force_auto_sync:
            self.get('RingSimulatedRoutersPerEmulatedRouter')
        return self._RingSimulatedRoutersPerEmulatedRouter

    @property
    def RingNumberOfRouters(self):
        """
        get the value of property _RingNumberOfRouters
        """
        if self.force_auto_sync:
            self.get('RingNumberOfRouters')
        return self._RingNumberOfRouters

    @property
    def RingEmulatedRouterPosition(self):
        """
        get the value of property _RingEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('RingEmulatedRouterPosition')
        return self._RingEmulatedRouterPosition

    @property
    def HubSimulatedRoutersCount(self):
        """
        get the value of property _HubSimulatedRoutersCount
        """
        if self.force_auto_sync:
            self.get('HubSimulatedRoutersCount')
        return self._HubSimulatedRoutersCount

    @property
    def HubSimulatedRoutersPerEmulatedRouter(self):
        """
        get the value of property _HubSimulatedRoutersPerEmulatedRouter
        """
        if self.force_auto_sync:
            self.get('HubSimulatedRoutersPerEmulatedRouter')
        return self._HubSimulatedRoutersPerEmulatedRouter

    @property
    def HubNumberOfRouters(self):
        """
        get the value of property _HubNumberOfRouters
        """
        if self.force_auto_sync:
            self.get('HubNumberOfRouters')
        return self._HubNumberOfRouters

    @property
    def HubEmulatedRouterPosition(self):
        """
        get the value of property _HubEmulatedRouterPosition
        """
        if self.force_auto_sync:
            self.get('HubEmulatedRouterPosition')
        return self._HubEmulatedRouterPosition

    @property
    def InterfaceStartIpv4Prefix(self):
        """
        get the value of property _InterfaceStartIpv4Prefix
        """
        if self.force_auto_sync:
            self.get('InterfaceStartIpv4Prefix')
        return self._InterfaceStartIpv4Prefix

    @property
    def InterfaceEndIpv4Prefix(self):
        """
        get the value of property _InterfaceEndIpv4Prefix
        """
        if self.force_auto_sync:
            self.get('InterfaceEndIpv4Prefix')
        return self._InterfaceEndIpv4Prefix

    @property
    def InterfaceStartIpv6Prefix(self):
        """
        get the value of property _InterfaceStartIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('InterfaceStartIpv6Prefix')
        return self._InterfaceStartIpv6Prefix

    @property
    def InterfaceEndIpv6Prefix(self):
        """
        get the value of property _InterfaceEndIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('InterfaceEndIpv6Prefix')
        return self._InterfaceEndIpv6Prefix

    @property
    def AdvertiseLoopbackAddress(self):
        """
        get the value of property _AdvertiseLoopbackAddress
        """
        if self.force_auto_sync:
            self.get('AdvertiseLoopbackAddress')
        return self._AdvertiseLoopbackAddress

    @property
    def EnableTrafficEngine(self):
        """
        get the value of property _EnableTrafficEngine
        """
        if self.force_auto_sync:
            self.get('EnableTrafficEngine')
        return self._EnableTrafficEngine

    @property
    def StartSystemId(self):
        """
        get the value of property _StartSystemId
        """
        if self.force_auto_sync:
            self.get('StartSystemId')
        return self._StartSystemId

    @property
    def SystemIdStep(self):
        """
        get the value of property _SystemIdStep
        """
        if self.force_auto_sync:
            self.get('SystemIdStep')
        return self._SystemIdStep

    @property
    def StartRouterId(self):
        """
        get the value of property _StartRouterId
        """
        if self.force_auto_sync:
            self.get('StartRouterId')
        return self._StartRouterId

    @property
    def RouterIdStep(self):
        """
        get the value of property _RouterIdStep
        """
        if self.force_auto_sync:
            self.get('RouterIdStep')
        return self._RouterIdStep

    @property
    def Ipv4InternalAdvEmulatedRouters(self):
        """
        get the value of property _Ipv4InternalAdvEmulatedRouters
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalAdvEmulatedRouters')
        return self._Ipv4InternalAdvEmulatedRouters

    @property
    def Ipv4InternalAdvSimulatedRouter(self):
        """
        get the value of property _Ipv4InternalAdvSimulatedRouter
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalAdvSimulatedRouter')
        return self._Ipv4InternalAdvSimulatedRouter

    @property
    def Ipv4InternalTotalNumberOfRoutes(self):
        """
        get the value of property _Ipv4InternalTotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalTotalNumberOfRoutes')
        return self._Ipv4InternalTotalNumberOfRoutes

    @property
    def Ipv4InternalRoutesOverride(self):
        """
        get the value of property _Ipv4InternalRoutesOverride
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalRoutesOverride')
        return self._Ipv4InternalRoutesOverride

    @property
    def Ipv4InternalStartRoutesPrefix(self):
        """
        get the value of property _Ipv4InternalStartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalStartRoutesPrefix')
        return self._Ipv4InternalStartRoutesPrefix

    @property
    def Ipv4InternalEndRoutesPrefix(self):
        """
        get the value of property _Ipv4InternalEndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalEndRoutesPrefix')
        return self._Ipv4InternalEndRoutesPrefix

    @property
    def Ipv4InternalRoutesNoneSeq(self):
        """
        get the value of property _Ipv4InternalRoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalRoutesNoneSeq')
        return self._Ipv4InternalRoutesNoneSeq

    @property
    def Ipv4InternalRoutesPrefixLenType(self):
        """
        get the value of property _Ipv4InternalRoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalRoutesPrefixLenType')
        return self._Ipv4InternalRoutesPrefixLenType

    @property
    def Ipv4InternalRoutesPrefixLenStart(self):
        """
        get the value of property _Ipv4InternalRoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalRoutesPrefixLenStart')
        return self._Ipv4InternalRoutesPrefixLenStart

    @property
    def Ipv4InternalRoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv4InternalRoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalRoutesPrefixLenEnd')
        return self._Ipv4InternalRoutesPrefixLenEnd

    @property
    def Ipv4InternalNarrowMetric(self):
        """
        get the value of property _Ipv4InternalNarrowMetric
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalNarrowMetric')
        return self._Ipv4InternalNarrowMetric

    @property
    def Ipv4InternalWideMetric(self):
        """
        get the value of property _Ipv4InternalWideMetric
        """
        if self.force_auto_sync:
            self.get('Ipv4InternalWideMetric')
        return self._Ipv4InternalWideMetric

    @property
    def Ipv4ExternalAdvEmulatedRouters(self):
        """
        get the value of property _Ipv4ExternalAdvEmulatedRouters
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalAdvEmulatedRouters')
        return self._Ipv4ExternalAdvEmulatedRouters

    @property
    def Ipv4ExternalAdvSimulatedRouter(self):
        """
        get the value of property _Ipv4ExternalAdvSimulatedRouter
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalAdvSimulatedRouter')
        return self._Ipv4ExternalAdvSimulatedRouter

    @property
    def Ipv4ExternalTotalNumberOfRoutes(self):
        """
        get the value of property _Ipv4ExternalTotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalTotalNumberOfRoutes')
        return self._Ipv4ExternalTotalNumberOfRoutes

    @property
    def Ipv4ExternalRoutesOverride(self):
        """
        get the value of property _Ipv4ExternalRoutesOverride
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalRoutesOverride')
        return self._Ipv4ExternalRoutesOverride

    @property
    def Ipv4ExternalStartRoutesPrefix(self):
        """
        get the value of property _Ipv4ExternalStartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalStartRoutesPrefix')
        return self._Ipv4ExternalStartRoutesPrefix

    @property
    def Ipv4ExternalEndRoutesPrefix(self):
        """
        get the value of property _Ipv4ExternalEndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalEndRoutesPrefix')
        return self._Ipv4ExternalEndRoutesPrefix

    @property
    def Ipv4ExternalRoutesNoneSeq(self):
        """
        get the value of property _Ipv4ExternalRoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalRoutesNoneSeq')
        return self._Ipv4ExternalRoutesNoneSeq

    @property
    def Ipv4ExternalRoutesPrefixLenType(self):
        """
        get the value of property _Ipv4ExternalRoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalRoutesPrefixLenType')
        return self._Ipv4ExternalRoutesPrefixLenType

    @property
    def Ipv4ExternalRoutesPrefixLenStart(self):
        """
        get the value of property _Ipv4ExternalRoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalRoutesPrefixLenStart')
        return self._Ipv4ExternalRoutesPrefixLenStart

    @property
    def Ipv4ExternalRoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv4ExternalRoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalRoutesPrefixLenEnd')
        return self._Ipv4ExternalRoutesPrefixLenEnd

    @property
    def Ipv4ExternalNarrowMetric(self):
        """
        get the value of property _Ipv4ExternalNarrowMetric
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalNarrowMetric')
        return self._Ipv4ExternalNarrowMetric

    @property
    def Ipv4ExternalWideMetric(self):
        """
        get the value of property _Ipv4ExternalWideMetric
        """
        if self.force_auto_sync:
            self.get('Ipv4ExternalWideMetric')
        return self._Ipv4ExternalWideMetric

    @property
    def Ipv6InternalAdvEmulatedRouters(self):
        """
        get the value of property _Ipv6InternalAdvEmulatedRouters
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalAdvEmulatedRouters')
        return self._Ipv6InternalAdvEmulatedRouters

    @property
    def Ipv6InternalAdvSimulatedRouter(self):
        """
        get the value of property _Ipv6InternalAdvSimulatedRouter
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalAdvSimulatedRouter')
        return self._Ipv6InternalAdvSimulatedRouter

    @property
    def Ipv6InternalTotalNumberOfRoutes(self):
        """
        get the value of property _Ipv6InternalTotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalTotalNumberOfRoutes')
        return self._Ipv6InternalTotalNumberOfRoutes

    @property
    def Ipv6InternalRoutesOverride(self):
        """
        get the value of property _Ipv6InternalRoutesOverride
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalRoutesOverride')
        return self._Ipv6InternalRoutesOverride

    @property
    def Ipv6InternalStartRoutesPrefix(self):
        """
        get the value of property _Ipv6InternalStartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalStartRoutesPrefix')
        return self._Ipv6InternalStartRoutesPrefix

    @property
    def Ipv6InternalEndRoutesPrefix(self):
        """
        get the value of property _Ipv6InternalEndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalEndRoutesPrefix')
        return self._Ipv6InternalEndRoutesPrefix

    @property
    def Ipv6InternalRoutesNoneSeq(self):
        """
        get the value of property _Ipv6InternalRoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalRoutesNoneSeq')
        return self._Ipv6InternalRoutesNoneSeq

    @property
    def Ipv6InternalRoutesPrefixLenType(self):
        """
        get the value of property _Ipv6InternalRoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalRoutesPrefixLenType')
        return self._Ipv6InternalRoutesPrefixLenType

    @property
    def Ipv6InternalRoutesPrefixLenStart(self):
        """
        get the value of property _Ipv6InternalRoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalRoutesPrefixLenStart')
        return self._Ipv6InternalRoutesPrefixLenStart

    @property
    def Ipv6InternalRoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv6InternalRoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalRoutesPrefixLenEnd')
        return self._Ipv6InternalRoutesPrefixLenEnd

    @property
    def Ipv6InternalWideMetric(self):
        """
        get the value of property _Ipv6InternalWideMetric
        """
        if self.force_auto_sync:
            self.get('Ipv6InternalWideMetric')
        return self._Ipv6InternalWideMetric

    @property
    def Ipv6ExternalAdvEmulatedRouters(self):
        """
        get the value of property _Ipv6ExternalAdvEmulatedRouters
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalAdvEmulatedRouters')
        return self._Ipv6ExternalAdvEmulatedRouters

    @property
    def Ipv6ExternalAdvSimulatedRouter(self):
        """
        get the value of property _Ipv6ExternalAdvSimulatedRouter
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalAdvSimulatedRouter')
        return self._Ipv6ExternalAdvSimulatedRouter

    @property
    def Ipv6ExternalTotalNumberOfRoutes(self):
        """
        get the value of property _Ipv6ExternalTotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalTotalNumberOfRoutes')
        return self._Ipv6ExternalTotalNumberOfRoutes

    @property
    def Ipv6ExternalRoutesOverride(self):
        """
        get the value of property _Ipv6ExternalRoutesOverride
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalRoutesOverride')
        return self._Ipv6ExternalRoutesOverride

    @property
    def Ipv6ExternalStartRoutesPrefix(self):
        """
        get the value of property _Ipv6ExternalStartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalStartRoutesPrefix')
        return self._Ipv6ExternalStartRoutesPrefix

    @property
    def Ipv6ExternalEndRoutesPrefix(self):
        """
        get the value of property _Ipv6ExternalEndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalEndRoutesPrefix')
        return self._Ipv6ExternalEndRoutesPrefix

    @property
    def Ipv6ExternalRoutesNoneSeq(self):
        """
        get the value of property _Ipv6ExternalRoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalRoutesNoneSeq')
        return self._Ipv6ExternalRoutesNoneSeq

    @property
    def Ipv6ExternalRoutesPrefixLenType(self):
        """
        get the value of property _Ipv6ExternalRoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalRoutesPrefixLenType')
        return self._Ipv6ExternalRoutesPrefixLenType

    @property
    def Ipv6ExternalRoutesPrefixLenStart(self):
        """
        get the value of property _Ipv6ExternalRoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalRoutesPrefixLenStart')
        return self._Ipv6ExternalRoutesPrefixLenStart

    @property
    def Ipv6ExternalRoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv6ExternalRoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalRoutesPrefixLenEnd')
        return self._Ipv6ExternalRoutesPrefixLenEnd

    @property
    def Ipv6ExternalWideMetric(self):
        """
        get the value of property _Ipv6ExternalWideMetric
        """
        if self.force_auto_sync:
            self.get('Ipv6ExternalWideMetric')
        return self._Ipv6ExternalWideMetric

    @CreateLspLevel.setter
    def CreateLspLevel(self, value):
        self._CreateLspLevel = value
        self.edit(CreateLspLevel=value)

    @TopologyType.setter
    def TopologyType(self, value):
        self._TopologyType = value
        self.edit(TopologyType=value)

    @TreeSimulatedRoutersCount.setter
    def TreeSimulatedRoutersCount(self, value):
        self._TreeSimulatedRoutersCount = value
        self.edit(TreeSimulatedRoutersCount=value)

    @TreeInterfaceType.setter
    def TreeInterfaceType(self, value):
        self._TreeInterfaceType = value
        self.edit(TreeInterfaceType=value)

    @TreeMaxInterfacesPerRouter.setter
    def TreeMaxInterfacesPerRouter(self, value):
        self._TreeMaxInterfacesPerRouter = value
        self.edit(TreeMaxInterfacesPerRouter=value)

    @TreeMaxRoutersPerTransitNetwork.setter
    def TreeMaxRoutersPerTransitNetwork(self, value):
        self._TreeMaxRoutersPerTransitNetwork = value
        self.edit(TreeMaxRoutersPerTransitNetwork=value)

    @GridSimulatedRoutersCount.setter
    def GridSimulatedRoutersCount(self, value):
        self._GridSimulatedRoutersCount = value
        self.edit(GridSimulatedRoutersCount=value)

    @GridSimulatedRoutersPerEmulatedRouter.setter
    def GridSimulatedRoutersPerEmulatedRouter(self, value):
        self._GridSimulatedRoutersPerEmulatedRouter = value
        self.edit(GridSimulatedRoutersPerEmulatedRouter=value)

    @GridNumberOfRows.setter
    def GridNumberOfRows(self, value):
        self._GridNumberOfRows = value
        self.edit(GridNumberOfRows=value)

    @GridNumberOfColumns.setter
    def GridNumberOfColumns(self, value):
        self._GridNumberOfColumns = value
        self.edit(GridNumberOfColumns=value)

    @GridEmulatedRouterPosition.setter
    def GridEmulatedRouterPosition(self, value):
        self._GridEmulatedRouterPosition = value
        self.edit(GridEmulatedRouterPosition=value)

    @GridEmulatedRouterRowIndex.setter
    def GridEmulatedRouterRowIndex(self, value):
        self._GridEmulatedRouterRowIndex = value
        self.edit(GridEmulatedRouterRowIndex=value)

    @GridEmulatedRouterColumnIndex.setter
    def GridEmulatedRouterColumnIndex(self, value):
        self._GridEmulatedRouterColumnIndex = value
        self.edit(GridEmulatedRouterColumnIndex=value)

    @MeshSimulatedRoutersCount.setter
    def MeshSimulatedRoutersCount(self, value):
        self._MeshSimulatedRoutersCount = value
        self.edit(MeshSimulatedRoutersCount=value)

    @MeshSimulatedRoutersPerEmulatedRouter.setter
    def MeshSimulatedRoutersPerEmulatedRouter(self, value):
        self._MeshSimulatedRoutersPerEmulatedRouter = value
        self.edit(MeshSimulatedRoutersPerEmulatedRouter=value)

    @MeshNumberOfRouters.setter
    def MeshNumberOfRouters(self, value):
        self._MeshNumberOfRouters = value
        self.edit(MeshNumberOfRouters=value)

    @MeshEmulatedRouterPosition.setter
    def MeshEmulatedRouterPosition(self, value):
        self._MeshEmulatedRouterPosition = value
        self.edit(MeshEmulatedRouterPosition=value)

    @RingSimulatedRoutersCount.setter
    def RingSimulatedRoutersCount(self, value):
        self._RingSimulatedRoutersCount = value
        self.edit(RingSimulatedRoutersCount=value)

    @RingSimulatedRoutersPerEmulatedRouter.setter
    def RingSimulatedRoutersPerEmulatedRouter(self, value):
        self._RingSimulatedRoutersPerEmulatedRouter = value
        self.edit(RingSimulatedRoutersPerEmulatedRouter=value)

    @RingNumberOfRouters.setter
    def RingNumberOfRouters(self, value):
        self._RingNumberOfRouters = value
        self.edit(RingNumberOfRouters=value)

    @RingEmulatedRouterPosition.setter
    def RingEmulatedRouterPosition(self, value):
        self._RingEmulatedRouterPosition = value
        self.edit(RingEmulatedRouterPosition=value)

    @HubSimulatedRoutersCount.setter
    def HubSimulatedRoutersCount(self, value):
        self._HubSimulatedRoutersCount = value
        self.edit(HubSimulatedRoutersCount=value)

    @HubSimulatedRoutersPerEmulatedRouter.setter
    def HubSimulatedRoutersPerEmulatedRouter(self, value):
        self._HubSimulatedRoutersPerEmulatedRouter = value
        self.edit(HubSimulatedRoutersPerEmulatedRouter=value)

    @HubNumberOfRouters.setter
    def HubNumberOfRouters(self, value):
        self._HubNumberOfRouters = value
        self.edit(HubNumberOfRouters=value)

    @HubEmulatedRouterPosition.setter
    def HubEmulatedRouterPosition(self, value):
        self._HubEmulatedRouterPosition = value
        self.edit(HubEmulatedRouterPosition=value)

    @InterfaceStartIpv4Prefix.setter
    def InterfaceStartIpv4Prefix(self, value):
        self._InterfaceStartIpv4Prefix = value
        self.edit(InterfaceStartIpv4Prefix=value)

    @InterfaceEndIpv4Prefix.setter
    def InterfaceEndIpv4Prefix(self, value):
        self._InterfaceEndIpv4Prefix = value
        self.edit(InterfaceEndIpv4Prefix=value)

    @InterfaceStartIpv6Prefix.setter
    def InterfaceStartIpv6Prefix(self, value):
        self._InterfaceStartIpv6Prefix = value
        self.edit(InterfaceStartIpv6Prefix=value)

    @InterfaceEndIpv6Prefix.setter
    def InterfaceEndIpv6Prefix(self, value):
        self._InterfaceEndIpv6Prefix = value
        self.edit(InterfaceEndIpv6Prefix=value)

    @AdvertiseLoopbackAddress.setter
    def AdvertiseLoopbackAddress(self, value):
        self._AdvertiseLoopbackAddress = value
        self.edit(AdvertiseLoopbackAddress=value)

    @EnableTrafficEngine.setter
    def EnableTrafficEngine(self, value):
        self._EnableTrafficEngine = value
        self.edit(EnableTrafficEngine=value)

    @StartSystemId.setter
    def StartSystemId(self, value):
        self._StartSystemId = value
        self.edit(StartSystemId=value)

    @SystemIdStep.setter
    def SystemIdStep(self, value):
        self._SystemIdStep = value
        self.edit(SystemIdStep=value)

    @StartRouterId.setter
    def StartRouterId(self, value):
        self._StartRouterId = value
        self.edit(StartRouterId=value)

    @RouterIdStep.setter
    def RouterIdStep(self, value):
        self._RouterIdStep = value
        self.edit(RouterIdStep=value)

    @Ipv4InternalAdvEmulatedRouters.setter
    def Ipv4InternalAdvEmulatedRouters(self, value):
        self._Ipv4InternalAdvEmulatedRouters = value
        self.edit(Ipv4InternalAdvEmulatedRouters=value)

    @Ipv4InternalAdvSimulatedRouter.setter
    def Ipv4InternalAdvSimulatedRouter(self, value):
        self._Ipv4InternalAdvSimulatedRouter = value
        self.edit(Ipv4InternalAdvSimulatedRouter=value)

    @Ipv4InternalTotalNumberOfRoutes.setter
    def Ipv4InternalTotalNumberOfRoutes(self, value):
        self._Ipv4InternalTotalNumberOfRoutes = value
        self.edit(Ipv4InternalTotalNumberOfRoutes=value)

    @Ipv4InternalRoutesOverride.setter
    def Ipv4InternalRoutesOverride(self, value):
        self._Ipv4InternalRoutesOverride = value
        self.edit(Ipv4InternalRoutesOverride=value)

    @Ipv4InternalStartRoutesPrefix.setter
    def Ipv4InternalStartRoutesPrefix(self, value):
        self._Ipv4InternalStartRoutesPrefix = value
        self.edit(Ipv4InternalStartRoutesPrefix=value)

    @Ipv4InternalEndRoutesPrefix.setter
    def Ipv4InternalEndRoutesPrefix(self, value):
        self._Ipv4InternalEndRoutesPrefix = value
        self.edit(Ipv4InternalEndRoutesPrefix=value)

    @Ipv4InternalRoutesNoneSeq.setter
    def Ipv4InternalRoutesNoneSeq(self, value):
        self._Ipv4InternalRoutesNoneSeq = value
        self.edit(Ipv4InternalRoutesNoneSeq=value)

    @Ipv4InternalRoutesPrefixLenType.setter
    def Ipv4InternalRoutesPrefixLenType(self, value):
        self._Ipv4InternalRoutesPrefixLenType = value
        self.edit(Ipv4InternalRoutesPrefixLenType=value)

    @Ipv4InternalRoutesPrefixLenStart.setter
    def Ipv4InternalRoutesPrefixLenStart(self, value):
        self._Ipv4InternalRoutesPrefixLenStart = value
        self.edit(Ipv4InternalRoutesPrefixLenStart=value)

    @Ipv4InternalRoutesPrefixLenEnd.setter
    def Ipv4InternalRoutesPrefixLenEnd(self, value):
        self._Ipv4InternalRoutesPrefixLenEnd = value
        self.edit(Ipv4InternalRoutesPrefixLenEnd=value)

    @Ipv4InternalNarrowMetric.setter
    def Ipv4InternalNarrowMetric(self, value):
        self._Ipv4InternalNarrowMetric = value
        self.edit(Ipv4InternalNarrowMetric=value)

    @Ipv4InternalWideMetric.setter
    def Ipv4InternalWideMetric(self, value):
        self._Ipv4InternalWideMetric = value
        self.edit(Ipv4InternalWideMetric=value)

    @Ipv4ExternalAdvEmulatedRouters.setter
    def Ipv4ExternalAdvEmulatedRouters(self, value):
        self._Ipv4ExternalAdvEmulatedRouters = value
        self.edit(Ipv4ExternalAdvEmulatedRouters=value)

    @Ipv4ExternalAdvSimulatedRouter.setter
    def Ipv4ExternalAdvSimulatedRouter(self, value):
        self._Ipv4ExternalAdvSimulatedRouter = value
        self.edit(Ipv4ExternalAdvSimulatedRouter=value)

    @Ipv4ExternalTotalNumberOfRoutes.setter
    def Ipv4ExternalTotalNumberOfRoutes(self, value):
        self._Ipv4ExternalTotalNumberOfRoutes = value
        self.edit(Ipv4ExternalTotalNumberOfRoutes=value)

    @Ipv4ExternalRoutesOverride.setter
    def Ipv4ExternalRoutesOverride(self, value):
        self._Ipv4ExternalRoutesOverride = value
        self.edit(Ipv4ExternalRoutesOverride=value)

    @Ipv4ExternalStartRoutesPrefix.setter
    def Ipv4ExternalStartRoutesPrefix(self, value):
        self._Ipv4ExternalStartRoutesPrefix = value
        self.edit(Ipv4ExternalStartRoutesPrefix=value)

    @Ipv4ExternalEndRoutesPrefix.setter
    def Ipv4ExternalEndRoutesPrefix(self, value):
        self._Ipv4ExternalEndRoutesPrefix = value
        self.edit(Ipv4ExternalEndRoutesPrefix=value)

    @Ipv4ExternalRoutesNoneSeq.setter
    def Ipv4ExternalRoutesNoneSeq(self, value):
        self._Ipv4ExternalRoutesNoneSeq = value
        self.edit(Ipv4ExternalRoutesNoneSeq=value)

    @Ipv4ExternalRoutesPrefixLenType.setter
    def Ipv4ExternalRoutesPrefixLenType(self, value):
        self._Ipv4ExternalRoutesPrefixLenType = value
        self.edit(Ipv4ExternalRoutesPrefixLenType=value)

    @Ipv4ExternalRoutesPrefixLenStart.setter
    def Ipv4ExternalRoutesPrefixLenStart(self, value):
        self._Ipv4ExternalRoutesPrefixLenStart = value
        self.edit(Ipv4ExternalRoutesPrefixLenStart=value)

    @Ipv4ExternalRoutesPrefixLenEnd.setter
    def Ipv4ExternalRoutesPrefixLenEnd(self, value):
        self._Ipv4ExternalRoutesPrefixLenEnd = value
        self.edit(Ipv4ExternalRoutesPrefixLenEnd=value)

    @Ipv4ExternalNarrowMetric.setter
    def Ipv4ExternalNarrowMetric(self, value):
        self._Ipv4ExternalNarrowMetric = value
        self.edit(Ipv4ExternalNarrowMetric=value)

    @Ipv4ExternalWideMetric.setter
    def Ipv4ExternalWideMetric(self, value):
        self._Ipv4ExternalWideMetric = value
        self.edit(Ipv4ExternalWideMetric=value)

    @Ipv6InternalAdvEmulatedRouters.setter
    def Ipv6InternalAdvEmulatedRouters(self, value):
        self._Ipv6InternalAdvEmulatedRouters = value
        self.edit(Ipv6InternalAdvEmulatedRouters=value)

    @Ipv6InternalAdvSimulatedRouter.setter
    def Ipv6InternalAdvSimulatedRouter(self, value):
        self._Ipv6InternalAdvSimulatedRouter = value
        self.edit(Ipv6InternalAdvSimulatedRouter=value)

    @Ipv6InternalTotalNumberOfRoutes.setter
    def Ipv6InternalTotalNumberOfRoutes(self, value):
        self._Ipv6InternalTotalNumberOfRoutes = value
        self.edit(Ipv6InternalTotalNumberOfRoutes=value)

    @Ipv6InternalRoutesOverride.setter
    def Ipv6InternalRoutesOverride(self, value):
        self._Ipv6InternalRoutesOverride = value
        self.edit(Ipv6InternalRoutesOverride=value)

    @Ipv6InternalStartRoutesPrefix.setter
    def Ipv6InternalStartRoutesPrefix(self, value):
        self._Ipv6InternalStartRoutesPrefix = value
        self.edit(Ipv6InternalStartRoutesPrefix=value)

    @Ipv6InternalEndRoutesPrefix.setter
    def Ipv6InternalEndRoutesPrefix(self, value):
        self._Ipv6InternalEndRoutesPrefix = value
        self.edit(Ipv6InternalEndRoutesPrefix=value)

    @Ipv6InternalRoutesNoneSeq.setter
    def Ipv6InternalRoutesNoneSeq(self, value):
        self._Ipv6InternalRoutesNoneSeq = value
        self.edit(Ipv6InternalRoutesNoneSeq=value)

    @Ipv6InternalRoutesPrefixLenType.setter
    def Ipv6InternalRoutesPrefixLenType(self, value):
        self._Ipv6InternalRoutesPrefixLenType = value
        self.edit(Ipv6InternalRoutesPrefixLenType=value)

    @Ipv6InternalRoutesPrefixLenStart.setter
    def Ipv6InternalRoutesPrefixLenStart(self, value):
        self._Ipv6InternalRoutesPrefixLenStart = value
        self.edit(Ipv6InternalRoutesPrefixLenStart=value)

    @Ipv6InternalRoutesPrefixLenEnd.setter
    def Ipv6InternalRoutesPrefixLenEnd(self, value):
        self._Ipv6InternalRoutesPrefixLenEnd = value
        self.edit(Ipv6InternalRoutesPrefixLenEnd=value)

    @Ipv6InternalWideMetric.setter
    def Ipv6InternalWideMetric(self, value):
        self._Ipv6InternalWideMetric = value
        self.edit(Ipv6InternalWideMetric=value)

    @Ipv6ExternalAdvEmulatedRouters.setter
    def Ipv6ExternalAdvEmulatedRouters(self, value):
        self._Ipv6ExternalAdvEmulatedRouters = value
        self.edit(Ipv6ExternalAdvEmulatedRouters=value)

    @Ipv6ExternalAdvSimulatedRouter.setter
    def Ipv6ExternalAdvSimulatedRouter(self, value):
        self._Ipv6ExternalAdvSimulatedRouter = value
        self.edit(Ipv6ExternalAdvSimulatedRouter=value)

    @Ipv6ExternalTotalNumberOfRoutes.setter
    def Ipv6ExternalTotalNumberOfRoutes(self, value):
        self._Ipv6ExternalTotalNumberOfRoutes = value
        self.edit(Ipv6ExternalTotalNumberOfRoutes=value)

    @Ipv6ExternalRoutesOverride.setter
    def Ipv6ExternalRoutesOverride(self, value):
        self._Ipv6ExternalRoutesOverride = value
        self.edit(Ipv6ExternalRoutesOverride=value)

    @Ipv6ExternalStartRoutesPrefix.setter
    def Ipv6ExternalStartRoutesPrefix(self, value):
        self._Ipv6ExternalStartRoutesPrefix = value
        self.edit(Ipv6ExternalStartRoutesPrefix=value)

    @Ipv6ExternalEndRoutesPrefix.setter
    def Ipv6ExternalEndRoutesPrefix(self, value):
        self._Ipv6ExternalEndRoutesPrefix = value
        self.edit(Ipv6ExternalEndRoutesPrefix=value)

    @Ipv6ExternalRoutesNoneSeq.setter
    def Ipv6ExternalRoutesNoneSeq(self, value):
        self._Ipv6ExternalRoutesNoneSeq = value
        self.edit(Ipv6ExternalRoutesNoneSeq=value)

    @Ipv6ExternalRoutesPrefixLenType.setter
    def Ipv6ExternalRoutesPrefixLenType(self, value):
        self._Ipv6ExternalRoutesPrefixLenType = value
        self.edit(Ipv6ExternalRoutesPrefixLenType=value)

    @Ipv6ExternalRoutesPrefixLenStart.setter
    def Ipv6ExternalRoutesPrefixLenStart(self, value):
        self._Ipv6ExternalRoutesPrefixLenStart = value
        self.edit(Ipv6ExternalRoutesPrefixLenStart=value)

    @Ipv6ExternalRoutesPrefixLenEnd.setter
    def Ipv6ExternalRoutesPrefixLenEnd(self, value):
        self._Ipv6ExternalRoutesPrefixLenEnd = value
        self.edit(Ipv6ExternalRoutesPrefixLenEnd=value)

    @Ipv6ExternalWideMetric.setter
    def Ipv6ExternalWideMetric(self, value):
        self._Ipv6ExternalWideMetric = value
        self.edit(Ipv6ExternalWideMetric=value)

    def _set_createlsplevel_with_str(self, value):
        seperate = value.find(':')
        exec('self._CreateLspLevel = EnumCreateLspLevel.%s' % value[:seperate])

    def _set_topologytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TopologyType = EnumLspTopologyType.%s' % value[:seperate])

    def _set_treesimulatedrouterscount_with_str(self, value):
        try:
            self._TreeSimulatedRoutersCount = int(value)
        except ValueError:
            self._TreeSimulatedRoutersCount = hex(int(value, 16))

    def _set_treeinterfacetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TreeInterfaceType = EnumNetworkType.%s' % value[:seperate])

    def _set_treemaxinterfacesperrouter_with_str(self, value):
        try:
            self._TreeMaxInterfacesPerRouter = int(value)
        except ValueError:
            self._TreeMaxInterfacesPerRouter = hex(int(value, 16))

    def _set_treemaxrouterspertransitnetwork_with_str(self, value):
        try:
            self._TreeMaxRoutersPerTransitNetwork = int(value)
        except ValueError:
            self._TreeMaxRoutersPerTransitNetwork = hex(int(value, 16))

    def _set_gridsimulatedrouterscount_with_str(self, value):
        try:
            self._GridSimulatedRoutersCount = int(value)
        except ValueError:
            self._GridSimulatedRoutersCount = hex(int(value, 16))

    def _set_gridsimulatedroutersperemulatedrouter_with_str(self, value):
        try:
            self._GridSimulatedRoutersPerEmulatedRouter = int(value)
        except ValueError:
            self._GridSimulatedRoutersPerEmulatedRouter = hex(int(value, 16))

    def _set_gridnumberofrows_with_str(self, value):
        try:
            self._GridNumberOfRows = int(value)
        except ValueError:
            self._GridNumberOfRows = hex(int(value, 16))

    def _set_gridnumberofcolumns_with_str(self, value):
        try:
            self._GridNumberOfColumns = int(value)
        except ValueError:
            self._GridNumberOfColumns = hex(int(value, 16))

    def _set_gridemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._GridEmulatedRouterPosition = EnumTopologyRouterPosition.%s' % value[:seperate])

    def _set_gridemulatedrouterrowindex_with_str(self, value):
        try:
            self._GridEmulatedRouterRowIndex = int(value)
        except ValueError:
            self._GridEmulatedRouterRowIndex = hex(int(value, 16))

    def _set_gridemulatedroutercolumnindex_with_str(self, value):
        try:
            self._GridEmulatedRouterColumnIndex = int(value)
        except ValueError:
            self._GridEmulatedRouterColumnIndex = hex(int(value, 16))

    def _set_meshsimulatedrouterscount_with_str(self, value):
        try:
            self._MeshSimulatedRoutersCount = int(value)
        except ValueError:
            self._MeshSimulatedRoutersCount = hex(int(value, 16))

    def _set_meshsimulatedroutersperemulatedrouter_with_str(self, value):
        try:
            self._MeshSimulatedRoutersPerEmulatedRouter = int(value)
        except ValueError:
            self._MeshSimulatedRoutersPerEmulatedRouter = hex(int(value, 16))

    def _set_meshnumberofrouters_with_str(self, value):
        try:
            self._MeshNumberOfRouters = int(value)
        except ValueError:
            self._MeshNumberOfRouters = hex(int(value, 16))

    def _set_meshemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._MeshEmulatedRouterPosition = EnumTopologyRouterPosition.%s' % value[:seperate])

    def _set_ringsimulatedrouterscount_with_str(self, value):
        try:
            self._RingSimulatedRoutersCount = int(value)
        except ValueError:
            self._RingSimulatedRoutersCount = hex(int(value, 16))

    def _set_ringsimulatedroutersperemulatedrouter_with_str(self, value):
        try:
            self._RingSimulatedRoutersPerEmulatedRouter = int(value)
        except ValueError:
            self._RingSimulatedRoutersPerEmulatedRouter = hex(int(value, 16))

    def _set_ringnumberofrouters_with_str(self, value):
        try:
            self._RingNumberOfRouters = int(value)
        except ValueError:
            self._RingNumberOfRouters = hex(int(value, 16))

    def _set_ringemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._RingEmulatedRouterPosition = EnumTopologyRouterPosition.%s' % value[:seperate])

    def _set_hubsimulatedrouterscount_with_str(self, value):
        try:
            self._HubSimulatedRoutersCount = int(value)
        except ValueError:
            self._HubSimulatedRoutersCount = hex(int(value, 16))

    def _set_hubsimulatedroutersperemulatedrouter_with_str(self, value):
        try:
            self._HubSimulatedRoutersPerEmulatedRouter = int(value)
        except ValueError:
            self._HubSimulatedRoutersPerEmulatedRouter = hex(int(value, 16))

    def _set_hubnumberofrouters_with_str(self, value):
        try:
            self._HubNumberOfRouters = int(value)
        except ValueError:
            self._HubNumberOfRouters = hex(int(value, 16))

    def _set_hubemulatedrouterposition_with_str(self, value):
        seperate = value.find(':')
        exec('self._HubEmulatedRouterPosition = EnumHubTopologyRouterPosition.%s' % value[:seperate])

    def _set_interfacestartipv4prefix_with_str(self, value):
        self._InterfaceStartIpv4Prefix = value

    def _set_interfaceendipv4prefix_with_str(self, value):
        self._InterfaceEndIpv4Prefix = value

    def _set_interfacestartipv6prefix_with_str(self, value):
        self._InterfaceStartIpv6Prefix = value

    def _set_interfaceendipv6prefix_with_str(self, value):
        self._InterfaceEndIpv6Prefix = value

    def _set_advertiseloopbackaddress_with_str(self, value):
        self._AdvertiseLoopbackAddress = (value == 'True')

    def _set_enabletrafficengine_with_str(self, value):
        self._EnableTrafficEngine = (value == 'True')

    def _set_startsystemid_with_str(self, value):
        self._StartSystemId = value

    def _set_systemidstep_with_str(self, value):
        self._SystemIdStep = value

    def _set_startrouterid_with_str(self, value):
        self._StartRouterId = value

    def _set_routeridstep_with_str(self, value):
        self._RouterIdStep = value

    def _set_ipv4internaladvemulatedrouters_with_str(self, value):
        self._Ipv4InternalAdvEmulatedRouters = (value == 'True')

    def _set_ipv4internaladvsimulatedrouter_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4InternalAdvSimulatedRouter = EnumSimuRouterAdvertiseType.%s' % value[:seperate])

    def _set_ipv4internaltotalnumberofroutes_with_str(self, value):
        try:
            self._Ipv4InternalTotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv4InternalTotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv4internalroutesoverride_with_str(self, value):
        self._Ipv4InternalRoutesOverride = (value == 'True')

    def _set_ipv4internalstartroutesprefix_with_str(self, value):
        self._Ipv4InternalStartRoutesPrefix = value

    def _set_ipv4internalendroutesprefix_with_str(self, value):
        self._Ipv4InternalEndRoutesPrefix = value

    def _set_ipv4internalroutesnoneseq_with_str(self, value):
        self._Ipv4InternalRoutesNoneSeq = (value == 'True')

    def _set_ipv4internalroutesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4InternalRoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv4internalroutesprefixlenstart_with_str(self, value):
        try:
            self._Ipv4InternalRoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv4InternalRoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv4internalroutesprefixlenend_with_str(self, value):
        try:
            self._Ipv4InternalRoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv4InternalRoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv4internalnarrowmetric_with_str(self, value):
        try:
            self._Ipv4InternalNarrowMetric = int(value)
        except ValueError:
            self._Ipv4InternalNarrowMetric = hex(int(value, 16))

    def _set_ipv4internalwidemetric_with_str(self, value):
        try:
            self._Ipv4InternalWideMetric = int(value)
        except ValueError:
            self._Ipv4InternalWideMetric = hex(int(value, 16))

    def _set_ipv4externaladvemulatedrouters_with_str(self, value):
        self._Ipv4ExternalAdvEmulatedRouters = (value == 'True')

    def _set_ipv4externaladvsimulatedrouter_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4ExternalAdvSimulatedRouter = EnumSimuRouterAdvertiseType.%s' % value[:seperate])

    def _set_ipv4externaltotalnumberofroutes_with_str(self, value):
        try:
            self._Ipv4ExternalTotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv4ExternalTotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv4externalroutesoverride_with_str(self, value):
        self._Ipv4ExternalRoutesOverride = (value == 'True')

    def _set_ipv4externalstartroutesprefix_with_str(self, value):
        self._Ipv4ExternalStartRoutesPrefix = value

    def _set_ipv4externalendroutesprefix_with_str(self, value):
        self._Ipv4ExternalEndRoutesPrefix = value

    def _set_ipv4externalroutesnoneseq_with_str(self, value):
        self._Ipv4ExternalRoutesNoneSeq = (value == 'True')

    def _set_ipv4externalroutesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4ExternalRoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv4externalroutesprefixlenstart_with_str(self, value):
        try:
            self._Ipv4ExternalRoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv4ExternalRoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv4externalroutesprefixlenend_with_str(self, value):
        try:
            self._Ipv4ExternalRoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv4ExternalRoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv4externalnarrowmetric_with_str(self, value):
        try:
            self._Ipv4ExternalNarrowMetric = int(value)
        except ValueError:
            self._Ipv4ExternalNarrowMetric = hex(int(value, 16))

    def _set_ipv4externalwidemetric_with_str(self, value):
        try:
            self._Ipv4ExternalWideMetric = int(value)
        except ValueError:
            self._Ipv4ExternalWideMetric = hex(int(value, 16))

    def _set_ipv6internaladvemulatedrouters_with_str(self, value):
        self._Ipv6InternalAdvEmulatedRouters = (value == 'True')

    def _set_ipv6internaladvsimulatedrouter_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6InternalAdvSimulatedRouter = EnumSimuRouterAdvertiseType.%s' % value[:seperate])

    def _set_ipv6internaltotalnumberofroutes_with_str(self, value):
        try:
            self._Ipv6InternalTotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv6InternalTotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv6internalroutesoverride_with_str(self, value):
        self._Ipv6InternalRoutesOverride = (value == 'True')

    def _set_ipv6internalstartroutesprefix_with_str(self, value):
        self._Ipv6InternalStartRoutesPrefix = value

    def _set_ipv6internalendroutesprefix_with_str(self, value):
        self._Ipv6InternalEndRoutesPrefix = value

    def _set_ipv6internalroutesnoneseq_with_str(self, value):
        self._Ipv6InternalRoutesNoneSeq = (value == 'True')

    def _set_ipv6internalroutesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6InternalRoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv6internalroutesprefixlenstart_with_str(self, value):
        try:
            self._Ipv6InternalRoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv6InternalRoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv6internalroutesprefixlenend_with_str(self, value):
        try:
            self._Ipv6InternalRoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv6InternalRoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv6internalwidemetric_with_str(self, value):
        try:
            self._Ipv6InternalWideMetric = int(value)
        except ValueError:
            self._Ipv6InternalWideMetric = hex(int(value, 16))

    def _set_ipv6externaladvemulatedrouters_with_str(self, value):
        self._Ipv6ExternalAdvEmulatedRouters = (value == 'True')

    def _set_ipv6externaladvsimulatedrouter_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6ExternalAdvSimulatedRouter = EnumSimuRouterAdvertiseType.%s' % value[:seperate])

    def _set_ipv6externaltotalnumberofroutes_with_str(self, value):
        try:
            self._Ipv6ExternalTotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv6ExternalTotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv6externalroutesoverride_with_str(self, value):
        self._Ipv6ExternalRoutesOverride = (value == 'True')

    def _set_ipv6externalstartroutesprefix_with_str(self, value):
        self._Ipv6ExternalStartRoutesPrefix = value

    def _set_ipv6externalendroutesprefix_with_str(self, value):
        self._Ipv6ExternalEndRoutesPrefix = value

    def _set_ipv6externalroutesnoneseq_with_str(self, value):
        self._Ipv6ExternalRoutesNoneSeq = (value == 'True')

    def _set_ipv6externalroutesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6ExternalRoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv6externalroutesprefixlenstart_with_str(self, value):
        try:
            self._Ipv6ExternalRoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv6ExternalRoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv6externalroutesprefixlenend_with_str(self, value):
        try:
            self._Ipv6ExternalRoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv6ExternalRoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv6externalwidemetric_with_str(self, value):
        try:
            self._Ipv6ExternalWideMetric = int(value)
        except ValueError:
            self._Ipv6ExternalWideMetric = hex(int(value, 16))

