"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class AddressCachingCapacityConfig(Rfc2889Config):
    def __init__(self, AgingTime=None, LearnRate=None, MonitorPortHandles=None, AddrMaxValue=None, AddrMinValue=None, AddrInitValue=None, AddrResolution=None, DiagramMode=None, **kwargs):
        self._AgingTime = AgingTime  # Aging Time (sec)
        self._LearnRate = LearnRate  # Learning Rate (frames/sec)
        self._MonitorPortHandles = MonitorPortHandles  # Monitor Port
        self._AddrMaxValue = AddrMaxValue  # Maximum
        self._AddrMinValue = AddrMinValue  # Minimum
        self._AddrInitValue = AddrInitValue  # Initial
        self._AddrResolution = AddrResolution  # Resolution
        self._DiagramMode = DiagramMode  # Diagram Mode

        properties = kwargs.copy()
        if AgingTime is not None:
            properties['AgingTime'] = AgingTime
        if LearnRate is not None:
            properties['LearnRate'] = LearnRate
        if MonitorPortHandles is not None:
            properties['MonitorPortHandles'] = MonitorPortHandles
        if AddrMaxValue is not None:
            properties['AddrMaxValue'] = AddrMaxValue
        if AddrMinValue is not None:
            properties['AddrMinValue'] = AddrMinValue
        if AddrInitValue is not None:
            properties['AddrInitValue'] = AddrInitValue
        if AddrResolution is not None:
            properties['AddrResolution'] = AddrResolution
        if DiagramMode is not None:
            properties['DiagramMode'] = DiagramMode

        # call base class function, and it will send message to renix server to create a class.
        super(AddressCachingCapacityConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AgingTime=None, LearnRate=None, MonitorPortHandles=None, AddrMaxValue=None, AddrMinValue=None, AddrInitValue=None, AddrResolution=None, DiagramMode=None, **kwargs):
        properties = kwargs.copy()
        if AgingTime is not None:
            self._AgingTime = AgingTime
            properties['AgingTime'] = AgingTime
        if LearnRate is not None:
            self._LearnRate = LearnRate
            properties['LearnRate'] = LearnRate
        if MonitorPortHandles is not None:
            self._MonitorPortHandles = MonitorPortHandles
            properties['MonitorPortHandles'] = MonitorPortHandles
        if AddrMaxValue is not None:
            self._AddrMaxValue = AddrMaxValue
            properties['AddrMaxValue'] = AddrMaxValue
        if AddrMinValue is not None:
            self._AddrMinValue = AddrMinValue
            properties['AddrMinValue'] = AddrMinValue
        if AddrInitValue is not None:
            self._AddrInitValue = AddrInitValue
            properties['AddrInitValue'] = AddrInitValue
        if AddrResolution is not None:
            self._AddrResolution = AddrResolution
            properties['AddrResolution'] = AddrResolution
        if DiagramMode is not None:
            self._DiagramMode = DiagramMode
            properties['DiagramMode'] = DiagramMode

        super(AddressCachingCapacityConfig, self).edit(**properties)

    @property
    def AgingTime(self):
        """
        get the value of property _AgingTime
        """
        if self.force_auto_sync:
            self.get('AgingTime')
        return self._AgingTime

    @property
    def LearnRate(self):
        """
        get the value of property _LearnRate
        """
        if self.force_auto_sync:
            self.get('LearnRate')
        return self._LearnRate

    @property
    def MonitorPortHandles(self):
        """
        get the value of property _MonitorPortHandles
        """
        if self.force_auto_sync:
            self.get('MonitorPortHandles')
        return self._MonitorPortHandles

    @property
    def AddrMaxValue(self):
        """
        get the value of property _AddrMaxValue
        """
        if self.force_auto_sync:
            self.get('AddrMaxValue')
        return self._AddrMaxValue

    @property
    def AddrMinValue(self):
        """
        get the value of property _AddrMinValue
        """
        if self.force_auto_sync:
            self.get('AddrMinValue')
        return self._AddrMinValue

    @property
    def AddrInitValue(self):
        """
        get the value of property _AddrInitValue
        """
        if self.force_auto_sync:
            self.get('AddrInitValue')
        return self._AddrInitValue

    @property
    def AddrResolution(self):
        """
        get the value of property _AddrResolution
        """
        if self.force_auto_sync:
            self.get('AddrResolution')
        return self._AddrResolution

    @property
    def DiagramMode(self):
        """
        get the value of property _DiagramMode
        """
        if self.force_auto_sync:
            self.get('DiagramMode')
        return self._DiagramMode

    @AgingTime.setter
    def AgingTime(self, value):
        self._AgingTime = value
        self.edit(AgingTime=value)

    @LearnRate.setter
    def LearnRate(self, value):
        self._LearnRate = value
        self.edit(LearnRate=value)

    @MonitorPortHandles.setter
    def MonitorPortHandles(self, value):
        self._MonitorPortHandles = value
        self.edit(MonitorPortHandles=value)

    @AddrMaxValue.setter
    def AddrMaxValue(self, value):
        self._AddrMaxValue = value
        self.edit(AddrMaxValue=value)

    @AddrMinValue.setter
    def AddrMinValue(self, value):
        self._AddrMinValue = value
        self.edit(AddrMinValue=value)

    @AddrInitValue.setter
    def AddrInitValue(self, value):
        self._AddrInitValue = value
        self.edit(AddrInitValue=value)

    @AddrResolution.setter
    def AddrResolution(self, value):
        self._AddrResolution = value
        self.edit(AddrResolution=value)

    @DiagramMode.setter
    def DiagramMode(self, value):
        self._DiagramMode = value
        self.edit(DiagramMode=value)

    def _set_agingtime_with_str(self, value):
        try:
            self._AgingTime = int(value)
        except ValueError:
            self._AgingTime = hex(int(value, 16))

    def _set_learnrate_with_str(self, value):
        try:
            self._LearnRate = int(value)
        except ValueError:
            self._LearnRate = hex(int(value, 16))

    def _set_monitorporthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MonitorPortHandles = tmp_value.split()

    def _set_addrmaxvalue_with_str(self, value):
        try:
            self._AddrMaxValue = int(value)
        except ValueError:
            self._AddrMaxValue = hex(int(value, 16))

    def _set_addrminvalue_with_str(self, value):
        try:
            self._AddrMinValue = int(value)
        except ValueError:
            self._AddrMinValue = hex(int(value, 16))

    def _set_addrinitvalue_with_str(self, value):
        try:
            self._AddrInitValue = int(value)
        except ValueError:
            self._AddrInitValue = hex(int(value, 16))

    def _set_addrresolution_with_str(self, value):
        try:
            self._AddrResolution = int(value)
        except ValueError:
            self._AddrResolution = hex(int(value, 16))

    def _set_diagrammode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DiagramMode = EnumDiagramMode.%s' % value[:seperate])

