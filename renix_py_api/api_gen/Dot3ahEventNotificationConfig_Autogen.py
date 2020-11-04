"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot3ahEventNotificationConfig(ROMObject):
    def __init__(self, InitialTime=None, EventRepeatPeriod=None, EnableErroredFrameEvent=None, EfeWindow=None, EfeThreshold=None, EfeErrorCount=None, EnableErroredFramePeriodEvent=None, EfpeWindow=None, EfpeThreshold=None, EfpeErrorCount=None, EnableErroredSymbolPeriodEvent=None, EspeWindow=None, EspeThreshold=None, EspeErrorCount=None, EnableErroredFrameSecondsSummaryEvent=None, EfsseWindow=None, EfsseThreshold=None, EfsseCount=None, EnableOrgSpecEvent=None, OrgSpecEventOUI=None, OrgSpecEventData=None, **kwargs):
        self._InitialTime = InitialTime  # Initial Time (100ms)
        self._EventRepeatPeriod = EventRepeatPeriod  # Event Repeat Period (sec)
        self._EnableErroredFrameEvent = EnableErroredFrameEvent  # Enable Errored Frame Event
        self._EfeWindow = EfeWindow  # EFE Window (100ms)
        self._EfeThreshold = EfeThreshold  # EFE Threshold (frame)
        self._EfeErrorCount = EfeErrorCount  # EFE Error Count
        self._EnableErroredFramePeriodEvent = EnableErroredFramePeriodEvent  # Enable Errored Frame Period Event
        self._EfpeWindow = EfpeWindow  # EFPE Window (frame)
        self._EfpeThreshold = EfpeThreshold  # EFPE Threshold (frame)
        self._EfpeErrorCount = EfpeErrorCount  # EFPE Error Count
        self._EnableErroredSymbolPeriodEvent = EnableErroredSymbolPeriodEvent  # Enable Errored Symbol Period Event
        self._EspeWindow = EspeWindow  # ESPE Window (symbol)
        self._EspeThreshold = EspeThreshold  # ESPE Threshold (symbol)
        self._EspeErrorCount = EspeErrorCount  # ESPE Error Count
        self._EnableErroredFrameSecondsSummaryEvent = EnableErroredFrameSecondsSummaryEvent  # Enable Errored Frame Seconds Summary Event
        self._EfsseWindow = EfsseWindow  # EFSSE Window (100ms)
        self._EfsseThreshold = EfsseThreshold  # EFSSE Threshold (frames/sec)
        self._EfsseCount = EfsseCount  # EFSSE Error Count
        self._EnableOrgSpecEvent = EnableOrgSpecEvent  # Enable Organization Specific Event
        self._OrgSpecEventOUI = OrgSpecEventOUI  # Organization Specific Event OUI
        self._OrgSpecEventData = OrgSpecEventData  # Organization Specific Event Data

        properties = kwargs.copy()
        if InitialTime is not None:
            properties['InitialTime'] = InitialTime
        if EventRepeatPeriod is not None:
            properties['EventRepeatPeriod'] = EventRepeatPeriod
        if EnableErroredFrameEvent is not None:
            properties['EnableErroredFrameEvent'] = EnableErroredFrameEvent
        if EfeWindow is not None:
            properties['EfeWindow'] = EfeWindow
        if EfeThreshold is not None:
            properties['EfeThreshold'] = EfeThreshold
        if EfeErrorCount is not None:
            properties['EfeErrorCount'] = EfeErrorCount
        if EnableErroredFramePeriodEvent is not None:
            properties['EnableErroredFramePeriodEvent'] = EnableErroredFramePeriodEvent
        if EfpeWindow is not None:
            properties['EfpeWindow'] = EfpeWindow
        if EfpeThreshold is not None:
            properties['EfpeThreshold'] = EfpeThreshold
        if EfpeErrorCount is not None:
            properties['EfpeErrorCount'] = EfpeErrorCount
        if EnableErroredSymbolPeriodEvent is not None:
            properties['EnableErroredSymbolPeriodEvent'] = EnableErroredSymbolPeriodEvent
        if EspeWindow is not None:
            properties['EspeWindow'] = EspeWindow
        if EspeThreshold is not None:
            properties['EspeThreshold'] = EspeThreshold
        if EspeErrorCount is not None:
            properties['EspeErrorCount'] = EspeErrorCount
        if EnableErroredFrameSecondsSummaryEvent is not None:
            properties['EnableErroredFrameSecondsSummaryEvent'] = EnableErroredFrameSecondsSummaryEvent
        if EfsseWindow is not None:
            properties['EfsseWindow'] = EfsseWindow
        if EfsseThreshold is not None:
            properties['EfsseThreshold'] = EfsseThreshold
        if EfsseCount is not None:
            properties['EfsseCount'] = EfsseCount
        if EnableOrgSpecEvent is not None:
            properties['EnableOrgSpecEvent'] = EnableOrgSpecEvent
        if OrgSpecEventOUI is not None:
            properties['OrgSpecEventOUI'] = OrgSpecEventOUI
        if OrgSpecEventData is not None:
            properties['OrgSpecEventData'] = OrgSpecEventData

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahEventNotificationConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, InitialTime=None, EventRepeatPeriod=None, EnableErroredFrameEvent=None, EfeWindow=None, EfeThreshold=None, EfeErrorCount=None, EnableErroredFramePeriodEvent=None, EfpeWindow=None, EfpeThreshold=None, EfpeErrorCount=None, EnableErroredSymbolPeriodEvent=None, EspeWindow=None, EspeThreshold=None, EspeErrorCount=None, EnableErroredFrameSecondsSummaryEvent=None, EfsseWindow=None, EfsseThreshold=None, EfsseCount=None, EnableOrgSpecEvent=None, OrgSpecEventOUI=None, OrgSpecEventData=None, **kwargs):
        properties = kwargs.copy()
        if InitialTime is not None:
            self._InitialTime = InitialTime
            properties['InitialTime'] = InitialTime
        if EventRepeatPeriod is not None:
            self._EventRepeatPeriod = EventRepeatPeriod
            properties['EventRepeatPeriod'] = EventRepeatPeriod
        if EnableErroredFrameEvent is not None:
            self._EnableErroredFrameEvent = EnableErroredFrameEvent
            properties['EnableErroredFrameEvent'] = EnableErroredFrameEvent
        if EfeWindow is not None:
            self._EfeWindow = EfeWindow
            properties['EfeWindow'] = EfeWindow
        if EfeThreshold is not None:
            self._EfeThreshold = EfeThreshold
            properties['EfeThreshold'] = EfeThreshold
        if EfeErrorCount is not None:
            self._EfeErrorCount = EfeErrorCount
            properties['EfeErrorCount'] = EfeErrorCount
        if EnableErroredFramePeriodEvent is not None:
            self._EnableErroredFramePeriodEvent = EnableErroredFramePeriodEvent
            properties['EnableErroredFramePeriodEvent'] = EnableErroredFramePeriodEvent
        if EfpeWindow is not None:
            self._EfpeWindow = EfpeWindow
            properties['EfpeWindow'] = EfpeWindow
        if EfpeThreshold is not None:
            self._EfpeThreshold = EfpeThreshold
            properties['EfpeThreshold'] = EfpeThreshold
        if EfpeErrorCount is not None:
            self._EfpeErrorCount = EfpeErrorCount
            properties['EfpeErrorCount'] = EfpeErrorCount
        if EnableErroredSymbolPeriodEvent is not None:
            self._EnableErroredSymbolPeriodEvent = EnableErroredSymbolPeriodEvent
            properties['EnableErroredSymbolPeriodEvent'] = EnableErroredSymbolPeriodEvent
        if EspeWindow is not None:
            self._EspeWindow = EspeWindow
            properties['EspeWindow'] = EspeWindow
        if EspeThreshold is not None:
            self._EspeThreshold = EspeThreshold
            properties['EspeThreshold'] = EspeThreshold
        if EspeErrorCount is not None:
            self._EspeErrorCount = EspeErrorCount
            properties['EspeErrorCount'] = EspeErrorCount
        if EnableErroredFrameSecondsSummaryEvent is not None:
            self._EnableErroredFrameSecondsSummaryEvent = EnableErroredFrameSecondsSummaryEvent
            properties['EnableErroredFrameSecondsSummaryEvent'] = EnableErroredFrameSecondsSummaryEvent
        if EfsseWindow is not None:
            self._EfsseWindow = EfsseWindow
            properties['EfsseWindow'] = EfsseWindow
        if EfsseThreshold is not None:
            self._EfsseThreshold = EfsseThreshold
            properties['EfsseThreshold'] = EfsseThreshold
        if EfsseCount is not None:
            self._EfsseCount = EfsseCount
            properties['EfsseCount'] = EfsseCount
        if EnableOrgSpecEvent is not None:
            self._EnableOrgSpecEvent = EnableOrgSpecEvent
            properties['EnableOrgSpecEvent'] = EnableOrgSpecEvent
        if OrgSpecEventOUI is not None:
            self._OrgSpecEventOUI = OrgSpecEventOUI
            properties['OrgSpecEventOUI'] = OrgSpecEventOUI
        if OrgSpecEventData is not None:
            self._OrgSpecEventData = OrgSpecEventData
            properties['OrgSpecEventData'] = OrgSpecEventData

        super(Dot3ahEventNotificationConfig, self).edit(**properties)

    @property
    def InitialTime(self):
        """
        get the value of property _InitialTime
        """
        if self.force_auto_sync:
            self.get('InitialTime')
        return self._InitialTime

    @property
    def EventRepeatPeriod(self):
        """
        get the value of property _EventRepeatPeriod
        """
        if self.force_auto_sync:
            self.get('EventRepeatPeriod')
        return self._EventRepeatPeriod

    @property
    def EnableErroredFrameEvent(self):
        """
        get the value of property _EnableErroredFrameEvent
        """
        if self.force_auto_sync:
            self.get('EnableErroredFrameEvent')
        return self._EnableErroredFrameEvent

    @property
    def EfeWindow(self):
        """
        get the value of property _EfeWindow
        """
        if self.force_auto_sync:
            self.get('EfeWindow')
        return self._EfeWindow

    @property
    def EfeThreshold(self):
        """
        get the value of property _EfeThreshold
        """
        if self.force_auto_sync:
            self.get('EfeThreshold')
        return self._EfeThreshold

    @property
    def EfeErrorCount(self):
        """
        get the value of property _EfeErrorCount
        """
        if self.force_auto_sync:
            self.get('EfeErrorCount')
        return self._EfeErrorCount

    @property
    def EnableErroredFramePeriodEvent(self):
        """
        get the value of property _EnableErroredFramePeriodEvent
        """
        if self.force_auto_sync:
            self.get('EnableErroredFramePeriodEvent')
        return self._EnableErroredFramePeriodEvent

    @property
    def EfpeWindow(self):
        """
        get the value of property _EfpeWindow
        """
        if self.force_auto_sync:
            self.get('EfpeWindow')
        return self._EfpeWindow

    @property
    def EfpeThreshold(self):
        """
        get the value of property _EfpeThreshold
        """
        if self.force_auto_sync:
            self.get('EfpeThreshold')
        return self._EfpeThreshold

    @property
    def EfpeErrorCount(self):
        """
        get the value of property _EfpeErrorCount
        """
        if self.force_auto_sync:
            self.get('EfpeErrorCount')
        return self._EfpeErrorCount

    @property
    def EnableErroredSymbolPeriodEvent(self):
        """
        get the value of property _EnableErroredSymbolPeriodEvent
        """
        if self.force_auto_sync:
            self.get('EnableErroredSymbolPeriodEvent')
        return self._EnableErroredSymbolPeriodEvent

    @property
    def EspeWindow(self):
        """
        get the value of property _EspeWindow
        """
        if self.force_auto_sync:
            self.get('EspeWindow')
        return self._EspeWindow

    @property
    def EspeThreshold(self):
        """
        get the value of property _EspeThreshold
        """
        if self.force_auto_sync:
            self.get('EspeThreshold')
        return self._EspeThreshold

    @property
    def EspeErrorCount(self):
        """
        get the value of property _EspeErrorCount
        """
        if self.force_auto_sync:
            self.get('EspeErrorCount')
        return self._EspeErrorCount

    @property
    def EnableErroredFrameSecondsSummaryEvent(self):
        """
        get the value of property _EnableErroredFrameSecondsSummaryEvent
        """
        if self.force_auto_sync:
            self.get('EnableErroredFrameSecondsSummaryEvent')
        return self._EnableErroredFrameSecondsSummaryEvent

    @property
    def EfsseWindow(self):
        """
        get the value of property _EfsseWindow
        """
        if self.force_auto_sync:
            self.get('EfsseWindow')
        return self._EfsseWindow

    @property
    def EfsseThreshold(self):
        """
        get the value of property _EfsseThreshold
        """
        if self.force_auto_sync:
            self.get('EfsseThreshold')
        return self._EfsseThreshold

    @property
    def EfsseCount(self):
        """
        get the value of property _EfsseCount
        """
        if self.force_auto_sync:
            self.get('EfsseCount')
        return self._EfsseCount

    @property
    def EnableOrgSpecEvent(self):
        """
        get the value of property _EnableOrgSpecEvent
        """
        if self.force_auto_sync:
            self.get('EnableOrgSpecEvent')
        return self._EnableOrgSpecEvent

    @property
    def OrgSpecEventOUI(self):
        """
        get the value of property _OrgSpecEventOUI
        """
        if self.force_auto_sync:
            self.get('OrgSpecEventOUI')
        return self._OrgSpecEventOUI

    @property
    def OrgSpecEventData(self):
        """
        get the value of property _OrgSpecEventData
        """
        if self.force_auto_sync:
            self.get('OrgSpecEventData')
        return self._OrgSpecEventData

    @InitialTime.setter
    def InitialTime(self, value):
        self._InitialTime = value
        self.edit(InitialTime=value)

    @EventRepeatPeriod.setter
    def EventRepeatPeriod(self, value):
        self._EventRepeatPeriod = value
        self.edit(EventRepeatPeriod=value)

    @EnableErroredFrameEvent.setter
    def EnableErroredFrameEvent(self, value):
        self._EnableErroredFrameEvent = value
        self.edit(EnableErroredFrameEvent=value)

    @EfeWindow.setter
    def EfeWindow(self, value):
        self._EfeWindow = value
        self.edit(EfeWindow=value)

    @EfeThreshold.setter
    def EfeThreshold(self, value):
        self._EfeThreshold = value
        self.edit(EfeThreshold=value)

    @EfeErrorCount.setter
    def EfeErrorCount(self, value):
        self._EfeErrorCount = value
        self.edit(EfeErrorCount=value)

    @EnableErroredFramePeriodEvent.setter
    def EnableErroredFramePeriodEvent(self, value):
        self._EnableErroredFramePeriodEvent = value
        self.edit(EnableErroredFramePeriodEvent=value)

    @EfpeWindow.setter
    def EfpeWindow(self, value):
        self._EfpeWindow = value
        self.edit(EfpeWindow=value)

    @EfpeThreshold.setter
    def EfpeThreshold(self, value):
        self._EfpeThreshold = value
        self.edit(EfpeThreshold=value)

    @EfpeErrorCount.setter
    def EfpeErrorCount(self, value):
        self._EfpeErrorCount = value
        self.edit(EfpeErrorCount=value)

    @EnableErroredSymbolPeriodEvent.setter
    def EnableErroredSymbolPeriodEvent(self, value):
        self._EnableErroredSymbolPeriodEvent = value
        self.edit(EnableErroredSymbolPeriodEvent=value)

    @EspeWindow.setter
    def EspeWindow(self, value):
        self._EspeWindow = value
        self.edit(EspeWindow=value)

    @EspeThreshold.setter
    def EspeThreshold(self, value):
        self._EspeThreshold = value
        self.edit(EspeThreshold=value)

    @EspeErrorCount.setter
    def EspeErrorCount(self, value):
        self._EspeErrorCount = value
        self.edit(EspeErrorCount=value)

    @EnableErroredFrameSecondsSummaryEvent.setter
    def EnableErroredFrameSecondsSummaryEvent(self, value):
        self._EnableErroredFrameSecondsSummaryEvent = value
        self.edit(EnableErroredFrameSecondsSummaryEvent=value)

    @EfsseWindow.setter
    def EfsseWindow(self, value):
        self._EfsseWindow = value
        self.edit(EfsseWindow=value)

    @EfsseThreshold.setter
    def EfsseThreshold(self, value):
        self._EfsseThreshold = value
        self.edit(EfsseThreshold=value)

    @EfsseCount.setter
    def EfsseCount(self, value):
        self._EfsseCount = value
        self.edit(EfsseCount=value)

    @EnableOrgSpecEvent.setter
    def EnableOrgSpecEvent(self, value):
        self._EnableOrgSpecEvent = value
        self.edit(EnableOrgSpecEvent=value)

    @OrgSpecEventOUI.setter
    def OrgSpecEventOUI(self, value):
        self._OrgSpecEventOUI = value
        self.edit(OrgSpecEventOUI=value)

    @OrgSpecEventData.setter
    def OrgSpecEventData(self, value):
        self._OrgSpecEventData = value
        self.edit(OrgSpecEventData=value)

    def _set_initialtime_with_str(self, value):
        try:
            self._InitialTime = int(value)
        except ValueError:
            self._InitialTime = hex(int(value, 16))

    def _set_eventrepeatperiod_with_str(self, value):
        try:
            self._EventRepeatPeriod = int(value)
        except ValueError:
            self._EventRepeatPeriod = hex(int(value, 16))

    def _set_enableerroredframeevent_with_str(self, value):
        self._EnableErroredFrameEvent = (value == 'True')

    def _set_efewindow_with_str(self, value):
        try:
            self._EfeWindow = int(value)
        except ValueError:
            self._EfeWindow = hex(int(value, 16))

    def _set_efethreshold_with_str(self, value):
        try:
            self._EfeThreshold = int(value)
        except ValueError:
            self._EfeThreshold = hex(int(value, 16))

    def _set_efeerrorcount_with_str(self, value):
        try:
            self._EfeErrorCount = int(value)
        except ValueError:
            self._EfeErrorCount = hex(int(value, 16))

    def _set_enableerroredframeperiodevent_with_str(self, value):
        self._EnableErroredFramePeriodEvent = (value == 'True')

    def _set_efpewindow_with_str(self, value):
        try:
            self._EfpeWindow = int(value)
        except ValueError:
            self._EfpeWindow = hex(int(value, 16))

    def _set_efpethreshold_with_str(self, value):
        try:
            self._EfpeThreshold = int(value)
        except ValueError:
            self._EfpeThreshold = hex(int(value, 16))

    def _set_efpeerrorcount_with_str(self, value):
        try:
            self._EfpeErrorCount = int(value)
        except ValueError:
            self._EfpeErrorCount = hex(int(value, 16))

    def _set_enableerroredsymbolperiodevent_with_str(self, value):
        self._EnableErroredSymbolPeriodEvent = (value == 'True')

    def _set_espewindow_with_str(self, value):
        try:
            self._EspeWindow = int(value)
        except ValueError:
            self._EspeWindow = hex(int(value, 16))

    def _set_espethreshold_with_str(self, value):
        try:
            self._EspeThreshold = int(value)
        except ValueError:
            self._EspeThreshold = hex(int(value, 16))

    def _set_espeerrorcount_with_str(self, value):
        try:
            self._EspeErrorCount = int(value)
        except ValueError:
            self._EspeErrorCount = hex(int(value, 16))

    def _set_enableerroredframesecondssummaryevent_with_str(self, value):
        self._EnableErroredFrameSecondsSummaryEvent = (value == 'True')

    def _set_efssewindow_with_str(self, value):
        try:
            self._EfsseWindow = int(value)
        except ValueError:
            self._EfsseWindow = hex(int(value, 16))

    def _set_efssethreshold_with_str(self, value):
        try:
            self._EfsseThreshold = int(value)
        except ValueError:
            self._EfsseThreshold = hex(int(value, 16))

    def _set_efssecount_with_str(self, value):
        try:
            self._EfsseCount = int(value)
        except ValueError:
            self._EfsseCount = hex(int(value, 16))

    def _set_enableorgspecevent_with_str(self, value):
        self._EnableOrgSpecEvent = (value == 'True')

    def _set_orgspeceventoui_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OrgSpecEventOUI = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OrgSpecEventOUI.append(int(str_value))
            except ValueError:
                self._OrgSpecEventOUI.append(hex(int(str_value, 16)))

    def _set_orgspeceventdata_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OrgSpecEventData = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OrgSpecEventData.append(int(str_value))
            except ValueError:
                self._OrgSpecEventData.append(hex(int(str_value, 16)))

