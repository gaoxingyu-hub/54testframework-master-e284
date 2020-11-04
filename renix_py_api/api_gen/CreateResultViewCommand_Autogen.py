"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateResultViewCommand(ROMCommand):
    def __init__(self, DataClassName=None, ResultViewType=None, **kwargs):
        self._DataClassName = DataClassName  # Result Class Name
        self._ResultViewType = ResultViewType  # Result View Type
        self._ResultViewHandle = ''  # Result View, not editable

        properties = kwargs.copy()
        if DataClassName is not None:
            properties['DataClassName'] = DataClassName
        if ResultViewType is not None:
            properties['ResultViewType'] = ResultViewType

        # call base class function, and it will send message to renix server to create a class.
        super(CreateResultViewCommand, self).__init__(**properties)

    @property
    def DataClassName(self):
        """
        get the value of property _DataClassName
        """
        return self._DataClassName

    @property
    def ResultViewType(self):
        """
        get the value of property _ResultViewType
        """
        return self._ResultViewType

    @property
    def ResultViewHandle(self):
        """
        get the value of property _ResultViewHandle
        """
        return self._ResultViewHandle

    @DataClassName.setter
    def DataClassName(self, value):
        self._DataClassName = value

    @ResultViewType.setter
    def ResultViewType(self, value):
        self._ResultViewType = value

    def _set_dataclassname_with_str(self, value):
        self._DataClassName = value

    def _set_resultviewtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ResultViewType = EnumResultType.%s' % value[:seperate])

    def _set_resultviewhandle_with_str(self, value):
        self._ResultViewHandle = value

    def _set_output_property(self, value):
        self._set_resultviewhandle_with_str(value)

