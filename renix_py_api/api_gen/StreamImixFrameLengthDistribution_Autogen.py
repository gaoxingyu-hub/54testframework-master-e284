"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamImixFrameLengthDistribution(ROMObject):
    def __init__(self, RandomLength=None, FixedLength=None, MinLength=None, MaxLength=None, Weight=None, **kwargs):
        self._RandomLength = RandomLength  # Random Length
        self._FixedLength = FixedLength  # Fixed Length
        self._MinLength = MinLength  # Min Length
        self._MaxLength = MaxLength  # Max Length
        self._Weight = Weight  # Weight
        self._Percentage = '100%'  # Percentage, not editable

        properties = kwargs.copy()
        if RandomLength is not None:
            properties['RandomLength'] = RandomLength
        if FixedLength is not None:
            properties['FixedLength'] = FixedLength
        if MinLength is not None:
            properties['MinLength'] = MinLength
        if MaxLength is not None:
            properties['MaxLength'] = MaxLength
        if Weight is not None:
            properties['Weight'] = Weight

        # call base class function, and it will send message to renix server to create a class.
        super(StreamImixFrameLengthDistribution, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RandomLength=None, FixedLength=None, MinLength=None, MaxLength=None, Weight=None, **kwargs):
        properties = kwargs.copy()
        if RandomLength is not None:
            self._RandomLength = RandomLength
            properties['RandomLength'] = RandomLength
        if FixedLength is not None:
            self._FixedLength = FixedLength
            properties['FixedLength'] = FixedLength
        if MinLength is not None:
            self._MinLength = MinLength
            properties['MinLength'] = MinLength
        if MaxLength is not None:
            self._MaxLength = MaxLength
            properties['MaxLength'] = MaxLength
        if Weight is not None:
            self._Weight = Weight
            properties['Weight'] = Weight

        super(StreamImixFrameLengthDistribution, self).edit(**properties)

    @property
    def RandomLength(self):
        """
        get the value of property _RandomLength
        """
        if self.force_auto_sync:
            self.get('RandomLength')
        return self._RandomLength

    @property
    def FixedLength(self):
        """
        get the value of property _FixedLength
        """
        if self.force_auto_sync:
            self.get('FixedLength')
        return self._FixedLength

    @property
    def MinLength(self):
        """
        get the value of property _MinLength
        """
        if self.force_auto_sync:
            self.get('MinLength')
        return self._MinLength

    @property
    def MaxLength(self):
        """
        get the value of property _MaxLength
        """
        if self.force_auto_sync:
            self.get('MaxLength')
        return self._MaxLength

    @property
    def Weight(self):
        """
        get the value of property _Weight
        """
        if self.force_auto_sync:
            self.get('Weight')
        return self._Weight

    @property
    def Percentage(self):
        """
        get the value of property _Percentage
        """
        if self.force_auto_sync:
            self.get('Percentage')
        return self._Percentage

    @RandomLength.setter
    def RandomLength(self, value):
        self._RandomLength = value
        self.edit(RandomLength=value)

    @FixedLength.setter
    def FixedLength(self, value):
        self._FixedLength = value
        self.edit(FixedLength=value)

    @MinLength.setter
    def MinLength(self, value):
        self._MinLength = value
        self.edit(MinLength=value)

    @MaxLength.setter
    def MaxLength(self, value):
        self._MaxLength = value
        self.edit(MaxLength=value)

    @Weight.setter
    def Weight(self, value):
        self._Weight = value
        self.edit(Weight=value)

    def _set_randomlength_with_str(self, value):
        self._RandomLength = (value == 'True')

    def _set_fixedlength_with_str(self, value):
        try:
            self._FixedLength = int(value)
        except ValueError:
            self._FixedLength = hex(int(value, 16))

    def _set_minlength_with_str(self, value):
        try:
            self._MinLength = int(value)
        except ValueError:
            self._MinLength = hex(int(value, 16))

    def _set_maxlength_with_str(self, value):
        try:
            self._MaxLength = int(value)
        except ValueError:
            self._MaxLength = hex(int(value, 16))

    def _set_weight_with_str(self, value):
        try:
            self._Weight = int(value)
        except ValueError:
            self._Weight = hex(int(value, 16))

    def _set_percentage_with_str(self, value):
        self._Percentage = value

