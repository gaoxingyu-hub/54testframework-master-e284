"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ReservePortCommand(ROMCommand):
    def __init__(self, LocationList=None, WaitForPortStatusUp=None, **kwargs):
        self._LocationList = LocationList  # Port Location List
        self._OnlinePorts = None  # Port Handles, not editable
        self._WaitForPortStatusUp = WaitForPortStatusUp  # Wait for the port status to be up

        properties = kwargs.copy()
        if LocationList is not None:
            properties['LocationList'] = LocationList
        if WaitForPortStatusUp is not None:
            properties['WaitForPortStatusUp'] = WaitForPortStatusUp

        # call base class function, and it will send message to renix server to create a class.
        super(ReservePortCommand, self).__init__(**properties)

    @property
    def LocationList(self):
        """
        get the value of property _LocationList
        """
        return self._LocationList

    @property
    def OnlinePorts(self):
        """
        get the value of property _OnlinePorts
        """
        return self._OnlinePorts

    @property
    def WaitForPortStatusUp(self):
        """
        get the value of property _WaitForPortStatusUp
        """
        return self._WaitForPortStatusUp

    @LocationList.setter
    def LocationList(self, value):
        self._LocationList = value

    @WaitForPortStatusUp.setter
    def WaitForPortStatusUp(self, value):
        self._WaitForPortStatusUp = value

    def _set_locationlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LocationList = tmp_value.split()

    def _set_onlineports_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OnlinePorts = tmp_value.split()

    def _set_waitforportstatusup_with_str(self, value):
        self._WaitForPortStatusUp = (value == 'True')

    def _set_output_property(self, value):
        self._set_onlineports_with_str(value)

