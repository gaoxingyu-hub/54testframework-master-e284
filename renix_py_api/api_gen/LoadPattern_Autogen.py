"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LoadPattern(ROMObject):
    def __init__(self, LoadValue=None, RampTime=None, SteadyTime=None, **kwargs):
        self._LoadValue = LoadValue  # Load Value
        self._RampTime = RampTime  # Ramp Time
        self._SteadyTime = SteadyTime  # Steady Time

        properties = kwargs.copy()
        if LoadValue is not None:
            properties['LoadValue'] = LoadValue
        if RampTime is not None:
            properties['RampTime'] = RampTime
        if SteadyTime is not None:
            properties['SteadyTime'] = SteadyTime

        # call base class function, and it will send message to renix server to create a class.
        super(LoadPattern, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LoadValue=None, RampTime=None, SteadyTime=None, **kwargs):
        properties = kwargs.copy()
        if LoadValue is not None:
            self._LoadValue = LoadValue
            properties['LoadValue'] = LoadValue
        if RampTime is not None:
            self._RampTime = RampTime
            properties['RampTime'] = RampTime
        if SteadyTime is not None:
            self._SteadyTime = SteadyTime
            properties['SteadyTime'] = SteadyTime

        super(LoadPattern, self).edit(**properties)

    @property
    def LoadValue(self):
        """
        get the value of property _LoadValue
        """
        if self.force_auto_sync:
            self.get('LoadValue')
        return self._LoadValue

    @property
    def RampTime(self):
        """
        get the value of property _RampTime
        """
        if self.force_auto_sync:
            self.get('RampTime')
        return self._RampTime

    @property
    def SteadyTime(self):
        """
        get the value of property _SteadyTime
        """
        if self.force_auto_sync:
            self.get('SteadyTime')
        return self._SteadyTime

    @LoadValue.setter
    def LoadValue(self, value):
        self._LoadValue = value
        self.edit(LoadValue=value)

    @RampTime.setter
    def RampTime(self, value):
        self._RampTime = value
        self.edit(RampTime=value)

    @SteadyTime.setter
    def SteadyTime(self, value):
        self._SteadyTime = value
        self.edit(SteadyTime=value)

    def _set_loadvalue_with_str(self, value):
        try:
            self._LoadValue = int(value)
        except ValueError:
            self._LoadValue = hex(int(value, 16))

    def _set_ramptime_with_str(self, value):
        try:
            self._RampTime = int(value)
        except ValueError:
            self._RampTime = hex(int(value, 16))

    def _set_steadytime_with_str(self, value):
        try:
            self._SteadyTime = int(value)
        except ValueError:
            self._SteadyTime = hex(int(value, 16))

