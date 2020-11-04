"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BaseLoadProfileConfig_Autogen import BaseLoadProfileConfig


@rom_manager.rom
class SearchLoadProfileConfig(BaseLoadProfileConfig):
    def __init__(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, Backoff=None, AcceptableFrameLoss=None, IgnoreMinMaxLimit=None, EnableMaxLatencyThreshold=None, EnableOutOfSeqThreshold=None, MaxLatencyThreshold=None, OutOfSeqThreshold=None, **kwargs):
        self._TrafficLoadSearchMode = TrafficLoadSearchMode  # Search mode
        self._LowestRate = LowestRate  # Rate Lower Limit (%)
        self._UppermostRate = UppermostRate  # Rate Upper Limit (%)
        self._InitRate = InitRate  # Initial Rate (%)
        self._RateStep = RateStep  # Step Rate (%)
        self._RateResolution = RateResolution  # Resolution Rate (%)
        self._Backoff = Backoff  # Back-off (%)
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss (%)
        self._IgnoreMinMaxLimit = IgnoreMinMaxLimit  # Ignore Lower/Upper limits
        self._EnableMaxLatencyThreshold = EnableMaxLatencyThreshold  # Enable Max Latency Threshold (us)
        self._EnableOutOfSeqThreshold = EnableOutOfSeqThreshold  # Enable Out of Seq Threshold (us)
        self._MaxLatencyThreshold = MaxLatencyThreshold  # Max Latency Threshold
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
        if EnableMaxLatencyThreshold is not None:
            properties['EnableMaxLatencyThreshold'] = EnableMaxLatencyThreshold
        if EnableOutOfSeqThreshold is not None:
            properties['EnableOutOfSeqThreshold'] = EnableOutOfSeqThreshold
        if MaxLatencyThreshold is not None:
            properties['MaxLatencyThreshold'] = MaxLatencyThreshold
        if OutOfSeqThreshold is not None:
            properties['OutOfSeqThreshold'] = OutOfSeqThreshold

        # call base class function, and it will send message to renix server to create a class.
        super(SearchLoadProfileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficLoadSearchMode=None, LowestRate=None, UppermostRate=None, InitRate=None, RateStep=None, RateResolution=None, Backoff=None, AcceptableFrameLoss=None, IgnoreMinMaxLimit=None, EnableMaxLatencyThreshold=None, EnableOutOfSeqThreshold=None, MaxLatencyThreshold=None, OutOfSeqThreshold=None, **kwargs):
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

        super(SearchLoadProfileConfig, self).edit(**properties)

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

    def _set_enablemaxlatencythreshold_with_str(self, value):
        self._EnableMaxLatencyThreshold = (value == 'True')

    def _set_enableoutofseqthreshold_with_str(self, value):
        self._EnableOutOfSeqThreshold = (value == 'True')

    def _set_maxlatencythreshold_with_str(self, value):
        self._MaxLatencyThreshold = float(value)

    def _set_outofseqthreshold_with_str(self, value):
        self._OutOfSeqThreshold = float(value)

