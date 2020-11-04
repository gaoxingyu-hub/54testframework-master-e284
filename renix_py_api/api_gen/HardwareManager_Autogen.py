"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HardwareManager(ROMObject):
    def __init__(self, DisplayIpInReservation=None, **kwargs):
        self._DisplayIpInReservation = DisplayIpInReservation  # Display IP in Reservation Information

        properties = kwargs.copy()
        if DisplayIpInReservation is not None:
            properties['DisplayIpInReservation'] = DisplayIpInReservation

        # call base class function, and it will send message to renix server to create a class.
        super(HardwareManager, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DisplayIpInReservation=None, **kwargs):
        properties = kwargs.copy()
        if DisplayIpInReservation is not None:
            self._DisplayIpInReservation = DisplayIpInReservation
            properties['DisplayIpInReservation'] = DisplayIpInReservation

        super(HardwareManager, self).edit(**properties)

    @property
    def DisplayIpInReservation(self):
        """
        get the value of property _DisplayIpInReservation
        """
        if self.force_auto_sync:
            self.get('DisplayIpInReservation')
        return self._DisplayIpInReservation

    @DisplayIpInReservation.setter
    def DisplayIpInReservation(self, value):
        self._DisplayIpInReservation = value
        self.edit(DisplayIpInReservation=value)

    def _set_displayipinreservation_with_str(self, value):
        self._DisplayIpInReservation = (value == 'True')

