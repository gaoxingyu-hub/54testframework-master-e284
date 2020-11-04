"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class IgmpProtocolConfig(L23ProtocolConfig):
    def __init__(self, IgmpMulticastVersion=None, IgmpPackReports=None, IgmpForceSingleInitialJoin=None, IgmpForceRobustJoin=None, IgmpRobustnessVariable=None, IgmpUnsolicitedReportInterval=None, IgmpForceLeave=None, Igmpv1RouterPresentTimeout=None, IgmpIPv4DoNotFragment=None, IgmpIPv4TosValue=None, **kwargs):
        self._IgmpHostState = EnumIgmpHostState.NONMEMBER  # Host State, not editable
        self._IgmpMulticastVersion = IgmpMulticastVersion  # Multicast Version
        self._IgmpGroupCount = 0  # Group Count, not editable
        self._IgmpSourceCount = 0  # Source Count, not editable
        self._IgmpPackReports = IgmpPackReports  # Pack Reports
        self._IgmpForceSingleInitialJoin = IgmpForceSingleInitialJoin  # Force Single Initial Join
        self._IgmpForceRobustJoin = IgmpForceRobustJoin  # Force Robust Join
        self._IgmpRobustnessVariable = IgmpRobustnessVariable  # Robustness Variable
        self._IgmpUnsolicitedReportInterval = IgmpUnsolicitedReportInterval  # Unsolicited Report Interval (sec)
        self._IgmpForceLeave = IgmpForceLeave  # Force Leave
        self._Igmpv1RouterPresentTimeout = Igmpv1RouterPresentTimeout  # V1 Router Present Timeout(sec)
        self._IgmpIPv4DoNotFragment = IgmpIPv4DoNotFragment  # IPv4 Don't Fragment (DF bit)
        self._IgmpIPv4TosValue = IgmpIPv4TosValue  # IPv4 TOS value(Hex)

        properties = kwargs.copy()
        if IgmpMulticastVersion is not None:
            properties['IgmpMulticastVersion'] = IgmpMulticastVersion
        if IgmpPackReports is not None:
            properties['IgmpPackReports'] = IgmpPackReports
        if IgmpForceSingleInitialJoin is not None:
            properties['IgmpForceSingleInitialJoin'] = IgmpForceSingleInitialJoin
        if IgmpForceRobustJoin is not None:
            properties['IgmpForceRobustJoin'] = IgmpForceRobustJoin
        if IgmpRobustnessVariable is not None:
            properties['IgmpRobustnessVariable'] = IgmpRobustnessVariable
        if IgmpUnsolicitedReportInterval is not None:
            properties['IgmpUnsolicitedReportInterval'] = IgmpUnsolicitedReportInterval
        if IgmpForceLeave is not None:
            properties['IgmpForceLeave'] = IgmpForceLeave
        if Igmpv1RouterPresentTimeout is not None:
            properties['Igmpv1RouterPresentTimeout'] = Igmpv1RouterPresentTimeout
        if IgmpIPv4DoNotFragment is not None:
            properties['IgmpIPv4DoNotFragment'] = IgmpIPv4DoNotFragment
        if IgmpIPv4TosValue is not None:
            properties['IgmpIPv4TosValue'] = IgmpIPv4TosValue

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IgmpMulticastVersion=None, IgmpPackReports=None, IgmpForceSingleInitialJoin=None, IgmpForceRobustJoin=None, IgmpRobustnessVariable=None, IgmpUnsolicitedReportInterval=None, IgmpForceLeave=None, Igmpv1RouterPresentTimeout=None, IgmpIPv4DoNotFragment=None, IgmpIPv4TosValue=None, **kwargs):
        properties = kwargs.copy()
        if IgmpMulticastVersion is not None:
            self._IgmpMulticastVersion = IgmpMulticastVersion
            properties['IgmpMulticastVersion'] = IgmpMulticastVersion
        if IgmpPackReports is not None:
            self._IgmpPackReports = IgmpPackReports
            properties['IgmpPackReports'] = IgmpPackReports
        if IgmpForceSingleInitialJoin is not None:
            self._IgmpForceSingleInitialJoin = IgmpForceSingleInitialJoin
            properties['IgmpForceSingleInitialJoin'] = IgmpForceSingleInitialJoin
        if IgmpForceRobustJoin is not None:
            self._IgmpForceRobustJoin = IgmpForceRobustJoin
            properties['IgmpForceRobustJoin'] = IgmpForceRobustJoin
        if IgmpRobustnessVariable is not None:
            self._IgmpRobustnessVariable = IgmpRobustnessVariable
            properties['IgmpRobustnessVariable'] = IgmpRobustnessVariable
        if IgmpUnsolicitedReportInterval is not None:
            self._IgmpUnsolicitedReportInterval = IgmpUnsolicitedReportInterval
            properties['IgmpUnsolicitedReportInterval'] = IgmpUnsolicitedReportInterval
        if IgmpForceLeave is not None:
            self._IgmpForceLeave = IgmpForceLeave
            properties['IgmpForceLeave'] = IgmpForceLeave
        if Igmpv1RouterPresentTimeout is not None:
            self._Igmpv1RouterPresentTimeout = Igmpv1RouterPresentTimeout
            properties['Igmpv1RouterPresentTimeout'] = Igmpv1RouterPresentTimeout
        if IgmpIPv4DoNotFragment is not None:
            self._IgmpIPv4DoNotFragment = IgmpIPv4DoNotFragment
            properties['IgmpIPv4DoNotFragment'] = IgmpIPv4DoNotFragment
        if IgmpIPv4TosValue is not None:
            self._IgmpIPv4TosValue = IgmpIPv4TosValue
            properties['IgmpIPv4TosValue'] = IgmpIPv4TosValue

        super(IgmpProtocolConfig, self).edit(**properties)

    @property
    def IgmpHostState(self):
        """
        get the value of property _IgmpHostState
        """
        if self.force_auto_sync:
            self.get('IgmpHostState')
        return self._IgmpHostState

    @property
    def IgmpMulticastVersion(self):
        """
        get the value of property _IgmpMulticastVersion
        """
        if self.force_auto_sync:
            self.get('IgmpMulticastVersion')
        return self._IgmpMulticastVersion

    @property
    def IgmpGroupCount(self):
        """
        get the value of property _IgmpGroupCount
        """
        if self.force_auto_sync:
            self.get('IgmpGroupCount')
        return self._IgmpGroupCount

    @property
    def IgmpSourceCount(self):
        """
        get the value of property _IgmpSourceCount
        """
        if self.force_auto_sync:
            self.get('IgmpSourceCount')
        return self._IgmpSourceCount

    @property
    def IgmpPackReports(self):
        """
        get the value of property _IgmpPackReports
        """
        if self.force_auto_sync:
            self.get('IgmpPackReports')
        return self._IgmpPackReports

    @property
    def IgmpForceSingleInitialJoin(self):
        """
        get the value of property _IgmpForceSingleInitialJoin
        """
        if self.force_auto_sync:
            self.get('IgmpForceSingleInitialJoin')
        return self._IgmpForceSingleInitialJoin

    @property
    def IgmpForceRobustJoin(self):
        """
        get the value of property _IgmpForceRobustJoin
        """
        if self.force_auto_sync:
            self.get('IgmpForceRobustJoin')
        return self._IgmpForceRobustJoin

    @property
    def IgmpRobustnessVariable(self):
        """
        get the value of property _IgmpRobustnessVariable
        """
        if self.force_auto_sync:
            self.get('IgmpRobustnessVariable')
        return self._IgmpRobustnessVariable

    @property
    def IgmpUnsolicitedReportInterval(self):
        """
        get the value of property _IgmpUnsolicitedReportInterval
        """
        if self.force_auto_sync:
            self.get('IgmpUnsolicitedReportInterval')
        return self._IgmpUnsolicitedReportInterval

    @property
    def IgmpForceLeave(self):
        """
        get the value of property _IgmpForceLeave
        """
        if self.force_auto_sync:
            self.get('IgmpForceLeave')
        return self._IgmpForceLeave

    @property
    def Igmpv1RouterPresentTimeout(self):
        """
        get the value of property _Igmpv1RouterPresentTimeout
        """
        if self.force_auto_sync:
            self.get('Igmpv1RouterPresentTimeout')
        return self._Igmpv1RouterPresentTimeout

    @property
    def IgmpIPv4DoNotFragment(self):
        """
        get the value of property _IgmpIPv4DoNotFragment
        """
        if self.force_auto_sync:
            self.get('IgmpIPv4DoNotFragment')
        return self._IgmpIPv4DoNotFragment

    @property
    def IgmpIPv4TosValue(self):
        """
        get the value of property _IgmpIPv4TosValue
        """
        if self.force_auto_sync:
            self.get('IgmpIPv4TosValue')
        return self._IgmpIPv4TosValue

    @IgmpMulticastVersion.setter
    def IgmpMulticastVersion(self, value):
        self._IgmpMulticastVersion = value
        self.edit(IgmpMulticastVersion=value)

    @IgmpPackReports.setter
    def IgmpPackReports(self, value):
        self._IgmpPackReports = value
        self.edit(IgmpPackReports=value)

    @IgmpForceSingleInitialJoin.setter
    def IgmpForceSingleInitialJoin(self, value):
        self._IgmpForceSingleInitialJoin = value
        self.edit(IgmpForceSingleInitialJoin=value)

    @IgmpForceRobustJoin.setter
    def IgmpForceRobustJoin(self, value):
        self._IgmpForceRobustJoin = value
        self.edit(IgmpForceRobustJoin=value)

    @IgmpRobustnessVariable.setter
    def IgmpRobustnessVariable(self, value):
        self._IgmpRobustnessVariable = value
        self.edit(IgmpRobustnessVariable=value)

    @IgmpUnsolicitedReportInterval.setter
    def IgmpUnsolicitedReportInterval(self, value):
        self._IgmpUnsolicitedReportInterval = value
        self.edit(IgmpUnsolicitedReportInterval=value)

    @IgmpForceLeave.setter
    def IgmpForceLeave(self, value):
        self._IgmpForceLeave = value
        self.edit(IgmpForceLeave=value)

    @Igmpv1RouterPresentTimeout.setter
    def Igmpv1RouterPresentTimeout(self, value):
        self._Igmpv1RouterPresentTimeout = value
        self.edit(Igmpv1RouterPresentTimeout=value)

    @IgmpIPv4DoNotFragment.setter
    def IgmpIPv4DoNotFragment(self, value):
        self._IgmpIPv4DoNotFragment = value
        self.edit(IgmpIPv4DoNotFragment=value)

    @IgmpIPv4TosValue.setter
    def IgmpIPv4TosValue(self, value):
        self._IgmpIPv4TosValue = value
        self.edit(IgmpIPv4TosValue=value)

    def _set_igmphoststate_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpHostState = EnumIgmpHostState.%s' % value[:seperate])

    def _set_igmpmulticastversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpMulticastVersion = EnumIgmpMulticastVersion.%s' % value[:seperate])

    def _set_igmpgroupcount_with_str(self, value):
        try:
            self._IgmpGroupCount = int(value)
        except ValueError:
            self._IgmpGroupCount = hex(int(value, 16))

    def _set_igmpsourcecount_with_str(self, value):
        try:
            self._IgmpSourceCount = int(value)
        except ValueError:
            self._IgmpSourceCount = hex(int(value, 16))

    def _set_igmppackreports_with_str(self, value):
        self._IgmpPackReports = (value == 'True')

    def _set_igmpforcesingleinitialjoin_with_str(self, value):
        self._IgmpForceSingleInitialJoin = (value == 'True')

    def _set_igmpforcerobustjoin_with_str(self, value):
        self._IgmpForceRobustJoin = (value == 'True')

    def _set_igmprobustnessvariable_with_str(self, value):
        try:
            self._IgmpRobustnessVariable = int(value)
        except ValueError:
            self._IgmpRobustnessVariable = hex(int(value, 16))

    def _set_igmpunsolicitedreportinterval_with_str(self, value):
        try:
            self._IgmpUnsolicitedReportInterval = int(value)
        except ValueError:
            self._IgmpUnsolicitedReportInterval = hex(int(value, 16))

    def _set_igmpforceleave_with_str(self, value):
        self._IgmpForceLeave = (value == 'True')

    def _set_igmpv1routerpresenttimeout_with_str(self, value):
        try:
            self._Igmpv1RouterPresentTimeout = int(value)
        except ValueError:
            self._Igmpv1RouterPresentTimeout = hex(int(value, 16))

    def _set_igmpipv4donotfragment_with_str(self, value):
        self._IgmpIPv4DoNotFragment = (value == 'True')

    def _set_igmpipv4tosvalue_with_str(self, value):
        try:
            self._IgmpIPv4TosValue = int(value)
        except ValueError:
            self._IgmpIPv4TosValue = hex(int(value, 16))

