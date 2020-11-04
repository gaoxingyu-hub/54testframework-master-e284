"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DynamicValue_Autogen import DynamicValue


@rom_manager.rom
class DynamicEnumValue(DynamicValue):
    def __init__(self, EnumType=None, Value=None, **kwargs):
        self._EnumType = EnumType  # Enum Type
        self._Value = Value  # Value

        properties = kwargs.copy()
        if EnumType is not None:
            properties['EnumType'] = EnumType
        if Value is not None:
            properties['Value'] = Value

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicEnumValue, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnumType=None, Value=None, **kwargs):
        properties = kwargs.copy()
        if EnumType is not None:
            self._EnumType = EnumType
            properties['EnumType'] = EnumType
        if Value is not None:
            self._Value = Value
            properties['Value'] = Value

        super(DynamicEnumValue, self).edit(**properties)

    @property
    def EnumType(self):
        """
        get the value of property _EnumType
        """
        if self.force_auto_sync:
            self.get('EnumType')
        return self._EnumType

    @property
    def Value(self):
        """
        get the value of property _Value
        """
        if self.force_auto_sync:
            self.get('Value')
        return self._Value

    @EnumType.setter
    def EnumType(self, value):
        self._EnumType = value
        self.edit(EnumType=value)

    @Value.setter
    def Value(self, value):
        self._Value = value
        self.edit(Value=value)

    def _set_enumtype_with_str(self, value):
        self._EnumType = value

    def _set_value_with_str(self, value):
        try:
            self._Value = int(value)
        except ValueError:
            self._Value = hex(int(value, 16))

