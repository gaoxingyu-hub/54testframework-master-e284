"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BgpPathAttributeConfig(ROMObject):
    def __init__(self, PathAttributeType=None, OptionalFlag=None, TransitiveFlag=None, PartialFlag=None, ExtendedLengthFlag=None, AttributeValue=None, **kwargs):
        self._PathAttributeType = PathAttributeType  # Path Attribute Type
        self._OptionalFlag = OptionalFlag  # Optional Flag
        self._TransitiveFlag = TransitiveFlag  # Transitive Flag
        self._PartialFlag = PartialFlag  # Partial Flag
        self._ExtendedLengthFlag = ExtendedLengthFlag  # Extended Length Flag
        self._AttributeExtendedLength = 0  # Path Attribute Length, not editable
        self._AttributeValue = AttributeValue  # Path Attribute Value

        properties = kwargs.copy()
        if PathAttributeType is not None:
            properties['PathAttributeType'] = PathAttributeType
        if OptionalFlag is not None:
            properties['OptionalFlag'] = OptionalFlag
        if TransitiveFlag is not None:
            properties['TransitiveFlag'] = TransitiveFlag
        if PartialFlag is not None:
            properties['PartialFlag'] = PartialFlag
        if ExtendedLengthFlag is not None:
            properties['ExtendedLengthFlag'] = ExtendedLengthFlag
        if AttributeValue is not None:
            properties['AttributeValue'] = AttributeValue

        # call base class function, and it will send message to renix server to create a class.
        super(BgpPathAttributeConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PathAttributeType=None, OptionalFlag=None, TransitiveFlag=None, PartialFlag=None, ExtendedLengthFlag=None, AttributeValue=None, **kwargs):
        properties = kwargs.copy()
        if PathAttributeType is not None:
            self._PathAttributeType = PathAttributeType
            properties['PathAttributeType'] = PathAttributeType
        if OptionalFlag is not None:
            self._OptionalFlag = OptionalFlag
            properties['OptionalFlag'] = OptionalFlag
        if TransitiveFlag is not None:
            self._TransitiveFlag = TransitiveFlag
            properties['TransitiveFlag'] = TransitiveFlag
        if PartialFlag is not None:
            self._PartialFlag = PartialFlag
            properties['PartialFlag'] = PartialFlag
        if ExtendedLengthFlag is not None:
            self._ExtendedLengthFlag = ExtendedLengthFlag
            properties['ExtendedLengthFlag'] = ExtendedLengthFlag
        if AttributeValue is not None:
            self._AttributeValue = AttributeValue
            properties['AttributeValue'] = AttributeValue

        super(BgpPathAttributeConfig, self).edit(**properties)

    @property
    def PathAttributeType(self):
        """
        get the value of property _PathAttributeType
        """
        if self.force_auto_sync:
            self.get('PathAttributeType')
        return self._PathAttributeType

    @property
    def OptionalFlag(self):
        """
        get the value of property _OptionalFlag
        """
        if self.force_auto_sync:
            self.get('OptionalFlag')
        return self._OptionalFlag

    @property
    def TransitiveFlag(self):
        """
        get the value of property _TransitiveFlag
        """
        if self.force_auto_sync:
            self.get('TransitiveFlag')
        return self._TransitiveFlag

    @property
    def PartialFlag(self):
        """
        get the value of property _PartialFlag
        """
        if self.force_auto_sync:
            self.get('PartialFlag')
        return self._PartialFlag

    @property
    def ExtendedLengthFlag(self):
        """
        get the value of property _ExtendedLengthFlag
        """
        if self.force_auto_sync:
            self.get('ExtendedLengthFlag')
        return self._ExtendedLengthFlag

    @property
    def AttributeExtendedLength(self):
        """
        get the value of property _AttributeExtendedLength
        """
        if self.force_auto_sync:
            self.get('AttributeExtendedLength')
        return self._AttributeExtendedLength

    @property
    def AttributeValue(self):
        """
        get the value of property _AttributeValue
        """
        if self.force_auto_sync:
            self.get('AttributeValue')
        return self._AttributeValue

    @PathAttributeType.setter
    def PathAttributeType(self, value):
        self._PathAttributeType = value
        self.edit(PathAttributeType=value)

    @OptionalFlag.setter
    def OptionalFlag(self, value):
        self._OptionalFlag = value
        self.edit(OptionalFlag=value)

    @TransitiveFlag.setter
    def TransitiveFlag(self, value):
        self._TransitiveFlag = value
        self.edit(TransitiveFlag=value)

    @PartialFlag.setter
    def PartialFlag(self, value):
        self._PartialFlag = value
        self.edit(PartialFlag=value)

    @ExtendedLengthFlag.setter
    def ExtendedLengthFlag(self, value):
        self._ExtendedLengthFlag = value
        self.edit(ExtendedLengthFlag=value)

    @AttributeValue.setter
    def AttributeValue(self, value):
        self._AttributeValue = value
        self.edit(AttributeValue=value)

    def _set_pathattributetype_with_str(self, value):
        try:
            self._PathAttributeType = int(value)
        except ValueError:
            self._PathAttributeType = hex(int(value, 16))

    def _set_optionalflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._OptionalFlag = EnumPathAttributeOptionalFlag.%s' % value[:seperate])

    def _set_transitiveflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransitiveFlag = EnumPathAttributeTransitiveFlag.%s' % value[:seperate])

    def _set_partialflag_with_str(self, value):
        seperate = value.find(':')
        exec('self._PartialFlag = EnumPathAttributePartialFlag.%s' % value[:seperate])

    def _set_extendedlengthflag_with_str(self, value):
        self._ExtendedLengthFlag = (value == 'True')

    def _set_attributeextendedlength_with_str(self, value):
        try:
            self._AttributeExtendedLength = int(value)
        except ValueError:
            self._AttributeExtendedLength = hex(int(value, 16))

    def _set_attributevalue_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AttributeValue = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._AttributeValue.append(int(str_value))
            except ValueError:
                self._AttributeValue.append(hex(int(str_value, 16)))

