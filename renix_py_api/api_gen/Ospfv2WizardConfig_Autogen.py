"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class Ospfv2WizardConfig(ProtocolWizardConfig):
    def __init__(self, AreaId=None, AreaIdStep=None, EnableAreaIdStepByPort=None, AreaIdStepByPort=None, NetworkType=None, Priority=None, AuthenticationType=None, Password=None, Md5KeyId=None, Options=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableBfd=None, **kwargs):
        self._AreaId = AreaId  # Area ID
        self._AreaIdStep = AreaIdStep  # Area ID Step
        self._EnableAreaIdStepByPort = EnableAreaIdStepByPort  # Enable Graceful Restart
        self._AreaIdStepByPort = AreaIdStepByPort  # Area ID Step
        self._NetworkType = NetworkType  # Network Type
        self._Priority = Priority  # Router Priority
        self._AuthenticationType = AuthenticationType  # Authentication Type
        self._Password = Password  # Password
        self._Md5KeyId = Md5KeyId  # MD5 Key ID
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)  # Options
        self._EnableGracefulRestart = EnableGracefulRestart  # Enable Graceful Restart
        self._GracefulRestartReason = GracefulRestartReason  # Graceful Restart Reason
        self._EnableBfd = EnableBfd  # Enable BFD

        properties = kwargs.copy()
        if AreaId is not None:
            properties['AreaId'] = AreaId
        if AreaIdStep is not None:
            properties['AreaIdStep'] = AreaIdStep
        if EnableAreaIdStepByPort is not None:
            properties['EnableAreaIdStepByPort'] = EnableAreaIdStepByPort
        if AreaIdStepByPort is not None:
            properties['AreaIdStepByPort'] = AreaIdStepByPort
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            properties['Priority'] = Priority
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
        if EnableGracefulRestart is not None:
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if GracefulRestartReason is not None:
            properties['GracefulRestartReason'] = GracefulRestartReason
        if EnableBfd is not None:
            properties['EnableBfd'] = EnableBfd

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2WizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AreaId=None, AreaIdStep=None, EnableAreaIdStepByPort=None, AreaIdStepByPort=None, NetworkType=None, Priority=None, AuthenticationType=None, Password=None, Md5KeyId=None, Options=None, EnableGracefulRestart=None, GracefulRestartReason=None, EnableBfd=None, **kwargs):
        properties = kwargs.copy()
        if AreaId is not None:
            self._AreaId = AreaId
            properties['AreaId'] = AreaId
        if AreaIdStep is not None:
            self._AreaIdStep = AreaIdStep
            properties['AreaIdStep'] = AreaIdStep
        if EnableAreaIdStepByPort is not None:
            self._EnableAreaIdStepByPort = EnableAreaIdStepByPort
            properties['EnableAreaIdStepByPort'] = EnableAreaIdStepByPort
        if AreaIdStepByPort is not None:
            self._AreaIdStepByPort = AreaIdStepByPort
            properties['AreaIdStepByPort'] = AreaIdStepByPort
        if NetworkType is not None:
            self._NetworkType = NetworkType
            properties['NetworkType'] = NetworkType
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
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
        if EnableGracefulRestart is not None:
            self._EnableGracefulRestart = EnableGracefulRestart
            properties['EnableGracefulRestart'] = EnableGracefulRestart
        if GracefulRestartReason is not None:
            self._GracefulRestartReason = GracefulRestartReason
            properties['GracefulRestartReason'] = GracefulRestartReason
        if EnableBfd is not None:
            self._EnableBfd = EnableBfd
            properties['EnableBfd'] = EnableBfd

        super(Ospfv2WizardConfig, self).edit(**properties)

    @property
    def AreaId(self):
        """
        get the value of property _AreaId
        """
        if self.force_auto_sync:
            self.get('AreaId')
        return self._AreaId

    @property
    def AreaIdStep(self):
        """
        get the value of property _AreaIdStep
        """
        if self.force_auto_sync:
            self.get('AreaIdStep')
        return self._AreaIdStep

    @property
    def EnableAreaIdStepByPort(self):
        """
        get the value of property _EnableAreaIdStepByPort
        """
        if self.force_auto_sync:
            self.get('EnableAreaIdStepByPort')
        return self._EnableAreaIdStepByPort

    @property
    def AreaIdStepByPort(self):
        """
        get the value of property _AreaIdStepByPort
        """
        if self.force_auto_sync:
            self.get('AreaIdStepByPort')
        return self._AreaIdStepByPort

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
    def EnableBfd(self):
        """
        get the value of property _EnableBfd
        """
        if self.force_auto_sync:
            self.get('EnableBfd')
        return self._EnableBfd

    @AreaId.setter
    def AreaId(self, value):
        self._AreaId = value
        self.edit(AreaId=value)

    @AreaIdStep.setter
    def AreaIdStep(self, value):
        self._AreaIdStep = value
        self.edit(AreaIdStep=value)

    @EnableAreaIdStepByPort.setter
    def EnableAreaIdStepByPort(self, value):
        self._EnableAreaIdStepByPort = value
        self.edit(EnableAreaIdStepByPort=value)

    @AreaIdStepByPort.setter
    def AreaIdStepByPort(self, value):
        self._AreaIdStepByPort = value
        self.edit(AreaIdStepByPort=value)

    @NetworkType.setter
    def NetworkType(self, value):
        self._NetworkType = value
        self.edit(NetworkType=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

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

    @EnableGracefulRestart.setter
    def EnableGracefulRestart(self, value):
        self._EnableGracefulRestart = value
        self.edit(EnableGracefulRestart=value)

    @GracefulRestartReason.setter
    def GracefulRestartReason(self, value):
        self._GracefulRestartReason = value
        self.edit(GracefulRestartReason=value)

    @EnableBfd.setter
    def EnableBfd(self, value):
        self._EnableBfd = value
        self.edit(EnableBfd=value)

    def _set_areaid_with_str(self, value):
        self._AreaId = value

    def _set_areaidstep_with_str(self, value):
        self._AreaIdStep = value

    def _set_enableareaidstepbyport_with_str(self, value):
        self._EnableAreaIdStepByPort = (value == 'True')

    def _set_areaidstepbyport_with_str(self, value):
        self._AreaIdStepByPort = value

    def _set_networktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._NetworkType = EnumOspfNetworkType.%s' % value[:seperate])

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

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

    def _set_enablegracefulrestart_with_str(self, value):
        self._EnableGracefulRestart = (value == 'True')

    def _set_gracefulrestartreason_with_str(self, value):
        seperate = value.find(':')
        exec('self._GracefulRestartReason = EnumOspfv2ReasonType.%s' % value[:seperate])

    def _set_enablebfd_with_str(self, value):
        self._EnableBfd = (value == 'True')

