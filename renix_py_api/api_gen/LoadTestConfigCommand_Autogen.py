"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class LoadTestConfigCommand(ROMCommand):
    def __init__(self, SourceObjectHandle=None, TestConfig=None, **kwargs):
        self._SourceObjectHandle = SourceObjectHandle  # Source Object Handle
        self._TestConfig = TestConfig  # Test Config File Path
        self._ObjectHandle = ''  # Loaded Object Handle, not editable

        properties = kwargs.copy()
        if SourceObjectHandle is not None:
            properties['SourceObjectHandle'] = SourceObjectHandle
        if TestConfig is not None:
            properties['TestConfig'] = TestConfig

        # call base class function, and it will send message to renix server to create a class.
        super(LoadTestConfigCommand, self).__init__(**properties)

    @property
    def SourceObjectHandle(self):
        """
        get the value of property _SourceObjectHandle
        """
        return self._SourceObjectHandle

    @property
    def TestConfig(self):
        """
        get the value of property _TestConfig
        """
        return self._TestConfig

    @property
    def ObjectHandle(self):
        """
        get the value of property _ObjectHandle
        """
        return self._ObjectHandle

    @SourceObjectHandle.setter
    def SourceObjectHandle(self, value):
        self._SourceObjectHandle = value

    @TestConfig.setter
    def TestConfig(self, value):
        self._TestConfig = value

    def _set_sourceobjecthandle_with_str(self, value):
        self._SourceObjectHandle = value

    def _set_testconfig_with_str(self, value):
        self._TestConfig = value

    def _set_objecthandle_with_str(self, value):
        self._ObjectHandle = value

    def _set_output_property(self, value):
        self._set_objecthandle_with_str(value)

