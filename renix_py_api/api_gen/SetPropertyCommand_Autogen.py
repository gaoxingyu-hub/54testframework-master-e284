"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SetPropertyCommand(ROMCommand):
    def __init__(self, ObjectHandles=None, PropertyName=None, PropertyValues=None, **kwargs):
        self._ObjectHandles = ObjectHandles  # Objects Handles
        self._PropertyName = PropertyName  # Property Name
        self._PropertyValues = PropertyValues  # Property Value

        properties = kwargs.copy()
        if ObjectHandles is not None:
            properties['ObjectHandles'] = ObjectHandles
        if PropertyName is not None:
            properties['PropertyName'] = PropertyName
        if PropertyValues is not None:
            properties['PropertyValues'] = PropertyValues

        # call base class function, and it will send message to renix server to create a class.
        super(SetPropertyCommand, self).__init__(**properties)

    @property
    def ObjectHandles(self):
        """
        get the value of property _ObjectHandles
        """
        return self._ObjectHandles

    @property
    def PropertyName(self):
        """
        get the value of property _PropertyName
        """
        return self._PropertyName

    @property
    def PropertyValues(self):
        """
        get the value of property _PropertyValues
        """
        return self._PropertyValues

    @ObjectHandles.setter
    def ObjectHandles(self, value):
        self._ObjectHandles = value

    @PropertyName.setter
    def PropertyName(self, value):
        self._PropertyName = value

    @PropertyValues.setter
    def PropertyValues(self, value):
        self._PropertyValues = value

    def _set_objecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectHandles = tmp_value.split()

    def _set_propertyname_with_str(self, value):
        self._PropertyName = value

    def _set_propertyvalues_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PropertyValues = tmp_value.split()

