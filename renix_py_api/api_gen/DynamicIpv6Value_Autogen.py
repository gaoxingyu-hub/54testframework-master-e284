"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DynamicValue_Autogen import DynamicValue


@rom_manager.rom
class DynamicIpv6Value(DynamicValue):
    def __init__(self, Value=None, **kwargs):
        self._Value = Value  # Value

        properties = kwargs.copy()
        if Value is not None:
            properties['Value'] = Value

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicIpv6Value, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Value=None, **kwargs):
        properties = kwargs.copy()
        if Value is not None:
            self._Value = Value
            properties['Value'] = Value

        super(DynamicIpv6Value, self).edit(**properties)

    @property
    def Value(self):
        """
        get the value of property _Value
        """
        if self.force_auto_sync:
            self.get('Value')
        return self._Value

    @Value.setter
    def Value(self, value):
        self._Value = value
        self.edit(Value=value)

    def _set_value_with_str(self, value):
        self._Value = value

