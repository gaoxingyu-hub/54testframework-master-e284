"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv6ServerCustomOptionsConfig(ROMObject):
    def __init__(self, OptionVal=None, IncludeMsg=None, Wildcards=None, StringIsHexadecimal=None, OptionPayload=None, OptionHexPayload=None, **kwargs):
        self._OptionVal = OptionVal  # Option Value
        self._IncludeMsg = swap_int_to_enum_flag(IncludeMsg, EnumDhcpv6ServerIncludeMsg)  # Include in Message
        self._Wildcards = Wildcards  # Wildcards
        self._StringIsHexadecimal = StringIsHexadecimal  # String is Hexadecimal
        self._OptionPayload = OptionPayload  # Option Payload
        self._OptionHexPayload = OptionHexPayload  # Option Payload

        properties = kwargs.copy()
        if OptionVal is not None:
            properties['OptionVal'] = OptionVal
        if IncludeMsg is not None:
            if isinstance(IncludeMsg, Flag):
                properties['IncludeMsg'] = IncludeMsg.value
            else:
                properties['IncludeMsg'] = IncludeMsg
        if Wildcards is not None:
            properties['Wildcards'] = Wildcards
        if StringIsHexadecimal is not None:
            properties['StringIsHexadecimal'] = StringIsHexadecimal
        if OptionPayload is not None:
            properties['OptionPayload'] = OptionPayload
        if OptionHexPayload is not None:
            properties['OptionHexPayload'] = OptionHexPayload

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ServerCustomOptionsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OptionVal=None, IncludeMsg=None, Wildcards=None, StringIsHexadecimal=None, OptionPayload=None, OptionHexPayload=None, **kwargs):
        properties = kwargs.copy()
        if OptionVal is not None:
            self._OptionVal = OptionVal
            properties['OptionVal'] = OptionVal
        if IncludeMsg is not None:
            self._IncludeMsg = swap_int_to_enum_flag(IncludeMsg, EnumDhcpv6ServerIncludeMsg)
            if isinstance(IncludeMsg, Flag):
                properties['IncludeMsg'] = IncludeMsg.value
            else:
                properties['IncludeMsg'] = IncludeMsg
        if Wildcards is not None:
            self._Wildcards = Wildcards
            properties['Wildcards'] = Wildcards
        if StringIsHexadecimal is not None:
            self._StringIsHexadecimal = StringIsHexadecimal
            properties['StringIsHexadecimal'] = StringIsHexadecimal
        if OptionPayload is not None:
            self._OptionPayload = OptionPayload
            properties['OptionPayload'] = OptionPayload
        if OptionHexPayload is not None:
            self._OptionHexPayload = OptionHexPayload
            properties['OptionHexPayload'] = OptionHexPayload

        super(Dhcpv6ServerCustomOptionsConfig, self).edit(**properties)

    @property
    def OptionVal(self):
        """
        get the value of property _OptionVal
        """
        if self.force_auto_sync:
            self.get('OptionVal')
        return self._OptionVal

    @property
    def IncludeMsg(self):
        """
        get the value of property _IncludeMsg
        """
        if self.force_auto_sync:
            self.get('IncludeMsg')
        return self._IncludeMsg

    @property
    def Wildcards(self):
        """
        get the value of property _Wildcards
        """
        if self.force_auto_sync:
            self.get('Wildcards')
        return self._Wildcards

    @property
    def StringIsHexadecimal(self):
        """
        get the value of property _StringIsHexadecimal
        """
        if self.force_auto_sync:
            self.get('StringIsHexadecimal')
        return self._StringIsHexadecimal

    @property
    def OptionPayload(self):
        """
        get the value of property _OptionPayload
        """
        if self.force_auto_sync:
            self.get('OptionPayload')
        return self._OptionPayload

    @property
    def OptionHexPayload(self):
        """
        get the value of property _OptionHexPayload
        """
        if self.force_auto_sync:
            self.get('OptionHexPayload')
        return self._OptionHexPayload

    @OptionVal.setter
    def OptionVal(self, value):
        self._OptionVal = value
        self.edit(OptionVal=value)

    @IncludeMsg.setter
    def IncludeMsg(self, value):
        self._IncludeMsg = swap_int_to_enum_flag(value, EnumDhcpv6ServerIncludeMsg)
        if isinstance(value, Flag):
            self.edit(IncludeMsg=value.value)
        else:
            self.edit(IncludeMsg=value)

    @Wildcards.setter
    def Wildcards(self, value):
        self._Wildcards = value
        self.edit(Wildcards=value)

    @StringIsHexadecimal.setter
    def StringIsHexadecimal(self, value):
        self._StringIsHexadecimal = value
        self.edit(StringIsHexadecimal=value)

    @OptionPayload.setter
    def OptionPayload(self, value):
        self._OptionPayload = value
        self.edit(OptionPayload=value)

    @OptionHexPayload.setter
    def OptionHexPayload(self, value):
        self._OptionHexPayload = value
        self.edit(OptionHexPayload=value)

    def _set_optionval_with_str(self, value):
        try:
            self._OptionVal = int(value)
        except ValueError:
            self._OptionVal = hex(int(value, 16))

    def _set_includemsg_with_str(self, value):
        seperate = value.find(':')
        self._IncludeMsg = swap_int_to_enum_flag(int(value[seperate+1:]), EnumDhcpv6ServerIncludeMsg)

    def _set_wildcards_with_str(self, value):
        self._Wildcards = (value == 'True')

    def _set_stringishexadecimal_with_str(self, value):
        self._StringIsHexadecimal = (value == 'True')

    def _set_optionpayload_with_str(self, value):
        self._OptionPayload = value

    def _set_optionhexpayload_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OptionHexPayload = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OptionHexPayload.append(int(str_value))
            except ValueError:
                self._OptionHexPayload.append(hex(int(str_value, 16)))

