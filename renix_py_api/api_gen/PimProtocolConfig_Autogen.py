"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class PimProtocolConfig(L23ProtocolConfig):
    def __init__(self, SessionMode=None, IpVersion=None, DrPriority=None, GenIdMode=None, BsrEnable=None, BsrPriority=None, BsrInterval=None, HelloInterval=None, HelloHoldTime=None, JoinPruneInterval=None, JoinPruneHoldTime=None, **kwargs):
        self._State = EnumPimState.DISABLED  # State, not editable
        self._SessionMode = SessionMode  # Session Mode
        self._IpVersion = IpVersion  # IP Version
        self._DrPriority = DrPriority  # DR Priority
        self._DrAddr = '0.0.0.0'  # DR Address, not editable
        self._DrIpv6Addr = '::'  # DR IPv6 Address, not editable
        self._GenIdMode = GenIdMode  # Generation ID Mode
        self._BsrEnable = BsrEnable  # BSR Enable
        self._BsrState = EnumBsrState.IDLE  # BSR State, not editable
        self._BsrPriority = BsrPriority  # BSR Priority
        self._BsrInterval = BsrInterval  # BSR Interval (sec)
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._HelloHoldTime = HelloHoldTime  # Hello Hold Time (sec)
        self._JoinPruneInterval = JoinPruneInterval  # Join/Prune Interval (sec)
        self._JoinPruneHoldTime = JoinPruneHoldTime  # Join/Prune Hold Time (sec)

        properties = kwargs.copy()
        if SessionMode is not None:
            properties['SessionMode'] = SessionMode
        if IpVersion is not None:
            properties['IpVersion'] = IpVersion
        if DrPriority is not None:
            properties['DrPriority'] = DrPriority
        if GenIdMode is not None:
            properties['GenIdMode'] = GenIdMode
        if BsrEnable is not None:
            properties['BsrEnable'] = BsrEnable
        if BsrPriority is not None:
            properties['BsrPriority'] = BsrPriority
        if BsrInterval is not None:
            properties['BsrInterval'] = BsrInterval
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if HelloHoldTime is not None:
            properties['HelloHoldTime'] = HelloHoldTime
        if JoinPruneInterval is not None:
            properties['JoinPruneInterval'] = JoinPruneInterval
        if JoinPruneHoldTime is not None:
            properties['JoinPruneHoldTime'] = JoinPruneHoldTime

        # call base class function, and it will send message to renix server to create a class.
        super(PimProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SessionMode=None, IpVersion=None, DrPriority=None, GenIdMode=None, BsrEnable=None, BsrPriority=None, BsrInterval=None, HelloInterval=None, HelloHoldTime=None, JoinPruneInterval=None, JoinPruneHoldTime=None, **kwargs):
        properties = kwargs.copy()
        if SessionMode is not None:
            self._SessionMode = SessionMode
            properties['SessionMode'] = SessionMode
        if IpVersion is not None:
            self._IpVersion = IpVersion
            properties['IpVersion'] = IpVersion
        if DrPriority is not None:
            self._DrPriority = DrPriority
            properties['DrPriority'] = DrPriority
        if GenIdMode is not None:
            self._GenIdMode = GenIdMode
            properties['GenIdMode'] = GenIdMode
        if BsrEnable is not None:
            self._BsrEnable = BsrEnable
            properties['BsrEnable'] = BsrEnable
        if BsrPriority is not None:
            self._BsrPriority = BsrPriority
            properties['BsrPriority'] = BsrPriority
        if BsrInterval is not None:
            self._BsrInterval = BsrInterval
            properties['BsrInterval'] = BsrInterval
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if HelloHoldTime is not None:
            self._HelloHoldTime = HelloHoldTime
            properties['HelloHoldTime'] = HelloHoldTime
        if JoinPruneInterval is not None:
            self._JoinPruneInterval = JoinPruneInterval
            properties['JoinPruneInterval'] = JoinPruneInterval
        if JoinPruneHoldTime is not None:
            self._JoinPruneHoldTime = JoinPruneHoldTime
            properties['JoinPruneHoldTime'] = JoinPruneHoldTime

        super(PimProtocolConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def SessionMode(self):
        """
        get the value of property _SessionMode
        """
        if self.force_auto_sync:
            self.get('SessionMode')
        return self._SessionMode

    @property
    def IpVersion(self):
        """
        get the value of property _IpVersion
        """
        if self.force_auto_sync:
            self.get('IpVersion')
        return self._IpVersion

    @property
    def DrPriority(self):
        """
        get the value of property _DrPriority
        """
        if self.force_auto_sync:
            self.get('DrPriority')
        return self._DrPriority

    @property
    def DrAddr(self):
        """
        get the value of property _DrAddr
        """
        if self.force_auto_sync:
            self.get('DrAddr')
        return self._DrAddr

    @property
    def DrIpv6Addr(self):
        """
        get the value of property _DrIpv6Addr
        """
        if self.force_auto_sync:
            self.get('DrIpv6Addr')
        return self._DrIpv6Addr

    @property
    def GenIdMode(self):
        """
        get the value of property _GenIdMode
        """
        if self.force_auto_sync:
            self.get('GenIdMode')
        return self._GenIdMode

    @property
    def BsrEnable(self):
        """
        get the value of property _BsrEnable
        """
        if self.force_auto_sync:
            self.get('BsrEnable')
        return self._BsrEnable

    @property
    def BsrState(self):
        """
        get the value of property _BsrState
        """
        if self.force_auto_sync:
            self.get('BsrState')
        return self._BsrState

    @property
    def BsrPriority(self):
        """
        get the value of property _BsrPriority
        """
        if self.force_auto_sync:
            self.get('BsrPriority')
        return self._BsrPriority

    @property
    def BsrInterval(self):
        """
        get the value of property _BsrInterval
        """
        if self.force_auto_sync:
            self.get('BsrInterval')
        return self._BsrInterval

    @property
    def HelloInterval(self):
        """
        get the value of property _HelloInterval
        """
        if self.force_auto_sync:
            self.get('HelloInterval')
        return self._HelloInterval

    @property
    def HelloHoldTime(self):
        """
        get the value of property _HelloHoldTime
        """
        if self.force_auto_sync:
            self.get('HelloHoldTime')
        return self._HelloHoldTime

    @property
    def JoinPruneInterval(self):
        """
        get the value of property _JoinPruneInterval
        """
        if self.force_auto_sync:
            self.get('JoinPruneInterval')
        return self._JoinPruneInterval

    @property
    def JoinPruneHoldTime(self):
        """
        get the value of property _JoinPruneHoldTime
        """
        if self.force_auto_sync:
            self.get('JoinPruneHoldTime')
        return self._JoinPruneHoldTime

    @SessionMode.setter
    def SessionMode(self, value):
        self._SessionMode = value
        self.edit(SessionMode=value)

    @IpVersion.setter
    def IpVersion(self, value):
        self._IpVersion = value
        self.edit(IpVersion=value)

    @DrPriority.setter
    def DrPriority(self, value):
        self._DrPriority = value
        self.edit(DrPriority=value)

    @GenIdMode.setter
    def GenIdMode(self, value):
        self._GenIdMode = value
        self.edit(GenIdMode=value)

    @BsrEnable.setter
    def BsrEnable(self, value):
        self._BsrEnable = value
        self.edit(BsrEnable=value)

    @BsrPriority.setter
    def BsrPriority(self, value):
        self._BsrPriority = value
        self.edit(BsrPriority=value)

    @BsrInterval.setter
    def BsrInterval(self, value):
        self._BsrInterval = value
        self.edit(BsrInterval=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @HelloHoldTime.setter
    def HelloHoldTime(self, value):
        self._HelloHoldTime = value
        self.edit(HelloHoldTime=value)

    @JoinPruneInterval.setter
    def JoinPruneInterval(self, value):
        self._JoinPruneInterval = value
        self.edit(JoinPruneInterval=value)

    @JoinPruneHoldTime.setter
    def JoinPruneHoldTime(self, value):
        self._JoinPruneHoldTime = value
        self.edit(JoinPruneHoldTime=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumPimState.%s' % value[:seperate])

    def _set_sessionmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SessionMode = EnumSessionMode.%s' % value[:seperate])

    def _set_ipversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IpVersion = EnumPimIpVersion.%s' % value[:seperate])

    def _set_drpriority_with_str(self, value):
        try:
            self._DrPriority = int(value)
        except ValueError:
            self._DrPriority = hex(int(value, 16))

    def _set_draddr_with_str(self, value):
        self._DrAddr = value

    def _set_dripv6addr_with_str(self, value):
        self._DrIpv6Addr = value

    def _set_genidmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._GenIdMode = EnumGenIdMode.%s' % value[:seperate])

    def _set_bsrenable_with_str(self, value):
        self._BsrEnable = (value == 'True')

    def _set_bsrstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._BsrState = EnumBsrState.%s' % value[:seperate])

    def _set_bsrpriority_with_str(self, value):
        try:
            self._BsrPriority = int(value)
        except ValueError:
            self._BsrPriority = hex(int(value, 16))

    def _set_bsrinterval_with_str(self, value):
        try:
            self._BsrInterval = int(value)
        except ValueError:
            self._BsrInterval = hex(int(value, 16))

    def _set_hellointerval_with_str(self, value):
        try:
            self._HelloInterval = int(value)
        except ValueError:
            self._HelloInterval = hex(int(value, 16))

    def _set_helloholdtime_with_str(self, value):
        try:
            self._HelloHoldTime = int(value)
        except ValueError:
            self._HelloHoldTime = hex(int(value, 16))

    def _set_joinpruneinterval_with_str(self, value):
        try:
            self._JoinPruneInterval = int(value)
        except ValueError:
            self._JoinPruneInterval = hex(int(value, 16))

    def _set_joinpruneholdtime_with_str(self, value):
        try:
            self._JoinPruneHoldTime = int(value)
        except ValueError:
            self._JoinPruneHoldTime = hex(int(value, 16))

