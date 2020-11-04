"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BenchmarkResult_Autogen import BenchmarkResult


@rom_manager.rom
class BenchmarkL23IterationResult(BenchmarkResult):
    def __init__(self, **kwargs):
        self._TestStatus = ''  # Test Status, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkL23IterationResult, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(BenchmarkL23IterationResult, self).edit(**properties)

    @property
    def TestStatus(self):
        """
        get the value of property _TestStatus
        """
        if self.force_auto_sync:
            self.get('TestStatus')
        return self._TestStatus

    def _set_teststatus_with_str(self, value):
        self._TestStatus = value

