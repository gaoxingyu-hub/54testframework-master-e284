"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PppoeCustomOption(ROMObject):
    def __init__(self, OptionValue=None, SubPortocolType=None, UseWildcards=None, StringIsHexadecimal=None, OptionData=None, OptionHexData=None, **kwargs):
        self._OptionValue = OptionValue  # Option Value
        self._SubPortocolType = SubPortocolType  # Sub-protocol Type
        self._UseWildcards = UseWildcards  # Use Wildcards
        self._StringIsHexadecimal = StringIsHexadecimal  # String is Hexadecimal
        self._OptionData = OptionData  # Option Data
        self._OptionHexData = OptionHexData  # Option Data(Hex)

        properties = kwargs.copy()
        if OptionValue is not None:
            properties['OptionValue'] = OptionValue
        if SubPortocolType is not None:
            properties['SubPortocolType'] = SubPortocolType
        if UseWildcards is not None:
            properties['UseWildcards'] = UseWildcards
        if StringIsHexadecimal is not None:
            properties['StringIsHexadecimal'] = StringIsHexadecimal
        if OptionData is not None:
            properties['OptionData'] = OptionData
        if OptionHexData is not None:
            properties['OptionHexData'] = OptionHexData

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeCustomOption, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OptionValue=None, SubPortocolType=None, UseWildcards=None, StringIsHexadecimal=None, OptionData=None, OptionHexData=None, **kwargs):
        properties = kwargs.copy()
        if OptionValue is not None:
            self._OptionValue = OptionValue
            properties['OptionValue'] = OptionValue
        if SubPortocolType is not None:
            self._SubPortocolType = SubPortocolType
            properties['SubPortocolType'] = SubPortocolType
        if UseWildcards is not None:
            self._UseWildcards = UseWildcards
            properties['UseWildcards'] = UseWildcards
        if StringIsHexadecimal is not None:
            self._StringIsHexadecimal = StringIsHexadecimal
            properties['StringIsHexadecimal'] = StringIsHexadecimal
        if OptionData is not None:
            self._OptionData = OptionData
            properties['OptionData'] = OptionData
        if OptionHexData is not None:
            self._OptionHexData = OptionHexData
            properties['OptionHexData'] = OptionHexData

        super(PppoeCustomOption, self).edit(**properties)

    @property
    def OptionValue(self):
        """
        get the value of property _OptionValue
        """
        if self.force_auto_sync:
            self.get('OptionValue')
        return self._OptionValue

    @property
    def SubPortocolType(self):
        """
        get the value of property _SubPortocolType
        """
        if self.force_auto_sync:
            self.get('SubPortocolType')
        return self._SubPortocolType

    @property
    def UseWildcards(self):
        """
        get the value of property _UseWildcards
        """
        if self.force_auto_sync:
            self.get('UseWildcards')
        return self._UseWildcards

    @property
    def StringIsHexadecimal(self):
        """
        get the value of property _StringIsHexadecimal
        """
        if self.force_auto_sync:
            self.get('StringIsHexadecimal')
        return self._StringIsHexadecimal

    @property
    def OptionData(self):
        """
        get the value of property _OptionData
        """
        if self.force_auto_sync:
            self.get('OptionData')
        return self._OptionData

    @property
    def OptionHexData(self):
        """
        get the value of property _OptionHexData
        """
        if self.force_auto_sync:
            self.get('OptionHexData')
        return self._OptionHexData

    @OptionValue.setter
    def OptionValue(self, value):
        self._OptionValue = value
        self.edit(OptionValue=value)

    @SubPortocolType.setter
    def SubPortocolType(self, value):
        self._SubPortocolType = value
        self.edit(SubPortocolType=value)

    @UseWildcards.setter
    def UseWildcards(self, value):
        self._UseWildcards = value
        self.edit(UseWildcards=value)

    @StringIsHexadecimal.setter
    def StringIsHexadecimal(self, value):
        self._StringIsHexadecimal = value
        self.edit(StringIsHexadecimal=value)

    @OptionData.setter
    def OptionData(self, value):
        self._OptionData = value
        self.edit(OptionData=value)

    @OptionHexData.setter
    def OptionHexData(self, value):
        self._OptionHexData = value
        self.edit(OptionHexData=value)

    def _set_optionvalue_with_str(self, value):
        try:
            self._OptionValue = int(value)
        except ValueError:
            self._OptionValue = hex(int(value, 16))

    def _set_subportocoltype_with_str(self, value):
        seperate = value.find(':')
        exec('self._SubPortocolType = EnumPppoeCustomOptionSubProtocolType.%s' % value[:seperate])

    def _set_usewildcards_with_str(self, value):
        self._UseWildcards = (value == 'True')

    def _set_stringishexadecimal_with_str(self, value):
        self._StringIsHexadecimal = (value == 'True')

    def _set_optiondata_with_str(self, value):
        self._OptionData = value

    def _set_optionhexdata_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OptionHexData = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OptionHexData.append(int(str_value))
            except ValueError:
                self._OptionHexData.append(hex(int(str_value, 16)))

