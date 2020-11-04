"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class LoadTestCaseCommand(ROMCommand):
    def __init__(self, TestCase=None, **kwargs):
        self._TestCase = TestCase  # Test Case File Path

        properties = kwargs.copy()
        if TestCase is not None:
            properties['TestCase'] = TestCase

        # call base class function, and it will send message to renix server to create a class.
        super(LoadTestCaseCommand, self).__init__(**properties)

    @property
    def TestCase(self):
        """
        get the value of property _TestCase
        """
        return self._TestCase

    @TestCase.setter
    def TestCase(self, value):
        self._TestCase = value

    def _set_testcase_with_str(self, value):
        self._TestCase = value

