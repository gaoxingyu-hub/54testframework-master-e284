"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillInterestedVLANsSubTLVConfig(ROMObject):
    def __init__(self, AssociateNickname=None, RootBridgeIDs=None, M4=None, M6=None, StartVLANID=None, EndVLANID=None, AppointedForwarderStatusLostCount=None, **kwargs):
        self._AssociateNickname = AssociateNickname  # Associate Nickname
        self._RootBridgeIDs = RootBridgeIDs  # Root Bridge IDs
        self._M4 = M4  # M4
        self._M6 = M6  # M6
        self._StartVLANID = StartVLANID  # Start VLAN ID
        self._EndVLANID = EndVLANID  # End VLAN ID
        self._AppointedForwarderStatusLostCount = AppointedForwarderStatusLostCount  # Appointed Forwarder Status Lost Count

        properties = kwargs.copy()
        if AssociateNickname is not None:
            properties['AssociateNickname'] = AssociateNickname
        if RootBridgeIDs is not None:
            properties['RootBridgeIDs'] = RootBridgeIDs
        if M4 is not None:
            properties['M4'] = M4
        if M6 is not None:
            properties['M6'] = M6
        if StartVLANID is not None:
            properties['StartVLANID'] = StartVLANID
        if EndVLANID is not None:
            properties['EndVLANID'] = EndVLANID
        if AppointedForwarderStatusLostCount is not None:
            properties['AppointedForwarderStatusLostCount'] = AppointedForwarderStatusLostCount

        # call base class function, and it will send message to renix server to create a class.
        super(TrillInterestedVLANsSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AssociateNickname=None, RootBridgeIDs=None, M4=None, M6=None, StartVLANID=None, EndVLANID=None, AppointedForwarderStatusLostCount=None, **kwargs):
        properties = kwargs.copy()
        if AssociateNickname is not None:
            self._AssociateNickname = AssociateNickname
            properties['AssociateNickname'] = AssociateNickname
        if RootBridgeIDs is not None:
            self._RootBridgeIDs = RootBridgeIDs
            properties['RootBridgeIDs'] = RootBridgeIDs
        if M4 is not None:
            self._M4 = M4
            properties['M4'] = M4
        if M6 is not None:
            self._M6 = M6
            properties['M6'] = M6
        if StartVLANID is not None:
            self._StartVLANID = StartVLANID
            properties['StartVLANID'] = StartVLANID
        if EndVLANID is not None:
            self._EndVLANID = EndVLANID
            properties['EndVLANID'] = EndVLANID
        if AppointedForwarderStatusLostCount is not None:
            self._AppointedForwarderStatusLostCount = AppointedForwarderStatusLostCount
            properties['AppointedForwarderStatusLostCount'] = AppointedForwarderStatusLostCount

        super(TrillInterestedVLANsSubTLVConfig, self).edit(**properties)

    @property
    def AssociateNickname(self):
        """
        get the value of property _AssociateNickname
        """
        if self.force_auto_sync:
            self.get('AssociateNickname')
        return self._AssociateNickname

    @property
    def RootBridgeIDs(self):
        """
        get the value of property _RootBridgeIDs
        """
        if self.force_auto_sync:
            self.get('RootBridgeIDs')
        return self._RootBridgeIDs

    @property
    def M4(self):
        """
        get the value of property _M4
        """
        if self.force_auto_sync:
            self.get('M4')
        return self._M4

    @property
    def M6(self):
        """
        get the value of property _M6
        """
        if self.force_auto_sync:
            self.get('M6')
        return self._M6

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

    @property
    def AppointedForwarderStatusLostCount(self):
        """
        get the value of property _AppointedForwarderStatusLostCount
        """
        if self.force_auto_sync:
            self.get('AppointedForwarderStatusLostCount')
        return self._AppointedForwarderStatusLostCount

    @AssociateNickname.setter
    def AssociateNickname(self, value):
        self._AssociateNickname = value
        self.edit(AssociateNickname=value)

    @RootBridgeIDs.setter
    def RootBridgeIDs(self, value):
        self._RootBridgeIDs = value
        self.edit(RootBridgeIDs=value)

    @M4.setter
    def M4(self, value):
        self._M4 = value
        self.edit(M4=value)

    @M6.setter
    def M6(self, value):
        self._M6 = value
        self.edit(M6=value)

    @StartVLANID.setter
    def StartVLANID(self, value):
        self._StartVLANID = value
        self.edit(StartVLANID=value)

    @EndVLANID.setter
    def EndVLANID(self, value):
        self._EndVLANID = value
        self.edit(EndVLANID=value)

    @AppointedForwarderStatusLostCount.setter
    def AppointedForwarderStatusLostCount(self, value):
        self._AppointedForwarderStatusLostCount = value
        self.edit(AppointedForwarderStatusLostCount=value)

    def _set_associatenickname_with_str(self, value):
        try:
            self._AssociateNickname = int(value)
        except ValueError:
            self._AssociateNickname = hex(int(value, 16))

    def _set_rootbridgeids_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RootBridgeIDs = tmp_value.split()

    def _set_m4_with_str(self, value):
        self._M4 = (value == 'True')

    def _set_m6_with_str(self, value):
        self._M6 = (value == 'True')

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

    def _set_appointedforwarderstatuslostcount_with_str(self, value):
        try:
            self._AppointedForwarderStatusLostCount = int(value)
        except ValueError:
            self._AppointedForwarderStatusLostCount = hex(int(value, 16))

