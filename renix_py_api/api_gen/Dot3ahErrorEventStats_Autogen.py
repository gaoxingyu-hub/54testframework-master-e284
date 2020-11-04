"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot3ahErrorEventStats(Result):
    def __init__(self, **kwargs):
        self._SessionHandle = ''  # 802.3ah Session Name, not editable
        self._EventType = ''  # Errored Event Type, not editable
        self._TimeStamp = 0  # Time Stamp, not editable
        self._WindowsSize = 0  # Windows Size, not editable
        self._Threshold = 0  # Threshold, not editable
        self._ErrorCount = 0  # Errored Count, not editable
        self._ErrorRunningTotal = 0  # Error Running Total, not editable
        self._EventRunningTotal = 0  # Event Running Total, not editable
        self._OrgUniqueId = ''  # Organization Unique ID, not editable
        self._OrgSpecificData = ''  # Organization Specific Data, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahErrorEventStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionHandle(self):
        """
        get the value of property _SessionHandle
        """
        if self.force_auto_sync:
            self.get('SessionHandle')
        return self._SessionHandle

    @property
    def EventType(self):
        """
        get the value of property _EventType
        """
        if self.force_auto_sync:
            self.get('EventType')
        return self._EventType

    @property
    def TimeStamp(self):
        """
        get the value of property _TimeStamp
        """
        if self.force_auto_sync:
            self.get('TimeStamp')
        return self._TimeStamp

    @property
    def WindowsSize(self):
        """
        get the value of property _WindowsSize
        """
        if self.force_auto_sync:
            self.get('WindowsSize')
        return self._WindowsSize

    @property
    def Threshold(self):
        """
        get the value of property _Threshold
        """
        if self.force_auto_sync:
            self.get('Threshold')
        return self._Threshold

    @property
    def ErrorCount(self):
        """
        get the value of property _ErrorCount
        """
        if self.force_auto_sync:
            self.get('ErrorCount')
        return self._ErrorCount

    @property
    def ErrorRunningTotal(self):
        """
        get the value of property _ErrorRunningTotal
        """
        if self.force_auto_sync:
            self.get('ErrorRunningTotal')
        return self._ErrorRunningTotal

    @property
    def EventRunningTotal(self):
        """
        get the value of property _EventRunningTotal
        """
        if self.force_auto_sync:
            self.get('EventRunningTotal')
        return self._EventRunningTotal

    @property
    def OrgUniqueId(self):
        """
        get the value of property _OrgUniqueId
        """
        if self.force_auto_sync:
            self.get('OrgUniqueId')
        return self._OrgUniqueId

    @property
    def OrgSpecificData(self):
        """
        get the value of property _OrgSpecificData
        """
        if self.force_auto_sync:
            self.get('OrgSpecificData')
        return self._OrgSpecificData

    def _set_sessionhandle_with_str(self, value):
        self._SessionHandle = value

    def _set_eventtype_with_str(self, value):
        self._EventType = value

    def _set_timestamp_with_str(self, value):
        try:
            self._TimeStamp = int(value)
        except ValueError:
            self._TimeStamp = hex(int(value, 16))

    def _set_windowssize_with_str(self, value):
        try:
            self._WindowsSize = int(value)
        except ValueError:
            self._WindowsSize = hex(int(value, 16))

    def _set_threshold_with_str(self, value):
        try:
            self._Threshold = int(value)
        except ValueError:
            self._Threshold = hex(int(value, 16))

    def _set_errorcount_with_str(self, value):
        try:
            self._ErrorCount = int(value)
        except ValueError:
            self._ErrorCount = hex(int(value, 16))

    def _set_errorrunningtotal_with_str(self, value):
        try:
            self._ErrorRunningTotal = int(value)
        except ValueError:
            self._ErrorRunningTotal = hex(int(value, 16))

    def _set_eventrunningtotal_with_str(self, value):
        try:
            self._EventRunningTotal = int(value)
        except ValueError:
            self._EventRunningTotal = hex(int(value, 16))

    def _set_orguniqueid_with_str(self, value):
        self._OrgUniqueId = value

    def _set_orgspecificdata_with_str(self, value):
        self._OrgSpecificData = value

