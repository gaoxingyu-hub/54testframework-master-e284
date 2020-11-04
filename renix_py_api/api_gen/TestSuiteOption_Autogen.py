"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TestSuiteOption(ROMObject):
    def __init__(self, ResultPath=None, **kwargs):
        self._ResultPath = ResultPath  # Result Path

        properties = kwargs.copy()
        if ResultPath is not None:
            properties['ResultPath'] = ResultPath

        # call base class function, and it will send message to renix server to create a class.
        super(TestSuiteOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ResultPath=None, **kwargs):
        properties = kwargs.copy()
        if ResultPath is not None:
            self._ResultPath = ResultPath
            properties['ResultPath'] = ResultPath

        super(TestSuiteOption, self).edit(**properties)

    @property
    def ResultPath(self):
        """
        get the value of property _ResultPath
        """
        if self.force_auto_sync:
            self.get('ResultPath')
        return self._ResultPath

    @ResultPath.setter
    def ResultPath(self, value):
        self._ResultPath = value
        self.edit(ResultPath=value)

    def _set_resultpath_with_str(self, value):
        self._ResultPath = value

