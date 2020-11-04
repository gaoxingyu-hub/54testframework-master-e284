"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dhcpv6ServerConfig(L23ProtocolConfig):
    def __init__(self, EmulationMode=None, RenewalTimer=None, RebindingTimer=None, EnableDelayedAuth=None, DhcpRealm=None, AuthenticationKeyId=None, AuthenticationKey=None, AuthenticationKeyType=None, EnabledReconfigureKey=None, ReconfigureKey=None, ReconfigureKeyType=None, EnabledDhcpv6Only=None, **kwargs):
        self._EmulationMode = EmulationMode  # Emulation Mode
        self._ServerState = EnumDhcpv6ServerState.NOTSTART  # State, not editable
        self._RenewalTimer = RenewalTimer  # Renewal Timer(%)
        self._RebindingTimer = RebindingTimer  # Rebinding Timer(%)
        self._EnableDelayedAuth = EnableDelayedAuth  # Enable Delayed Authentication 
        self._DhcpRealm = DhcpRealm  # DHCP Realm
        self._AuthenticationKeyId = AuthenticationKeyId  # Authentication Key ID
        self._AuthenticationKey = AuthenticationKey  # Authentication Key
        self._AuthenticationKeyType = AuthenticationKeyType  # Authentication Key Type
        self._EnabledReconfigureKey = EnabledReconfigureKey  # Enable Reconfigure Key
        self._ReconfigureKey = ReconfigureKey  # Reconfigure Key
        self._ReconfigureKeyType = ReconfigureKeyType  # Reconfigure Key  Type
        self._EnabledDhcpv6Only = EnabledDhcpv6Only  # Enable DHCPv6 Only

        properties = kwargs.copy()
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode
        if RenewalTimer is not None:
            properties['RenewalTimer'] = RenewalTimer
        if RebindingTimer is not None:
            properties['RebindingTimer'] = RebindingTimer
        if EnableDelayedAuth is not None:
            properties['EnableDelayedAuth'] = EnableDelayedAuth
        if DhcpRealm is not None:
            properties['DhcpRealm'] = DhcpRealm
        if AuthenticationKeyId is not None:
            properties['AuthenticationKeyId'] = AuthenticationKeyId
        if AuthenticationKey is not None:
            properties['AuthenticationKey'] = AuthenticationKey
        if AuthenticationKeyType is not None:
            properties['AuthenticationKeyType'] = AuthenticationKeyType
        if EnabledReconfigureKey is not None:
            properties['EnabledReconfigureKey'] = EnabledReconfigureKey
        if ReconfigureKey is not None:
            properties['ReconfigureKey'] = ReconfigureKey
        if ReconfigureKeyType is not None:
            properties['ReconfigureKeyType'] = ReconfigureKeyType
        if EnabledDhcpv6Only is not None:
            properties['EnabledDhcpv6Only'] = EnabledDhcpv6Only

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ServerConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EmulationMode=None, RenewalTimer=None, RebindingTimer=None, EnableDelayedAuth=None, DhcpRealm=None, AuthenticationKeyId=None, AuthenticationKey=None, AuthenticationKeyType=None, EnabledReconfigureKey=None, ReconfigureKey=None, ReconfigureKeyType=None, EnabledDhcpv6Only=None, **kwargs):
        properties = kwargs.copy()
        if EmulationMode is not None:
            self._EmulationMode = EmulationMode
            properties['EmulationMode'] = EmulationMode
        if RenewalTimer is not None:
            self._RenewalTimer = RenewalTimer
            properties['RenewalTimer'] = RenewalTimer
        if RebindingTimer is not None:
            self._RebindingTimer = RebindingTimer
            properties['RebindingTimer'] = RebindingTimer
        if EnableDelayedAuth is not None:
            self._EnableDelayedAuth = EnableDelayedAuth
            properties['EnableDelayedAuth'] = EnableDelayedAuth
        if DhcpRealm is not None:
            self._DhcpRealm = DhcpRealm
            properties['DhcpRealm'] = DhcpRealm
        if AuthenticationKeyId is not None:
            self._AuthenticationKeyId = AuthenticationKeyId
            properties['AuthenticationKeyId'] = AuthenticationKeyId
        if AuthenticationKey is not None:
            self._AuthenticationKey = AuthenticationKey
            properties['AuthenticationKey'] = AuthenticationKey
        if AuthenticationKeyType is not None:
            self._AuthenticationKeyType = AuthenticationKeyType
            properties['AuthenticationKeyType'] = AuthenticationKeyType
        if EnabledReconfigureKey is not None:
            self._EnabledReconfigureKey = EnabledReconfigureKey
            properties['EnabledReconfigureKey'] = EnabledReconfigureKey
        if ReconfigureKey is not None:
            self._ReconfigureKey = ReconfigureKey
            properties['ReconfigureKey'] = ReconfigureKey
        if ReconfigureKeyType is not None:
            self._ReconfigureKeyType = ReconfigureKeyType
            properties['ReconfigureKeyType'] = ReconfigureKeyType
        if EnabledDhcpv6Only is not None:
            self._EnabledDhcpv6Only = EnabledDhcpv6Only
            properties['EnabledDhcpv6Only'] = EnabledDhcpv6Only

        super(Dhcpv6ServerConfig, self).edit(**properties)

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        if self.force_auto_sync:
            self.get('EmulationMode')
        return self._EmulationMode

    @property
    def ServerState(self):
        """
        get the value of property _ServerState
        """
        if self.force_auto_sync:
            self.get('ServerState')
        return self._ServerState

    @property
    def RenewalTimer(self):
        """
        get the value of property _RenewalTimer
        """
        if self.force_auto_sync:
            self.get('RenewalTimer')
        return self._RenewalTimer

    @property
    def RebindingTimer(self):
        """
        get the value of property _RebindingTimer
        """
        if self.force_auto_sync:
            self.get('RebindingTimer')
        return self._RebindingTimer

    @property
    def EnableDelayedAuth(self):
        """
        get the value of property _EnableDelayedAuth
        """
        if self.force_auto_sync:
            self.get('EnableDelayedAuth')
        return self._EnableDelayedAuth

    @property
    def DhcpRealm(self):
        """
        get the value of property _DhcpRealm
        """
        if self.force_auto_sync:
            self.get('DhcpRealm')
        return self._DhcpRealm

    @property
    def AuthenticationKeyId(self):
        """
        get the value of property _AuthenticationKeyId
        """
        if self.force_auto_sync:
            self.get('AuthenticationKeyId')
        return self._AuthenticationKeyId

    @property
    def AuthenticationKey(self):
        """
        get the value of property _AuthenticationKey
        """
        if self.force_auto_sync:
            self.get('AuthenticationKey')
        return self._AuthenticationKey

    @property
    def AuthenticationKeyType(self):
        """
        get the value of property _AuthenticationKeyType
        """
        if self.force_auto_sync:
            self.get('AuthenticationKeyType')
        return self._AuthenticationKeyType

    @property
    def EnabledReconfigureKey(self):
        """
        get the value of property _EnabledReconfigureKey
        """
        if self.force_auto_sync:
            self.get('EnabledReconfigureKey')
        return self._EnabledReconfigureKey

    @property
    def ReconfigureKey(self):
        """
        get the value of property _ReconfigureKey
        """
        if self.force_auto_sync:
            self.get('ReconfigureKey')
        return self._ReconfigureKey

    @property
    def ReconfigureKeyType(self):
        """
        get the value of property _ReconfigureKeyType
        """
        if self.force_auto_sync:
            self.get('ReconfigureKeyType')
        return self._ReconfigureKeyType

    @property
    def EnabledDhcpv6Only(self):
        """
        get the value of property _EnabledDhcpv6Only
        """
        if self.force_auto_sync:
            self.get('EnabledDhcpv6Only')
        return self._EnabledDhcpv6Only

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value
        self.edit(EmulationMode=value)

    @RenewalTimer.setter
    def RenewalTimer(self, value):
        self._RenewalTimer = value
        self.edit(RenewalTimer=value)

    @RebindingTimer.setter
    def RebindingTimer(self, value):
        self._RebindingTimer = value
        self.edit(RebindingTimer=value)

    @EnableDelayedAuth.setter
    def EnableDelayedAuth(self, value):
        self._EnableDelayedAuth = value
        self.edit(EnableDelayedAuth=value)

    @DhcpRealm.setter
    def DhcpRealm(self, value):
        self._DhcpRealm = value
        self.edit(DhcpRealm=value)

    @AuthenticationKeyId.setter
    def AuthenticationKeyId(self, value):
        self._AuthenticationKeyId = value
        self.edit(AuthenticationKeyId=value)

    @AuthenticationKey.setter
    def AuthenticationKey(self, value):
        self._AuthenticationKey = value
        self.edit(AuthenticationKey=value)

    @AuthenticationKeyType.setter
    def AuthenticationKeyType(self, value):
        self._AuthenticationKeyType = value
        self.edit(AuthenticationKeyType=value)

    @EnabledReconfigureKey.setter
    def EnabledReconfigureKey(self, value):
        self._EnabledReconfigureKey = value
        self.edit(EnabledReconfigureKey=value)

    @ReconfigureKey.setter
    def ReconfigureKey(self, value):
        self._ReconfigureKey = value
        self.edit(ReconfigureKey=value)

    @ReconfigureKeyType.setter
    def ReconfigureKeyType(self, value):
        self._ReconfigureKeyType = value
        self.edit(ReconfigureKeyType=value)

    @EnabledDhcpv6Only.setter
    def EnabledDhcpv6Only(self, value):
        self._EnabledDhcpv6Only = value
        self.edit(EnabledDhcpv6Only=value)

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumDhcpv6EmulationServerMode.%s' % value[:seperate])

    def _set_serverstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ServerState = EnumDhcpv6ServerState.%s' % value[:seperate])

    def _set_renewaltimer_with_str(self, value):
        self._RenewalTimer = float(value)

    def _set_rebindingtimer_with_str(self, value):
        self._RebindingTimer = float(value)

    def _set_enabledelayedauth_with_str(self, value):
        self._EnableDelayedAuth = (value == 'True')

    def _set_dhcprealm_with_str(self, value):
        self._DhcpRealm = value

    def _set_authenticationkeyid_with_str(self, value):
        try:
            self._AuthenticationKeyId = int(value)
        except ValueError:
            self._AuthenticationKeyId = hex(int(value, 16))

    def _set_authenticationkey_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AuthenticationKey = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AuthenticationKey.append(int(str_value))
            except ValueError:
                self._AuthenticationKey.append(hex(int(str_value, 16)))

    def _set_authenticationkeytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AuthenticationKeyType = EnumDhcpv6KeyType.%s' % value[:seperate])

    def _set_enabledreconfigurekey_with_str(self, value):
        self._EnabledReconfigureKey = (value == 'True')

    def _set_reconfigurekey_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ReconfigureKey = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._ReconfigureKey.append(int(str_value))
            except ValueError:
                self._ReconfigureKey.append(hex(int(str_value, 16)))

    def _set_reconfigurekeytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ReconfigureKeyType = EnumDhcpv6KeyType.%s' % value[:seperate])

    def _set_enableddhcpv6only_with_str(self, value):
        self._EnabledDhcpv6Only = (value == 'True')

