"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc3918Config_Autogen import Rfc3918Config


@rom_manager.rom
class AggregatedMulticastThroughputConfig(Rfc3918Config):
    def __init__(self, AcceptableFrameLoss=None, TrafficLoadSearchMode=None, MinimumRate=None, MaximumRate=None, InitRate=None, RateStep=None, RateResolution=None, TrafficLoadBackoff=None, IgnoreTrafficLoadLimit=None, EnableMaxLatency=None, MaxLatencyThreshold=None, McGroupCountMode=None, McGroupCount=None, RandomMinMcGroupCount=None, RandomMaxMcGroupCount=None, McGroupCountStart=None, McGroupCountStep=None, McGroupCountEnd=None, McGroupCountCustom=None, **kwargs):
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)
        self._TrafficLoadSearchMode = TrafficLoadSearchMode  # Traffic load search mode
        self._MinimumRate = MinimumRate  # Minimum Rate
        self._MaximumRate = MaximumRate  # Maximum Rate(%)
        self._InitRate = InitRate  # Init Rate(%)
        self._RateStep = RateStep  # Rate Step(%)
        self._RateResolution = RateResolution  # Rate Resolution(%)
        self._TrafficLoadBackoff = TrafficLoadBackoff  # Back Off
        self._IgnoreTrafficLoadLimit = IgnoreTrafficLoadLimit  # Ignore Minimum and Maximum Limits
        self._EnableMaxLatency = EnableMaxLatency  # Enable Maximum Latency Threshhold(us)
        self._MaxLatencyThreshold = MaxLatencyThreshold  # Maximum Latency Threshold
        self._McGroupCountMode = McGroupCountMode  # Multicast Group Mode
        self._McGroupCount = McGroupCount  # Multicast Group Count
        self._RandomMinMcGroupCount = RandomMinMcGroupCount  # Min
        self._RandomMaxMcGroupCount = RandomMaxMcGroupCount  # Max
        self._McGroupCountStart = McGroupCountStart  # Start
        self._McGroupCountStep = McGroupCountStep  # Step
        self._McGroupCountEnd = McGroupCountEnd  # End
        self._McGroupCountCustom = McGroupCountCustom  # Custom

        properties = kwargs.copy()
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if TrafficLoadSearchMode is not None:
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if MinimumRate is not None:
            properties['MinimumRate'] = MinimumRate
        if MaximumRate is not None:
            properties['MaximumRate'] = MaximumRate
        if InitRate is not None:
            properties['InitRate'] = InitRate
        if RateStep is not None:
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            properties['RateResolution'] = RateResolution
        if TrafficLoadBackoff is not None:
            properties['TrafficLoadBackoff'] = TrafficLoadBackoff
        if IgnoreTrafficLoadLimit is not None:
            properties['IgnoreTrafficLoadLimit'] = IgnoreTrafficLoadLimit
        if EnableMaxLatency is not None:
            properties['EnableMaxLatency'] = EnableMaxLatency
        if MaxLatencyThreshold is not None:
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if McGroupCountMode is not None:
            properties['McGroupCountMode'] = McGroupCountMode
        if McGroupCount is not None:
            properties['McGroupCount'] = McGroupCount
        if RandomMinMcGroupCount is not None:
            properties['RandomMinMcGroupCount'] = RandomMinMcGroupCount
        if RandomMaxMcGroupCount is not None:
            properties['RandomMaxMcGroupCount'] = RandomMaxMcGroupCount
        if McGroupCountStart is not None:
            properties['McGroupCountStart'] = McGroupCountStart
        if McGroupCountStep is not None:
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountEnd is not None:
            properties['McGroupCountEnd'] = McGroupCountEnd
        if McGroupCountCustom is not None:
            properties['McGroupCountCustom'] = McGroupCountCustom

        # call base class function, and it will send message to renix server to create a class.
        super(AggregatedMulticastThroughputConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AcceptableFrameLoss=None, TrafficLoadSearchMode=None, MinimumRate=None, MaximumRate=None, InitRate=None, RateStep=None, RateResolution=None, TrafficLoadBackoff=None, IgnoreTrafficLoadLimit=None, EnableMaxLatency=None, MaxLatencyThreshold=None, McGroupCountMode=None, McGroupCount=None, RandomMinMcGroupCount=None, RandomMaxMcGroupCount=None, McGroupCountStart=None, McGroupCountStep=None, McGroupCountEnd=None, McGroupCountCustom=None, **kwargs):
        properties = kwargs.copy()
        if AcceptableFrameLoss is not None:
            self._AcceptableFrameLoss = AcceptableFrameLoss
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if TrafficLoadSearchMode is not None:
            self._TrafficLoadSearchMode = TrafficLoadSearchMode
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if MinimumRate is not None:
            self._MinimumRate = MinimumRate
            properties['MinimumRate'] = MinimumRate
        if MaximumRate is not None:
            self._MaximumRate = MaximumRate
            properties['MaximumRate'] = MaximumRate
        if InitRate is not None:
            self._InitRate = InitRate
            properties['InitRate'] = InitRate
        if RateStep is not None:
            self._RateStep = RateStep
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            self._RateResolution = RateResolution
            properties['RateResolution'] = RateResolution
        if TrafficLoadBackoff is not None:
            self._TrafficLoadBackoff = TrafficLoadBackoff
            properties['TrafficLoadBackoff'] = TrafficLoadBackoff
        if IgnoreTrafficLoadLimit is not None:
            self._IgnoreTrafficLoadLimit = IgnoreTrafficLoadLimit
            properties['IgnoreTrafficLoadLimit'] = IgnoreTrafficLoadLimit
        if EnableMaxLatency is not None:
            self._EnableMaxLatency = EnableMaxLatency
            properties['EnableMaxLatency'] = EnableMaxLatency
        if MaxLatencyThreshold is not None:
            self._MaxLatencyThreshold = MaxLatencyThreshold
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if McGroupCountMode is not None:
            self._McGroupCountMode = McGroupCountMode
            properties['McGroupCountMode'] = McGroupCountMode
        if McGroupCount is not None:
            self._McGroupCount = McGroupCount
            properties['McGroupCount'] = McGroupCount
        if RandomMinMcGroupCount is not None:
            self._RandomMinMcGroupCount = RandomMinMcGroupCount
            properties['RandomMinMcGroupCount'] = RandomMinMcGroupCount
        if RandomMaxMcGroupCount is not None:
            self._RandomMaxMcGroupCount = RandomMaxMcGroupCount
            properties['RandomMaxMcGroupCount'] = RandomMaxMcGroupCount
        if McGroupCountStart is not None:
            self._McGroupCountStart = McGroupCountStart
            properties['McGroupCountStart'] = McGroupCountStart
        if McGroupCountStep is not None:
            self._McGroupCountStep = McGroupCountStep
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountEnd is not None:
            self._McGroupCountEnd = McGroupCountEnd
            properties['McGroupCountEnd'] = McGroupCountEnd
        if McGroupCountCustom is not None:
            self._McGroupCountCustom = McGroupCountCustom
            properties['McGroupCountCustom'] = McGroupCountCustom

        super(AggregatedMulticastThroughputConfig, self).edit(**properties)

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        if self.force_auto_sync:
            self.get('AcceptableFrameLoss')
        return self._AcceptableFrameLoss

    @property
    def TrafficLoadSearchMode(self):
        """
        get the value of property _TrafficLoadSearchMode
        """
        if self.force_auto_sync:
            self.get('TrafficLoadSearchMode')
        return self._TrafficLoadSearchMode

    @property
    def MinimumRate(self):
        """
        get the value of property _MinimumRate
        """
        if self.force_auto_sync:
            self.get('MinimumRate')
        return self._MinimumRate

    @property
    def MaximumRate(self):
        """
        get the value of property _MaximumRate
        """
        if self.force_auto_sync:
            self.get('MaximumRate')
        return self._MaximumRate

    @property
    def InitRate(self):
        """
        get the value of property _InitRate
        """
        if self.force_auto_sync:
            self.get('InitRate')
        return self._InitRate

    @property
    def RateStep(self):
        """
        get the value of property _RateStep
        """
        if self.force_auto_sync:
            self.get('RateStep')
        return self._RateStep

    @property
    def RateResolution(self):
        """
        get the value of property _RateResolution
        """
        if self.force_auto_sync:
            self.get('RateResolution')
        return self._RateResolution

    @property
    def TrafficLoadBackoff(self):
        """
        get the value of property _TrafficLoadBackoff
        """
        if self.force_auto_sync:
            self.get('TrafficLoadBackoff')
        return self._TrafficLoadBackoff

    @property
    def IgnoreTrafficLoadLimit(self):
        """
        get the value of property _IgnoreTrafficLoadLimit
        """
        if self.force_auto_sync:
            self.get('IgnoreTrafficLoadLimit')
        return self._IgnoreTrafficLoadLimit

    @property
    def EnableMaxLatency(self):
        """
        get the value of property _EnableMaxLatency
        """
        if self.force_auto_sync:
            self.get('EnableMaxLatency')
        return self._EnableMaxLatency

    @property
    def MaxLatencyThreshold(self):
        """
        get the value of property _MaxLatencyThreshold
        """
        if self.force_auto_sync:
            self.get('MaxLatencyThreshold')
        return self._MaxLatencyThreshold

    @property
    def McGroupCountMode(self):
        """
        get the value of property _McGroupCountMode
        """
        if self.force_auto_sync:
            self.get('McGroupCountMode')
        return self._McGroupCountMode

    @property
    def McGroupCount(self):
        """
        get the value of property _McGroupCount
        """
        if self.force_auto_sync:
            self.get('McGroupCount')
        return self._McGroupCount

    @property
    def RandomMinMcGroupCount(self):
        """
        get the value of property _RandomMinMcGroupCount
        """
        if self.force_auto_sync:
            self.get('RandomMinMcGroupCount')
        return self._RandomMinMcGroupCount

    @property
    def RandomMaxMcGroupCount(self):
        """
        get the value of property _RandomMaxMcGroupCount
        """
        if self.force_auto_sync:
            self.get('RandomMaxMcGroupCount')
        return self._RandomMaxMcGroupCount

    @property
    def McGroupCountStart(self):
        """
        get the value of property _McGroupCountStart
        """
        if self.force_auto_sync:
            self.get('McGroupCountStart')
        return self._McGroupCountStart

    @property
    def McGroupCountStep(self):
        """
        get the value of property _McGroupCountStep
        """
        if self.force_auto_sync:
            self.get('McGroupCountStep')
        return self._McGroupCountStep

    @property
    def McGroupCountEnd(self):
        """
        get the value of property _McGroupCountEnd
        """
        if self.force_auto_sync:
            self.get('McGroupCountEnd')
        return self._McGroupCountEnd

    @property
    def McGroupCountCustom(self):
        """
        get the value of property _McGroupCountCustom
        """
        if self.force_auto_sync:
            self.get('McGroupCountCustom')
        return self._McGroupCountCustom

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value
        self.edit(AcceptableFrameLoss=value)

    @TrafficLoadSearchMode.setter
    def TrafficLoadSearchMode(self, value):
        self._TrafficLoadSearchMode = value
        self.edit(TrafficLoadSearchMode=value)

    @MinimumRate.setter
    def MinimumRate(self, value):
        self._MinimumRate = value
        self.edit(MinimumRate=value)

    @MaximumRate.setter
    def MaximumRate(self, value):
        self._MaximumRate = value
        self.edit(MaximumRate=value)

    @InitRate.setter
    def InitRate(self, value):
        self._InitRate = value
        self.edit(InitRate=value)

    @RateStep.setter
    def RateStep(self, value):
        self._RateStep = value
        self.edit(RateStep=value)

    @RateResolution.setter
    def RateResolution(self, value):
        self._RateResolution = value
        self.edit(RateResolution=value)

    @TrafficLoadBackoff.setter
    def TrafficLoadBackoff(self, value):
        self._TrafficLoadBackoff = value
        self.edit(TrafficLoadBackoff=value)

    @IgnoreTrafficLoadLimit.setter
    def IgnoreTrafficLoadLimit(self, value):
        self._IgnoreTrafficLoadLimit = value
        self.edit(IgnoreTrafficLoadLimit=value)

    @EnableMaxLatency.setter
    def EnableMaxLatency(self, value):
        self._EnableMaxLatency = value
        self.edit(EnableMaxLatency=value)

    @MaxLatencyThreshold.setter
    def MaxLatencyThreshold(self, value):
        self._MaxLatencyThreshold = value
        self.edit(MaxLatencyThreshold=value)

    @McGroupCountMode.setter
    def McGroupCountMode(self, value):
        self._McGroupCountMode = value
        self.edit(McGroupCountMode=value)

    @McGroupCount.setter
    def McGroupCount(self, value):
        self._McGroupCount = value
        self.edit(McGroupCount=value)

    @RandomMinMcGroupCount.setter
    def RandomMinMcGroupCount(self, value):
        self._RandomMinMcGroupCount = value
        self.edit(RandomMinMcGroupCount=value)

    @RandomMaxMcGroupCount.setter
    def RandomMaxMcGroupCount(self, value):
        self._RandomMaxMcGroupCount = value
        self.edit(RandomMaxMcGroupCount=value)

    @McGroupCountStart.setter
    def McGroupCountStart(self, value):
        self._McGroupCountStart = value
        self.edit(McGroupCountStart=value)

    @McGroupCountStep.setter
    def McGroupCountStep(self, value):
        self._McGroupCountStep = value
        self.edit(McGroupCountStep=value)

    @McGroupCountEnd.setter
    def McGroupCountEnd(self, value):
        self._McGroupCountEnd = value
        self.edit(McGroupCountEnd=value)

    @McGroupCountCustom.setter
    def McGroupCountCustom(self, value):
        self._McGroupCountCustom = value
        self.edit(McGroupCountCustom=value)

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_trafficloadsearchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadSearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_minimumrate_with_str(self, value):
        self._MinimumRate = float(value)

    def _set_maximumrate_with_str(self, value):
        self._MaximumRate = float(value)

    def _set_initrate_with_str(self, value):
        self._InitRate = float(value)

    def _set_ratestep_with_str(self, value):
        self._RateStep = float(value)

    def _set_rateresolution_with_str(self, value):
        self._RateResolution = float(value)

    def _set_trafficloadbackoff_with_str(self, value):
        self._TrafficLoadBackoff = float(value)

    def _set_ignoretrafficloadlimit_with_str(self, value):
        self._IgnoreTrafficLoadLimit = (value == 'True')

    def _set_enablemaxlatency_with_str(self, value):
        self._EnableMaxLatency = (value == 'True')

    def _set_maxlatencythreshold_with_str(self, value):
        self._MaxLatencyThreshold = float(value)

    def _set_mcgroupcountmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._McGroupCountMode = EnumMulticastGroupCountMode.%s' % value[:seperate])

    def _set_mcgroupcount_with_str(self, value):
        try:
            self._McGroupCount = int(value)
        except ValueError:
            self._McGroupCount = hex(int(value, 16))

    def _set_randomminmcgroupcount_with_str(self, value):
        try:
            self._RandomMinMcGroupCount = int(value)
        except ValueError:
            self._RandomMinMcGroupCount = hex(int(value, 16))

    def _set_randommaxmcgroupcount_with_str(self, value):
        try:
            self._RandomMaxMcGroupCount = int(value)
        except ValueError:
            self._RandomMaxMcGroupCount = hex(int(value, 16))

    def _set_mcgroupcountstart_with_str(self, value):
        try:
            self._McGroupCountStart = int(value)
        except ValueError:
            self._McGroupCountStart = hex(int(value, 16))

    def _set_mcgroupcountstep_with_str(self, value):
        try:
            self._McGroupCountStep = int(value)
        except ValueError:
            self._McGroupCountStep = hex(int(value, 16))

    def _set_mcgroupcountend_with_str(self, value):
        try:
            self._McGroupCountEnd = int(value)
        except ValueError:
            self._McGroupCountEnd = hex(int(value, 16))

    def _set_mcgroupcountcustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._McGroupCountCustom = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._McGroupCountCustom.append(int(str_value))
            except ValueError:
                self._McGroupCountCustom.append(hex(int(str_value, 16)))

