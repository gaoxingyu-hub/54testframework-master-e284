"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class IgmpQuerierProtocolConfig(L23ProtocolConfig):
    def __init__(self, QuerierVersion=None, RobustnessVariable=None, QueryInterval=None, QueryResponseInterval=None, StartupQueryCount=None, LastMemberQueryInterval=None, LastMemberQueryCount=None, IPv4DoNotFragment=None, IPv4TosValue=None, **kwargs):
        self._RouterState = EnumIgmpRouterState.NOTSTARTED  # Router State, not editable
        self._QuerierVersion = QuerierVersion  # Multicast Version
        self._RobustnessVariable = RobustnessVariable  # Robustness Variable
        self._QueryInterval = QueryInterval  # Query Interval(sec)
        self._QueryResponseInterval = QueryResponseInterval  # Query Response Interval(msec)
        self._StartupQueryCount = StartupQueryCount  # Startup Query Count
        self._LastMemberQueryInterval = LastMemberQueryInterval  # Last Member Query Interval(msec)
        self._LastMemberQueryCount = LastMemberQueryCount  # Last Member Query Count(msec)
        self._IPv4DoNotFragment = IPv4DoNotFragment  # IPv4 Don't Fragment(DF bit)
        self._IPv4TosValue = IPv4TosValue  # IPv4 TOS value(Hex)

        properties = kwargs.copy()
        if QuerierVersion is not None:
            properties['QuerierVersion'] = QuerierVersion
        if RobustnessVariable is not None:
            properties['RobustnessVariable'] = RobustnessVariable
        if QueryInterval is not None:
            properties['QueryInterval'] = QueryInterval
        if QueryResponseInterval is not None:
            properties['QueryResponseInterval'] = QueryResponseInterval
        if StartupQueryCount is not None:
            properties['StartupQueryCount'] = StartupQueryCount
        if LastMemberQueryInterval is not None:
            properties['LastMemberQueryInterval'] = LastMemberQueryInterval
        if LastMemberQueryCount is not None:
            properties['LastMemberQueryCount'] = LastMemberQueryCount
        if IPv4DoNotFragment is not None:
            properties['IPv4DoNotFragment'] = IPv4DoNotFragment
        if IPv4TosValue is not None:
            properties['IPv4TosValue'] = IPv4TosValue

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpQuerierProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, QuerierVersion=None, RobustnessVariable=None, QueryInterval=None, QueryResponseInterval=None, StartupQueryCount=None, LastMemberQueryInterval=None, LastMemberQueryCount=None, IPv4DoNotFragment=None, IPv4TosValue=None, **kwargs):
        properties = kwargs.copy()
        if QuerierVersion is not None:
            self._QuerierVersion = QuerierVersion
            properties['QuerierVersion'] = QuerierVersion
        if RobustnessVariable is not None:
            self._RobustnessVariable = RobustnessVariable
            properties['RobustnessVariable'] = RobustnessVariable
        if QueryInterval is not None:
            self._QueryInterval = QueryInterval
            properties['QueryInterval'] = QueryInterval
        if QueryResponseInterval is not None:
            self._QueryResponseInterval = QueryResponseInterval
            properties['QueryResponseInterval'] = QueryResponseInterval
        if StartupQueryCount is not None:
            self._StartupQueryCount = StartupQueryCount
            properties['StartupQueryCount'] = StartupQueryCount
        if LastMemberQueryInterval is not None:
            self._LastMemberQueryInterval = LastMemberQueryInterval
            properties['LastMemberQueryInterval'] = LastMemberQueryInterval
        if LastMemberQueryCount is not None:
            self._LastMemberQueryCount = LastMemberQueryCount
            properties['LastMemberQueryCount'] = LastMemberQueryCount
        if IPv4DoNotFragment is not None:
            self._IPv4DoNotFragment = IPv4DoNotFragment
            properties['IPv4DoNotFragment'] = IPv4DoNotFragment
        if IPv4TosValue is not None:
            self._IPv4TosValue = IPv4TosValue
            properties['IPv4TosValue'] = IPv4TosValue

        super(IgmpQuerierProtocolConfig, self).edit(**properties)

    @property
    def RouterState(self):
        """
        get the value of property _RouterState
        """
        if self.force_auto_sync:
            self.get('RouterState')
        return self._RouterState

    @property
    def QuerierVersion(self):
        """
        get the value of property _QuerierVersion
        """
        if self.force_auto_sync:
            self.get('QuerierVersion')
        return self._QuerierVersion

    @property
    def RobustnessVariable(self):
        """
        get the value of property _RobustnessVariable
        """
        if self.force_auto_sync:
            self.get('RobustnessVariable')
        return self._RobustnessVariable

    @property
    def QueryInterval(self):
        """
        get the value of property _QueryInterval
        """
        if self.force_auto_sync:
            self.get('QueryInterval')
        return self._QueryInterval

    @property
    def QueryResponseInterval(self):
        """
        get the value of property _QueryResponseInterval
        """
        if self.force_auto_sync:
            self.get('QueryResponseInterval')
        return self._QueryResponseInterval

    @property
    def StartupQueryCount(self):
        """
        get the value of property _StartupQueryCount
        """
        if self.force_auto_sync:
            self.get('StartupQueryCount')
        return self._StartupQueryCount

    @property
    def LastMemberQueryInterval(self):
        """
        get the value of property _LastMemberQueryInterval
        """
        if self.force_auto_sync:
            self.get('LastMemberQueryInterval')
        return self._LastMemberQueryInterval

    @property
    def LastMemberQueryCount(self):
        """
        get the value of property _LastMemberQueryCount
        """
        if self.force_auto_sync:
            self.get('LastMemberQueryCount')
        return self._LastMemberQueryCount

    @property
    def IPv4DoNotFragment(self):
        """
        get the value of property _IPv4DoNotFragment
        """
        if self.force_auto_sync:
            self.get('IPv4DoNotFragment')
        return self._IPv4DoNotFragment

    @property
    def IPv4TosValue(self):
        """
        get the value of property _IPv4TosValue
        """
        if self.force_auto_sync:
            self.get('IPv4TosValue')
        return self._IPv4TosValue

    @QuerierVersion.setter
    def QuerierVersion(self, value):
        self._QuerierVersion = value
        self.edit(QuerierVersion=value)

    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        self._RobustnessVariable = value
        self.edit(RobustnessVariable=value)

    @QueryInterval.setter
    def QueryInterval(self, value):
        self._QueryInterval = value
        self.edit(QueryInterval=value)

    @QueryResponseInterval.setter
    def QueryResponseInterval(self, value):
        self._QueryResponseInterval = value
        self.edit(QueryResponseInterval=value)

    @StartupQueryCount.setter
    def StartupQueryCount(self, value):
        self._StartupQueryCount = value
        self.edit(StartupQueryCount=value)

    @LastMemberQueryInterval.setter
    def LastMemberQueryInterval(self, value):
        self._LastMemberQueryInterval = value
        self.edit(LastMemberQueryInterval=value)

    @LastMemberQueryCount.setter
    def LastMemberQueryCount(self, value):
        self._LastMemberQueryCount = value
        self.edit(LastMemberQueryCount=value)

    @IPv4DoNotFragment.setter
    def IPv4DoNotFragment(self, value):
        self._IPv4DoNotFragment = value
        self.edit(IPv4DoNotFragment=value)

    @IPv4TosValue.setter
    def IPv4TosValue(self, value):
        self._IPv4TosValue = value
        self.edit(IPv4TosValue=value)

    def _set_routerstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouterState = EnumIgmpRouterState.%s' % value[:seperate])

    def _set_querierversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._QuerierVersion = EnumIgmpQuerierVersion.%s' % value[:seperate])

    def _set_robustnessvariable_with_str(self, value):
        try:
            self._RobustnessVariable = int(value)
        except ValueError:
            self._RobustnessVariable = hex(int(value, 16))

    def _set_queryinterval_with_str(self, value):
        try:
            self._QueryInterval = int(value)
        except ValueError:
            self._QueryInterval = hex(int(value, 16))

    def _set_queryresponseinterval_with_str(self, value):
        try:
            self._QueryResponseInterval = int(value)
        except ValueError:
            self._QueryResponseInterval = hex(int(value, 16))

    def _set_startupquerycount_with_str(self, value):
        try:
            self._StartupQueryCount = int(value)
        except ValueError:
            self._StartupQueryCount = hex(int(value, 16))

    def _set_lastmemberqueryinterval_with_str(self, value):
        try:
            self._LastMemberQueryInterval = int(value)
        except ValueError:
            self._LastMemberQueryInterval = hex(int(value, 16))

    def _set_lastmemberquerycount_with_str(self, value):
        try:
            self._LastMemberQueryCount = int(value)
        except ValueError:
            self._LastMemberQueryCount = hex(int(value, 16))

    def _set_ipv4donotfragment_with_str(self, value):
        self._IPv4DoNotFragment = (value == 'True')

    def _set_ipv4tosvalue_with_str(self, value):
        try:
            self._IPv4TosValue = int(value)
        except ValueError:
            self._IPv4TosValue = hex(int(value, 16))

