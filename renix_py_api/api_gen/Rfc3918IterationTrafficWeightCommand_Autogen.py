"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Rfc3918IterationTrafficWeightCommand(TrafficTestCommand):
    def __init__(self, McTrafficPercentageMode=None, McTrafficPercentage=None, RandomMinMcTrafficPercentage=None, RandomMaxMcTrafficPercentage=None, McTrafficPercentageStart=None, McTrafficPercentageStep=None, McTrafficPercentageEnd=None, McTrafficPercentageCustom=None, **kwargs):
        self._McTrafficPercentageMode = McTrafficPercentageMode  # Multicast Traffic Percentage Mode
        self._McTrafficPercentage = McTrafficPercentage  # End
        self._RandomMinMcTrafficPercentage = RandomMinMcTrafficPercentage  # Min
        self._RandomMaxMcTrafficPercentage = RandomMaxMcTrafficPercentage  # Max
        self._McTrafficPercentageStart = McTrafficPercentageStart  # Start
        self._McTrafficPercentageStep = McTrafficPercentageStep  # Step
        self._McTrafficPercentageEnd = McTrafficPercentageEnd  # End
        self._McTrafficPercentageCustom = McTrafficPercentageCustom  # Custom

        properties = kwargs.copy()
        if McTrafficPercentageMode is not None:
            properties['McTrafficPercentageMode'] = McTrafficPercentageMode
        if McTrafficPercentage is not None:
            properties['McTrafficPercentage'] = McTrafficPercentage
        if RandomMinMcTrafficPercentage is not None:
            properties['RandomMinMcTrafficPercentage'] = RandomMinMcTrafficPercentage
        if RandomMaxMcTrafficPercentage is not None:
            properties['RandomMaxMcTrafficPercentage'] = RandomMaxMcTrafficPercentage
        if McTrafficPercentageStart is not None:
            properties['McTrafficPercentageStart'] = McTrafficPercentageStart
        if McTrafficPercentageStep is not None:
            properties['McTrafficPercentageStep'] = McTrafficPercentageStep
        if McTrafficPercentageEnd is not None:
            properties['McTrafficPercentageEnd'] = McTrafficPercentageEnd
        if McTrafficPercentageCustom is not None:
            properties['McTrafficPercentageCustom'] = McTrafficPercentageCustom

        # call base class function, and it will send message to renix server to create a class.
        super(Rfc3918IterationTrafficWeightCommand, self).__init__(**properties)

    @property
    def McTrafficPercentageMode(self):
        """
        get the value of property _McTrafficPercentageMode
        """
        return self._McTrafficPercentageMode

    @property
    def McTrafficPercentage(self):
        """
        get the value of property _McTrafficPercentage
        """
        return self._McTrafficPercentage

    @property
    def RandomMinMcTrafficPercentage(self):
        """
        get the value of property _RandomMinMcTrafficPercentage
        """
        return self._RandomMinMcTrafficPercentage

    @property
    def RandomMaxMcTrafficPercentage(self):
        """
        get the value of property _RandomMaxMcTrafficPercentage
        """
        return self._RandomMaxMcTrafficPercentage

    @property
    def McTrafficPercentageStart(self):
        """
        get the value of property _McTrafficPercentageStart
        """
        return self._McTrafficPercentageStart

    @property
    def McTrafficPercentageStep(self):
        """
        get the value of property _McTrafficPercentageStep
        """
        return self._McTrafficPercentageStep

    @property
    def McTrafficPercentageEnd(self):
        """
        get the value of property _McTrafficPercentageEnd
        """
        return self._McTrafficPercentageEnd

    @property
    def McTrafficPercentageCustom(self):
        """
        get the value of property _McTrafficPercentageCustom
        """
        return self._McTrafficPercentageCustom

    @McTrafficPercentageMode.setter
    def McTrafficPercentageMode(self, value):
        self._McTrafficPercentageMode = value

    @McTrafficPercentage.setter
    def McTrafficPercentage(self, value):
        self._McTrafficPercentage = value

    @RandomMinMcTrafficPercentage.setter
    def RandomMinMcTrafficPercentage(self, value):
        self._RandomMinMcTrafficPercentage = value

    @RandomMaxMcTrafficPercentage.setter
    def RandomMaxMcTrafficPercentage(self, value):
        self._RandomMaxMcTrafficPercentage = value

    @McTrafficPercentageStart.setter
    def McTrafficPercentageStart(self, value):
        self._McTrafficPercentageStart = value

    @McTrafficPercentageStep.setter
    def McTrafficPercentageStep(self, value):
        self._McTrafficPercentageStep = value

    @McTrafficPercentageEnd.setter
    def McTrafficPercentageEnd(self, value):
        self._McTrafficPercentageEnd = value

    @McTrafficPercentageCustom.setter
    def McTrafficPercentageCustom(self, value):
        self._McTrafficPercentageCustom = value

    def _set_mctrafficpercentagemode_with_str(self, value):
        seperate = value.find(':')
        exec('self._McTrafficPercentageMode = EnumMulticastPercentageMode.%s' % value[:seperate])

    def _set_mctrafficpercentage_with_str(self, value):
        self._McTrafficPercentage = float(value)

    def _set_randomminmctrafficpercentage_with_str(self, value):
        self._RandomMinMcTrafficPercentage = float(value)

    def _set_randommaxmctrafficpercentage_with_str(self, value):
        self._RandomMaxMcTrafficPercentage = float(value)

    def _set_mctrafficpercentagestart_with_str(self, value):
        self._McTrafficPercentageStart = float(value)

    def _set_mctrafficpercentagestep_with_str(self, value):
        self._McTrafficPercentageStep = float(value)

    def _set_mctrafficpercentageend_with_str(self, value):
        self._McTrafficPercentageEnd = float(value)

    def _set_mctrafficpercentagecustom_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._McTrafficPercentageCustom = []
        values = tmp_value.split()
        for str_value in values:
            self._McTrafficPercentageCustom.append(float(str_value))

