"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Y1564SmartScripterCommand_Autogen import Y1564SmartScripterCommand


@rom_manager.rom
class Y1564LoadSizeCommand(Y1564SmartScripterCommand):
    def __init__(self, LoadUnit=None, FixedLoad=None, AdjustStreamTemplateLoadMode=None, **kwargs):
        self._LoadUnit = LoadUnit  # Load Unit
        self._FixedLoad = FixedLoad  # Fixed Load
        self._AdjustStreamTemplateLoadMode = AdjustStreamTemplateLoadMode  # Load Type

        properties = kwargs.copy()
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit
        if FixedLoad is not None:
            properties['FixedLoad'] = FixedLoad
        if AdjustStreamTemplateLoadMode is not None:
            properties['AdjustStreamTemplateLoadMode'] = AdjustStreamTemplateLoadMode

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564LoadSizeCommand, self).__init__(**properties)

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
    def AdjustStreamTemplateLoadMode(self):
        """
        get the value of property _AdjustStreamTemplateLoadMode
        """
        return self._AdjustStreamTemplateLoadMode

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value

    @FixedLoad.setter
    def FixedLoad(self, value):
        self._FixedLoad = value

    @AdjustStreamTemplateLoadMode.setter
    def AdjustStreamTemplateLoadMode(self, value):
        self._AdjustStreamTemplateLoadMode = value

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumLoadUnit.%s' % value[:seperate])

    def _set_fixedload_with_str(self, value):
        self._FixedLoad = float(value)

    def _set_adjuststreamtemplateloadmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._AdjustStreamTemplateLoadMode = EnumAdjustStreamTemplateLoad.%s' % value[:seperate])

