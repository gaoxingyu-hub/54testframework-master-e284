"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetCardModeCommand(ROMCommand):
    def __init__(self, CardList=None, **kwargs):
        self._CardList = CardList  # Card Handles
        self._Mode = None  # Card Mode, not editable

        properties = kwargs.copy()
        if CardList is not None:
            properties['CardList'] = CardList

        # call base class function, and it will send message to renix server to create a class.
        super(GetCardModeCommand, self).__init__(**properties)

    @property
    def CardList(self):
        """
        get the value of property _CardList
        """
        return self._CardList

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        return self._Mode

    @CardList.setter
    def CardList(self, value):
        self._CardList = value

    def _set_cardlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CardList = tmp_value.split()

    def _set_mode_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Mode = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = str_value[seperate+1:]
            enum_value = swap_int_to_enum_flag(int(enum_value), EnumCardMode)
            self._Mode.append(enum_value)

    def _set_output_property(self, value):
        self._set_mode_with_str(value)

