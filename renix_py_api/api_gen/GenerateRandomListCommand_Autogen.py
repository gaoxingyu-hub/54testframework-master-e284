"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GenerateRandomListCommand(ROMCommand):
    def __init__(self, PropertyType=None, PropertyBitLength=None, ModifierStart=None, ModifierEnd=None, ModifierSeed=None, ModifierCount=None, ModifierOffset=None, ModifierMask=None, **kwargs):
        self._PropertyType = PropertyType  # Property Type
        self._PropertyBitLength = PropertyBitLength  # Field bit Length
        self._ModifierStart = ModifierStart  # Random Start
        self._ModifierEnd = ModifierEnd  # Random End
        self._ModifierSeed = ModifierSeed  # Random Seed
        self._ModifierCount = ModifierCount  # Random Count
        self._ModifierOffset = ModifierOffset  # Random Offset
        self._ModifierMask = ModifierMask  # Random Mask

        properties = kwargs.copy()
        if PropertyType is not None:
            properties['PropertyType'] = PropertyType
        if PropertyBitLength is not None:
            properties['PropertyBitLength'] = PropertyBitLength
        if ModifierStart is not None:
            properties['ModifierStart'] = ModifierStart
        if ModifierEnd is not None:
            properties['ModifierEnd'] = ModifierEnd
        if ModifierSeed is not None:
            properties['ModifierSeed'] = ModifierSeed
        if ModifierCount is not None:
            properties['ModifierCount'] = ModifierCount
        if ModifierOffset is not None:
            properties['ModifierOffset'] = ModifierOffset
        if ModifierMask is not None:
            properties['ModifierMask'] = ModifierMask

        # call base class function, and it will send message to renix server to create a class.
        super(GenerateRandomListCommand, self).__init__(**properties)

    @property
    def PropertyType(self):
        """
        get the value of property _PropertyType
        """
        return self._PropertyType

    @property
    def PropertyBitLength(self):
        """
        get the value of property _PropertyBitLength
        """
        return self._PropertyBitLength

    @property
    def ModifierStart(self):
        """
        get the value of property _ModifierStart
        """
        return self._ModifierStart

    @property
    def ModifierEnd(self):
        """
        get the value of property _ModifierEnd
        """
        return self._ModifierEnd

    @property
    def ModifierSeed(self):
        """
        get the value of property _ModifierSeed
        """
        return self._ModifierSeed

    @property
    def ModifierCount(self):
        """
        get the value of property _ModifierCount
        """
        return self._ModifierCount

    @property
    def ModifierOffset(self):
        """
        get the value of property _ModifierOffset
        """
        return self._ModifierOffset

    @property
    def ModifierMask(self):
        """
        get the value of property _ModifierMask
        """
        return self._ModifierMask

    @PropertyType.setter
    def PropertyType(self, value):
        self._PropertyType = value

    @PropertyBitLength.setter
    def PropertyBitLength(self, value):
        self._PropertyBitLength = value

    @ModifierStart.setter
    def ModifierStart(self, value):
        self._ModifierStart = value

    @ModifierEnd.setter
    def ModifierEnd(self, value):
        self._ModifierEnd = value

    @ModifierSeed.setter
    def ModifierSeed(self, value):
        self._ModifierSeed = value

    @ModifierCount.setter
    def ModifierCount(self, value):
        self._ModifierCount = value

    @ModifierOffset.setter
    def ModifierOffset(self, value):
        self._ModifierOffset = value

    @ModifierMask.setter
    def ModifierMask(self, value):
        self._ModifierMask = value

    def _set_propertytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._PropertyType = EnumPropertyType.%s' % value[:seperate])

    def _set_propertybitlength_with_str(self, value):
        try:
            self._PropertyBitLength = int(value)
        except ValueError:
            self._PropertyBitLength = hex(int(value, 16))

    def _set_modifierstart_with_str(self, value):
        self._ModifierStart = value

    def _set_modifierend_with_str(self, value):
        self._ModifierEnd = value

    def _set_modifierseed_with_str(self, value):
        try:
            self._ModifierSeed = int(value)
        except ValueError:
            self._ModifierSeed = hex(int(value, 16))

    def _set_modifiercount_with_str(self, value):
        try:
            self._ModifierCount = int(value)
        except ValueError:
            self._ModifierCount = hex(int(value, 16))

    def _set_modifieroffset_with_str(self, value):
        try:
            self._ModifierOffset = int(value)
        except ValueError:
            self._ModifierOffset = hex(int(value, 16))

    def _set_modifiermask_with_str(self, value):
        self._ModifierMask = value

