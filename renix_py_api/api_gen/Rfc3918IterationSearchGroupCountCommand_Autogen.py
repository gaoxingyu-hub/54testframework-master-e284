"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Rfc3918IterationSearchGroupCountCommand(TrafficTestCommand):
    def __init__(self, SearchMode=None, MinMcGroupCount=None, MaxMcGroupCount=None, InitMcGroupCount=None, McGroupCountStep=None, McGroupCountResolution=None, McGroupCountBackoff=None, **kwargs):
        self._SearchMode = SearchMode  # Multicast Group Count Search Mode
        self._MinMcGroupCount = MinMcGroupCount  # Minimum Multicast Group Count
        self._MaxMcGroupCount = MaxMcGroupCount  # Maximum Multicast Group Count
        self._InitMcGroupCount = InitMcGroupCount  # Initial Multicast Group Count
        self._McGroupCountStep = McGroupCountStep  # Multicast Group Count Step
        self._McGroupCountResolution = McGroupCountResolution  # Multicast Group Count Resolution
        self._McGroupCountBackoff = McGroupCountBackoff  # BackOff

        properties = kwargs.copy()
        if SearchMode is not None:
            properties['SearchMode'] = SearchMode
        if MinMcGroupCount is not None:
            properties['MinMcGroupCount'] = MinMcGroupCount
        if MaxMcGroupCount is not None:
            properties['MaxMcGroupCount'] = MaxMcGroupCount
        if InitMcGroupCount is not None:
            properties['InitMcGroupCount'] = InitMcGroupCount
        if McGroupCountStep is not None:
            properties['McGroupCountStep'] = McGroupCountStep
        if McGroupCountResolution is not None:
            properties['McGroupCountResolution'] = McGroupCountResolution
        if McGroupCountBackoff is not None:
            properties['McGroupCountBackoff'] = McGroupCountBackoff

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc3918IterationSearchGroupCountCommand, self).__init__(**properties)

    @property
    def SearchMode(self):
        """
        get the value of property _SearchMode
        """
        return self._SearchMode

    @property
    def MinMcGroupCount(self):
        """
        get the value of property _MinMcGroupCount
        """
        return self._MinMcGroupCount

    @property
    def MaxMcGroupCount(self):
        """
        get the value of property _MaxMcGroupCount
        """
        return self._MaxMcGroupCount

    @property
    def InitMcGroupCount(self):
        """
        get the value of property _InitMcGroupCount
        """
        return self._InitMcGroupCount

    @property
    def McGroupCountStep(self):
        """
        get the value of property _McGroupCountStep
        """
        return self._McGroupCountStep

    @property
    def McGroupCountResolution(self):
        """
        get the value of property _McGroupCountResolution
        """
        return self._McGroupCountResolution

    @property
    def McGroupCountBackoff(self):
        """
        get the value of property _McGroupCountBackoff
        """
        return self._McGroupCountBackoff

    @SearchMode.setter
    def SearchMode(self, value):
        self._SearchMode = value

    @MinMcGroupCount.setter
    def MinMcGroupCount(self, value):
        self._MinMcGroupCount = value

    @MaxMcGroupCount.setter
    def MaxMcGroupCount(self, value):
        self._MaxMcGroupCount = value

    @InitMcGroupCount.setter
    def InitMcGroupCount(self, value):
        self._InitMcGroupCount = value

    @McGroupCountStep.setter
    def McGroupCountStep(self, value):
        self._McGroupCountStep = value

    @McGroupCountResolution.setter
    def McGroupCountResolution(self, value):
        self._McGroupCountResolution = value

    @McGroupCountBackoff.setter
    def McGroupCountBackoff(self, value):
        self._McGroupCountBackoff = value

    def _set_searchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_minmcgroupcount_with_str(self, value):
        try:
            self._MinMcGroupCount = int(value)
        except ValueError:
            self._MinMcGroupCount = hex(int(value, 16))

    def _set_maxmcgroupcount_with_str(self, value):
        try:
            self._MaxMcGroupCount = int(value)
        except ValueError:
            self._MaxMcGroupCount = hex(int(value, 16))

    def _set_initmcgroupcount_with_str(self, value):
        try:
            self._InitMcGroupCount = int(value)
        except ValueError:
            self._InitMcGroupCount = hex(int(value, 16))

    def _set_mcgroupcountstep_with_str(self, value):
        try:
            self._McGroupCountStep = int(value)
        except ValueError:
            self._McGroupCountStep = hex(int(value, 16))

    def _set_mcgroupcountresolution_with_str(self, value):
        self._McGroupCountResolution = float(value)

    def _set_mcgroupcountbackoff_with_str(self, value):
        self._McGroupCountBackoff = float(value)

