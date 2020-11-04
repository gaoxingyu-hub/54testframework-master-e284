"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889Config_Autogen import Rfc2889Config


@rom_manager.rom
class AddressLearningRateConfig(Rfc2889Config):
    def __init__(self, AgingTime=None, NumberOfAddresses=None, MonitorPortHandles=None, RateMaxValue=None, RateMinValue=None, RateInitValue=None, RateResolution=None, DiagramMode=None, **kwargs):
        self._AgingTime = AgingTime  # Aging Time (sec)
        self._NumberOfAddresses = NumberOfAddresses  # Number Of Addresses
        self._MonitorPortHandles = MonitorPortHandles  # Monitor Port
        self._RateMaxValue = RateMaxValue  # Maximum
        self._RateMinValue = RateMinValue  # Minimum
        self._RateInitValue = RateInitValue  # Initial
        self._RateResolution = RateResolution  # Resolution
        self._DiagramMode = DiagramMode  # Diagram Mode

        properties = kwargs.copy()
        if AgingTime is not None:
            properties['AgingTime'] = AgingTime
        if NumberOfAddresses is not None:
            properties['NumberOfAddresses'] = NumberOfAddresses
        if MonitorPortHandles is not None:
            properties['MonitorPortHandles'] = MonitorPortHandles
        if RateMaxValue is not None:
            properties['RateMaxValue'] = RateMaxValue
        if RateMinValue is not None:
            properties['RateMinValue'] = RateMinValue
        if RateInitValue is not None:
            properties['RateInitValue'] = RateInitValue
        if RateResolution is not None:
            properties['RateResolution'] = RateResolution
        if DiagramMode is not None:
            properties['DiagramMode'] = DiagramMode

        # call base class function, and it will send message to renix server to create a class.
        super(AddressLearningRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AgingTime=None, NumberOfAddresses=None, MonitorPortHandles=None, RateMaxValue=None, RateMinValue=None, RateInitValue=None, RateResolution=None, DiagramMode=None, **kwargs):
        properties = kwargs.copy()
        if AgingTime is not None:
            self._AgingTime = AgingTime
            properties['AgingTime'] = AgingTime
        if NumberOfAddresses is not None:
            self._NumberOfAddresses = NumberOfAddresses
            properties['NumberOfAddresses'] = NumberOfAddresses
        if MonitorPortHandles is not None:
            self._MonitorPortHandles = MonitorPortHandles
            properties['MonitorPortHandles'] = MonitorPortHandles
        if RateMaxValue is not None:
            self._RateMaxValue = RateMaxValue
            properties['RateMaxValue'] = RateMaxValue
        if RateMinValue is not None:
            self._RateMinValue = RateMinValue
            properties['RateMinValue'] = RateMinValue
        if RateInitValue is not None:
            self._RateInitValue = RateInitValue
            properties['RateInitValue'] = RateInitValue
        if RateResolution is not None:
            self._RateResolution = RateResolution
            properties['RateResolution'] = RateResolution
        if DiagramMode is not None:
            self._DiagramMode = DiagramMode
            properties['DiagramMode'] = DiagramMode

        super(AddressLearningRateConfig, self).edit(**properties)

    @property
    def AgingTime(self):
        """
        get the value of property _AgingTime
        """
        if self.force_auto_sync:
            self.get('AgingTime')
        return self._AgingTime

    @property
    def NumberOfAddresses(self):
        """
        get the value of property _NumberOfAddresses
        """
        if self.force_auto_sync:
            self.get('NumberOfAddresses')
        return self._NumberOfAddresses

    @property
    def MonitorPortHandles(self):
        """
        get the value of property _MonitorPortHandles
        """
        if self.force_auto_sync:
            self.get('MonitorPortHandles')
        return self._MonitorPortHandles

    @property
    def RateMaxValue(self):
        """
        get the value of property _RateMaxValue
        """
        if self.force_auto_sync:
            self.get('RateMaxValue')
        return self._RateMaxValue

    @property
    def RateMinValue(self):
        """
        get the value of property _RateMinValue
        """
        if self.force_auto_sync:
            self.get('RateMinValue')
        return self._RateMinValue

    @property
    def RateInitValue(self):
        """
        get the value of property _RateInitValue
        """
        if self.force_auto_sync:
            self.get('RateInitValue')
        return self._RateInitValue

    @property
    def RateResolution(self):
        """
        get the value of property _RateResolution
        """
        if self.force_auto_sync:
            self.get('RateResolution')
        return self._RateResolution

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

    @NumberOfAddresses.setter
    def NumberOfAddresses(self, value):
        self._NumberOfAddresses = value
        self.edit(NumberOfAddresses=value)

    @MonitorPortHandles.setter
    def MonitorPortHandles(self, value):
        self._MonitorPortHandles = value
        self.edit(MonitorPortHandles=value)

    @RateMaxValue.setter
    def RateMaxValue(self, value):
        self._RateMaxValue = value
        self.edit(RateMaxValue=value)

    @RateMinValue.setter
    def RateMinValue(self, value):
        self._RateMinValue = value
        self.edit(RateMinValue=value)

    @RateInitValue.setter
    def RateInitValue(self, value):
        self._RateInitValue = value
        self.edit(RateInitValue=value)

    @RateResolution.setter
    def RateResolution(self, value):
        self._RateResolution = value
        self.edit(RateResolution=value)

    @DiagramMode.setter
    def DiagramMode(self, value):
        self._DiagramMode = value
        self.edit(DiagramMode=value)

    def _set_agingtime_with_str(self, value):
        try:
            self._AgingTime = int(value)
        except ValueError:
            self._AgingTime = hex(int(value, 16))

    def _set_numberofaddresses_with_str(self, value):
        try:
            self._NumberOfAddresses = int(value)
        except ValueError:
            self._NumberOfAddresses = hex(int(value, 16))

    def _set_monitorporthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MonitorPortHandles = tmp_value.split()

    def _set_ratemaxvalue_with_str(self, value):
        try:
            self._RateMaxValue = int(value)
        except ValueError:
            self._RateMaxValue = hex(int(value, 16))

    def _set_rateminvalue_with_str(self, value):
        try:
            self._RateMinValue = int(value)
        except ValueError:
            self._RateMinValue = hex(int(value, 16))

    def _set_rateinitvalue_with_str(self, value):
        try:
            self._RateInitValue = int(value)
        except ValueError:
            self._RateInitValue = hex(int(value, 16))

    def _set_rateresolution_with_str(self, value):
        try:
            self._RateResolution = int(value)
        except ValueError:
            self._RateResolution = hex(int(value, 16))

    def _set_diagrammode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DiagramMode = EnumDiagramMode.%s' % value[:seperate])

