"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BgpRoutePoolBaseConfig(ROMObject):
    def __init__(self, RouteCount=None, SubAfi=None, Origin=None, AsPath=None, AsPathType=None, UseSessionAddressAsNextHop=None, LocalPref=None, EnableMed=None, MultExitDisc=None, AtomicAggregate=None, EnableAggregator=None, AggregatorAsNumber=None, AggregatorIp=None, EnableOriginatorId=None, OriginatorId=None, EnableClusterIdList=None, ClusterIdList=None, EnableCommunity=None, CommunityType=None, CommunityAsNumber=None, CommunityId=None, **kwargs):
        self._RouteCount = RouteCount  # Route Count
        self._SubAfi = SubAfi  # Sub-AFI
        self._Origin = Origin  # ORIGIN
        self._AsPath = AsPath  # AS Path
        self._AsPathType = AsPathType  # AS Path Type
        self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop  # Use Session Address as Next Hop
        self._EnableLocalPref = True  # Enable Local Preference, not editable
        self._LocalPref = LocalPref  # Local Preference
        self._EnableMed = EnableMed  # Enable Multi Exit Discriminator
        self._MultExitDisc = MultExitDisc  # Multi Exit Discriminator
        self._AtomicAggregate = AtomicAggregate  # Atomic Aggregate
        self._EnableAggregator = EnableAggregator  # Enable Aggregator
        self._AggregatorAsNumber = AggregatorAsNumber  # Aggregator AS Number
        self._AggregatorIp = AggregatorIp  # Aggregator IP
        self._EnableOriginatorId = EnableOriginatorId  # Enable Originator ID
        self._OriginatorId = OriginatorId  # Originator ID
        self._EnableClusterIdList = EnableClusterIdList  # Enable Cluster ID List
        self._ClusterIdList = ClusterIdList  # Cluster ID List
        self._EnableCommunity = EnableCommunity  # Enable Community
        self._CommunityType = CommunityType  # Community Type
        self._CommunityAsNumber = CommunityAsNumber  # Community AS Number
        self._CommunityId = CommunityId  # Community ID

        properties = kwargs.copy()
        if RouteCount is not None:
            properties['RouteCount'] = RouteCount
        if SubAfi is not None:
            properties['SubAfi'] = SubAfi
        if Origin is not None:
            properties['Origin'] = Origin
        if AsPath is not None:
            properties['AsPath'] = AsPath
        if AsPathType is not None:
            properties['AsPathType'] = AsPathType
        if UseSessionAddressAsNextHop is not None:
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if LocalPref is not None:
            properties['LocalPref'] = LocalPref
        if EnableMed is not None:
            properties['EnableMed'] = EnableMed
        if MultExitDisc is not None:
            properties['MultExitDisc'] = MultExitDisc
        if AtomicAggregate is not None:
            properties['AtomicAggregate'] = AtomicAggregate
        if EnableAggregator is not None:
            properties['EnableAggregator'] = EnableAggregator
        if AggregatorAsNumber is not None:
            properties['AggregatorAsNumber'] = AggregatorAsNumber
        if AggregatorIp is not None:
            properties['AggregatorIp'] = AggregatorIp
        if EnableOriginatorId is not None:
            properties['EnableOriginatorId'] = EnableOriginatorId
        if OriginatorId is not None:
            properties['OriginatorId'] = OriginatorId
        if EnableClusterIdList is not None:
            properties['EnableClusterIdList'] = EnableClusterIdList
        if ClusterIdList is not None:
            properties['ClusterIdList'] = ClusterIdList
        if EnableCommunity is not None:
            properties['EnableCommunity'] = EnableCommunity
        if CommunityType is not None:
            properties['CommunityType'] = CommunityType
        if CommunityAsNumber is not None:
            properties['CommunityAsNumber'] = CommunityAsNumber
        if CommunityId is not None:
            properties['CommunityId'] = CommunityId

        # call base class function, and it will send message to renix server to create a class.
        super(BgpRoutePoolBaseConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteCount=None, SubAfi=None, Origin=None, AsPath=None, AsPathType=None, UseSessionAddressAsNextHop=None, LocalPref=None, EnableMed=None, MultExitDisc=None, AtomicAggregate=None, EnableAggregator=None, AggregatorAsNumber=None, AggregatorIp=None, EnableOriginatorId=None, OriginatorId=None, EnableClusterIdList=None, ClusterIdList=None, EnableCommunity=None, CommunityType=None, CommunityAsNumber=None, CommunityId=None, **kwargs):
        properties = kwargs.copy()
        if RouteCount is not None:
            self._RouteCount = RouteCount
            properties['RouteCount'] = RouteCount
        if SubAfi is not None:
            self._SubAfi = SubAfi
            properties['SubAfi'] = SubAfi
        if Origin is not None:
            self._Origin = Origin
            properties['Origin'] = Origin
        if AsPath is not None:
            self._AsPath = AsPath
            properties['AsPath'] = AsPath
        if AsPathType is not None:
            self._AsPathType = AsPathType
            properties['AsPathType'] = AsPathType
        if UseSessionAddressAsNextHop is not None:
            self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if LocalPref is not None:
            self._LocalPref = LocalPref
            properties['LocalPref'] = LocalPref
        if EnableMed is not None:
            self._EnableMed = EnableMed
            properties['EnableMed'] = EnableMed
        if MultExitDisc is not None:
            self._MultExitDisc = MultExitDisc
            properties['MultExitDisc'] = MultExitDisc
        if AtomicAggregate is not None:
            self._AtomicAggregate = AtomicAggregate
            properties['AtomicAggregate'] = AtomicAggregate
        if EnableAggregator is not None:
            self._EnableAggregator = EnableAggregator
            properties['EnableAggregator'] = EnableAggregator
        if AggregatorAsNumber is not None:
            self._AggregatorAsNumber = AggregatorAsNumber
            properties['AggregatorAsNumber'] = AggregatorAsNumber
        if AggregatorIp is not None:
            self._AggregatorIp = AggregatorIp
            properties['AggregatorIp'] = AggregatorIp
        if EnableOriginatorId is not None:
            self._EnableOriginatorId = EnableOriginatorId
            properties['EnableOriginatorId'] = EnableOriginatorId
        if OriginatorId is not None:
            self._OriginatorId = OriginatorId
            properties['OriginatorId'] = OriginatorId
        if EnableClusterIdList is not None:
            self._EnableClusterIdList = EnableClusterIdList
            properties['EnableClusterIdList'] = EnableClusterIdList
        if ClusterIdList is not None:
            self._ClusterIdList = ClusterIdList
            properties['ClusterIdList'] = ClusterIdList
        if EnableCommunity is not None:
            self._EnableCommunity = EnableCommunity
            properties['EnableCommunity'] = EnableCommunity
        if CommunityType is not None:
            self._CommunityType = CommunityType
            properties['CommunityType'] = CommunityType
        if CommunityAsNumber is not None:
            self._CommunityAsNumber = CommunityAsNumber
            properties['CommunityAsNumber'] = CommunityAsNumber
        if CommunityId is not None:
            self._CommunityId = CommunityId
            properties['CommunityId'] = CommunityId

        super(BgpRoutePoolBaseConfig, self).edit(**properties)

    @property
    def RouteCount(self):
        """
        get the value of property _RouteCount
        """
        if self.force_auto_sync:
            self.get('RouteCount')
        return self._RouteCount

    @property
    def SubAfi(self):
        """
        get the value of property _SubAfi
        """
        if self.force_auto_sync:
            self.get('SubAfi')
        return self._SubAfi

    @property
    def Origin(self):
        """
        get the value of property _Origin
        """
        if self.force_auto_sync:
            self.get('Origin')
        return self._Origin

    @property
    def AsPath(self):
        """
        get the value of property _AsPath
        """
        if self.force_auto_sync:
            self.get('AsPath')
        return self._AsPath

    @property
    def AsPathType(self):
        """
        get the value of property _AsPathType
        """
        if self.force_auto_sync:
            self.get('AsPathType')
        return self._AsPathType

    @property
    def UseSessionAddressAsNextHop(self):
        """
        get the value of property _UseSessionAddressAsNextHop
        """
        if self.force_auto_sync:
            self.get('UseSessionAddressAsNextHop')
        return self._UseSessionAddressAsNextHop

    @property
    def EnableLocalPref(self):
        """
        get the value of property _EnableLocalPref
        """
        if self.force_auto_sync:
            self.get('EnableLocalPref')
        return self._EnableLocalPref

    @property
    def LocalPref(self):
        """
        get the value of property _LocalPref
        """
        if self.force_auto_sync:
            self.get('LocalPref')
        return self._LocalPref

    @property
    def EnableMed(self):
        """
        get the value of property _EnableMed
        """
        if self.force_auto_sync:
            self.get('EnableMed')
        return self._EnableMed

    @property
    def MultExitDisc(self):
        """
        get the value of property _MultExitDisc
        """
        if self.force_auto_sync:
            self.get('MultExitDisc')
        return self._MultExitDisc

    @property
    def AtomicAggregate(self):
        """
        get the value of property _AtomicAggregate
        """
        if self.force_auto_sync:
            self.get('AtomicAggregate')
        return self._AtomicAggregate

    @property
    def EnableAggregator(self):
        """
        get the value of property _EnableAggregator
        """
        if self.force_auto_sync:
            self.get('EnableAggregator')
        return self._EnableAggregator

    @property
    def AggregatorAsNumber(self):
        """
        get the value of property _AggregatorAsNumber
        """
        if self.force_auto_sync:
            self.get('AggregatorAsNumber')
        return self._AggregatorAsNumber

    @property
    def AggregatorIp(self):
        """
        get the value of property _AggregatorIp
        """
        if self.force_auto_sync:
            self.get('AggregatorIp')
        return self._AggregatorIp

    @property
    def EnableOriginatorId(self):
        """
        get the value of property _EnableOriginatorId
        """
        if self.force_auto_sync:
            self.get('EnableOriginatorId')
        return self._EnableOriginatorId

    @property
    def OriginatorId(self):
        """
        get the value of property _OriginatorId
        """
        if self.force_auto_sync:
            self.get('OriginatorId')
        return self._OriginatorId

    @property
    def EnableClusterIdList(self):
        """
        get the value of property _EnableClusterIdList
        """
        if self.force_auto_sync:
            self.get('EnableClusterIdList')
        return self._EnableClusterIdList

    @property
    def ClusterIdList(self):
        """
        get the value of property _ClusterIdList
        """
        if self.force_auto_sync:
            self.get('ClusterIdList')
        return self._ClusterIdList

    @property
    def EnableCommunity(self):
        """
        get the value of property _EnableCommunity
        """
        if self.force_auto_sync:
            self.get('EnableCommunity')
        return self._EnableCommunity

    @property
    def CommunityType(self):
        """
        get the value of property _CommunityType
        """
        if self.force_auto_sync:
            self.get('CommunityType')
        return self._CommunityType

    @property
    def CommunityAsNumber(self):
        """
        get the value of property _CommunityAsNumber
        """
        if self.force_auto_sync:
            self.get('CommunityAsNumber')
        return self._CommunityAsNumber

    @property
    def CommunityId(self):
        """
        get the value of property _CommunityId
        """
        if self.force_auto_sync:
            self.get('CommunityId')
        return self._CommunityId

    @RouteCount.setter
    def RouteCount(self, value):
        self._RouteCount = value
        self.edit(RouteCount=value)

    @SubAfi.setter
    def SubAfi(self, value):
        self._SubAfi = value
        self.edit(SubAfi=value)

    @Origin.setter
    def Origin(self, value):
        self._Origin = value
        self.edit(Origin=value)

    @AsPath.setter
    def AsPath(self, value):
        self._AsPath = value
        self.edit(AsPath=value)

    @AsPathType.setter
    def AsPathType(self, value):
        self._AsPathType = value
        self.edit(AsPathType=value)

    @UseSessionAddressAsNextHop.setter
    def UseSessionAddressAsNextHop(self, value):
        self._UseSessionAddressAsNextHop = value
        self.edit(UseSessionAddressAsNextHop=value)

    @LocalPref.setter
    def LocalPref(self, value):
        self._LocalPref = value
        self.edit(LocalPref=value)

    @EnableMed.setter
    def EnableMed(self, value):
        self._EnableMed = value
        self.edit(EnableMed=value)

    @MultExitDisc.setter
    def MultExitDisc(self, value):
        self._MultExitDisc = value
        self.edit(MultExitDisc=value)

    @AtomicAggregate.setter
    def AtomicAggregate(self, value):
        self._AtomicAggregate = value
        self.edit(AtomicAggregate=value)

    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._EnableAggregator = value
        self.edit(EnableAggregator=value)

    @AggregatorAsNumber.setter
    def AggregatorAsNumber(self, value):
        self._AggregatorAsNumber = value
        self.edit(AggregatorAsNumber=value)

    @AggregatorIp.setter
    def AggregatorIp(self, value):
        self._AggregatorIp = value
        self.edit(AggregatorIp=value)

    @EnableOriginatorId.setter
    def EnableOriginatorId(self, value):
        self._EnableOriginatorId = value
        self.edit(EnableOriginatorId=value)

    @OriginatorId.setter
    def OriginatorId(self, value):
        self._OriginatorId = value
        self.edit(OriginatorId=value)

    @EnableClusterIdList.setter
    def EnableClusterIdList(self, value):
        self._EnableClusterIdList = value
        self.edit(EnableClusterIdList=value)

    @ClusterIdList.setter
    def ClusterIdList(self, value):
        self._ClusterIdList = value
        self.edit(ClusterIdList=value)

    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._EnableCommunity = value
        self.edit(EnableCommunity=value)

    @CommunityType.setter
    def CommunityType(self, value):
        self._CommunityType = value
        self.edit(CommunityType=value)

    @CommunityAsNumber.setter
    def CommunityAsNumber(self, value):
        self._CommunityAsNumber = value
        self.edit(CommunityAsNumber=value)

    @CommunityId.setter
    def CommunityId(self, value):
        self._CommunityId = value
        self.edit(CommunityId=value)

    def _set_routecount_with_str(self, value):
        try:
            self._RouteCount = int(value)
        except ValueError:
            self._RouteCount = hex(int(value, 16))

    def _set_subafi_with_str(self, value):
        seperate = value.find(':')
        exec('self._SubAfi = EnumBgpSubAfi.%s' % value[:seperate])

    def _set_origin_with_str(self, value):
        seperate = value.find(':')
        exec('self._Origin = EnumBgpOrigin.%s' % value[:seperate])

    def _set_aspath_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AsPath = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AsPath.append(int(str_value))
            except ValueError:
                self._AsPath.append(hex(int(str_value, 16)))

    def _set_aspathtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AsPathType = EnumBgpAsPathType.%s' % value[:seperate])

    def _set_usesessionaddressasnexthop_with_str(self, value):
        self._UseSessionAddressAsNextHop = (value == 'True')

    def _set_enablelocalpref_with_str(self, value):
        self._EnableLocalPref = (value == 'True')

    def _set_localpref_with_str(self, value):
        try:
            self._LocalPref = int(value)
        except ValueError:
            self._LocalPref = hex(int(value, 16))

    def _set_enablemed_with_str(self, value):
        self._EnableMed = (value == 'True')

    def _set_multexitdisc_with_str(self, value):
        try:
            self._MultExitDisc = int(value)
        except ValueError:
            self._MultExitDisc = hex(int(value, 16))

    def _set_atomicaggregate_with_str(self, value):
        self._AtomicAggregate = (value == 'True')

    def _set_enableaggregator_with_str(self, value):
        self._EnableAggregator = (value == 'True')

    def _set_aggregatorasnumber_with_str(self, value):
        try:
            self._AggregatorAsNumber = int(value)
        except ValueError:
            self._AggregatorAsNumber = hex(int(value, 16))

    def _set_aggregatorip_with_str(self, value):
        self._AggregatorIp = value

    def _set_enableoriginatorid_with_str(self, value):
        self._EnableOriginatorId = (value == 'True')

    def _set_originatorid_with_str(self, value):
        self._OriginatorId = value

    def _set_enableclusteridlist_with_str(self, value):
        self._EnableClusterIdList = (value == 'True')

    def _set_clusteridlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ClusterIdList = tmp_value.split()

    def _set_enablecommunity_with_str(self, value):
        self._EnableCommunity = (value == 'True')

    def _set_communitytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CommunityType = EnumBgpCommunityType.%s' % value[:seperate])

    def _set_communityasnumber_with_str(self, value):
        try:
            self._CommunityAsNumber = int(value)
        except ValueError:
            self._CommunityAsNumber = hex(int(value, 16))

    def _set_communityid_with_str(self, value):
        try:
            self._CommunityId = int(value)
        except ValueError:
            self._CommunityId = hex(int(value, 16))

