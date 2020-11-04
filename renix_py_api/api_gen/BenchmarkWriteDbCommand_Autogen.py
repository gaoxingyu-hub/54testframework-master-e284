"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationCommand_Autogen import IterationCommand


@rom_manager.rom
class BenchmarkWriteDbCommand(IterationCommand):
    def __init__(self, **kwargs):
        self._SummaryFile = ''  # Summary DB file name, not editable
        self._IterDbFile = ''  # Iter DB file name, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkWriteDbCommand, self).__init__(**properties)

    @property
    def SummaryFile(self):
        """
        get the value of property _SummaryFile
        """
        return self._SummaryFile

    @property
    def IterDbFile(self):
        """
        get the value of property _IterDbFile
        """
        return self._IterDbFile

    def _set_summaryfile_with_str(self, value):
        self._SummaryFile = value

    def _set_iterdbfile_with_str(self, value):
        self._IterDbFile = value

