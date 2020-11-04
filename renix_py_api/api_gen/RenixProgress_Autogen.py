"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class RenixProgress(ROMObject):
    def __init__(self, **kwargs):
        self._Progress = 0  # Progress, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(RenixProgress, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(RenixProgress, self).edit(**properties)

    @property
    def Progress(self):
        """
        get the value of property _Progress
        """
        if self.force_auto_sync:
            self.get('Progress')
        return self._Progress

    def _set_progress_with_str(self, value):
        try:
            self._Progress = int(value)
        except ValueError:
            self._Progress = hex(int(value, 16))

