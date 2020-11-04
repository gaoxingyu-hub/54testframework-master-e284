"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SwitchCardModeCommand(ROMCommand):
    def __init__(self, CardList=None, Mode=None, **kwargs):
        self._CardList = CardList  # Card Handles
        self._Mode = swap_int_to_enum_flag(Mode, EnumCardMode)  # Card Mode
        self._Results = None  # Results, not editable

        properties = kwargs.copy()
        if CardList is not None:
            properties['CardList'] = CardList
        if Mode is not None:
            if isinstance(Mode, Flag):
                properties['Mode'] = Mode.value
            else:
                properties['Mode'] = Mode

        # call base class function, and it will send message to renix server to create a class.
        super(SwitchCardModeCommand, self).__init__(**properties)

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

    @property
    def Results(self):
        """
        get the value of property _Results
        """
        return self._Results

    @CardList.setter
    def CardList(self, value):
        self._CardList = value

    @Mode.setter
    def Mode(self, value):
        self._Mode = value

    def _set_cardlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._CardList = tmp_value.split()

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        self._Mode = swap_int_to_enum_flag(int(value[seperate+1:]), EnumCardMode)

    def _set_results_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Results = tmp_value.split()

    def _set_output_property(self, value):
        self._set_results_with_str(value)

