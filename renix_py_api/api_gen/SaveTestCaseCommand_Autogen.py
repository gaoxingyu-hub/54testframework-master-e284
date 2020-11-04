"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SaveTestCaseCommand(ROMCommand):
    def __init__(self, TestCase=None, **kwargs):
        self._TestCase = TestCase  # Test Case File Name
        self._TestCaseFile = ''  # Saved Test Case File, not editable

        properties = kwargs.copy()
        if TestCase is not None:
            properties['TestCase'] = TestCase

        # call base class function, and it will send message to renix server to create a class.
        super(SaveTestCaseCommand, self).__init__(**properties)

    @property
    def TestCase(self):
        """
        get the value of property _TestCase
        """
        return self._TestCase

    @property
    def TestCaseFile(self):
        """
        get the value of property _TestCaseFile
        """
        return self._TestCaseFile

    @TestCase.setter
    def TestCase(self, value):
        self._TestCase = value

    def _set_testcase_with_str(self, value):
        self._TestCase = value

    def _set_testcasefile_with_str(self, value):
        self._TestCaseFile = value

    def _set_output_property(self, value):
        self._set_testcasefile_with_str(value)

