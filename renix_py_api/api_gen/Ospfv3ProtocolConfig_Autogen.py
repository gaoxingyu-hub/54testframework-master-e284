"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Ospfv3ProtocolConfig(L23ProtocolConfig):
    def __init__(self, EnableOspfv3=None, InstanceId=None, AreaId=None, EnableBfd=None, NetworkType=None, Priority=None, InterfaceId=None, InterfaceCost=None, Options=None, EnableOspfv3Mtu=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableViewRoutes=None, HelloInterval=None, RouterDeadInterval=None, LsaRetransInterval=None, LsaRefreshTime=None, **kwargs):
        self._EnableOspfv3 = EnableOspfv3  # Enable
        self._RouterState = EnumOspfRouterState.NOTSTART  # Router State, not editable
        self._AdjacencyStatus = EnumOspfAdjacencyState.DOWN  # Adjacency Status, not editable
        self._InstanceId = InstanceId  # Instance ID
        self._AreaId = AreaId  # Area ID
        self._EnableBfd = EnableBfd  # Enable BFD
        self._NetworkType = NetworkType  # Network Type
        self._Priority = Priority  # Router Priority
        self._InterfaceId = InterfaceId  # Interface ID
        self._InterfaceCost = InterfaceCost  # Interface Cost
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv3OptionBit)  # Options
        self._EnableOspfv3Mtu = EnableOspfv3Mtu  # Enable OSPFv3 MTU
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._GracefulRestartReason = GracefulRestartReason  # Graceful Restart Reason
        self._EnableViewRoutes = EnableViewRoutes  # Enable View Routes
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._RouterDeadInterval = RouterDeadInterval  # Router Dead Interval (sec)
        self._LsaRetransInterval = LsaRetransInterval  # LSA Retransmit Interval (sec)
        self._LsaRefreshTime = LsaRefreshTime  # LSA Refresh Time (sec)
        self._RouterLsaCount = 0  # Router LSA Count, not editable
        self._NetworkLsaCount = 0  # Network LSA Count, not editable
        self._InterAreaPrefixLsaCount = 0  # Inter-Area Prefix LSA Count, not editable
        self._InterAreaRouterLsaCount = 0  # Inter-Area Router LSA Count, not editable
        self._AsExternalLsaCount = 0  # As External LSA Count, not editable
        self._NssaExternalLsaCount = 0  # NSSA LSA Count, not editable
        self._LinkLsaCount = 0  # Link LSA Count, not editable
        self._IntraAreaPrefixLsaCount = 0  # Intra Area Prefix LSA Count, not editable

        properties = kwargs.copy()
        if EnableOspfv3 is not None:
            properties['EnableOspfv3'] = EnableOspfv3
        if InstanceId is not None:
            properties['InstanceId'] = InstanceId
        if AreaId is not None:
            properties['AreaId'] = AreaId
        if EnableBfd is not None:
            properties['EnableBfd'] = EnableBfd
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            properties['Priority'] = Priority
        if InterfaceId is not None:
            properties['InterfaceId'] = InterfaceId
        if InterfaceCost is not None:
            properties['InterfaceCost'] = InterfaceCost
        if Options is not None:
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if EnableOspfv3Mtu is not None:
            properties['EnableOspfv3Mtu'] = EnableOspfv3Mtu
        if EnableGracefulRestart is not None:
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if GracefulRestartReason is not None:
            properties['GracefulRestartReason'] = GracefulRestartReason
        if EnableViewRoutes is not None:
            properties['EnableViewRoutes'] = EnableViewRoutes
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if RouterDeadInterval is not None:
            properties['RouterDeadInterval'] = RouterDeadInterval
        if LsaRetransInterval is not None:
            properties['LsaRetransInterval'] = LsaRetransInterval
        if LsaRefreshTime is not None:
            properties['LsaRefreshTime'] = LsaRefreshTime

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3ProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableOspfv3=None, InstanceId=None, AreaId=None, EnableBfd=None, NetworkType=None, Priority=None, InterfaceId=None, InterfaceCost=None, Options=None, EnableOspfv3Mtu=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableViewRoutes=None, HelloInterval=None, RouterDeadInterval=None, LsaRetransInterval=None, LsaRefreshTime=None, **kwargs):
        properties = kwargs.copy()
        if EnableOspfv3 is not None:
            self._EnableOspfv3 = EnableOspfv3
            properties['EnableOspfv3'] = EnableOspfv3
        if InstanceId is not None:
            self._InstanceId = InstanceId
            properties['InstanceId'] = InstanceId
        if AreaId is not None:
            self._AreaId = AreaId
            properties['AreaId'] = AreaId
        if EnableBfd is not None:
            self._EnableBfd = EnableBfd
            properties['EnableBfd'] = EnableBfd
        if NetworkType is not None:
            self._NetworkType = NetworkType
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if InterfaceId is not None:
            self._InterfaceId = InterfaceId
            properties['InterfaceId'] = InterfaceId
        if InterfaceCost is not None:
            self._InterfaceCost = InterfaceCost
            properties['InterfaceCost'] = InterfaceCost
        if Options is not None:
            self._Options = swap_int_to_enum_flag(Options, EnumOspfv3OptionBit)
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if EnableOspfv3Mtu is not None:
            self._EnableOspfv3Mtu = EnableOspfv3Mtu
            properties['EnableOspfv3Mtu'] = EnableOspfv3Mtu
        if EnableGracefulRestart is not None:
            self._EnableGracefulRestart = EnableGracefulRestart
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if GracefulRestartReason is not None:
            self._GracefulRestartReason = GracefulRestartReason
            properties['GracefulRestartReason'] = GracefulRestartReason
        if EnableViewRoutes is not None:
            self._EnableViewRoutes = EnableViewRoutes
            properties['EnableViewRoutes'] = EnableViewRoutes
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if RouterDeadInterval is not None:
            self._RouterDeadInterval = RouterDeadInterval
            properties['RouterDeadInterval'] = RouterDeadInterval
        if LsaRetransInterval is not None:
            self._LsaRetransInterval = LsaRetransInterval
            properties['LsaRetransInterval'] = LsaRetransInterval
        if LsaRefreshTime is not None:
            self._LsaRefreshTime = LsaRefreshTime
            properties['LsaRefreshTime'] = LsaRefreshTime

        super(Ospfv3ProtocolConfig, self).edit(**properties)

    @property
    def EnableOspfv3(self):
        """
        get the value of property _EnableOspfv3
        """
        if self.force_auto_sync:
            self.get('EnableOspfv3')
        return self._EnableOspfv3

    @property
    def RouterState(self):
        """
        get the value of property _RouterState
        """
        if self.force_auto_sync:
            self.get('RouterState')
        return self._RouterState

    @property
    def AdjacencyStatus(self):
        """
        get the value of property _AdjacencyStatus
        """
        if self.force_auto_sync:
            self.get('AdjacencyStatus')
        return self._AdjacencyStatus

    @property
    def InstanceId(self):
        """
        get the value of property _InstanceId
        """
        if self.force_auto_sync:
            self.get('InstanceId')
        return self._InstanceId

    @property
    def AreaId(self):
        """
        get the value of property _AreaId
        """
        if self.force_auto_sync:
            self.get('AreaId')
        return self._AreaId

    @property
    def EnableBfd(self):
        """
        get the value of property _EnableBfd
        """
        if self.force_auto_sync:
            self.get('EnableBfd')
        return self._EnableBfd

    @property
    def NetworkType(self):
        """
        get the value of property _NetworkType
        """
        if self.force_auto_sync:
            self.get('NetworkType')
        return self._NetworkType

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def InterfaceId(self):
        """
        get the value of property _InterfaceId
        """
        if self.force_auto_sync:
            self.get('InterfaceId')
        return self._InterfaceId

    @property
    def InterfaceCost(self):
        """
        get the value of property _InterfaceCost
        """
        if self.force_auto_sync:
            self.get('InterfaceCost')
        return self._InterfaceCost

    @property
    def Options(self):
        """
        get the value of property _Options
        """
        if self.force_auto_sync:
            self.get('Options')
        return self._Options

    @property
    def EnableOspfv3Mtu(self):
        """
        get the value of property _EnableOspfv3Mtu
        """
        if self.force_auto_sync:
            self.get('EnableOspfv3Mtu')
        return self._EnableOspfv3Mtu

    @property
    def EnableGracefulRestart(self):
        """
        get the value of property _EnableGracefulRestart
        """
        if self.force_auto_sync:
            self.get('EnableGracefulRestart')
        return self._EnableGracefulRestart

    @property
    def GracefulRestartReason(self):
        """
        get the value of property _GracefulRestartReason
        """
        if self.force_auto_sync:
            self.get('GracefulRestartReason')
        return self._GracefulRestartReason

    @property
    def EnableViewRoutes(self):
        """
        get the value of property _EnableViewRoutes
        """
        if self.force_auto_sync:
            self.get('EnableViewRoutes')
        return self._EnableViewRoutes

    @property
    def HelloInterval(self):
        """
        get the value of property _HelloInterval
        """
        if self.force_auto_sync:
            self.get('HelloInterval')
        return self._HelloInterval

    @property
    def RouterDeadInterval(self):
        """
        get the value of property _RouterDeadInterval
        """
        if self.force_auto_sync:
            self.get('RouterDeadInterval')
        return self._RouterDeadInterval

    @property
    def LsaRetransInterval(self):
        """
        get the value of property _LsaRetransInterval
        """
        if self.force_auto_sync:
            self.get('LsaRetransInterval')
        return self._LsaRetransInterval

    @property
    def LsaRefreshTime(self):
        """
        get the value of property _LsaRefreshTime
        """
        if self.force_auto_sync:
            self.get('LsaRefreshTime')
        return self._LsaRefreshTime

    @property
    def RouterLsaCount(self):
        """
        get the value of property _RouterLsaCount
        """
        if self.force_auto_sync:
            self.get('RouterLsaCount')
        return self._RouterLsaCount

    @property
    def NetworkLsaCount(self):
        """
        get the value of property _NetworkLsaCount
        """
        if self.force_auto_sync:
            self.get('NetworkLsaCount')
        return self._NetworkLsaCount

    @property
    def InterAreaPrefixLsaCount(self):
        """
        get the value of property _InterAreaPrefixLsaCount
        """
        if self.force_auto_sync:
            self.get('InterAreaPrefixLsaCount')
        return self._InterAreaPrefixLsaCount

    @property
    def InterAreaRouterLsaCount(self):
        """
        get the value of property _InterAreaRouterLsaCount
        """
        if self.force_auto_sync:
            self.get('InterAreaRouterLsaCount')
        return self._InterAreaRouterLsaCount

    @property
    def AsExternalLsaCount(self):
        """
        get the value of property _AsExternalLsaCount
        """
        if self.force_auto_sync:
            self.get('AsExternalLsaCount')
        return self._AsExternalLsaCount

    @property
    def NssaExternalLsaCount(self):
        """
        get the value of property _NssaExternalLsaCount
        """
        if self.force_auto_sync:
            self.get('NssaExternalLsaCount')
        return self._NssaExternalLsaCount

    @property
    def LinkLsaCount(self):
        """
        get the value of property _LinkLsaCount
        """
        if self.force_auto_sync:
            self.get('LinkLsaCount')
        return self._LinkLsaCount

    @property
    def IntraAreaPrefixLsaCount(self):
        """
        get the value of property _IntraAreaPrefixLsaCount
        """
        if self.force_auto_sync:
            self.get('IntraAreaPrefixLsaCount')
        return self._IntraAreaPrefixLsaCount

    @EnableOspfv3.setter
    def EnableOspfv3(self, value):
        self._EnableOspfv3 = value
        self.edit(EnableOspfv3=value)

    @InstanceId.setter
    def InstanceId(self, value):
        self._InstanceId = value
        self.edit(InstanceId=value)

    @AreaId.setter
    def AreaId(self, value):
        self._AreaId = value
        self.edit(AreaId=value)

    @EnableBfd.setter
    def EnableBfd(self, value):
        self._EnableBfd = value
        self.edit(EnableBfd=value)

    @NetworkType.setter
    def NetworkType(self, value):
        self._NetworkType = value
        self.edit(NetworkType=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @InterfaceId.setter
    def InterfaceId(self, value):
        self._InterfaceId = value
        self.edit(InterfaceId=value)

    @InterfaceCost.setter
    def InterfaceCost(self, value):
        self._InterfaceCost = value
        self.edit(InterfaceCost=value)

    @Options.setter
    def Options(self, value):
        self._Options = swap_int_to_enum_flag(value, EnumOspfv3OptionBit)
        if isinstance(value, Flag):
            self.edit(Options=value.value)
        else:
            self.edit(Options=value)

    @EnableOspfv3Mtu.setter
    def EnableOspfv3Mtu(self, value):
        self._EnableOspfv3Mtu = value
        self.edit(EnableOspfv3Mtu=value)

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._EnableGracefulRestart = value
        self.edit(EnableGracefulRestart=value)

    @GracefulRestartReason.setter
    def GracefulRestartReason(self, value):
        self._GracefulRestartReason = value
        self.edit(GracefulRestartReason=value)

    @EnableViewRoutes.setter
    def EnableViewRoutes(self, value):
        self._EnableViewRoutes = value
        self.edit(EnableViewRoutes=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @RouterDeadInterval.setter
    def RouterDeadInterval(self, value):
        self._RouterDeadInterval = value
        self.edit(RouterDeadInterval=value)

    @LsaRetransInterval.setter
    def LsaRetransInterval(self, value):
        self._LsaRetransInterval = value
        self.edit(LsaRetransInterval=value)

    @LsaRefreshTime.setter
    def LsaRefreshTime(self, value):
        self._LsaRefreshTime = value
        self.edit(LsaRefreshTime=value)

    def _set_enableospfv3_with_str(self, value):
        self._EnableOspfv3 = (value == 'True')

    def _set_routerstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterState = EnumOspfRouterState.%s' % value[:seperate])

    def _set_adjacencystatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._AdjacencyStatus = EnumOspfAdjacencyState.%s' % value[:seperate])

    def _set_instanceid_with_str(self, value):
        try:
            self._InstanceId = int(value)
        except ValueError:
            self._InstanceId = hex(int(value, 16))

    def _set_areaid_with_str(self, value):
        self._AreaId = value

    def _set_enablebfd_with_str(self, value):
        self._EnableBfd = (value == 'True')

    def _set_networktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._NetworkType = EnumOspfNetworkType.%s' % value[:seperate])

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_interfaceid_with_str(self, value):
        try:
            self._InterfaceId = int(value)
        except ValueError:
            self._InterfaceId = hex(int(value, 16))

    def _set_interfacecost_with_str(self, value):
        try:
            self._InterfaceCost = int(value)
        except ValueError:
            self._InterfaceCost = hex(int(value, 16))

    def _set_options_with_str(self, value):
        seperate = value.find(':')
        self._Options = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv3OptionBit)

    def _set_enableospfv3mtu_with_str(self, value):
        self._EnableOspfv3Mtu = (value == 'True')

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_gracefulrestartreason_with_str(self, value):
        seperate = value.find(':')
        exec('self._GracefulRestartReason = EnumOspfv3ReasonType.%s' % value[:seperate])

    def _set_enableviewroutes_with_str(self, value):
        self._EnableViewRoutes = (value == 'True')

    def _set_hellointerval_with_str(self, value):
        try:
            self._HelloInterval = int(value)
        except ValueError:
            self._HelloInterval = hex(int(value, 16))

    def _set_routerdeadinterval_with_str(self, value):
        try:
            self._RouterDeadInterval = int(value)
        except ValueError:
            self._RouterDeadInterval = hex(int(value, 16))

    def _set_lsaretransinterval_with_str(self, value):
        try:
            self._LsaRetransInterval = int(value)
        except ValueError:
            self._LsaRetransInterval = hex(int(value, 16))

    def _set_lsarefreshtime_with_str(self, value):
        try:
            self._LsaRefreshTime = int(value)
        except ValueError:
            self._LsaRefreshTime = hex(int(value, 16))

    def _set_routerlsacount_with_str(self, value):
        try:
            self._RouterLsaCount = int(value)
        except ValueError:
            self._RouterLsaCount = hex(int(value, 16))

    def _set_networklsacount_with_str(self, value):
        try:
            self._NetworkLsaCount = int(value)
        except ValueError:
            self._NetworkLsaCount = hex(int(value, 16))

    def _set_interareaprefixlsacount_with_str(self, value):
        try:
            self._InterAreaPrefixLsaCount = int(value)
        except ValueError:
            self._InterAreaPrefixLsaCount = hex(int(value, 16))

    def _set_interarearouterlsacount_with_str(self, value):
        try:
            self._InterAreaRouterLsaCount = int(value)
        except ValueError:
            self._InterAreaRouterLsaCount = hex(int(value, 16))

    def _set_asexternallsacount_with_str(self, value):
        try:
            self._AsExternalLsaCount = int(value)
        except ValueError:
            self._AsExternalLsaCount = hex(int(value, 16))

    def _set_nssaexternallsacount_with_str(self, value):
        try:
            self._NssaExternalLsaCount = int(value)
        except ValueError:
            self._NssaExternalLsaCount = hex(int(value, 16))

    def _set_linklsacount_with_str(self, value):
        try:
            self._LinkLsaCount = int(value)
        except ValueError:
            self._LinkLsaCount = hex(int(value, 16))

    def _set_intraareaprefixlsacount_with_str(self, value):
        try:
            self._IntraAreaPrefixLsaCount = int(value)
        except ValueError:
            self._IntraAreaPrefixLsaCount = hex(int(value, 16))

