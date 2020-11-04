"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Ospfv2ProtocolConfig(L23ProtocolConfig):
    def __init__(self, EnableOspfv2=None, AreaId=None, EnableBfd=None, NetworkType=None, Priority=None, InterfaceCost=None, AuthenticationType=None, Password=None, Md5KeyId=None, Options=None, EnableOspfv2Mtu=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableViewRoutes=None, HelloInterval=None, RouterDeadInterval=None, LsaRetransInterval=None, LsaRefreshTime=None, **kwargs):
        self._EnableOspfv2 = EnableOspfv2  # Enable
        self._RouterState = EnumOspfRouterState.DISABLE  # Router State, not editable
        self._AdjacencyStatus = EnumOspfAdjacencyState.DOWN  # Adjacency Status, not editable
        self._AreaId = AreaId  # Area ID
        self._EnableBfd = EnableBfd  # Enable BFD
        self._NetworkType = NetworkType  # Network Type
        self._Priority = Priority  # Router Priority
        self._InterfaceCost = InterfaceCost  # Interface Cost
        self._AuthenticationType = AuthenticationType  # Authentication Type
        self._Password = Password  # Password
        self._Md5KeyId = Md5KeyId  # MD5 Key ID
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)  # Options
        self._EnableOspfv2Mtu = EnableOspfv2Mtu  # Enable OSPF MTU
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._GracefulRestartReason = GracefulRestartReason  # Graceful Restart Reason
        self._EnableViewRoutes = EnableViewRoutes  # Enable View Routes
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._RouterDeadInterval = RouterDeadInterval  # Router Dead Interval (sec)
        self._LsaRetransInterval = LsaRetransInterval  # LSA Retransmit Interval (sec)
        self._LsaRefreshTime = LsaRefreshTime  # LSA Refresh Time (sec)
        self._RouterLsaCount = 0  # Router LSA Count, not editable
        self._NetworkLsaCount = 0  # Network LSA Count, not editable
        self._SummaryLsaCount = 0  # Summary LSA Count, not editable
        self._AsbrSummaryLsaCount = 0  # ASBR Summary LSA Count, not editable
        self._ExternalLsaCount = 0  # External/NSSA LSA Count, not editable
        self._TeLsaCount = 0  # Te LSA Count, not editable

        properties = kwargs.copy()
        if EnableOspfv2 is not None:
            properties['EnableOspfv2'] = EnableOspfv2
        if AreaId is not None:
            properties['AreaId'] = AreaId
        if EnableBfd is not None:
            properties['EnableBfd'] = EnableBfd
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            properties['Priority'] = Priority
        if InterfaceCost is not None:
            properties['InterfaceCost'] = InterfaceCost
        if AuthenticationType is not None:
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            properties['Password'] = Password
        if Md5KeyId is not None:
            properties['Md5KeyId'] = Md5KeyId
        if Options is not None:
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if EnableOspfv2Mtu is not None:
            properties['EnableOspfv2Mtu'] = EnableOspfv2Mtu
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
        super(Ospfv2ProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableOspfv2=None, AreaId=None, EnableBfd=None, NetworkType=None, Priority=None, InterfaceCost=None, AuthenticationType=None, Password=None, Md5KeyId=None, Options=None, EnableOspfv2Mtu=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableViewRoutes=None, HelloInterval=None, RouterDeadInterval=None, LsaRetransInterval=None, LsaRefreshTime=None, **kwargs):
        properties = kwargs.copy()
        if EnableOspfv2 is not None:
            self._EnableOspfv2 = EnableOspfv2
            properties['EnableOspfv2'] = EnableOspfv2
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
        if InterfaceCost is not None:
            self._InterfaceCost = InterfaceCost
            properties['InterfaceCost'] = InterfaceCost
        if AuthenticationType is not None:
            self._AuthenticationType = AuthenticationType
            properties['AuthenticationType'] = AuthenticationType
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if Md5KeyId is not None:
            self._Md5KeyId = Md5KeyId
            properties['Md5KeyId'] = Md5KeyId
        if Options is not None:
            self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if EnableOspfv2Mtu is not None:
            self._EnableOspfv2Mtu = EnableOspfv2Mtu
            properties['EnableOspfv2Mtu'] = EnableOspfv2Mtu
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

        super(Ospfv2ProtocolConfig, self).edit(**properties)

    @property
    def EnableOspfv2(self):
        """
        get the value of property _EnableOspfv2
        """
        if self.force_auto_sync:
            self.get('EnableOspfv2')
        return self._EnableOspfv2

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
    def InterfaceCost(self):
        """
        get the value of property _InterfaceCost
        """
        if self.force_auto_sync:
            self.get('InterfaceCost')
        return self._InterfaceCost

    @property
    def AuthenticationType(self):
        """
        get the value of property _AuthenticationType
        """
        if self.force_auto_sync:
            self.get('AuthenticationType')
        return self._AuthenticationType

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def Md5KeyId(self):
        """
        get the value of property _Md5KeyId
        """
        if self.force_auto_sync:
            self.get('Md5KeyId')
        return self._Md5KeyId

    @property
    def Options(self):
        """
        get the value of property _Options
        """
        if self.force_auto_sync:
            self.get('Options')
        return self._Options

    @property
    def EnableOspfv2Mtu(self):
        """
        get the value of property _EnableOspfv2Mtu
        """
        if self.force_auto_sync:
            self.get('EnableOspfv2Mtu')
        return self._EnableOspfv2Mtu

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
    def SummaryLsaCount(self):
        """
        get the value of property _SummaryLsaCount
        """
        if self.force_auto_sync:
            self.get('SummaryLsaCount')
        return self._SummaryLsaCount

    @property
    def AsbrSummaryLsaCount(self):
        """
        get the value of property _AsbrSummaryLsaCount
        """
        if self.force_auto_sync:
            self.get('AsbrSummaryLsaCount')
        return self._AsbrSummaryLsaCount

    @property
    def ExternalLsaCount(self):
        """
        get the value of property _ExternalLsaCount
        """
        if self.force_auto_sync:
            self.get('ExternalLsaCount')
        return self._ExternalLsaCount

    @property
    def TeLsaCount(self):
        """
        get the value of property _TeLsaCount
        """
        if self.force_auto_sync:
            self.get('TeLsaCount')
        return self._TeLsaCount

    @EnableOspfv2.setter
    def EnableOspfv2(self, value):
        self._EnableOspfv2 = value
        self.edit(EnableOspfv2=value)

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

    @InterfaceCost.setter
    def InterfaceCost(self, value):
        self._InterfaceCost = value
        self.edit(InterfaceCost=value)

    @AuthenticationType.setter
    def AuthenticationType(self, value):
        self._AuthenticationType = value
        self.edit(AuthenticationType=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @Md5KeyId.setter
    def Md5KeyId(self, value):
        self._Md5KeyId = value
        self.edit(Md5KeyId=value)

    @Options.setter
    def Options(self, value):
        self._Options = swap_int_to_enum_flag(value, EnumOspfv2OptionBit)
        if isinstance(value, Flag):
            self.edit(Options=value.value)
        else:
            self.edit(Options=value)

    @EnableOspfv2Mtu.setter
    def EnableOspfv2Mtu(self, value):
        self._EnableOspfv2Mtu = value
        self.edit(EnableOspfv2Mtu=value)

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

    def _set_enableospfv2_with_str(self, value):
        self._EnableOspfv2 = (value == 'True')

    def _set_routerstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterState = EnumOspfRouterState.%s' % value[:seperate])

    def _set_adjacencystatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._AdjacencyStatus = EnumOspfAdjacencyState.%s' % value[:seperate])

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

    def _set_interfacecost_with_str(self, value):
        try:
            self._InterfaceCost = int(value)
        except ValueError:
            self._InterfaceCost = hex(int(value, 16))

    def _set_authenticationtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationType = EnumOspfAuthType.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_md5keyid_with_str(self, value):
        try:
            self._Md5KeyId = int(value)
        except ValueError:
            self._Md5KeyId = hex(int(value, 16))

    def _set_options_with_str(self, value):
        seperate = value.find(':')
        self._Options = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv2OptionBit)

    def _set_enableospfv2mtu_with_str(self, value):
        self._EnableOspfv2Mtu = (value == 'True')

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_gracefulrestartreason_with_str(self, value):
        seperate = value.find(':')
        exec('self._GracefulRestartReason = EnumOspfv2ReasonType.%s' % value[:seperate])

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

    def _set_summarylsacount_with_str(self, value):
        try:
            self._SummaryLsaCount = int(value)
        except ValueError:
            self._SummaryLsaCount = hex(int(value, 16))

    def _set_asbrsummarylsacount_with_str(self, value):
        try:
            self._AsbrSummaryLsaCount = int(value)
        except ValueError:
            self._AsbrSummaryLsaCount = hex(int(value, 16))

    def _set_externallsacount_with_str(self, value):
        try:
            self._ExternalLsaCount = int(value)
        except ValueError:
            self._ExternalLsaCount = hex(int(value, 16))

    def _set_telsacount_with_str(self, value):
        try:
            self._TeLsaCount = int(value)
        except ValueError:
            self._TeLsaCount = hex(int(value, 16))

