"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpMatchFieldConfig(ROMObject):
    def __init__(self, Type=None, Value=None, Mask=None, ModifierType=None, ModifierStep=None, ModifierCount=None, **kwargs):
        self._Type = Type  # Type
        self._Value = Value  # Value
        self._Mask = Mask  # Mask
        self._ModifierType = ModifierType  # Modifier Type
        self._ModifierStep = ModifierStep  # Modifier Step
        self._ModifierCount = ModifierCount  # Modifier Count

        properties = kwargs.copy()
        if Type is not None:
            properties['Type'] = Type
        if Value is not None:
            properties['Value'] = Value
        if Mask is not None:
            properties['Mask'] = Mask
        if ModifierType is not None:
            properties['ModifierType'] = ModifierType
        if ModifierStep is not None:
            properties['ModifierStep'] = ModifierStep
        if ModifierCount is not None:
            properties['ModifierCount'] = ModifierCount

        # call base class function, and it will send message to renix server to create a class.
        super(OfpMatchFieldConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Type=None, Value=None, Mask=None, ModifierType=None, ModifierStep=None, ModifierCount=None, **kwargs):
        properties = kwargs.copy()
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type
        if Value is not None:
            self._Value = Value
            properties['Value'] = Value
        if Mask is not None:
            self._Mask = Mask
            properties['Mask'] = Mask
        if ModifierType is not None:
            self._ModifierType = ModifierType
            properties['ModifierType'] = ModifierType
        if ModifierStep is not None:
            self._ModifierStep = ModifierStep
            properties['ModifierStep'] = ModifierStep
        if ModifierCount is not None:
            self._ModifierCount = ModifierCount
            properties['ModifierCount'] = ModifierCount

        super(OfpMatchFieldConfig, self).edit(**properties)

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @property
    def Value(self):
        """
        get the value of property _Value
        """
        if self.force_auto_sync:
            self.get('Value')
        return self._Value

    @property
    def Mask(self):
        """
        get the value of property _Mask
        """
        if self.force_auto_sync:
            self.get('Mask')
        return self._Mask

    @property
    def ModifierType(self):
        """
        get the value of property _ModifierType
        """
        if self.force_auto_sync:
            self.get('ModifierType')
        return self._ModifierType

    @property
    def ModifierStep(self):
        """
        get the value of property _ModifierStep
        """
        if self.force_auto_sync:
            self.get('ModifierStep')
        return self._ModifierStep

    @property
    def ModifierCount(self):
        """
        get the value of property _ModifierCount
        """
        if self.force_auto_sync:
            self.get('ModifierCount')
        return self._ModifierCount

    @Type.setter
    def Type(self, value):
        self._Type = value
        self.edit(Type=value)

    @Value.setter
    def Value(self, value):
        self._Value = value
        self.edit(Value=value)

    @Mask.setter
    def Mask(self, value):
        self._Mask = value
        self.edit(Mask=value)

    @ModifierType.setter
    def ModifierType(self, value):
        self._ModifierType = value
        self.edit(ModifierType=value)

    @ModifierStep.setter
    def ModifierStep(self, value):
        self._ModifierStep = value
        self.edit(ModifierStep=value)

    @ModifierCount.setter
    def ModifierCount(self, value):
        self._ModifierCount = value
        self.edit(ModifierCount=value)

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpField.%s' % value[:seperate])

    def _set_value_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Value = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Value.append(int(str_value))
            except ValueError:
                self._Value.append(hex(int(str_value, 16)))

    def _set_mask_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Mask = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Mask.append(int(str_value))
            except ValueError:
                self._Mask.append(hex(int(str_value, 16)))

    def _set_modifiertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ModifierType = EnumOfpModifier.%s' % value[:seperate])

    def _set_modifierstep_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ModifierStep = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._ModifierStep.append(int(str_value))
            except ValueError:
                self._ModifierStep.append(hex(int(str_value, 16)))

    def _set_modifiercount_with_str(self, value):
        try:
            self._ModifierCount = int(value)
        except ValueError:
            self._ModifierCount = hex(int(value, 16))

