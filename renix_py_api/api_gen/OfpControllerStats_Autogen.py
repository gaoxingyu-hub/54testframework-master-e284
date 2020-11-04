"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class OfpControllerStats(Result):
    def __init__(self, **kwargs):
        self._Handle = ''  # Controller Name, not editable
        self._Duration = 0  # Duration (ms), not editable
        self._ConnectedSwitchCount = 0  # Connected Switch Count, not editable
        self._BarrierRequestCount = 0  # Barrier Requests Sent, not editable
        self._BarrierReplyCount = 0  # Barrier Replies Received, not editable
        self._BarrierRequestTimeoutCount = 0  # Barrier Requests Timeout Count, not editable
        self._BarrierRemainingCount = 0  # Barrier Requests Outstanding, not editable
        self._LastBarrierResponseTime = 0  # Last Barrier Response Time (ms), not editable
        self._MissPacketInCount = 0  # Total Packet-In with Table-Miss, not editable
        self._MatchPacketInCount = 0  # Total Packet-In with Match, not editable
        self._TotalPacketOutCount = 0  # Total Packet-Out, not editable
        self._AddFlowCount = 0  # Total Flows Added, not editable
        self._ModifyFlowCount = 0  # Total Flows Modified, not editable
        self._DeleteFlowCount = 0  # Total Flows Deleted, not editable
        self._FlowModErrorCount = 0  # Total FlowMod Error, not editable
        self._FlowRemovedCount = 0  # Total Flow-Removed Received, not editable
        self._AddGroupCount = 0  # Total Groups Added, not editable
        self._ModifyGroupCount = 0  # Total Groups Modified, not editable
        self._DeleteGroupCount = 0  # Total Groups Deleted, not editable
        self._GroupModErrorCount = 0  # Total GroupMod Error, not editable
        self._AddMeterCount = 0  # Total Meters Added, not editable
        self._ModifyMeterCount = 0  # Total Meters Modified, not editable
        self._DeleteMeterCount = 0  # Total Meters Deleted, not editable
        self._MeterModErrorCount = 0  # Total MeterMod Error, not editable
        self._RoleRequestCount = 0  # Role Requests Sent, not editable
        self._RoleReplyCount = 0  # Role Replies Received, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(OfpControllerStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Handle(self):
        """
        get the value of property _Handle
        """
        if self.force_auto_sync:
            self.get('Handle')
        return self._Handle

    @property
    def Duration(self):
        """
        get the value of property _Duration
        """
        if self.force_auto_sync:
            self.get('Duration')
        return self._Duration

    @property
    def ConnectedSwitchCount(self):
        """
        get the value of property _ConnectedSwitchCount
        """
        if self.force_auto_sync:
            self.get('ConnectedSwitchCount')
        return self._ConnectedSwitchCount

    @property
    def BarrierRequestCount(self):
        """
        get the value of property _BarrierRequestCount
        """
        if self.force_auto_sync:
            self.get('BarrierRequestCount')
        return self._BarrierRequestCount

    @property
    def BarrierReplyCount(self):
        """
        get the value of property _BarrierReplyCount
        """
        if self.force_auto_sync:
            self.get('BarrierReplyCount')
        return self._BarrierReplyCount

    @property
    def BarrierRequestTimeoutCount(self):
        """
        get the value of property _BarrierRequestTimeoutCount
        """
        if self.force_auto_sync:
            self.get('BarrierRequestTimeoutCount')
        return self._BarrierRequestTimeoutCount

    @property
    def BarrierRemainingCount(self):
        """
        get the value of property _BarrierRemainingCount
        """
        if self.force_auto_sync:
            self.get('BarrierRemainingCount')
        return self._BarrierRemainingCount

    @property
    def LastBarrierResponseTime(self):
        """
        get the value of property _LastBarrierResponseTime
        """
        if self.force_auto_sync:
            self.get('LastBarrierResponseTime')
        return self._LastBarrierResponseTime

    @property
    def MissPacketInCount(self):
        """
        get the value of property _MissPacketInCount
        """
        if self.force_auto_sync:
            self.get('MissPacketInCount')
        return self._MissPacketInCount

    @property
    def MatchPacketInCount(self):
        """
        get the value of property _MatchPacketInCount
        """
        if self.force_auto_sync:
            self.get('MatchPacketInCount')
        return self._MatchPacketInCount

    @property
    def TotalPacketOutCount(self):
        """
        get the value of property _TotalPacketOutCount
        """
        if self.force_auto_sync:
            self.get('TotalPacketOutCount')
        return self._TotalPacketOutCount

    @property
    def AddFlowCount(self):
        """
        get the value of property _AddFlowCount
        """
        if self.force_auto_sync:
            self.get('AddFlowCount')
        return self._AddFlowCount

    @property
    def ModifyFlowCount(self):
        """
        get the value of property _ModifyFlowCount
        """
        if self.force_auto_sync:
            self.get('ModifyFlowCount')
        return self._ModifyFlowCount

    @property
    def DeleteFlowCount(self):
        """
        get the value of property _DeleteFlowCount
        """
        if self.force_auto_sync:
            self.get('DeleteFlowCount')
        return self._DeleteFlowCount

    @property
    def FlowModErrorCount(self):
        """
        get the value of property _FlowModErrorCount
        """
        if self.force_auto_sync:
            self.get('FlowModErrorCount')
        return self._FlowModErrorCount

    @property
    def FlowRemovedCount(self):
        """
        get the value of property _FlowRemovedCount
        """
        if self.force_auto_sync:
            self.get('FlowRemovedCount')
        return self._FlowRemovedCount

    @property
    def AddGroupCount(self):
        """
        get the value of property _AddGroupCount
        """
        if self.force_auto_sync:
            self.get('AddGroupCount')
        return self._AddGroupCount

    @property
    def ModifyGroupCount(self):
        """
        get the value of property _ModifyGroupCount
        """
        if self.force_auto_sync:
            self.get('ModifyGroupCount')
        return self._ModifyGroupCount

    @property
    def DeleteGroupCount(self):
        """
        get the value of property _DeleteGroupCount
        """
        if self.force_auto_sync:
            self.get('DeleteGroupCount')
        return self._DeleteGroupCount

    @property
    def GroupModErrorCount(self):
        """
        get the value of property _GroupModErrorCount
        """
        if self.force_auto_sync:
            self.get('GroupModErrorCount')
        return self._GroupModErrorCount

    @property
    def AddMeterCount(self):
        """
        get the value of property _AddMeterCount
        """
        if self.force_auto_sync:
            self.get('AddMeterCount')
        return self._AddMeterCount

    @property
    def ModifyMeterCount(self):
        """
        get the value of property _ModifyMeterCount
        """
        if self.force_auto_sync:
            self.get('ModifyMeterCount')
        return self._ModifyMeterCount

    @property
    def DeleteMeterCount(self):
        """
        get the value of property _DeleteMeterCount
        """
        if self.force_auto_sync:
            self.get('DeleteMeterCount')
        return self._DeleteMeterCount

    @property
    def MeterModErrorCount(self):
        """
        get the value of property _MeterModErrorCount
        """
        if self.force_auto_sync:
            self.get('MeterModErrorCount')
        return self._MeterModErrorCount

    @property
    def RoleRequestCount(self):
        """
        get the value of property _RoleRequestCount
        """
        if self.force_auto_sync:
            self.get('RoleRequestCount')
        return self._RoleRequestCount

    @property
    def RoleReplyCount(self):
        """
        get the value of property _RoleReplyCount
        """
        if self.force_auto_sync:
            self.get('RoleReplyCount')
        return self._RoleReplyCount

    def _set_handle_with_str(self, value):
        self._Handle = value

    def _set_duration_with_str(self, value):
        try:
            self._Duration = int(value)
        except ValueError:
            self._Duration = hex(int(value, 16))

    def _set_connectedswitchcount_with_str(self, value):
        try:
            self._ConnectedSwitchCount = int(value)
        except ValueError:
            self._ConnectedSwitchCount = hex(int(value, 16))

    def _set_barrierrequestcount_with_str(self, value):
        try:
            self._BarrierRequestCount = int(value)
        except ValueError:
            self._BarrierRequestCount = hex(int(value, 16))

    def _set_barrierreplycount_with_str(self, value):
        try:
            self._BarrierReplyCount = int(value)
        except ValueError:
            self._BarrierReplyCount = hex(int(value, 16))

    def _set_barrierrequesttimeoutcount_with_str(self, value):
        try:
            self._BarrierRequestTimeoutCount = int(value)
        except ValueError:
            self._BarrierRequestTimeoutCount = hex(int(value, 16))

    def _set_barrierremainingcount_with_str(self, value):
        try:
            self._BarrierRemainingCount = int(value)
        except ValueError:
            self._BarrierRemainingCount = hex(int(value, 16))

    def _set_lastbarrierresponsetime_with_str(self, value):
        try:
            self._LastBarrierResponseTime = int(value)
        except ValueError:
            self._LastBarrierResponseTime = hex(int(value, 16))

    def _set_misspacketincount_with_str(self, value):
        try:
            self._MissPacketInCount = int(value)
        except ValueError:
            self._MissPacketInCount = hex(int(value, 16))

    def _set_matchpacketincount_with_str(self, value):
        try:
            self._MatchPacketInCount = int(value)
        except ValueError:
            self._MatchPacketInCount = hex(int(value, 16))

    def _set_totalpacketoutcount_with_str(self, value):
        try:
            self._TotalPacketOutCount = int(value)
        except ValueError:
            self._TotalPacketOutCount = hex(int(value, 16))

    def _set_addflowcount_with_str(self, value):
        try:
            self._AddFlowCount = int(value)
        except ValueError:
            self._AddFlowCount = hex(int(value, 16))

    def _set_modifyflowcount_with_str(self, value):
        try:
            self._ModifyFlowCount = int(value)
        except ValueError:
            self._ModifyFlowCount = hex(int(value, 16))

    def _set_deleteflowcount_with_str(self, value):
        try:
            self._DeleteFlowCount = int(value)
        except ValueError:
            self._DeleteFlowCount = hex(int(value, 16))

    def _set_flowmoderrorcount_with_str(self, value):
        try:
            self._FlowModErrorCount = int(value)
        except ValueError:
            self._FlowModErrorCount = hex(int(value, 16))

    def _set_flowremovedcount_with_str(self, value):
        try:
            self._FlowRemovedCount = int(value)
        except ValueError:
            self._FlowRemovedCount = hex(int(value, 16))

    def _set_addgroupcount_with_str(self, value):
        try:
            self._AddGroupCount = int(value)
        except ValueError:
            self._AddGroupCount = hex(int(value, 16))

    def _set_modifygroupcount_with_str(self, value):
        try:
            self._ModifyGroupCount = int(value)
        except ValueError:
            self._ModifyGroupCount = hex(int(value, 16))

    def _set_deletegroupcount_with_str(self, value):
        try:
            self._DeleteGroupCount = int(value)
        except ValueError:
            self._DeleteGroupCount = hex(int(value, 16))

    def _set_groupmoderrorcount_with_str(self, value):
        try:
            self._GroupModErrorCount = int(value)
        except ValueError:
            self._GroupModErrorCount = hex(int(value, 16))

    def _set_addmetercount_with_str(self, value):
        try:
            self._AddMeterCount = int(value)
        except ValueError:
            self._AddMeterCount = hex(int(value, 16))

    def _set_modifymetercount_with_str(self, value):
        try:
            self._ModifyMeterCount = int(value)
        except ValueError:
            self._ModifyMeterCount = hex(int(value, 16))

    def _set_deletemetercount_with_str(self, value):
        try:
            self._DeleteMeterCount = int(value)
        except ValueError:
            self._DeleteMeterCount = hex(int(value, 16))

    def _set_metermoderrorcount_with_str(self, value):
        try:
            self._MeterModErrorCount = int(value)
        except ValueError:
            self._MeterModErrorCount = hex(int(value, 16))

    def _set_rolerequestcount_with_str(self, value):
        try:
            self._RoleRequestCount = int(value)
        except ValueError:
            self._RoleRequestCount = hex(int(value, 16))

    def _set_rolereplycount_with_str(self, value):
        try:
            self._RoleReplyCount = int(value)
        except ValueError:
            self._RoleReplyCount = hex(int(value, 16))

