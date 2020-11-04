"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class MldProtocolConfig(L23ProtocolConfig):
    def __init__(self, MldMulticastVersion=None, MldPackReports=None, MldForceSingleInitialJoin=None, MldForceRobustJoin=None, MldRobustnessVariable=None, MldUnsolicitedReportInterval=None, MldForceLeave=None, MldTrafficClassValue=None, **kwargs):
        self._MldHostState = EnumMldHostState.NONMEMBER  # Host State, not editable
        self._MldMulticastVersion = MldMulticastVersion  # Multicast Version
        self._MldGroupCount = 0  # Group Count, not editable
        self._MldSourceCount = 0  # Source Count, not editable
        self._MldPackReports = MldPackReports  # Pack Reports
        self._MldForceSingleInitialJoin = MldForceSingleInitialJoin  # Force Single Initial Join
        self._MldForceRobustJoin = MldForceRobustJoin  # Force Robust Join
        self._MldRobustnessVariable = MldRobustnessVariable  # Robustness Variable
        self._MldUnsolicitedReportInterval = MldUnsolicitedReportInterval  # Unsolicited Report Interval (sec)
        self._MldForceLeave = MldForceLeave  # Force Leave
        self._MldTrafficClassValue = MldTrafficClassValue  # IPv6 Traffic Class value

        properties = kwargs.copy()
        if MldMulticastVersion is not None:
            properties['MldMulticastVersion'] = MldMulticastVersion
        if MldPackReports is not None:
            properties['MldPackReports'] = MldPackReports
        if MldForceSingleInitialJoin is not None:
            properties['MldForceSingleInitialJoin'] = MldForceSingleInitialJoin
        if MldForceRobustJoin is not None:
            properties['MldForceRobustJoin'] = MldForceRobustJoin
        if MldRobustnessVariable is not None:
            properties['MldRobustnessVariable'] = MldRobustnessVariable
        if MldUnsolicitedReportInterval is not None:
            properties['MldUnsolicitedReportInterval'] = MldUnsolicitedReportInterval
        if MldForceLeave is not None:
            properties['MldForceLeave'] = MldForceLeave
        if MldTrafficClassValue is not None:
            properties['MldTrafficClassValue'] = MldTrafficClassValue

        # call base class function, and it will send message to renix server to create a class.
        super(MldProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MldMulticastVersion=None, MldPackReports=None, MldForceSingleInitialJoin=None, MldForceRobustJoin=None, MldRobustnessVariable=None, MldUnsolicitedReportInterval=None, MldForceLeave=None, MldTrafficClassValue=None, **kwargs):
        properties = kwargs.copy()
        if MldMulticastVersion is not None:
            self._MldMulticastVersion = MldMulticastVersion
            properties['MldMulticastVersion'] = MldMulticastVersion
        if MldPackReports is not None:
            self._MldPackReports = MldPackReports
            properties['MldPackReports'] = MldPackReports
        if MldForceSingleInitialJoin is not None:
            self._MldForceSingleInitialJoin = MldForceSingleInitialJoin
            properties['MldForceSingleInitialJoin'] = MldForceSingleInitialJoin
        if MldForceRobustJoin is not None:
            self._MldForceRobustJoin = MldForceRobustJoin
            properties['MldForceRobustJoin'] = MldForceRobustJoin
        if MldRobustnessVariable is not None:
            self._MldRobustnessVariable = MldRobustnessVariable
            properties['MldRobustnessVariable'] = MldRobustnessVariable
        if MldUnsolicitedReportInterval is not None:
            self._MldUnsolicitedReportInterval = MldUnsolicitedReportInterval
            properties['MldUnsolicitedReportInterval'] = MldUnsolicitedReportInterval
        if MldForceLeave is not None:
            self._MldForceLeave = MldForceLeave
            properties['MldForceLeave'] = MldForceLeave
        if MldTrafficClassValue is not None:
            self._MldTrafficClassValue = MldTrafficClassValue
            properties['MldTrafficClassValue'] = MldTrafficClassValue

        super(MldProtocolConfig, self).edit(**properties)

    @property
    def MldHostState(self):
        """
        get the value of property _MldHostState
        """
        if self.force_auto_sync:
            self.get('MldHostState')
        return self._MldHostState

    @property
    def MldMulticastVersion(self):
        """
        get the value of property _MldMulticastVersion
        """
        if self.force_auto_sync:
            self.get('MldMulticastVersion')
        return self._MldMulticastVersion

    @property
    def MldGroupCount(self):
        """
        get the value of property _MldGroupCount
        """
        if self.force_auto_sync:
            self.get('MldGroupCount')
        return self._MldGroupCount

    @property
    def MldSourceCount(self):
        """
        get the value of property _MldSourceCount
        """
        if self.force_auto_sync:
            self.get('MldSourceCount')
        return self._MldSourceCount

    @property
    def MldPackReports(self):
        """
        get the value of property _MldPackReports
        """
        if self.force_auto_sync:
            self.get('MldPackReports')
        return self._MldPackReports

    @property
    def MldForceSingleInitialJoin(self):
        """
        get the value of property _MldForceSingleInitialJoin
        """
        if self.force_auto_sync:
            self.get('MldForceSingleInitialJoin')
        return self._MldForceSingleInitialJoin

    @property
    def MldForceRobustJoin(self):
        """
        get the value of property _MldForceRobustJoin
        """
        if self.force_auto_sync:
            self.get('MldForceRobustJoin')
        return self._MldForceRobustJoin

    @property
    def MldRobustnessVariable(self):
        """
        get the value of property _MldRobustnessVariable
        """
        if self.force_auto_sync:
            self.get('MldRobustnessVariable')
        return self._MldRobustnessVariable

    @property
    def MldUnsolicitedReportInterval(self):
        """
        get the value of property _MldUnsolicitedReportInterval
        """
        if self.force_auto_sync:
            self.get('MldUnsolicitedReportInterval')
        return self._MldUnsolicitedReportInterval

    @property
    def MldForceLeave(self):
        """
        get the value of property _MldForceLeave
        """
        if self.force_auto_sync:
            self.get('MldForceLeave')
        return self._MldForceLeave

    @property
    def MldTrafficClassValue(self):
        """
        get the value of property _MldTrafficClassValue
        """
        if self.force_auto_sync:
            self.get('MldTrafficClassValue')
        return self._MldTrafficClassValue

    @MldMulticastVersion.setter
    def MldMulticastVersion(self, value):
        self._MldMulticastVersion = value
        self.edit(MldMulticastVersion=value)

    @MldPackReports.setter
    def MldPackReports(self, value):
        self._MldPackReports = value
        self.edit(MldPackReports=value)

    @MldForceSingleInitialJoin.setter
    def MldForceSingleInitialJoin(self, value):
        self._MldForceSingleInitialJoin = value
        self.edit(MldForceSingleInitialJoin=value)

    @MldForceRobustJoin.setter
    def MldForceRobustJoin(self, value):
        self._MldForceRobustJoin = value
        self.edit(MldForceRobustJoin=value)

    @MldRobustnessVariable.setter
    def MldRobustnessVariable(self, value):
        self._MldRobustnessVariable = value
        self.edit(MldRobustnessVariable=value)

    @MldUnsolicitedReportInterval.setter
    def MldUnsolicitedReportInterval(self, value):
        self._MldUnsolicitedReportInterval = value
        self.edit(MldUnsolicitedReportInterval=value)

    @MldForceLeave.setter
    def MldForceLeave(self, value):
        self._MldForceLeave = value
        self.edit(MldForceLeave=value)

    @MldTrafficClassValue.setter
    def MldTrafficClassValue(self, value):
        self._MldTrafficClassValue = value
        self.edit(MldTrafficClassValue=value)

    def _set_mldhoststate_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldHostState = EnumMldHostState.%s' % value[:seperate])

    def _set_mldmulticastversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldMulticastVersion = EnumMldMulticastVersion.%s' % value[:seperate])

    def _set_mldgroupcount_with_str(self, value):
        try:
            self._MldGroupCount = int(value)
        except ValueError:
            self._MldGroupCount = hex(int(value, 16))

    def _set_mldsourcecount_with_str(self, value):
        try:
            self._MldSourceCount = int(value)
        except ValueError:
            self._MldSourceCount = hex(int(value, 16))

    def _set_mldpackreports_with_str(self, value):
        self._MldPackReports = (value == 'True')

    def _set_mldforcesingleinitialjoin_with_str(self, value):
        self._MldForceSingleInitialJoin = (value == 'True')

    def _set_mldforcerobustjoin_with_str(self, value):
        self._MldForceRobustJoin = (value == 'True')

    def _set_mldrobustnessvariable_with_str(self, value):
        try:
            self._MldRobustnessVariable = int(value)
        except ValueError:
            self._MldRobustnessVariable = hex(int(value, 16))

    def _set_mldunsolicitedreportinterval_with_str(self, value):
        try:
            self._MldUnsolicitedReportInterval = int(value)
        except ValueError:
            self._MldUnsolicitedReportInterval = hex(int(value, 16))

    def _set_mldforceleave_with_str(self, value):
        self._MldForceLeave = (value == 'True')

    def _set_mldtrafficclassvalue_with_str(self, value):
        try:
            self._MldTrafficClassValue = int(value)
        except ValueError:
            self._MldTrafficClassValue = hex(int(value, 16))

