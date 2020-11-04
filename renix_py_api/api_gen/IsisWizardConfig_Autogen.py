"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class IsisWizardConfig(ProtocolWizardConfig):
    def __init__(self, UseMacAsSystemId=None, SystemId=None, SystemIdStep=None, Level=None, IpVersion=None, NetworkType=None, Priority=None, MetricMode=None, AuthMethod=None, Password=None, Area=None, HelloPadding=None, EnableGracefulRestart=None, EnableBFD=None, **kwargs):
        self._UseMacAsSystemId = UseMacAsSystemId  # Use Source Mac As System ID
        self._SystemId = SystemId  # System ID
        self._SystemIdStep = SystemIdStep  # Step
        self._Level = Level  # Level
        self._IpVersion = IpVersion  # IP Version
        self._NetworkType = NetworkType  # Network Type
        self._Priority = Priority  # Router Priority
        self._MetricMode = MetricMode  # Metric Mode
        self._AuthMethod = AuthMethod  # Authentication
        self._Password = Password  # Password
        self._Area = Area  # Area
        self._HelloPadding = HelloPadding  # Hello Padding
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._EnableBFD = EnableBFD  # Enable BFD

        properties = kwargs.copy()
        if UseMacAsSystemId is not None:
            properties['UseMacAsSystemId'] = UseMacAsSystemId
        if SystemId is not None:
            properties['SystemId'] = SystemId
        if SystemIdStep is not None:
            properties['SystemIdStep'] = SystemIdStep
        if Level is not None:
            properties['Level'] = Level
        if IpVersion is not None:
            properties['IpVersion'] = IpVersion
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            properties['Priority'] = Priority
        if MetricMode is not None:
            properties['MetricMode'] = MetricMode
        if AuthMethod is not None:
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            properties['Password'] = Password
        if Area is not None:
            properties['Area'] = Area
        if HelloPadding is not None:
            properties['HelloPadding'] = HelloPadding
        if EnableGracefulRestart is not None:
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if EnableBFD is not None:
            properties['EnableBFD'] = EnableBFD

        # call base class function, and it will send message to renix server to create a class.
        super(IsisWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, UseMacAsSystemId=None, SystemId=None, SystemIdStep=None, Level=None, IpVersion=None, NetworkType=None, Priority=None, MetricMode=None, AuthMethod=None, Password=None, Area=None, HelloPadding=None, EnableGracefulRestart=None, EnableBFD=None, **kwargs):
        properties = kwargs.copy()
        if UseMacAsSystemId is not None:
            self._UseMacAsSystemId = UseMacAsSystemId
            properties['UseMacAsSystemId'] = UseMacAsSystemId
        if SystemId is not None:
            self._SystemId = SystemId
            properties['SystemId'] = SystemId
        if SystemIdStep is not None:
            self._SystemIdStep = SystemIdStep
            properties['SystemIdStep'] = SystemIdStep
        if Level is not None:
            self._Level = Level
            properties['Level'] = Level
        if IpVersion is not None:
            self._IpVersion = IpVersion
            properties['IpVersion'] = IpVersion
        if NetworkType is not None:
            self._NetworkType = NetworkType
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if MetricMode is not None:
            self._MetricMode = MetricMode
            properties['MetricMode'] = MetricMode
        if AuthMethod is not None:
            self._AuthMethod = AuthMethod
            properties['AuthMethod'] = AuthMethod
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if Area is not None:
            self._Area = Area
            properties['Area'] = Area
        if HelloPadding is not None:
            self._HelloPadding = HelloPadding
            properties['HelloPadding'] = HelloPadding
        if EnableGracefulRestart is not None:
            self._EnableGracefulRestart = EnableGracefulRestart
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if EnableBFD is not None:
            self._EnableBFD = EnableBFD
            properties['EnableBFD'] = EnableBFD

        super(IsisWizardConfig, self).edit(**properties)

    @property
    def UseMacAsSystemId(self):
        """
        get the value of property _UseMacAsSystemId
        """
        if self.force_auto_sync:
            self.get('UseMacAsSystemId')
        return self._UseMacAsSystemId

    @property
    def SystemId(self):
        """
        get the value of property _SystemId
        """
        if self.force_auto_sync:
            self.get('SystemId')
        return self._SystemId

    @property
    def SystemIdStep(self):
        """
        get the value of property _SystemIdStep
        """
        if self.force_auto_sync:
            self.get('SystemIdStep')
        return self._SystemIdStep

    @property
    def Level(self):
        """
        get the value of property _Level
        """
        if self.force_auto_sync:
            self.get('Level')
        return self._Level

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

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
    def MetricMode(self):
        """
        get the value of property _MetricMode
        """
        if self.force_auto_sync:
            self.get('MetricMode')
        return self._MetricMode

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
    def Area(self):
        """
        get the value of property _Area
        """
        if self.force_auto_sync:
            self.get('Area')
        return self._Area

    @property
    def HelloPadding(self):
        """
        get the value of property _HelloPadding
        """
        if self.force_auto_sync:
            self.get('HelloPadding')
        return self._HelloPadding

    @property
    def EnableGracefulRestart(self):
        """
        get the value of property _EnableGracefulRestart
        """
        if self.force_auto_sync:
            self.get('EnableGracefulRestart')
        return self._EnableGracefulRestart

    @property
    def EnableBFD(self):
        """
        get the value of property _EnableBFD
        """
        if self.force_auto_sync:
            self.get('EnableBFD')
        return self._EnableBFD

    @UseMacAsSystemId.setter
    def UseMacAsSystemId(self, value):
        self._UseMacAsSystemId = value
        self.edit(UseMacAsSystemId=value)

    @SystemId.setter
    def SystemId(self, value):
        self._SystemId = value
        self.edit(SystemId=value)

    @SystemIdStep.setter
    def SystemIdStep(self, value):
        self._SystemIdStep = value
        self.edit(SystemIdStep=value)

    @Level.setter
    def Level(self, value):
        self._Level = value
        self.edit(Level=value)

    @IpVersion.setter
    def IpVersion(self, value):
        self._IpVersion = value
        self.edit(IpVersion=value)

    @NetworkType.setter
    def NetworkType(self, value):
        self._NetworkType = value
        self.edit(NetworkType=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @MetricMode.setter
    def MetricMode(self, value):
        self._MetricMode = value
        self.edit(MetricMode=value)

    @AuthMethod.setter
    def AuthMethod(self, value):
        self._AuthMethod = value
        self.edit(AuthMethod=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @Area.setter
    def Area(self, value):
        self._Area = value
        self.edit(Area=value)

    @HelloPadding.setter
    def HelloPadding(self, value):
        self._HelloPadding = value
        self.edit(HelloPadding=value)

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._EnableGracefulRestart = value
        self.edit(EnableGracefulRestart=value)

    @EnableBFD.setter
    def EnableBFD(self, value):
        self._EnableBFD = value
        self.edit(EnableBFD=value)

    def _set_usemacassystemid_with_str(self, value):
        self._UseMacAsSystemId = (value == 'True')

    def _set_systemid_with_str(self, value):
        self._SystemId = value

    def _set_systemidstep_with_str(self, value):
        self._SystemIdStep = value

    def _set_level_with_str(self, value):
        seperate = value.find(':')
        exec('self._Level = EnumLevel.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumIpVersion.%s' % value[:seperate])

    def _set_networktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._NetworkType = EnumNetworkType.%s' % value[:seperate])

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_metricmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._MetricMode = EnumMetricMode.%s' % value[:seperate])

    def _set_authmethod_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthMethod = EnumAuthMethod.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_area_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Area = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Area.append(int(str_value))
            except ValueError:
                self._Area.append(hex(int(str_value, 16)))

    def _set_hellopadding_with_str(self, value):
        self._HelloPadding = (value == 'True')

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_enablebfd_with_str(self, value):
        self._EnableBFD = (value == 'True')

