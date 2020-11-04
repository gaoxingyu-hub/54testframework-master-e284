"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2544Config_Autogen import Rfc2544Config


@rom_manager.rom
class Rfc2544ThroughputConfig(Rfc2544Config):
    def __init__(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, Backoff=None, AcceptableFrameLoss=None, IgnoreMinMaxLimit=None, MaxLatency=None, EnableMaxLatencyThreshold=None, EnableOutOfSeqThreshold=None, MaxLatencyThreshold=None, OutOfSeqThreshold=None, **kwargs):
        self._TrafficLoadSearchMode = TrafficLoadSearchMode  # Traffic load search mode
        self._LowestRate = LowestRate  # Lowest Rate(%)
        self._UppermostRate = UppermostRate  # Uppermost Rate(%)
        self._InitRate = InitRate  # Init Rate(%)
        self._RateStep = RateStep  # Rate Step(%)
        self._RateResolution = RateResolution  # Rate Resolution(%)
        self._Backoff = Backoff  # Back Off
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)
        self._IgnoreMinMaxLimit = IgnoreMinMaxLimit  # Ignore Min and Max limit
        self._MaxLatency = MaxLatency  # Max Latency (ns)
        self._EnableMaxLatencyThreshold = EnableMaxLatencyThreshold  # Enable Maximum Latency Threshold (us)
        self._EnableOutOfSeqThreshold = EnableOutOfSeqThreshold  # Enable Maximum Latency Threshold (us)
        self._MaxLatencyThreshold = MaxLatencyThreshold  # Maximum Latency Threshold
        self._OutOfSeqThreshold = OutOfSeqThreshold  # Out of Sequence Threshold

        properties = kwargs.copy()
        if TrafficLoadSearchMode is not None:
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if LowestRate is not None:
            properties['LowestRate'] = LowestRate
        if UppermostRate is not None:
            properties['UppermostRate'] = UppermostRate
        if InitRate is not None:
            properties['InitRate'] = InitRate
        if RateStep is not None:
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            properties['RateResolution'] = RateResolution
        if Backoff is not None:
            properties['Backoff'] = Backoff
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if IgnoreMinMaxLimit is not None:
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit
        if MaxLatency is not None:
            properties['MaxLatency'] = MaxLatency
        if EnableMaxLatencyThreshold is not None:
            properties['EnableMaxLatencyThreshold'] = EnableMaxLatencyThreshold
        if EnableOutOfSeqThreshold is not None:
            properties['EnableOutOfSeqThreshold'] = EnableOutOfSeqThreshold
        if MaxLatencyThreshold is not None:
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if OutOfSeqThreshold is not None:
            properties['OutOfSeqThreshold'] = OutOfSeqThreshold

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc2544ThroughputConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, Backoff=None, AcceptableFrameLoss=None, IgnoreMinMaxLimit=None, MaxLatency=None, EnableMaxLatencyThreshold=None, EnableOutOfSeqThreshold=None, MaxLatencyThreshold=None, OutOfSeqThreshold=None, **kwargs):
        properties = kwargs.copy()
        if TrafficLoadSearchMode is not None:
            self._TrafficLoadSearchMode = TrafficLoadSearchMode
            properties['TrafficLoadSearchMode'] = TrafficLoadSearchMode
        if LowestRate is not None:
            self._LowestRate = LowestRate
            properties['LowestRate'] = LowestRate
        if UppermostRate is not None:
            self._UppermostRate = UppermostRate
            properties['UppermostRate'] = UppermostRate
        if InitRate is not None:
            self._InitRate = InitRate
            properties['InitRate'] = InitRate
        if RateStep is not None:
            self._RateStep = RateStep
            properties['RateStep'] = RateStep
        if RateResolution is not None:
            self._RateResolution = RateResolution
            properties['RateResolution'] = RateResolution
        if Backoff is not None:
            self._Backoff = Backoff
            properties['Backoff'] = Backoff
        if AcceptableFrameLoss is not None:
            self._AcceptableFrameLoss = AcceptableFrameLoss
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if IgnoreMinMaxLimit is not None:
            self._IgnoreMinMaxLimit = IgnoreMinMaxLimit
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit
        if MaxLatency is not None:
            self._MaxLatency = MaxLatency
            properties['MaxLatency'] = MaxLatency
        if EnableMaxLatencyThreshold is not None:
            self._EnableMaxLatencyThreshold = EnableMaxLatencyThreshold
            properties['EnableMaxLatencyThreshold'] = EnableMaxLatencyThreshold
        if EnableOutOfSeqThreshold is not None:
            self._EnableOutOfSeqThreshold = EnableOutOfSeqThreshold
            properties['EnableOutOfSeqThreshold'] = EnableOutOfSeqThreshold
        if MaxLatencyThreshold is not None:
            self._MaxLatencyThreshold = MaxLatencyThreshold
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if OutOfSeqThreshold is not None:
            self._OutOfSeqThreshold = OutOfSeqThreshold
            properties['OutOfSeqThreshold'] = OutOfSeqThreshold

        super(Rfc2544ThroughputConfig, self).edit(**properties)

    @property
    def TrafficLoadSearchMode(self):
        """
        get the value of property _TrafficLoadSearchMode
        """
        if self.force_auto_sync:
            self.get('TrafficLoadSearchMode')
        return self._TrafficLoadSearchMode

    @property
    def LowestRate(self):
        """
        get the value of property _LowestRate
        """
        if self.force_auto_sync:
            self.get('LowestRate')
        return self._LowestRate

    @property
    def UppermostRate(self):
        """
        get the value of property _UppermostRate
        """
        if self.force_auto_sync:
            self.get('UppermostRate')
        return self._UppermostRate

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
    def Backoff(self):
        """
        get the value of property _Backoff
        """
        if self.force_auto_sync:
            self.get('Backoff')
        return self._Backoff

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        if self.force_auto_sync:
            self.get('AcceptableFrameLoss')
        return self._AcceptableFrameLoss

    @property
    def IgnoreMinMaxLimit(self):
        """
        get the value of property _IgnoreMinMaxLimit
        """
        if self.force_auto_sync:
            self.get('IgnoreMinMaxLimit')
        return self._IgnoreMinMaxLimit

    @property
    def MaxLatency(self):
        """
        get the value of property _MaxLatency
        """
        if self.force_auto_sync:
            self.get('MaxLatency')
        return self._MaxLatency

    @property
    def EnableMaxLatencyThreshold(self):
        """
        get the value of property _EnableMaxLatencyThreshold
        """
        if self.force_auto_sync:
            self.get('EnableMaxLatencyThreshold')
        return self._EnableMaxLatencyThreshold

    @property
    def EnableOutOfSeqThreshold(self):
        """
        get the value of property _EnableOutOfSeqThreshold
        """
        if self.force_auto_sync:
            self.get('EnableOutOfSeqThreshold')
        return self._EnableOutOfSeqThreshold

    @property
    def MaxLatencyThreshold(self):
        """
        get the value of property _MaxLatencyThreshold
        """
        if self.force_auto_sync:
            self.get('MaxLatencyThreshold')
        return self._MaxLatencyThreshold

    @property
    def OutOfSeqThreshold(self):
        """
        get the value of property _OutOfSeqThreshold
        """
        if self.force_auto_sync:
            self.get('OutOfSeqThreshold')
        return self._OutOfSeqThreshold

    @TrafficLoadSearchMode.setter
    def TrafficLoadSearchMode(self, value):
        self._TrafficLoadSearchMode = value
        self.edit(TrafficLoadSearchMode=value)

    @LowestRate.setter
    def LowestRate(self, value):
        self._LowestRate = value
        self.edit(LowestRate=value)

    @UppermostRate.setter
    def UppermostRate(self, value):
        self._UppermostRate = value
        self.edit(UppermostRate=value)

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

    @Backoff.setter
    def Backoff(self, value):
        self._Backoff = value
        self.edit(Backoff=value)

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value
        self.edit(AcceptableFrameLoss=value)

    @IgnoreMinMaxLimit.setter
    def IgnoreMinMaxLimit(self, value):
        self._IgnoreMinMaxLimit = value
        self.edit(IgnoreMinMaxLimit=value)

    @MaxLatency.setter
    def MaxLatency(self, value):
        self._MaxLatency = value
        self.edit(MaxLatency=value)

    @EnableMaxLatencyThreshold.setter
    def EnableMaxLatencyThreshold(self, value):
        self._EnableMaxLatencyThreshold = value
        self.edit(EnableMaxLatencyThreshold=value)

    @EnableOutOfSeqThreshold.setter
    def EnableOutOfSeqThreshold(self, value):
        self._EnableOutOfSeqThreshold = value
        self.edit(EnableOutOfSeqThreshold=value)

    @MaxLatencyThreshold.setter
    def MaxLatencyThreshold(self, value):
        self._MaxLatencyThreshold = value
        self.edit(MaxLatencyThreshold=value)

    @OutOfSeqThreshold.setter
    def OutOfSeqThreshold(self, value):
        self._OutOfSeqThreshold = value
        self.edit(OutOfSeqThreshold=value)

    def _set_trafficloadsearchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficLoadSearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_lowestrate_with_str(self, value):
        self._LowestRate = float(value)

    def _set_uppermostrate_with_str(self, value):
        self._UppermostRate = float(value)

    def _set_initrate_with_str(self, value):
        self._InitRate = float(value)

    def _set_ratestep_with_str(self, value):
        self._RateStep = float(value)

    def _set_rateresolution_with_str(self, value):
        self._RateResolution = float(value)

    def _set_backoff_with_str(self, value):
        self._Backoff = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_ignoreminmaxlimit_with_str(self, value):
        self._IgnoreMinMaxLimit = (value == 'True')

    def _set_maxlatency_with_str(self, value):
        try:
            self._MaxLatency = int(value)
        except ValueError:
            self._MaxLatency = hex(int(value, 16))

    def _set_enablemaxlatencythreshold_with_str(self, value):
        self._EnableMaxLatencyThreshold = (value == 'True')

    def _set_enableoutofseqthreshold_with_str(self, value):
        self._EnableOutOfSeqThreshold = (value == 'True')

    def _set_maxlatencythreshold_with_str(self, value):
        self._MaxLatencyThreshold = float(value)

    def _set_outofseqthreshold_with_str(self, value):
        self._OutOfSeqThreshold = float(value)

