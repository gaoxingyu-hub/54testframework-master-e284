"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PlCommander(ROMObject):
    def __init__(self, Reset=None, ResetDone=None, UpdateSmartScriptor=None, **kwargs):
        self._Reset = Reset  # Reset PL
        self._ResetDone = ResetDone  # Reset Done
        self._UpdateSmartScriptor = UpdateSmartScriptor  # Update Smart Scriptor

        properties = kwargs.copy()
        if Reset is not None:
            properties['Reset'] = Reset
        if ResetDone is not None:
            properties['ResetDone'] = ResetDone
        if UpdateSmartScriptor is not None:
            properties['UpdateSmartScriptor'] = UpdateSmartScriptor

        # call base class function, and it will send message to renix server to create a class.
        super(PlCommander, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Reset=None, ResetDone=None, UpdateSmartScriptor=None, **kwargs):
        properties = kwargs.copy()
        if Reset is not None:
            self._Reset = Reset
            properties['Reset'] = Reset
        if ResetDone is not None:
            self._ResetDone = ResetDone
            properties['ResetDone'] = ResetDone
        if UpdateSmartScriptor is not None:
            self._UpdateSmartScriptor = UpdateSmartScriptor
            properties['UpdateSmartScriptor'] = UpdateSmartScriptor

        super(PlCommander, self).edit(**properties)

    @property
    def Reset(self):
        """
        get the value of property _Reset
        """
        if self.force_auto_sync:
            self.get('Reset')
        return self._Reset

    @property
    def ResetDone(self):
        """
        get the value of property _ResetDone
        """
        if self.force_auto_sync:
            self.get('ResetDone')
        return self._ResetDone

    @property
    def UpdateSmartScriptor(self):
        """
        get the value of property _UpdateSmartScriptor
        """
        if self.force_auto_sync:
            self.get('UpdateSmartScriptor')
        return self._UpdateSmartScriptor

    @Reset.setter
    def Reset(self, value):
        self._Reset = value
        self.edit(Reset=value)

    @ResetDone.setter
    def ResetDone(self, value):
        self._ResetDone = value
        self.edit(ResetDone=value)

    @UpdateSmartScriptor.setter
    def UpdateSmartScriptor(self, value):
        self._UpdateSmartScriptor = value
        self.edit(UpdateSmartScriptor=value)

    def _set_reset_with_str(self, value):
        self._Reset = (value == 'True')

    def _set_resetdone_with_str(self, value):
        self._ResetDone = (value == 'True')

    def _set_updatesmartscriptor_with_str(self, value):
        self._UpdateSmartScriptor = (value == 'True')

