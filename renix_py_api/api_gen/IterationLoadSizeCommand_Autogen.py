"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationStreamTemplateCommand_Autogen import IterationStreamTemplateCommand


@rom_manager.rom
class IterationLoadSizeCommand(IterationStreamTemplateCommand):
    def __init__(self, LoadMode=None, LoadUnit=None, FixedLoad=None, LoadStart=None, LoadStep=None, LoadEnd=None, RandomMinLoad=None, RandomMaxLoad=None, CustomLoadList=None, AdjustStreamTemplateLoadMode=None, **kwargs):
        self._LoadMode = LoadMode  # Load Type
        self._LoadUnit = LoadUnit  # %
        self._FixedLoad = FixedLoad  # Fixed Load
        self._LoadStart = LoadStart  # Load Start
        self._LoadStep = LoadStep  # Load Step
        self._LoadEnd = LoadEnd  # Load End
        self._RandomMinLoad = RandomMinLoad  # Min
        self._RandomMaxLoad = RandomMaxLoad  # Max
        self._CustomLoadList = CustomLoadList  # Custom Load List
        self._AdjustStreamTemplateLoadMode = AdjustStreamTemplateLoadMode  # Load Type

        properties = kwargs.copy()
        if LoadMode is not None:
            properties['LoadMode'] = LoadMode
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit
        if FixedLoad is not None:
            properties['FixedLoad'] = FixedLoad
        if LoadStart is not None:
            properties['LoadStart'] = LoadStart
        if LoadStep is not None:
            properties['LoadStep'] = LoadStep
        if LoadEnd is not None:
            properties['LoadEnd'] = LoadEnd
        if RandomMinLoad is not None:
            properties['RandomMinLoad'] = RandomMinLoad
        if RandomMaxLoad is not None:
            properties['RandomMaxLoad'] = RandomMaxLoad
        if CustomLoadList is not None:
            properties['CustomLoadList'] = CustomLoadList
        if AdjustStreamTemplateLoadMode is not None:
            properties['AdjustStreamTemplateLoadMode'] = AdjustStreamTemplateLoadMode

        # call base class function, and it will send message to renix server to create a class.
        super(IterationLoadSizeCommand, self).__init__(**properties)

    @property
    def LoadMode(self):
        """
        get the value of property _LoadMode
        """
        return self._LoadMode

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        return self._LoadUnit

    @property
    def FixedLoad(self):
        """
        get the value of property _FixedLoad
        """
        return self._FixedLoad

    @property
    def LoadStart(self):
        """
        get the value of property _LoadStart
        """
        return self._LoadStart

    @property
    def LoadStep(self):
        """
        get the value of property _LoadStep
        """
        return self._LoadStep

    @property
    def LoadEnd(self):
        """
        get the value of property _LoadEnd
        """
        return self._LoadEnd

    @property
    def RandomMinLoad(self):
        """
        get the value of property _RandomMinLoad
        """
        return self._RandomMinLoad

    @property
    def RandomMaxLoad(self):
        """
        get the value of property _RandomMaxLoad
        """
        return self._RandomMaxLoad

    @property
    def CustomLoadList(self):
        """
        get the value of property _CustomLoadList
        """
        return self._CustomLoadList

    @property
    def AdjustStreamTemplateLoadMode(self):
        """
        get the value of property _AdjustStreamTemplateLoadMode
        """
        return self._AdjustStreamTemplateLoadMode

    @LoadMode.setter
    def LoadMode(self, value):
        self._LoadMode = value

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value

    @FixedLoad.setter
    def FixedLoad(self, value):
        self._FixedLoad = value

    @LoadStart.setter
    def LoadStart(self, value):
        self._LoadStart = value

    @LoadStep.setter
    def LoadStep(self, value):
        self._LoadStep = value

    @LoadEnd.setter
    def LoadEnd(self, value):
        self._LoadEnd = value

    @RandomMinLoad.setter
    def RandomMinLoad(self, value):
        self._RandomMinLoad = value

    @RandomMaxLoad.setter
    def RandomMaxLoad(self, value):
        self._RandomMaxLoad = value

    @CustomLoadList.setter
    def CustomLoadList(self, value):
        self._CustomLoadList = value

    @AdjustStreamTemplateLoadMode.setter
    def AdjustStreamTemplateLoadMode(self, value):
        self._AdjustStreamTemplateLoadMode = value

    def _set_loadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadMode = EnumLoadMode.%s' % value[:seperate])

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

    def _set_fixedload_with_str(self, value):
        self._FixedLoad = float(value)

    def _set_loadstart_with_str(self, value):
        self._LoadStart = float(value)

    def _set_loadstep_with_str(self, value):
        self._LoadStep = float(value)

    def _set_loadend_with_str(self, value):
        self._LoadEnd = float(value)

    def _set_randomminload_with_str(self, value):
        self._RandomMinLoad = float(value)

    def _set_randommaxload_with_str(self, value):
        self._RandomMaxLoad = float(value)

    def _set_customloadlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CustomLoadList = []
        values = tmp_value.split()
        for str_value in values:
            self._CustomLoadList.append(float(str_value))

    def _set_adjuststreamtemplateloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AdjustStreamTemplateLoadMode = EnumAdjustStreamTemplateLoad.%s' % value[:seperate])

