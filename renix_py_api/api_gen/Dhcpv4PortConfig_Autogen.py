"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv4PortConfig(ROMObject):
    def __init__(self, SetupRate=None, TeardownRate=None, MaxOutstanding=None, LeaseTime=None, SessionRetryCount=None, MessageRetryCount=None, MessageTimeout=None, MaxMessageSize=None, **kwargs):
        self._SetupRate = SetupRate  # Setup Rate
        self._TeardownRate = TeardownRate  # Teardown Rate
        self._MaxOutstanding = MaxOutstanding  # Max Outstanding
        self._LeaseTime = LeaseTime  # Expect Lease Time (sec)
        self._SessionRetryCount = SessionRetryCount  # Session Retry Count
        self._MessageRetryCount = MessageRetryCount  # Message Retry Count
        self._MessageTimeout = MessageTimeout  # Message Timeout (secs)
        self._MaxMessageSize = MaxMessageSize  # Max Payload Size (Bytes)

        properties = kwargs.copy()
        if SetupRate is not None:
            properties['SetupRate'] = SetupRate
        if TeardownRate is not None:
            properties['TeardownRate'] = TeardownRate
        if MaxOutstanding is not None:
            properties['MaxOutstanding'] = MaxOutstanding
        if LeaseTime is not None:
            properties['LeaseTime'] = LeaseTime
        if SessionRetryCount is not None:
            properties['SessionRetryCount'] = SessionRetryCount
        if MessageRetryCount is not None:
            properties['MessageRetryCount'] = MessageRetryCount
        if MessageTimeout is not None:
            properties['MessageTimeout'] = MessageTimeout
        if MaxMessageSize is not None:
            properties['MaxMessageSize'] = MaxMessageSize

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4PortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SetupRate=None, TeardownRate=None, MaxOutstanding=None, LeaseTime=None, SessionRetryCount=None, MessageRetryCount=None, MessageTimeout=None, MaxMessageSize=None, **kwargs):
        properties = kwargs.copy()
        if SetupRate is not None:
            self._SetupRate = SetupRate
            properties['SetupRate'] = SetupRate
        if TeardownRate is not None:
            self._TeardownRate = TeardownRate
            properties['TeardownRate'] = TeardownRate
        if MaxOutstanding is not None:
            self._MaxOutstanding = MaxOutstanding
            properties['MaxOutstanding'] = MaxOutstanding
        if LeaseTime is not None:
            self._LeaseTime = LeaseTime
            properties['LeaseTime'] = LeaseTime
        if SessionRetryCount is not None:
            self._SessionRetryCount = SessionRetryCount
            properties['SessionRetryCount'] = SessionRetryCount
        if MessageRetryCount is not None:
            self._MessageRetryCount = MessageRetryCount
            properties['MessageRetryCount'] = MessageRetryCount
        if MessageTimeout is not None:
            self._MessageTimeout = MessageTimeout
            properties['MessageTimeout'] = MessageTimeout
        if MaxMessageSize is not None:
            self._MaxMessageSize = MaxMessageSize
            properties['MaxMessageSize'] = MaxMessageSize

        super(Dhcpv4PortConfig, self).edit(**properties)

    @property
    def SetupRate(self):
        """
        get the value of property _SetupRate
        """
        if self.force_auto_sync:
            self.get('SetupRate')
        return self._SetupRate

    @property
    def TeardownRate(self):
        """
        get the value of property _TeardownRate
        """
        if self.force_auto_sync:
            self.get('TeardownRate')
        return self._TeardownRate

    @property
    def MaxOutstanding(self):
        """
        get the value of property _MaxOutstanding
        """
        if self.force_auto_sync:
            self.get('MaxOutstanding')
        return self._MaxOutstanding

    @property
    def LeaseTime(self):
        """
        get the value of property _LeaseTime
        """
        if self.force_auto_sync:
            self.get('LeaseTime')
        return self._LeaseTime

    @property
    def SessionRetryCount(self):
        """
        get the value of property _SessionRetryCount
        """
        if self.force_auto_sync:
            self.get('SessionRetryCount')
        return self._SessionRetryCount

    @property
    def MessageRetryCount(self):
        """
        get the value of property _MessageRetryCount
        """
        if self.force_auto_sync:
            self.get('MessageRetryCount')
        return self._MessageRetryCount

    @property
    def MessageTimeout(self):
        """
        get the value of property _MessageTimeout
        """
        if self.force_auto_sync:
            self.get('MessageTimeout')
        return self._MessageTimeout

    @property
    def MaxMessageSize(self):
        """
        get the value of property _MaxMessageSize
        """
        if self.force_auto_sync:
            self.get('MaxMessageSize')
        return self._MaxMessageSize

    @SetupRate.setter
    def SetupRate(self, value):
        self._SetupRate = value
        self.edit(SetupRate=value)

    @TeardownRate.setter
    def TeardownRate(self, value):
        self._TeardownRate = value
        self.edit(TeardownRate=value)

    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._MaxOutstanding = value
        self.edit(MaxOutstanding=value)

    @LeaseTime.setter
    def LeaseTime(self, value):
        self._LeaseTime = value
        self.edit(LeaseTime=value)

    @SessionRetryCount.setter
    def SessionRetryCount(self, value):
        self._SessionRetryCount = value
        self.edit(SessionRetryCount=value)

    @MessageRetryCount.setter
    def MessageRetryCount(self, value):
        self._MessageRetryCount = value
        self.edit(MessageRetryCount=value)

    @MessageTimeout.setter
    def MessageTimeout(self, value):
        self._MessageTimeout = value
        self.edit(MessageTimeout=value)

    @MaxMessageSize.setter
    def MaxMessageSize(self, value):
        self._MaxMessageSize = value
        self.edit(MaxMessageSize=value)

    def _set_setuprate_with_str(self, value):
        try:
            self._SetupRate = int(value)
        except ValueError:
            self._SetupRate = hex(int(value, 16))

    def _set_teardownrate_with_str(self, value):
        try:
            self._TeardownRate = int(value)
        except ValueError:
            self._TeardownRate = hex(int(value, 16))

    def _set_maxoutstanding_with_str(self, value):
        try:
            self._MaxOutstanding = int(value)
        except ValueError:
            self._MaxOutstanding = hex(int(value, 16))

    def _set_leasetime_with_str(self, value):
        try:
            self._LeaseTime = int(value)
        except ValueError:
            self._LeaseTime = hex(int(value, 16))

    def _set_sessionretrycount_with_str(self, value):
        try:
            self._SessionRetryCount = int(value)
        except ValueError:
            self._SessionRetryCount = hex(int(value, 16))

    def _set_messageretrycount_with_str(self, value):
        try:
            self._MessageRetryCount = int(value)
        except ValueError:
            self._MessageRetryCount = hex(int(value, 16))

    def _set_messagetimeout_with_str(self, value):
        try:
            self._MessageTimeout = int(value)
        except ValueError:
            self._MessageTimeout = hex(int(value, 16))

    def _set_maxmessagesize_with_str(self, value):
        try:
            self._MaxMessageSize = int(value)
        except ValueError:
            self._MaxMessageSize = hex(int(value, 16))

