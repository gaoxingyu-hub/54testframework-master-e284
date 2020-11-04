"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class IsisProtocolConfig(L23ProtocolConfig):
    def __init__(self, Level=None, NetworkType=None, SystemId=None, Priority=None, AuthMethod=None, Password=None, CircuitId=None, Area1=None, Area2=None, Area3=None, MetricMode=None, TeRouterId=None, HelloInterval=None, HelloMultiplier=None, PsnInterval=None, LspRefreshTime=None, RetransInterval=None, HelloPadding=None, LspSize=None, ValidateIpAddr=None, EnableGracefulRestart=None, EnableViewRoutes=None, EnableBFD=None, **kwargs):
        self._RouterState = EnumRouterState.DISABLE  # Router State, not editable
        self._ThreeWayP2pAdjState = EnumThreeWayP2PAdjState.NOTSTART  # P2P Adjacency State, not editable
        self._L1BroadcastAdjState = EnumBroadcastAdjState.NOTSTART  # Broadcast L1 State, not editable
        self._L2BroadcastAdjState = EnumBroadcastAdjState.NOTSTART  # Broadcast L2 State, not editable
        self._IpVersion = EnumIpVersion.IPV4  # IP Version, not editable
        self._Level = Level  # Level
        self._NetworkType = NetworkType  # Network Type
        self._SystemId = SystemId  # System ID
        self._Priority = Priority  # Router Priority
        self._L1BroadcastLanId = ''  # L1 Broadcast Lan ID, not editable
        self._L2BroadcastLanId = ''  # L2 Broadcast Lan ID, not editable
        self._SystemIdLearned = '00:00:00:00:00:00'  # P2P Neighbor System ID, not editable
        self._CircuitIdLearned = 255  # P2P Neighbor Circuit ID, not editable
        self._AuthMethod = AuthMethod  # Authentication
        self._Password = Password  # Password
        self._CircuitId = CircuitId  # Circuit ID
        self._Area1 = Area1  # Area 1
        self._Area2 = Area2  # Area 2
        self._Area3 = Area3  # Area 3
        self._MetricMode = MetricMode  # Metric Mode
        self._TeRouterId = TeRouterId  # TE Router ID
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._HelloMultiplier = HelloMultiplier  # Hello Multiplier
        self._PsnInterval = PsnInterval  # PSN Interval (sec)
        self._LspRefreshTime = LspRefreshTime  # LSP Refresh Time (sec)
        self._RetransInterval = RetransInterval  # Retransmission Interval (sec)
        self._HelloPadding = HelloPadding  # Hello Padding
        self._LspSize = LspSize  # LSP Size
        self._ValidateIpAddr = ValidateIpAddr  # Validate Interface IP Address
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._LspCount = 0  # LSP Count, not editable
        self._EnableViewRoutes = EnableViewRoutes  # Enable View Routes
        self._EnableBFD = EnableBFD  # Enable BFD

        properties = kwargs.copy()
        if Level is not None:
            properties['Level'] = Level
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if SystemId is not None:
            properties['SystemId'] = SystemId
        if Priority is not None:
            properties['Priority'] = Priority
        if AuthMethod is not None:
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            properties['Password'] = Password
        if CircuitId is not None:
            properties['CircuitId'] = CircuitId
        if Area1 is not None:
            properties['Area1'] = Area1
        if Area2 is not None:
            properties['Area2'] = Area2
        if Area3 is not None:
            properties['Area3'] = Area3
        if MetricMode is not None:
            properties['MetricMode'] = MetricMode
        if TeRouterId is not None:
            properties['TeRouterId'] = TeRouterId
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if HelloMultiplier is not None:
            properties['HelloMultiplier'] = HelloMultiplier
        if PsnInterval is not None:
            properties['PsnInterval'] = PsnInterval
        if LspRefreshTime is not None:
            properties['LspRefreshTime'] = LspRefreshTime
        if RetransInterval is not None:
            properties['RetransInterval'] = RetransInterval
        if HelloPadding is not None:
            properties['HelloPadding'] = HelloPadding
        if LspSize is not None:
            properties['LspSize'] = LspSize
        if ValidateIpAddr is not None:
            properties['ValidateIpAddr'] = ValidateIpAddr
        if EnableGracefulRestart is not None:
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if EnableViewRoutes is not None:
            properties['EnableViewRoutes'] = EnableViewRoutes
        if EnableBFD is not None:
            properties['EnableBFD'] = EnableBFD

        # call base class function, and it will send message to renix server to create a class.
        super(IsisProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Level=None, NetworkType=None, SystemId=None, Priority=None, AuthMethod=None, Password=None, CircuitId=None, Area1=None, Area2=None, Area3=None, MetricMode=None, TeRouterId=None, HelloInterval=None, HelloMultiplier=None, PsnInterval=None, LspRefreshTime=None, RetransInterval=None, HelloPadding=None, LspSize=None, ValidateIpAddr=None, EnableGracefulRestart=None, EnableViewRoutes=None, EnableBFD=None, **kwargs):
        properties = kwargs.copy()
        if Level is not None:
            self._Level = Level
            properties['Level'] = Level
        if NetworkType is not None:
            self._NetworkType = NetworkType
            properties['NetworkType'] = NetworkType
        if SystemId is not None:
            self._SystemId = SystemId
            properties['SystemId'] = SystemId
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if AuthMethod is not None:
            self._AuthMethod = AuthMethod
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if CircuitId is not None:
            self._CircuitId = CircuitId
            properties['CircuitId'] = CircuitId
        if Area1 is not None:
            self._Area1 = Area1
            properties['Area1'] = Area1
        if Area2 is not None:
            self._Area2 = Area2
            properties['Area2'] = Area2
        if Area3 is not None:
            self._Area3 = Area3
            properties['Area3'] = Area3
        if MetricMode is not None:
            self._MetricMode = MetricMode
            properties['MetricMode'] = MetricMode
        if TeRouterId is not None:
            self._TeRouterId = TeRouterId
            properties['TeRouterId'] = TeRouterId
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if HelloMultiplier is not None:
            self._HelloMultiplier = HelloMultiplier
            properties['HelloMultiplier'] = HelloMultiplier
        if PsnInterval is not None:
            self._PsnInterval = PsnInterval
            properties['PsnInterval'] = PsnInterval
        if LspRefreshTime is not None:
            self._LspRefreshTime = LspRefreshTime
            properties['LspRefreshTime'] = LspRefreshTime
        if RetransInterval is not None:
            self._RetransInterval = RetransInterval
            properties['RetransInterval'] = RetransInterval
        if HelloPadding is not None:
            self._HelloPadding = HelloPadding
            properties['HelloPadding'] = HelloPadding
        if LspSize is not None:
            self._LspSize = LspSize
            properties['LspSize'] = LspSize
        if ValidateIpAddr is not None:
            self._ValidateIpAddr = ValidateIpAddr
            properties['ValidateIpAddr'] = ValidateIpAddr
        if EnableGracefulRestart is not None:
            self._EnableGracefulRestart = EnableGracefulRestart
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if EnableViewRoutes is not None:
            self._EnableViewRoutes = EnableViewRoutes
            properties['EnableViewRoutes'] = EnableViewRoutes
        if EnableBFD is not None:
            self._EnableBFD = EnableBFD
            properties['EnableBFD'] = EnableBFD

        super(IsisProtocolConfig, self).edit(**properties)

    @property
    def RouterState(self):
        """
        get the value of property _RouterState
        """
        if self.force_auto_sync:
            self.get('RouterState')
        return self._RouterState

    @property
    def ThreeWayP2pAdjState(self):
        """
        get the value of property _ThreeWayP2pAdjState
        """
        if self.force_auto_sync:
            self.get('ThreeWayP2pAdjState')
        return self._ThreeWayP2pAdjState

    @property
    def L1BroadcastAdjState(self):
        """
        get the value of property _L1BroadcastAdjState
        """
        if self.force_auto_sync:
            self.get('L1BroadcastAdjState')
        return self._L1BroadcastAdjState

    @property
    def L2BroadcastAdjState(self):
        """
        get the value of property _L2BroadcastAdjState
        """
        if self.force_auto_sync:
            self.get('L2BroadcastAdjState')
        return self._L2BroadcastAdjState

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @property
    def Level(self):
        """
        get the value of property _Level
        """
        if self.force_auto_sync:
            self.get('Level')
        return self._Level

    @property
    def NetworkType(self):
        """
        get the value of property _NetworkType
        """
        if self.force_auto_sync:
            self.get('NetworkType')
        return self._NetworkType

    @property
    def SystemId(self):
        """
        get the value of property _SystemId
        """
        if self.force_auto_sync:
            self.get('SystemId')
        return self._SystemId

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def L1BroadcastLanId(self):
        """
        get the value of property _L1BroadcastLanId
        """
        if self.force_auto_sync:
            self.get('L1BroadcastLanId')
        return self._L1BroadcastLanId

    @property
    def L2BroadcastLanId(self):
        """
        get the value of property _L2BroadcastLanId
        """
        if self.force_auto_sync:
            self.get('L2BroadcastLanId')
        return self._L2BroadcastLanId

    @property
    def SystemIdLearned(self):
        """
        get the value of property _SystemIdLearned
        """
        if self.force_auto_sync:
            self.get('SystemIdLearned')
        return self._SystemIdLearned

    @property
    def CircuitIdLearned(self):
        """
        get the value of property _CircuitIdLearned
        """
        if self.force_auto_sync:
            self.get('CircuitIdLearned')
        return self._CircuitIdLearned

    @property
    def AuthMethod(self):
        """
        get the value of property _AuthMethod
        """
        if self.force_auto_sync:
            self.get('AuthMethod')
        return self._AuthMethod

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def CircuitId(self):
        """
        get the value of property _CircuitId
        """
        if self.force_auto_sync:
            self.get('CircuitId')
        return self._CircuitId

    @property
    def Area1(self):
        """
        get the value of property _Area1
        """
        if self.force_auto_sync:
            self.get('Area1')
        return self._Area1

    @property
    def Area2(self):
        """
        get the value of property _Area2
        """
        if self.force_auto_sync:
            self.get('Area2')
        return self._Area2

    @property
    def Area3(self):
        """
        get the value of property _Area3
        """
        if self.force_auto_sync:
            self.get('Area3')
        return self._Area3

    @property
    def MetricMode(self):
        """
        get the value of property _MetricMode
        """
        if self.force_auto_sync:
            self.get('MetricMode')
        return self._MetricMode

    @property
    def TeRouterId(self):
        """
        get the value of property _TeRouterId
        """
        if self.force_auto_sync:
            self.get('TeRouterId')
        return self._TeRouterId

    @property
    def HelloInterval(self):
        """
        get the value of property _HelloInterval
        """
        if self.force_auto_sync:
            self.get('HelloInterval')
        return self._HelloInterval

    @property
    def HelloMultiplier(self):
        """
        get the value of property _HelloMultiplier
        """
        if self.force_auto_sync:
            self.get('HelloMultiplier')
        return self._HelloMultiplier

    @property
    def PsnInterval(self):
        """
        get the value of property _PsnInterval
        """
        if self.force_auto_sync:
            self.get('PsnInterval')
        return self._PsnInterval

    @property
    def LspRefreshTime(self):
        """
        get the value of property _LspRefreshTime
        """
        if self.force_auto_sync:
            self.get('LspRefreshTime')
        return self._LspRefreshTime

    @property
    def RetransInterval(self):
        """
        get the value of property _RetransInterval
        """
        if self.force_auto_sync:
            self.get('RetransInterval')
        return self._RetransInterval

    @property
    def HelloPadding(self):
        """
        get the value of property _HelloPadding
        """
        if self.force_auto_sync:
            self.get('HelloPadding')
        return self._HelloPadding

    @property
    def LspSize(self):
        """
        get the value of property _LspSize
        """
        if self.force_auto_sync:
            self.get('LspSize')
        return self._LspSize

    @property
    def ValidateIpAddr(self):
        """
        get the value of property _ValidateIpAddr
        """
        if self.force_auto_sync:
            self.get('ValidateIpAddr')
        return self._ValidateIpAddr

    @property
    def EnableGracefulRestart(self):
        """
        get the value of property _EnableGracefulRestart
        """
        if self.force_auto_sync:
            self.get('EnableGracefulRestart')
        return self._EnableGracefulRestart

    @property
    def LspCount(self):
        """
        get the value of property _LspCount
        """
        if self.force_auto_sync:
            self.get('LspCount')
        return self._LspCount

    @property
    def EnableViewRoutes(self):
        """
        get the value of property _EnableViewRoutes
        """
        if self.force_auto_sync:
            self.get('EnableViewRoutes')
        return self._EnableViewRoutes

    @property
    def EnableBFD(self):
        """
        get the value of property _EnableBFD
        """
        if self.force_auto_sync:
            self.get('EnableBFD')
        return self._EnableBFD

    @Level.setter
    def Level(self, value):
        self._Level = value
        self.edit(Level=value)

    @NetworkType.setter
    def NetworkType(self, value):
        self._NetworkType = value
        self.edit(NetworkType=value)

    @SystemId.setter
    def SystemId(self, value):
        self._SystemId = value
        self.edit(SystemId=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @AuthMethod.setter
    def AuthMethod(self, value):
        self._AuthMethod = value
        self.edit(AuthMethod=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @CircuitId.setter
    def CircuitId(self, value):
        self._CircuitId = value
        self.edit(CircuitId=value)

    @Area1.setter
    def Area1(self, value):
        self._Area1 = value
        self.edit(Area1=value)

    @Area2.setter
    def Area2(self, value):
        self._Area2 = value
        self.edit(Area2=value)

    @Area3.setter
    def Area3(self, value):
        self._Area3 = value
        self.edit(Area3=value)

    @MetricMode.setter
    def MetricMode(self, value):
        self._MetricMode = value
        self.edit(MetricMode=value)

    @TeRouterId.setter
    def TeRouterId(self, value):
        self._TeRouterId = value
        self.edit(TeRouterId=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._HelloMultiplier = value
        self.edit(HelloMultiplier=value)

    @PsnInterval.setter
    def PsnInterval(self, value):
        self._PsnInterval = value
        self.edit(PsnInterval=value)

    @LspRefreshTime.setter
    def LspRefreshTime(self, value):
        self._LspRefreshTime = value
        self.edit(LspRefreshTime=value)

    @RetransInterval.setter
    def RetransInterval(self, value):
        self._RetransInterval = value
        self.edit(RetransInterval=value)

    @HelloPadding.setter
    def HelloPadding(self, value):
        self._HelloPadding = value
        self.edit(HelloPadding=value)

    @LspSize.setter
    def LspSize(self, value):
        self._LspSize = value
        self.edit(LspSize=value)

    @ValidateIpAddr.setter
    def ValidateIpAddr(self, value):
        self._ValidateIpAddr = value
        self.edit(ValidateIpAddr=value)

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._EnableGracefulRestart = value
        self.edit(EnableGracefulRestart=value)

    @EnableViewRoutes.setter
    def EnableViewRoutes(self, value):
        self._EnableViewRoutes = value
        self.edit(EnableViewRoutes=value)

    @EnableBFD.setter
    def EnableBFD(self, value):
        self._EnableBFD = value
        self.edit(EnableBFD=value)

    def _set_routerstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterState = EnumRouterState.%s' % value[:seperate])

    def _set_threewayp2padjstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ThreeWayP2pAdjState = EnumThreeWayP2PAdjState.%s' % value[:seperate])

    def _set_l1broadcastadjstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._L1BroadcastAdjState = EnumBroadcastAdjState.%s' % value[:seperate])

    def _set_l2broadcastadjstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._L2BroadcastAdjState = EnumBroadcastAdjState.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumIpVersion.%s' % value[:seperate])

    def _set_level_with_str(self, value):
        seperate = value.find(':')
        exec('self._Level = EnumLevel.%s' % value[:seperate])

    def _set_networktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._NetworkType = EnumNetworkType.%s' % value[:seperate])

    def _set_systemid_with_str(self, value):
        self._SystemId = value

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_l1broadcastlanid_with_str(self, value):
        self._L1BroadcastLanId = value

    def _set_l2broadcastlanid_with_str(self, value):
        self._L2BroadcastLanId = value

    def _set_systemidlearned_with_str(self, value):
        self._SystemIdLearned = value

    def _set_circuitidlearned_with_str(self, value):
        try:
            self._CircuitIdLearned = int(value)
        except ValueError:
            self._CircuitIdLearned = hex(int(value, 16))

    def _set_authmethod_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthMethod = EnumAuthMethod.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_circuitid_with_str(self, value):
        try:
            self._CircuitId = int(value)
        except ValueError:
            self._CircuitId = hex(int(value, 16))

    def _set_area1_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Area1 = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Area1.append(int(str_value))
            except ValueError:
                self._Area1.append(hex(int(str_value, 16)))

    def _set_area2_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Area2 = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Area2.append(int(str_value))
            except ValueError:
                self._Area2.append(hex(int(str_value, 16)))

    def _set_area3_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Area3 = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Area3.append(int(str_value))
            except ValueError:
                self._Area3.append(hex(int(str_value, 16)))

    def _set_metricmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._MetricMode = EnumMetricMode.%s' % value[:seperate])

    def _set_terouterid_with_str(self, value):
        self._TeRouterId = value

    def _set_hellointerval_with_str(self, value):
        try:
            self._HelloInterval = int(value)
        except ValueError:
            self._HelloInterval = hex(int(value, 16))

    def _set_hellomultiplier_with_str(self, value):
        try:
            self._HelloMultiplier = int(value)
        except ValueError:
            self._HelloMultiplier = hex(int(value, 16))

    def _set_psninterval_with_str(self, value):
        try:
            self._PsnInterval = int(value)
        except ValueError:
            self._PsnInterval = hex(int(value, 16))

    def _set_lsprefreshtime_with_str(self, value):
        try:
            self._LspRefreshTime = int(value)
        except ValueError:
            self._LspRefreshTime = hex(int(value, 16))

    def _set_retransinterval_with_str(self, value):
        try:
            self._RetransInterval = int(value)
        except ValueError:
            self._RetransInterval = hex(int(value, 16))

    def _set_hellopadding_with_str(self, value):
        self._HelloPadding = (value == 'True')

    def _set_lspsize_with_str(self, value):
        try:
            self._LspSize = int(value)
        except ValueError:
            self._LspSize = hex(int(value, 16))

    def _set_validateipaddr_with_str(self, value):
        self._ValidateIpAddr = (value == 'True')

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_lspcount_with_str(self, value):
        try:
            self._LspCount = int(value)
        except ValueError:
            self._LspCount = hex(int(value, 16))

    def _set_enableviewroutes_with_str(self, value):
        self._EnableViewRoutes = (value == 'True')

    def _set_enablebfd_with_str(self, value):
        self._EnableBFD = (value == 'True')

