"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SaveTestCaseToPythonCommand(ROMCommand):
    def __init__(self, TestCaseName=None, TestCaseDir=None, **kwargs):
        self._TestCaseName = TestCaseName  # Test Case Name
        self._TestCaseDir = TestCaseDir  # Test Case Directory
        self._TestCaseFolder = ''  # Test Case Saved Folder, not editable

        properties = kwargs.copy()
        if TestCaseName is not None:
            properties['TestCaseName'] = TestCaseName
        if TestCaseDir is not None:
            properties['TestCaseDir'] = TestCaseDir

        # call base class function, and it will send message to renix server to create a class.
        super(SaveTestCaseToPythonCommand, self).__init__(**properties)

    @property
    def TestCaseName(self):
        """
        get the value of property _TestCaseName
        """
        return self._TestCaseName

    @property
    def TestCaseDir(self):
        """
        get the value of property _TestCaseDir
        """
        return self._TestCaseDir

    @property
    def TestCaseFolder(self):
        """
        get the value of property _TestCaseFolder
        """
        return self._TestCaseFolder

    @TestCaseName.setter
    def TestCaseName(self, value):
        self._TestCaseName = value

    @TestCaseDir.setter
    def TestCaseDir(self, value):
        self._TestCaseDir = value

    def _set_testcasename_with_str(self, value):
        self._TestCaseName = value

    def _set_testcasedir_with_str(self, value):
        self._TestCaseDir = value

    def _set_testcasefolder_with_str(self, value):
        self._TestCaseFolder = value

    def _set_output_property(self, value):
        self._set_testcasefolder_with_str(value)

