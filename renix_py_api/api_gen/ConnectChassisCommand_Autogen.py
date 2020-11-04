"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ConnectChassisCommand(ROMCommand):
    def __init__(self, HostnameList=None, ChassisList=None, **kwargs):
        self._HostnameList = HostnameList  # Chassis Hostnames
        self._ChassisList = ChassisList  # Chassis Handles
        self._ConnectedList = None  # Successfully Connected Chassis Handles, not editable

        properties = kwargs.copy()
        if HostnameList is not None:
            properties['HostnameList'] = HostnameList
        if ChassisList is not None:
            properties['ChassisList'] = ChassisList

        # call base class function, and it will send message to renix server to create a class.
        super(ConnectChassisCommand, self).__init__(**properties)

    @property
    def HostnameList(self):
        """
        get the value of property _HostnameList
        """
        return self._HostnameList

    @property
    def ChassisList(self):
        """
        get the value of property _ChassisList
        """
        return self._ChassisList

    @property
    def ConnectedList(self):
        """
        get the value of property _ConnectedList
        """
        return self._ConnectedList

    @HostnameList.setter
    def HostnameList(self, value):
        self._HostnameList = value

    @ChassisList.setter
    def ChassisList(self, value):
        self._ChassisList = value

    def _set_hostnamelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HostnameList = tmp_value.split()

    def _set_chassislist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChassisList = tmp_value.split()

    def _set_connectedlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ConnectedList = tmp_value.split()

    def _set_output_property(self, value):
        self._set_connectedlist_with_str(value)

