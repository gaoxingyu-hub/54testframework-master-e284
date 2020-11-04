"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillAppointmentInformationConfig(ROMObject):
    def __init__(self, AppointeeNickname=None, StartVLANID=None, EndVLANID=None, **kwargs):
        self._AppointeeNickname = AppointeeNickname  # Appointee Nickname
        self._StartVLANID = StartVLANID  # Start VLAN ID
        self._EndVLANID = EndVLANID  # End VLAN ID

        properties = kwargs.copy()
        if AppointeeNickname is not None:
            properties['AppointeeNickname'] = AppointeeNickname
        if StartVLANID is not None:
            properties['StartVLANID'] = StartVLANID
        if EndVLANID is not None:
            properties['EndVLANID'] = EndVLANID

        # call base class function, and it will send message to renix server to create a class.
        super(TrillAppointmentInformationConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AppointeeNickname=None, StartVLANID=None, EndVLANID=None, **kwargs):
        properties = kwargs.copy()
        if AppointeeNickname is not None:
            self._AppointeeNickname = AppointeeNickname
            properties['AppointeeNickname'] = AppointeeNickname
        if StartVLANID is not None:
            self._StartVLANID = StartVLANID
            properties['StartVLANID'] = StartVLANID
        if EndVLANID is not None:
            self._EndVLANID = EndVLANID
            properties['EndVLANID'] = EndVLANID

        super(TrillAppointmentInformationConfig, self).edit(**properties)

    @property
    def AppointeeNickname(self):
        """
        get the value of property _AppointeeNickname
        """
        if self.force_auto_sync:
            self.get('AppointeeNickname')
        return self._AppointeeNickname

    @property
    def StartVLANID(self):
        """
        get the value of property _StartVLANID
        """
        if self.force_auto_sync:
            self.get('StartVLANID')
        return self._StartVLANID

    @property
    def EndVLANID(self):
        """
        get the value of property _EndVLANID
        """
        if self.force_auto_sync:
            self.get('EndVLANID')
        return self._EndVLANID

    @AppointeeNickname.setter
    def AppointeeNickname(self, value):
        self._AppointeeNickname = value
        self.edit(AppointeeNickname=value)

    @StartVLANID.setter
    def StartVLANID(self, value):
        self._StartVLANID = value
        self.edit(StartVLANID=value)

    @EndVLANID.setter
    def EndVLANID(self, value):
        self._EndVLANID = value
        self.edit(EndVLANID=value)

    def _set_appointeenickname_with_str(self, value):
        try:
            self._AppointeeNickname = int(value)
        except ValueError:
            self._AppointeeNickname = hex(int(value, 16))

    def _set_startvlanid_with_str(self, value):
        try:
            self._StartVLANID = int(value)
        except ValueError:
            self._StartVLANID = hex(int(value, 16))

    def _set_endvlanid_with_str(self, value):
        try:
            self._EndVLANID = int(value)
        except ValueError:
            self._EndVLANID = hex(int(value, 16))

