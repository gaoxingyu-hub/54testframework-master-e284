"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ArpPortConfig(ROMObject):
    def __init__(self, ArpTimeout=None, Rate=None, RetryCount=None, SuppressDuplicateGateway=None, DelayTime=None, **kwargs):
        self._State = EnumArpState.IDLE  # State, not editable
        self._ArpTimeout = ArpTimeout  # ARP/ND Timeout (sec)
        self._Rate = Rate  # Rate (packets/sec)
        self._RetryCount = RetryCount  # Retry Count
        self._SuppressDuplicateGateway = SuppressDuplicateGateway  # Suppress Duplicate Gateway
        self._DelayTime = DelayTime  # Delay Before ARP/ND (sec)

        properties = kwargs.copy()
        if ArpTimeout is not None:
            properties['ArpTimeout'] = ArpTimeout
        if Rate is not None:
            properties['Rate'] = Rate
        if RetryCount is not None:
            properties['RetryCount'] = RetryCount
        if SuppressDuplicateGateway is not None:
            properties['SuppressDuplicateGateway'] = SuppressDuplicateGateway
        if DelayTime is not None:
            properties['DelayTime'] = DelayTime

        # call base class function, and it will send message to renix server to create a class.
        super(ArpPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ArpTimeout=None, Rate=None, RetryCount=None, SuppressDuplicateGateway=None, DelayTime=None, **kwargs):
        properties = kwargs.copy()
        if ArpTimeout is not None:
            self._ArpTimeout = ArpTimeout
            properties['ArpTimeout'] = ArpTimeout
        if Rate is not None:
            self._Rate = Rate
            properties['Rate'] = Rate
        if RetryCount is not None:
            self._RetryCount = RetryCount
            properties['RetryCount'] = RetryCount
        if SuppressDuplicateGateway is not None:
            self._SuppressDuplicateGateway = SuppressDuplicateGateway
            properties['SuppressDuplicateGateway'] = SuppressDuplicateGateway
        if DelayTime is not None:
            self._DelayTime = DelayTime
            properties['DelayTime'] = DelayTime

        super(ArpPortConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def ArpTimeout(self):
        """
        get the value of property _ArpTimeout
        """
        if self.force_auto_sync:
            self.get('ArpTimeout')
        return self._ArpTimeout

    @property
    def Rate(self):
        """
        get the value of property _Rate
        """
        if self.force_auto_sync:
            self.get('Rate')
        return self._Rate

    @property
    def RetryCount(self):
        """
        get the value of property _RetryCount
        """
        if self.force_auto_sync:
            self.get('RetryCount')
        return self._RetryCount

    @property
    def SuppressDuplicateGateway(self):
        """
        get the value of property _SuppressDuplicateGateway
        """
        if self.force_auto_sync:
            self.get('SuppressDuplicateGateway')
        return self._SuppressDuplicateGateway

    @property
    def DelayTime(self):
        """
        get the value of property _DelayTime
        """
        if self.force_auto_sync:
            self.get('DelayTime')
        return self._DelayTime

    @ArpTimeout.setter
    def ArpTimeout(self, value):
        self._ArpTimeout = value
        self.edit(ArpTimeout=value)

    @Rate.setter
    def Rate(self, value):
        self._Rate = value
        self.edit(Rate=value)

    @RetryCount.setter
    def RetryCount(self, value):
        self._RetryCount = value
        self.edit(RetryCount=value)

    @SuppressDuplicateGateway.setter
    def SuppressDuplicateGateway(self, value):
        self._SuppressDuplicateGateway = value
        self.edit(SuppressDuplicateGateway=value)

    @DelayTime.setter
    def DelayTime(self, value):
        self._DelayTime = value
        self.edit(DelayTime=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumArpState.%s' % value[:seperate])

    def _set_arptimeout_with_str(self, value):
        try:
            self._ArpTimeout = int(value)
        except ValueError:
            self._ArpTimeout = hex(int(value, 16))

    def _set_rate_with_str(self, value):
        try:
            self._Rate = int(value)
        except ValueError:
            self._Rate = hex(int(value, 16))

    def _set_retrycount_with_str(self, value):
        try:
            self._RetryCount = int(value)
        except ValueError:
            self._RetryCount = hex(int(value, 16))

    def _set_suppressduplicategateway_with_str(self, value):
        self._SuppressDuplicateGateway = (value == 'True')

    def _set_delaytime_with_str(self, value):
        try:
            self._DelayTime = int(value)
        except ValueError:
            self._DelayTime = hex(int(value, 16))

