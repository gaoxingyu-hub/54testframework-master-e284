"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkCommand_Autogen import BenchmarkCommand


@rom_manager.rom
class BenchmarkL23Command(BenchmarkCommand):
    def __init__(self, **kwargs):
        self._TestStatus = ''  # Test Status, not editable
        self._FileName = ''  # DB File Name, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkL23Command, self).__init__(**properties)

    @property
    def TestStatus(self):
        """
        get the value of property _TestStatus
        """
        return self._TestStatus

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        return self._FileName

    def _set_teststatus_with_str(self, value):
        self._TestStatus = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_output_property(self, value):
        self._set_filename_with_str(value)

