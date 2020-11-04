"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .RenixProgress_Autogen import RenixProgress


@rom_manager.rom
class RenixStepProgress(RenixProgress):
    def __init__(self, **kwargs):
        self._CurrentStep = ''  # Current Step, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(RenixStepProgress, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(RenixStepProgress, self).edit(**properties)

    @property
    def CurrentStep(self):
        """
        get the value of property _CurrentStep
        """
        if self.force_auto_sync:
            self.get('CurrentStep')
        return self._CurrentStep

    def _set_currentstep_with_str(self, value):
        self._CurrentStep = value

