"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Rfc3918IterationGroupCountCommand(TrafficTestCommand):
    def __init__(self, McGroupCountMode=None, McGroupCount=None, RandomMinMcGroupCount=None, RandomMaxMcGroupCount=None, McGroupCountStart=None, McGroupCountStep=None, McGroupCountEnd=None, McGroupCountCustom=None, **kwargs):
        self._McGroupCountMode = McGroupCountMode  # Multicast Group Mode
        self._McGroupCount = McGroupCount  # Multicast Group Count
        self._RandomMinMcGroupCount = RandomMinMcGroupCount  # Min
        self._RandomMaxMcGroupCount = RandomMaxMcGroupCount  # Max
        self._McGroupCountStart = McGroupCountStart  # Start
        self._McGroupCountStep = McGroupCountStep  # Step
        self._McGroupCountEnd = McGroupCountEnd  # End
        self._McGroupCountCustom = McGroupCountCustom  # Custom

        properties = kwargs.copy()
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
        super(Rfc3918IterationGroupCountCommand, self).__init__(**properties)

    @property
    def McGroupCountMode(self):
        """
        get the value of property _McGroupCountMode
        """
        return self._McGroupCountMode

    @property
    def McGroupCount(self):
        """
        get the value of property _McGroupCount
        """
        return self._McGroupCount

    @property
    def RandomMinMcGroupCount(self):
        """
        get the value of property _RandomMinMcGroupCount
        """
        return self._RandomMinMcGroupCount

    @property
    def RandomMaxMcGroupCount(self):
        """
        get the value of property _RandomMaxMcGroupCount
        """
        return self._RandomMaxMcGroupCount

    @property
    def McGroupCountStart(self):
        """
        get the value of property _McGroupCountStart
        """
        return self._McGroupCountStart

    @property
    def McGroupCountStep(self):
        """
        get the value of property _McGroupCountStep
        """
        return self._McGroupCountStep

    @property
    def McGroupCountEnd(self):
        """
        get the value of property _McGroupCountEnd
        """
        return self._McGroupCountEnd

    @property
    def McGroupCountCustom(self):
        """
        get the value of property _McGroupCountCustom
        """
        return self._McGroupCountCustom

    @McGroupCountMode.setter
    def McGroupCountMode(self, value):
        self._McGroupCountMode = value

    @McGroupCount.setter
    def McGroupCount(self, value):
        self._McGroupCount = value

    @RandomMinMcGroupCount.setter
    def RandomMinMcGroupCount(self, value):
        self._RandomMinMcGroupCount = value

    @RandomMaxMcGroupCount.setter
    def RandomMaxMcGroupCount(self, value):
        self._RandomMaxMcGroupCount = value

    @McGroupCountStart.setter
    def McGroupCountStart(self, value):
        self._McGroupCountStart = value

    @McGroupCountStep.setter
    def McGroupCountStep(self, value):
        self._McGroupCountStep = value

    @McGroupCountEnd.setter
    def McGroupCountEnd(self, value):
        self._McGroupCountEnd = value

    @McGroupCountCustom.setter
    def McGroupCountCustom(self, value):
        self._McGroupCountCustom = value

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

