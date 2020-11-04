"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DynamicAttribute_Autogen import DynamicAttribute


@rom_manager.rom
class DynamicS32Attribute(DynamicAttribute):
    def __init__(self, AttributeValue=None, **kwargs):
        self._AttributeValue = AttributeValue  # Attribute Value

        properties = kwargs.copy()
        if AttributeValue is not None:
            properties['AttributeValue'] = AttributeValue

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicS32Attribute, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AttributeValue=None, **kwargs):
        properties = kwargs.copy()
        if AttributeValue is not None:
            self._AttributeValue = AttributeValue
            properties['AttributeValue'] = AttributeValue

        super(DynamicS32Attribute, self).edit(**properties)

    @property
    def AttributeValue(self):
        """
        get the value of property _AttributeValue
        """
        if self.force_auto_sync:
            self.get('AttributeValue')
        return self._AttributeValue

    @AttributeValue.setter
    def AttributeValue(self, value):
        self._AttributeValue = value
        self.edit(AttributeValue=value)

    def _set_attributevalue_with_str(self, value):
        try:
            self._AttributeValue = int(value)
        except ValueError:
            self._AttributeValue = hex(int(value, 16))

