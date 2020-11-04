"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HardwareCard(ROMObject):
    def __init__(self, **kwargs):
        self._SlotNumber = 1  # Slot Number, not editable
        self._PartNumber = ''  # Part Number, not editable
        self._SerialNumber = ''  # Serial Number, not editable
        self._State = EnumCardState.CARD_DOWN  # Card State, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(HardwareCard, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(HardwareCard, self).edit(**properties)

    @property
    def SlotNumber(self):
        """
        get the value of property _SlotNumber
        """
        if self.force_auto_sync:
            self.get('SlotNumber')
        return self._SlotNumber

    @property
    def PartNumber(self):
        """
        get the value of property _PartNumber
        """
        if self.force_auto_sync:
            self.get('PartNumber')
        return self._PartNumber

    @property
    def SerialNumber(self):
        """
        get the value of property _SerialNumber
        """
        if self.force_auto_sync:
            self.get('SerialNumber')
        return self._SerialNumber

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    def _set_slotnumber_with_str(self, value):
        try:
            self._SlotNumber = int(value)
        except ValueError:
            self._SlotNumber = hex(int(value, 16))

    def _set_partnumber_with_str(self, value):
        self._PartNumber = value

    def _set_serialnumber_with_str(self, value):
        self._SerialNumber = value

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumCardState.%s' % value[:seperate])

