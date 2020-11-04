"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DynamicClass(ROMObject):
    def __init__(self, DynamicClassType=None, ClassDisplay=None, ClassDescription=None, IsSerializable=None, IsPrivate=None, IsSingleton=None, **kwargs):
        self._DynamicClassType = DynamicClassType  # Dynamic Class Type
        self._ClassDisplay = ClassDisplay  # Dynamic Class Display Name
        self._ClassDescription = ClassDescription  # Dynamic Class Description
        self._IsSerializable = IsSerializable  # Serializable
        self._IsPrivate = IsPrivate  # Private
        self._IsSingleton = IsSingleton  # Singleton

        properties = kwargs.copy()
        if DynamicClassType is not None:
            properties['DynamicClassType'] = DynamicClassType
        if ClassDisplay is not None:
            properties['ClassDisplay'] = ClassDisplay
        if ClassDescription is not None:
            properties['ClassDescription'] = ClassDescription
        if IsSerializable is not None:
            properties['IsSerializable'] = IsSerializable
        if IsPrivate is not None:
            properties['IsPrivate'] = IsPrivate
        if IsSingleton is not None:
            properties['IsSingleton'] = IsSingleton

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicClass, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DynamicClassType=None, ClassDisplay=None, ClassDescription=None, IsSerializable=None, IsPrivate=None, IsSingleton=None, **kwargs):
        properties = kwargs.copy()
        if DynamicClassType is not None:
            self._DynamicClassType = DynamicClassType
            properties['DynamicClassType'] = DynamicClassType
        if ClassDisplay is not None:
            self._ClassDisplay = ClassDisplay
            properties['ClassDisplay'] = ClassDisplay
        if ClassDescription is not None:
            self._ClassDescription = ClassDescription
            properties['ClassDescription'] = ClassDescription
        if IsSerializable is not None:
            self._IsSerializable = IsSerializable
            properties['IsSerializable'] = IsSerializable
        if IsPrivate is not None:
            self._IsPrivate = IsPrivate
            properties['IsPrivate'] = IsPrivate
        if IsSingleton is not None:
            self._IsSingleton = IsSingleton
            properties['IsSingleton'] = IsSingleton

        super(DynamicClass, self).edit(**properties)

    @property
    def DynamicClassType(self):
        """
        get the value of property _DynamicClassType
        """
        if self.force_auto_sync:
            self.get('DynamicClassType')
        return self._DynamicClassType

    @property
    def ClassDisplay(self):
        """
        get the value of property _ClassDisplay
        """
        if self.force_auto_sync:
            self.get('ClassDisplay')
        return self._ClassDisplay

    @property
    def ClassDescription(self):
        """
        get the value of property _ClassDescription
        """
        if self.force_auto_sync:
            self.get('ClassDescription')
        return self._ClassDescription

    @property
    def IsSerializable(self):
        """
        get the value of property _IsSerializable
        """
        if self.force_auto_sync:
            self.get('IsSerializable')
        return self._IsSerializable

    @property
    def IsPrivate(self):
        """
        get the value of property _IsPrivate
        """
        if self.force_auto_sync:
            self.get('IsPrivate')
        return self._IsPrivate

    @property
    def IsSingleton(self):
        """
        get the value of property _IsSingleton
        """
        if self.force_auto_sync:
            self.get('IsSingleton')
        return self._IsSingleton

    @DynamicClassType.setter
    def DynamicClassType(self, value):
        self._DynamicClassType = value
        self.edit(DynamicClassType=value)

    @ClassDisplay.setter
    def ClassDisplay(self, value):
        self._ClassDisplay = value
        self.edit(ClassDisplay=value)

    @ClassDescription.setter
    def ClassDescription(self, value):
        self._ClassDescription = value
        self.edit(ClassDescription=value)

    @IsSerializable.setter
    def IsSerializable(self, value):
        self._IsSerializable = value
        self.edit(IsSerializable=value)

    @IsPrivate.setter
    def IsPrivate(self, value):
        self._IsPrivate = value
        self.edit(IsPrivate=value)

    @IsSingleton.setter
    def IsSingleton(self, value):
        self._IsSingleton = value
        self.edit(IsSingleton=value)

    def _set_dynamicclasstype_with_str(self, value):
        seperate = value.find(':')
        exec('self._DynamicClassType = EnumDynamicClassType.%s' % value[:seperate])

    def _set_classdisplay_with_str(self, value):
        self._ClassDisplay = value

    def _set_classdescription_with_str(self, value):
        self._ClassDescription = value

    def _set_isserializable_with_str(self, value):
        self._IsSerializable = (value == 'True')

    def _set_isprivate_with_str(self, value):
        self._IsPrivate = (value == 'True')

    def _set_issingleton_with_str(self, value):
        self._IsSingleton = (value == 'True')

