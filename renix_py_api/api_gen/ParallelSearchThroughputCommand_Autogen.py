"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ParallelLoadCommand_Autogen import ParallelLoadCommand


@rom_manager.rom
class ParallelSearchThroughputCommand(ParallelLoadCommand):
    def __init__(self, BackOffMode=None, **kwargs):
        self._BackOffMode = BackOffMode  # Back-Off Mode

        properties = kwargs.copy()
        if BackOffMode is not None:
            properties['BackOffMode'] = BackOffMode

        # call base class function, and it will send message to renix server to create a class.
        super(ParallelSearchThroughputCommand, self).__init__(**properties)

    @property
    def BackOffMode(self):
        """
        get the value of property _BackOffMode
        """
        return self._BackOffMode

    @BackOffMode.setter
    def BackOffMode(self, value):
        self._BackOffMode = value

    def _set_backoffmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._BackOffMode = EnumBackOffMode.%s' % value[:seperate])

