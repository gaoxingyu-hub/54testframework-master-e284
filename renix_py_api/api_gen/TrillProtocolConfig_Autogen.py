"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class TrillProtocolConfig(L23ProtocolConfig):
    def __init__(self, SystemID=None, AnnouncingVLANs=None, DesiredDesignatedVLAN=None, EnableMTUTest=None, MinimumAcceptableMTU=None, BypassPseudonode=None, NumberOfMTURetries=None, MTUAckWaitTime=None, DRBPriority=None, Authentication=None, Password=None, InhibitionTime=None, TrillTrafficDisable=None, EndStationServiceDisabled=None, HostName=None, HelloInterval=None, HelloMultiplier=None, NetworkType=None, CircuitID=None, PSNInterval=None, CSNInterval=None, FloodDelay=None, LSPRefreshTime=None, **kwargs):
        self._ProtocolState = TrillProtocolStateEnum.DISABLED  # Protocol State, not editable
        self._RBridgeState = TrillDRBStateEnum.DOWN  # RBridge State, not editable
        self._SystemID = SystemID  # System ID
        self._AnnouncingVLANs = AnnouncingVLANs  # Announcing VLANs
        self._DesiredDesignatedVLAN = DesiredDesignatedVLAN  # Desired Designated VLAN
        self._EnableMTUTest = EnableMTUTest  # Enable MTU Test
        self._MinimumAcceptableMTU = MinimumAcceptableMTU  # Minimum Acceptable MTU
        self._BypassPseudonode = BypassPseudonode  # Bypass Pseudonode
        self._NumberOfMTURetries = NumberOfMTURetries  # Number of MTU Test Tries
        self._MTUAckWaitTime = MTUAckWaitTime  # MTU Ack Wait Time (sec)
        self._DRBPriority = DRBPriority  # DRB Priority
        self._Authentication = Authentication  # Authentication
        self._Password = Password  # Password
        self._InhibitionTime = InhibitionTime  # Inhibition Time
        self._TrillTrafficDisable = TrillTrafficDisable  # TRILL Traffic Disabled
        self._EndStationServiceDisabled = EndStationServiceDisabled  # End-Station Service Disabled
        self._HostName = HostName  # Host Name
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._HelloMultiplier = HelloMultiplier  # Hello Multiplier
        self._NetworkType = NetworkType  # Network Type
        self._CircuitID = CircuitID  # Circuit ID
        self._PSNInterval = PSNInterval  # PSN Interval (sec)
        self._CSNInterval = CSNInterval  # CSN Interval (sec)
        self._FloodDelay = FloodDelay  # Flood Delay (ms)
        self._LSPRefreshTime = LSPRefreshTime  # LSP Refresh Time (sec)
        self._LSPCount = 0  # LSP Count, not editable

        properties = kwargs.copy()
        if SystemID is not None:
            properties['SystemID'] = SystemID
        if AnnouncingVLANs is not None:
            properties['AnnouncingVLANs'] = AnnouncingVLANs
        if DesiredDesignatedVLAN is not None:
            properties['DesiredDesignatedVLAN'] = DesiredDesignatedVLAN
        if EnableMTUTest is not None:
            properties['EnableMTUTest'] = EnableMTUTest
        if MinimumAcceptableMTU is not None:
            properties['MinimumAcceptableMTU'] = MinimumAcceptableMTU
        if BypassPseudonode is not None:
            properties['BypassPseudonode'] = BypassPseudonode
        if NumberOfMTURetries is not None:
            properties['NumberOfMTURetries'] = NumberOfMTURetries
        if MTUAckWaitTime is not None:
            properties['MTUAckWaitTime'] = MTUAckWaitTime
        if DRBPriority is not None:
            properties['DRBPriority'] = DRBPriority
        if Authentication is not None:
            properties['Authentication'] = Authentication
        if Password is not None:
            properties['Password'] = Password
        if InhibitionTime is not None:
            properties['InhibitionTime'] = InhibitionTime
        if TrillTrafficDisable is not None:
            properties['TrillTrafficDisable'] = TrillTrafficDisable
        if EndStationServiceDisabled is not None:
            properties['EndStationServiceDisabled'] = EndStationServiceDisabled
        if HostName is not None:
            properties['HostName'] = HostName
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if HelloMultiplier is not None:
            properties['HelloMultiplier'] = HelloMultiplier
        if NetworkType is not None:
            properties['NetworkType'] = NetworkType
        if CircuitID is not None:
            properties['CircuitID'] = CircuitID
        if PSNInterval is not None:
            properties['PSNInterval'] = PSNInterval
        if CSNInterval is not None:
            properties['CSNInterval'] = CSNInterval
        if FloodDelay is not None:
            properties['FloodDelay'] = FloodDelay
        if LSPRefreshTime is not None:
            properties['LSPRefreshTime'] = LSPRefreshTime

        # call base class function, and it will send message to renix server to create a class.
        super(TrillProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SystemID=None, AnnouncingVLANs=None, DesiredDesignatedVLAN=None, EnableMTUTest=None, MinimumAcceptableMTU=None, BypassPseudonode=None, NumberOfMTURetries=None, MTUAckWaitTime=None, DRBPriority=None, Authentication=None, Password=None, InhibitionTime=None, TrillTrafficDisable=None, EndStationServiceDisabled=None, HostName=None, HelloInterval=None, HelloMultiplier=None, NetworkType=None, CircuitID=None, PSNInterval=None, CSNInterval=None, FloodDelay=None, LSPRefreshTime=None, **kwargs):
        properties = kwargs.copy()
        if SystemID is not None:
            self._SystemID = SystemID
            properties['SystemID'] = SystemID
        if AnnouncingVLANs is not None:
            self._AnnouncingVLANs = AnnouncingVLANs
            properties['AnnouncingVLANs'] = AnnouncingVLANs
        if DesiredDesignatedVLAN is not None:
            self._DesiredDesignatedVLAN = DesiredDesignatedVLAN
            properties['DesiredDesignatedVLAN'] = DesiredDesignatedVLAN
        if EnableMTUTest is not None:
            self._EnableMTUTest = EnableMTUTest
            properties['EnableMTUTest'] = EnableMTUTest
        if MinimumAcceptableMTU is not None:
            self._MinimumAcceptableMTU = MinimumAcceptableMTU
            properties['MinimumAcceptableMTU'] = MinimumAcceptableMTU
        if BypassPseudonode is not None:
            self._BypassPseudonode = BypassPseudonode
            properties['BypassPseudonode'] = BypassPseudonode
        if NumberOfMTURetries is not None:
            self._NumberOfMTURetries = NumberOfMTURetries
            properties['NumberOfMTURetries'] = NumberOfMTURetries
        if MTUAckWaitTime is not None:
            self._MTUAckWaitTime = MTUAckWaitTime
            properties['MTUAckWaitTime'] = MTUAckWaitTime
        if DRBPriority is not None:
            self._DRBPriority = DRBPriority
            properties['DRBPriority'] = DRBPriority
        if Authentication is not None:
            self._Authentication = Authentication
            properties['Authentication'] = Authentication
        if Password is not None:
            self._Password = Password
            properties['Password'] = Password
        if InhibitionTime is not None:
            self._InhibitionTime = InhibitionTime
            properties['InhibitionTime'] = InhibitionTime
        if TrillTrafficDisable is not None:
            self._TrillTrafficDisable = TrillTrafficDisable
            properties['TrillTrafficDisable'] = TrillTrafficDisable
        if EndStationServiceDisabled is not None:
            self._EndStationServiceDisabled = EndStationServiceDisabled
            properties['EndStationServiceDisabled'] = EndStationServiceDisabled
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if HelloMultiplier is not None:
            self._HelloMultiplier = HelloMultiplier
            properties['HelloMultiplier'] = HelloMultiplier
        if NetworkType is not None:
            self._NetworkType = NetworkType
            properties['NetworkType'] = NetworkType
        if CircuitID is not None:
            self._CircuitID = CircuitID
            properties['CircuitID'] = CircuitID
        if PSNInterval is not None:
            self._PSNInterval = PSNInterval
            properties['PSNInterval'] = PSNInterval
        if CSNInterval is not None:
            self._CSNInterval = CSNInterval
            properties['CSNInterval'] = CSNInterval
        if FloodDelay is not None:
            self._FloodDelay = FloodDelay
            properties['FloodDelay'] = FloodDelay
        if LSPRefreshTime is not None:
            self._LSPRefreshTime = LSPRefreshTime
            properties['LSPRefreshTime'] = LSPRefreshTime

        super(TrillProtocolConfig, self).edit(**properties)

    @property
    def ProtocolState(self):
        """
        get the value of property _ProtocolState
        """
        if self.force_auto_sync:
            self.get('ProtocolState')
        return self._ProtocolState

    @property
    def RBridgeState(self):
        """
        get the value of property _RBridgeState
        """
        if self.force_auto_sync:
            self.get('RBridgeState')
        return self._RBridgeState

    @property
    def SystemID(self):
        """
        get the value of property _SystemID
        """
        if self.force_auto_sync:
            self.get('SystemID')
        return self._SystemID

    @property
    def AnnouncingVLANs(self):
        """
        get the value of property _AnnouncingVLANs
        """
        if self.force_auto_sync:
            self.get('AnnouncingVLANs')
        return self._AnnouncingVLANs

    @property
    def DesiredDesignatedVLAN(self):
        """
        get the value of property _DesiredDesignatedVLAN
        """
        if self.force_auto_sync:
            self.get('DesiredDesignatedVLAN')
        return self._DesiredDesignatedVLAN

    @property
    def EnableMTUTest(self):
        """
        get the value of property _EnableMTUTest
        """
        if self.force_auto_sync:
            self.get('EnableMTUTest')
        return self._EnableMTUTest

    @property
    def MinimumAcceptableMTU(self):
        """
        get the value of property _MinimumAcceptableMTU
        """
        if self.force_auto_sync:
            self.get('MinimumAcceptableMTU')
        return self._MinimumAcceptableMTU

    @property
    def BypassPseudonode(self):
        """
        get the value of property _BypassPseudonode
        """
        if self.force_auto_sync:
            self.get('BypassPseudonode')
        return self._BypassPseudonode

    @property
    def NumberOfMTURetries(self):
        """
        get the value of property _NumberOfMTURetries
        """
        if self.force_auto_sync:
            self.get('NumberOfMTURetries')
        return self._NumberOfMTURetries

    @property
    def MTUAckWaitTime(self):
        """
        get the value of property _MTUAckWaitTime
        """
        if self.force_auto_sync:
            self.get('MTUAckWaitTime')
        return self._MTUAckWaitTime

    @property
    def DRBPriority(self):
        """
        get the value of property _DRBPriority
        """
        if self.force_auto_sync:
            self.get('DRBPriority')
        return self._DRBPriority

    @property
    def Authentication(self):
        """
        get the value of property _Authentication
        """
        if self.force_auto_sync:
            self.get('Authentication')
        return self._Authentication

    @property
    def Password(self):
        """
        get the value of property _Password
        """
        if self.force_auto_sync:
            self.get('Password')
        return self._Password

    @property
    def InhibitionTime(self):
        """
        get the value of property _InhibitionTime
        """
        if self.force_auto_sync:
            self.get('InhibitionTime')
        return self._InhibitionTime

    @property
    def TrillTrafficDisable(self):
        """
        get the value of property _TrillTrafficDisable
        """
        if self.force_auto_sync:
            self.get('TrillTrafficDisable')
        return self._TrillTrafficDisable

    @property
    def EndStationServiceDisabled(self):
        """
        get the value of property _EndStationServiceDisabled
        """
        if self.force_auto_sync:
            self.get('EndStationServiceDisabled')
        return self._EndStationServiceDisabled

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

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
    def NetworkType(self):
        """
        get the value of property _NetworkType
        """
        if self.force_auto_sync:
            self.get('NetworkType')
        return self._NetworkType

    @property
    def CircuitID(self):
        """
        get the value of property _CircuitID
        """
        if self.force_auto_sync:
            self.get('CircuitID')
        return self._CircuitID

    @property
    def PSNInterval(self):
        """
        get the value of property _PSNInterval
        """
        if self.force_auto_sync:
            self.get('PSNInterval')
        return self._PSNInterval

    @property
    def CSNInterval(self):
        """
        get the value of property _CSNInterval
        """
        if self.force_auto_sync:
            self.get('CSNInterval')
        return self._CSNInterval

    @property
    def FloodDelay(self):
        """
        get the value of property _FloodDelay
        """
        if self.force_auto_sync:
            self.get('FloodDelay')
        return self._FloodDelay

    @property
    def LSPRefreshTime(self):
        """
        get the value of property _LSPRefreshTime
        """
        if self.force_auto_sync:
            self.get('LSPRefreshTime')
        return self._LSPRefreshTime

    @property
    def LSPCount(self):
        """
        get the value of property _LSPCount
        """
        if self.force_auto_sync:
            self.get('LSPCount')
        return self._LSPCount

    @SystemID.setter
    def SystemID(self, value):
        self._SystemID = value
        self.edit(SystemID=value)

    @AnnouncingVLANs.setter
    def AnnouncingVLANs(self, value):
        self._AnnouncingVLANs = value
        self.edit(AnnouncingVLANs=value)

    @DesiredDesignatedVLAN.setter
    def DesiredDesignatedVLAN(self, value):
        self._DesiredDesignatedVLAN = value
        self.edit(DesiredDesignatedVLAN=value)

    @EnableMTUTest.setter
    def EnableMTUTest(self, value):
        self._EnableMTUTest = value
        self.edit(EnableMTUTest=value)

    @MinimumAcceptableMTU.setter
    def MinimumAcceptableMTU(self, value):
        self._MinimumAcceptableMTU = value
        self.edit(MinimumAcceptableMTU=value)

    @BypassPseudonode.setter
    def BypassPseudonode(self, value):
        self._BypassPseudonode = value
        self.edit(BypassPseudonode=value)

    @NumberOfMTURetries.setter
    def NumberOfMTURetries(self, value):
        self._NumberOfMTURetries = value
        self.edit(NumberOfMTURetries=value)

    @MTUAckWaitTime.setter
    def MTUAckWaitTime(self, value):
        self._MTUAckWaitTime = value
        self.edit(MTUAckWaitTime=value)

    @DRBPriority.setter
    def DRBPriority(self, value):
        self._DRBPriority = value
        self.edit(DRBPriority=value)

    @Authentication.setter
    def Authentication(self, value):
        self._Authentication = value
        self.edit(Authentication=value)

    @Password.setter
    def Password(self, value):
        self._Password = value
        self.edit(Password=value)

    @InhibitionTime.setter
    def InhibitionTime(self, value):
        self._InhibitionTime = value
        self.edit(InhibitionTime=value)

    @TrillTrafficDisable.setter
    def TrillTrafficDisable(self, value):
        self._TrillTrafficDisable = value
        self.edit(TrillTrafficDisable=value)

    @EndStationServiceDisabled.setter
    def EndStationServiceDisabled(self, value):
        self._EndStationServiceDisabled = value
        self.edit(EndStationServiceDisabled=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @HelloMultiplier.setter
    def HelloMultiplier(self, value):
        self._HelloMultiplier = value
        self.edit(HelloMultiplier=value)

    @NetworkType.setter
    def NetworkType(self, value):
        self._NetworkType = value
        self.edit(NetworkType=value)

    @CircuitID.setter
    def CircuitID(self, value):
        self._CircuitID = value
        self.edit(CircuitID=value)

    @PSNInterval.setter
    def PSNInterval(self, value):
        self._PSNInterval = value
        self.edit(PSNInterval=value)

    @CSNInterval.setter
    def CSNInterval(self, value):
        self._CSNInterval = value
        self.edit(CSNInterval=value)

    @FloodDelay.setter
    def FloodDelay(self, value):
        self._FloodDelay = value
        self.edit(FloodDelay=value)

    @LSPRefreshTime.setter
    def LSPRefreshTime(self, value):
        self._LSPRefreshTime = value
        self.edit(LSPRefreshTime=value)

    def _set_protocolstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProtocolState = TrillProtocolStateEnum.%s' % value[:seperate])

    def _set_rbridgestate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RBridgeState = TrillDRBStateEnum.%s' % value[:seperate])

    def _set_systemid_with_str(self, value):
        self._SystemID = value

    def _set_announcingvlans_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AnnouncingVLANs = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AnnouncingVLANs.append(int(str_value))
            except ValueError:
                self._AnnouncingVLANs.append(hex(int(str_value, 16)))

    def _set_desireddesignatedvlan_with_str(self, value):
        try:
            self._DesiredDesignatedVLAN = int(value)
        except ValueError:
            self._DesiredDesignatedVLAN = hex(int(value, 16))

    def _set_enablemtutest_with_str(self, value):
        self._EnableMTUTest = (value == 'True')

    def _set_minimumacceptablemtu_with_str(self, value):
        try:
            self._MinimumAcceptableMTU = int(value)
        except ValueError:
            self._MinimumAcceptableMTU = hex(int(value, 16))

    def _set_bypasspseudonode_with_str(self, value):
        self._BypassPseudonode = (value == 'True')

    def _set_numberofmturetries_with_str(self, value):
        try:
            self._NumberOfMTURetries = int(value)
        except ValueError:
            self._NumberOfMTURetries = hex(int(value, 16))

    def _set_mtuackwaittime_with_str(self, value):
        try:
            self._MTUAckWaitTime = int(value)
        except ValueError:
            self._MTUAckWaitTime = hex(int(value, 16))

    def _set_drbpriority_with_str(self, value):
        try:
            self._DRBPriority = int(value)
        except ValueError:
            self._DRBPriority = hex(int(value, 16))

    def _set_authentication_with_str(self, value):
        seperate = value.find(':')
        exec('self._Authentication = TrillAuthenticationTypeEnum.%s' % value[:seperate])

    def _set_password_with_str(self, value):
        self._Password = value

    def _set_inhibitiontime_with_str(self, value):
        try:
            self._InhibitionTime = int(value)
        except ValueError:
            self._InhibitionTime = hex(int(value, 16))

    def _set_trilltrafficdisable_with_str(self, value):
        self._TrillTrafficDisable = (value == 'True')

    def _set_endstationservicedisabled_with_str(self, value):
        self._EndStationServiceDisabled = (value == 'True')

    def _set_hostname_with_str(self, value):
        self._HostName = value

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

    def _set_networktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._NetworkType = TrillNetworkTypeEnum.%s' % value[:seperate])

    def _set_circuitid_with_str(self, value):
        try:
            self._CircuitID = int(value)
        except ValueError:
            self._CircuitID = hex(int(value, 16))

    def _set_psninterval_with_str(self, value):
        try:
            self._PSNInterval = int(value)
        except ValueError:
            self._PSNInterval = hex(int(value, 16))

    def _set_csninterval_with_str(self, value):
        try:
            self._CSNInterval = int(value)
        except ValueError:
            self._CSNInterval = hex(int(value, 16))

    def _set_flooddelay_with_str(self, value):
        try:
            self._FloodDelay = int(value)
        except ValueError:
            self._FloodDelay = hex(int(value, 16))

    def _set_lsprefreshtime_with_str(self, value):
        try:
            self._LSPRefreshTime = int(value)
        except ValueError:
            self._LSPRefreshTime = hex(int(value, 16))

    def _set_lspcount_with_str(self, value):
        try:
            self._LSPCount = int(value)
        except ValueError:
            self._LSPCount = hex(int(value, 16))

