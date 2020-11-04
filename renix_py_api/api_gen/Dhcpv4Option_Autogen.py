"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv4Option(ROMObject):
    def __init__(self, OptionTag=None, OptionType=None, EnableOptionValueList=None, OptionValue=None, **kwargs):
        self._OptionTag = OptionTag  # Option Tag
        self._OptionType = OptionType  # Option Type
        self._EnableOptionValueList = EnableOptionValueList  # Enable Option Value List
        self._OptionValue = OptionValue  # Option Value

        properties = kwargs.copy()
        if OptionTag is not None:
            properties['OptionTag'] = OptionTag
        if OptionType is not None:
            properties['OptionType'] = OptionType
        if EnableOptionValueList is not None:
            properties['EnableOptionValueList'] = EnableOptionValueList
        if OptionValue is not None:
            properties['OptionValue'] = OptionValue

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4Option, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OptionTag=None, OptionType=None, EnableOptionValueList=None, OptionValue=None, **kwargs):
        properties = kwargs.copy()
        if OptionTag is not None:
            self._OptionTag = OptionTag
            properties['OptionTag'] = OptionTag
        if OptionType is not None:
            self._OptionType = OptionType
            properties['OptionType'] = OptionType
        if EnableOptionValueList is not None:
            self._EnableOptionValueList = EnableOptionValueList
            properties['EnableOptionValueList'] = EnableOptionValueList
        if OptionValue is not None:
            self._OptionValue = OptionValue
            properties['OptionValue'] = OptionValue

        super(Dhcpv4Option, self).edit(**properties)

    @property
    def OptionTag(self):
        """
        get the value of property _OptionTag
        """
        if self.force_auto_sync:
            self.get('OptionTag')
        return self._OptionTag

    @property
    def OptionType(self):
        """
        get the value of property _OptionType
        """
        if self.force_auto_sync:
            self.get('OptionType')
        return self._OptionType

    @property
    def EnableOptionValueList(self):
        """
        get the value of property _EnableOptionValueList
        """
        if self.force_auto_sync:
            self.get('EnableOptionValueList')
        return self._EnableOptionValueList

    @property
    def OptionValue(self):
        """
        get the value of property _OptionValue
        """
        if self.force_auto_sync:
            self.get('OptionValue')
        return self._OptionValue

    @OptionTag.setter
    def OptionTag(self, value):
        self._OptionTag = value
        self.edit(OptionTag=value)

    @OptionType.setter
    def OptionType(self, value):
        self._OptionType = value
        self.edit(OptionType=value)

    @EnableOptionValueList.setter
    def EnableOptionValueList(self, value):
        self._EnableOptionValueList = value
        self.edit(EnableOptionValueList=value)

    @OptionValue.setter
    def OptionValue(self, value):
        self._OptionValue = value
        self.edit(OptionValue=value)

    def _set_optiontag_with_str(self, value):
        try:
            self._OptionTag = int(value)
        except ValueError:
            self._OptionTag = hex(int(value, 16))

    def _set_optiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OptionType = EnumDhcpv4OptionType.%s' % value[:seperate])

    def _set_enableoptionvaluelist_with_str(self, value):
        self._EnableOptionValueList = (value == 'True')

    def _set_optionvalue_with_str(self, value):
        self._OptionValue = value

