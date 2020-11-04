"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EthMediaConfig_Autogen import EthMediaConfig


@rom_manager.rom
class EthCopperConfig(EthMediaConfig):
    def __init__(self, Master=None, AutoMDIX=None, FastRetrain=None, **kwargs):
        self._Master = Master  # Master
        self._AutoMDIX = AutoMDIX  # Auto MDIX
        self._FastRetrain = FastRetrain  # FastRetrain

        properties = kwargs.copy()
        if Master is not None:
            properties['Master'] = Master
        if AutoMDIX is not None:
            properties['AutoMDIX'] = AutoMDIX
        if FastRetrain is not None:
            properties['FastRetrain'] = FastRetrain

        # call base class function, and it will send message to renix server to create a class.
        super(EthCopperConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Master=None, AutoMDIX=None, FastRetrain=None, **kwargs):
        properties = kwargs.copy()
        if Master is not None:
            self._Master = Master
            properties['Master'] = Master
        if AutoMDIX is not None:
            self._AutoMDIX = AutoMDIX
            properties['AutoMDIX'] = AutoMDIX
        if FastRetrain is not None:
            self._FastRetrain = FastRetrain
            properties['FastRetrain'] = FastRetrain

        super(EthCopperConfig, self).edit(**properties)

    @property
    def Master(self):
        """
        get the value of property _Master
        """
        if self.force_auto_sync:
            self.get('Master')
        return self._Master

    @property
    def AutoMDIX(self):
        """
        get the value of property _AutoMDIX
        """
        if self.force_auto_sync:
            self.get('AutoMDIX')
        return self._AutoMDIX

    @property
    def FastRetrain(self):
        """
        get the value of property _FastRetrain
        """
        if self.force_auto_sync:
            self.get('FastRetrain')
        return self._FastRetrain

    @Master.setter
    def Master(self, value):
        self._Master = value
        self.edit(Master=value)

    @AutoMDIX.setter
    def AutoMDIX(self, value):
        self._AutoMDIX = value
        self.edit(AutoMDIX=value)

    @FastRetrain.setter
    def FastRetrain(self, value):
        self._FastRetrain = value
        self.edit(FastRetrain=value)

    def _set_master_with_str(self, value):
        seperate = value.find(':')
        exec('self._Master = EnumMaster.%s' % value[:seperate])

    def _set_automdix_with_str(self, value):
        self._AutoMDIX = (value == 'True')

    def _set_fastretrain_with_str(self, value):
        self._FastRetrain = (value == 'True')

