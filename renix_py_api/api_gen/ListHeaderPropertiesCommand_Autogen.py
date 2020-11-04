"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ListHeaderPropertiesCommand(ROMCommand):
    def __init__(self, HeaderType=None, **kwargs):
        self._HeaderType = HeaderType  # Header Type
        self._Properties = None  # Header Properties, not editable

        properties = kwargs.copy()
        if HeaderType is not None:
            properties['HeaderType'] = HeaderType

        # call base class function, and it will send message to renix server to create a class.
        super(ListHeaderPropertiesCommand, self).__init__(**properties)

    @property
    def HeaderType(self):
        """
        get the value of property _HeaderType
        """
        return self._HeaderType

    @property
    def Properties(self):
        """
        get the value of property _Properties
        """
        return self._Properties

    @HeaderType.setter
    def HeaderType(self, value):
        self._HeaderType = value

    def _set_headertype_with_str(self, value):
        self._HeaderType = value

    def _set_properties_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Properties = tmp_value.split()

    def _set_output_property(self, value):
        self._set_properties_with_str(value)

