"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EthMedia_Autogen import EthMedia


@rom_manager.rom
class EthCopper(EthMedia):
    def __init__(self, **kwargs):
        self._Master = False  # Master, not editable
        self._FastRetrain = False  # FastRetrain, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(EthCopper, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(EthCopper, self).edit(**properties)

    @property
    def Master(self):
        """
        get the value of property _Master
        """
        if self.force_auto_sync:
            self.get('Master')
        return self._Master

    @property
    def FastRetrain(self):
        """
        get the value of property _FastRetrain
        """
        if self.force_auto_sync:
            self.get('FastRetrain')
        return self._FastRetrain

    def _set_master_with_str(self, value):
        self._Master = (value == 'True')

    def _set_fastretrain_with_str(self, value):
        self._FastRetrain = (value == 'True')

