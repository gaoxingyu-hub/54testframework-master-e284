"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv2TeLinkConfig(ROMObject):
    def __init__(self, EnableLocalIp=None, LocalIp=None, EnableRemoteIp=None, RemoteIp=None, EnableGroup=None, Group=None, EnableMaxBandwidth=None, MaximumBandwidth=None, EnableReservedBandwidth=None, ReservableBandwidth=None, EnableUnreservedBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
        self._EnableLocalIp = EnableLocalIp  # Enable Local IP
        self._LocalIp = LocalIp  # Local IP
        self._EnableRemoteIp = EnableRemoteIp  # Enable Remote IP
        self._RemoteIp = RemoteIp  # Remote IP
        self._EnableGroup = EnableGroup  # Enable Group 
        self._Group = Group  # Group (Color)
        self._EnableMaxBandwidth = EnableMaxBandwidth  # Enable Max Bandwidth
        self._MaximumBandwidth = MaximumBandwidth  # Maximum Bandwidth
        self._EnableReservedBandwidth = EnableReservedBandwidth  # Enable Reserved Bandwidth
        self._ReservableBandwidth = ReservableBandwidth  # Reservable Bandwidth
        self._EnableUnreservedBandwidth = EnableUnreservedBandwidth  # Enable Unreserved Bandwidth (Priority 0-7)
        self._UnreservedBandwidth0 = UnreservedBandwidth0  # Unreserved Bandwidth Priority 0
        self._UnreservedBandwidth1 = UnreservedBandwidth1  # Unreserved Bandwidth Priority 1
        self._UnreservedBandwidth2 = UnreservedBandwidth2  # Unreserved Bandwidth Priority 2
        self._UnreservedBandwidth3 = UnreservedBandwidth3  # Unreserved Bandwidth Priority 3
        self._UnreservedBandwidth4 = UnreservedBandwidth4  # Unreserved Bandwidth Priority 4
        self._UnreservedBandwidth5 = UnreservedBandwidth5  # Unreserved Bandwidth Priority 5
        self._UnreservedBandwidth6 = UnreservedBandwidth6  # Unreserved Bandwidth Priority 6
        self._UnreservedBandwidth7 = UnreservedBandwidth7  # Unreserved Bandwidth Priority 7

        properties = kwargs.copy()
        if EnableLocalIp is not None:
            properties['EnableLocalIp'] = EnableLocalIp
        if LocalIp is not None:
            properties['LocalIp'] = LocalIp
        if EnableRemoteIp is not None:
            properties['EnableRemoteIp'] = EnableRemoteIp
        if RemoteIp is not None:
            properties['RemoteIp'] = RemoteIp
        if EnableGroup is not None:
            properties['EnableGroup'] = EnableGroup
        if Group is not None:
            properties['Group'] = Group
        if EnableMaxBandwidth is not None:
            properties['EnableMaxBandwidth'] = EnableMaxBandwidth
        if MaximumBandwidth is not None:
            properties['MaximumBandwidth'] = MaximumBandwidth
        if EnableReservedBandwidth is not None:
            properties['EnableReservedBandwidth'] = EnableReservedBandwidth
        if ReservableBandwidth is not None:
            properties['ReservableBandwidth'] = ReservableBandwidth
        if EnableUnreservedBandwidth is not None:
            properties['EnableUnreservedBandwidth'] = EnableUnreservedBandwidth
        if UnreservedBandwidth0 is not None:
            properties['UnreservedBandwidth0'] = UnreservedBandwidth0
        if UnreservedBandwidth1 is not None:
            properties['UnreservedBandwidth1'] = UnreservedBandwidth1
        if UnreservedBandwidth2 is not None:
            properties['UnreservedBandwidth2'] = UnreservedBandwidth2
        if UnreservedBandwidth3 is not None:
            properties['UnreservedBandwidth3'] = UnreservedBandwidth3
        if UnreservedBandwidth4 is not None:
            properties['UnreservedBandwidth4'] = UnreservedBandwidth4
        if UnreservedBandwidth5 is not None:
            properties['UnreservedBandwidth5'] = UnreservedBandwidth5
        if UnreservedBandwidth6 is not None:
            properties['UnreservedBandwidth6'] = UnreservedBandwidth6
        if UnreservedBandwidth7 is not None:
            properties['UnreservedBandwidth7'] = UnreservedBandwidth7

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2TeLinkConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableLocalIp=None, LocalIp=None, EnableRemoteIp=None, RemoteIp=None, EnableGroup=None, Group=None, EnableMaxBandwidth=None, MaximumBandwidth=None, EnableReservedBandwidth=None, ReservableBandwidth=None, EnableUnreservedBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
        properties = kwargs.copy()
        if EnableLocalIp is not None:
            self._EnableLocalIp = EnableLocalIp
            properties['EnableLocalIp'] = EnableLocalIp
        if LocalIp is not None:
            self._LocalIp = LocalIp
            properties['LocalIp'] = LocalIp
        if EnableRemoteIp is not None:
            self._EnableRemoteIp = EnableRemoteIp
            properties['EnableRemoteIp'] = EnableRemoteIp
        if RemoteIp is not None:
            self._RemoteIp = RemoteIp
            properties['RemoteIp'] = RemoteIp
        if EnableGroup is not None:
            self._EnableGroup = EnableGroup
            properties['EnableGroup'] = EnableGroup
        if Group is not None:
            self._Group = Group
            properties['Group'] = Group
        if EnableMaxBandwidth is not None:
            self._EnableMaxBandwidth = EnableMaxBandwidth
            properties['EnableMaxBandwidth'] = EnableMaxBandwidth
        if MaximumBandwidth is not None:
            self._MaximumBandwidth = MaximumBandwidth
            properties['MaximumBandwidth'] = MaximumBandwidth
        if EnableReservedBandwidth is not None:
            self._EnableReservedBandwidth = EnableReservedBandwidth
            properties['EnableReservedBandwidth'] = EnableReservedBandwidth
        if ReservableBandwidth is not None:
            self._ReservableBandwidth = ReservableBandwidth
            properties['ReservableBandwidth'] = ReservableBandwidth
        if EnableUnreservedBandwidth is not None:
            self._EnableUnreservedBandwidth = EnableUnreservedBandwidth
            properties['EnableUnreservedBandwidth'] = EnableUnreservedBandwidth
        if UnreservedBandwidth0 is not None:
            self._UnreservedBandwidth0 = UnreservedBandwidth0
            properties['UnreservedBandwidth0'] = UnreservedBandwidth0
        if UnreservedBandwidth1 is not None:
            self._UnreservedBandwidth1 = UnreservedBandwidth1
            properties['UnreservedBandwidth1'] = UnreservedBandwidth1
        if UnreservedBandwidth2 is not None:
            self._UnreservedBandwidth2 = UnreservedBandwidth2
            properties['UnreservedBandwidth2'] = UnreservedBandwidth2
        if UnreservedBandwidth3 is not None:
            self._UnreservedBandwidth3 = UnreservedBandwidth3
            properties['UnreservedBandwidth3'] = UnreservedBandwidth3
        if UnreservedBandwidth4 is not None:
            self._UnreservedBandwidth4 = UnreservedBandwidth4
            properties['UnreservedBandwidth4'] = UnreservedBandwidth4
        if UnreservedBandwidth5 is not None:
            self._UnreservedBandwidth5 = UnreservedBandwidth5
            properties['UnreservedBandwidth5'] = UnreservedBandwidth5
        if UnreservedBandwidth6 is not None:
            self._UnreservedBandwidth6 = UnreservedBandwidth6
            properties['UnreservedBandwidth6'] = UnreservedBandwidth6
        if UnreservedBandwidth7 is not None:
            self._UnreservedBandwidth7 = UnreservedBandwidth7
            properties['UnreservedBandwidth7'] = UnreservedBandwidth7

        super(Ospfv2TeLinkConfig, self).edit(**properties)

    @property
    def EnableLocalIp(self):
        """
        get the value of property _EnableLocalIp
        """
        if self.force_auto_sync:
            self.get('EnableLocalIp')
        return self._EnableLocalIp

    @property
    def LocalIp(self):
        """
        get the value of property _LocalIp
        """
        if self.force_auto_sync:
            self.get('LocalIp')
        return self._LocalIp

    @property
    def EnableRemoteIp(self):
        """
        get the value of property _EnableRemoteIp
        """
        if self.force_auto_sync:
            self.get('EnableRemoteIp')
        return self._EnableRemoteIp

    @property
    def RemoteIp(self):
        """
        get the value of property _RemoteIp
        """
        if self.force_auto_sync:
            self.get('RemoteIp')
        return self._RemoteIp

    @property
    def EnableGroup(self):
        """
        get the value of property _EnableGroup
        """
        if self.force_auto_sync:
            self.get('EnableGroup')
        return self._EnableGroup

    @property
    def Group(self):
        """
        get the value of property _Group
        """
        if self.force_auto_sync:
            self.get('Group')
        return self._Group

    @property
    def EnableMaxBandwidth(self):
        """
        get the value of property _EnableMaxBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableMaxBandwidth')
        return self._EnableMaxBandwidth

    @property
    def MaximumBandwidth(self):
        """
        get the value of property _MaximumBandwidth
        """
        if self.force_auto_sync:
            self.get('MaximumBandwidth')
        return self._MaximumBandwidth

    @property
    def EnableReservedBandwidth(self):
        """
        get the value of property _EnableReservedBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableReservedBandwidth')
        return self._EnableReservedBandwidth

    @property
    def ReservableBandwidth(self):
        """
        get the value of property _ReservableBandwidth
        """
        if self.force_auto_sync:
            self.get('ReservableBandwidth')
        return self._ReservableBandwidth

    @property
    def EnableUnreservedBandwidth(self):
        """
        get the value of property _EnableUnreservedBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableUnreservedBandwidth')
        return self._EnableUnreservedBandwidth

    @property
    def UnreservedBandwidth0(self):
        """
        get the value of property _UnreservedBandwidth0
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth0')
        return self._UnreservedBandwidth0

    @property
    def UnreservedBandwidth1(self):
        """
        get the value of property _UnreservedBandwidth1
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth1')
        return self._UnreservedBandwidth1

    @property
    def UnreservedBandwidth2(self):
        """
        get the value of property _UnreservedBandwidth2
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth2')
        return self._UnreservedBandwidth2

    @property
    def UnreservedBandwidth3(self):
        """
        get the value of property _UnreservedBandwidth3
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth3')
        return self._UnreservedBandwidth3

    @property
    def UnreservedBandwidth4(self):
        """
        get the value of property _UnreservedBandwidth4
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth4')
        return self._UnreservedBandwidth4

    @property
    def UnreservedBandwidth5(self):
        """
        get the value of property _UnreservedBandwidth5
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth5')
        return self._UnreservedBandwidth5

    @property
    def UnreservedBandwidth6(self):
        """
        get the value of property _UnreservedBandwidth6
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth6')
        return self._UnreservedBandwidth6

    @property
    def UnreservedBandwidth7(self):
        """
        get the value of property _UnreservedBandwidth7
        """
        if self.force_auto_sync:
            self.get('UnreservedBandwidth7')
        return self._UnreservedBandwidth7

    @EnableLocalIp.setter
    def EnableLocalIp(self, value):
        self._EnableLocalIp = value
        self.edit(EnableLocalIp=value)

    @LocalIp.setter
    def LocalIp(self, value):
        self._LocalIp = value
        self.edit(LocalIp=value)

    @EnableRemoteIp.setter
    def EnableRemoteIp(self, value):
        self._EnableRemoteIp = value
        self.edit(EnableRemoteIp=value)

    @RemoteIp.setter
    def RemoteIp(self, value):
        self._RemoteIp = value
        self.edit(RemoteIp=value)

    @EnableGroup.setter
    def EnableGroup(self, value):
        self._EnableGroup = value
        self.edit(EnableGroup=value)

    @Group.setter
    def Group(self, value):
        self._Group = value
        self.edit(Group=value)

    @EnableMaxBandwidth.setter
    def EnableMaxBandwidth(self, value):
        self._EnableMaxBandwidth = value
        self.edit(EnableMaxBandwidth=value)

    @MaximumBandwidth.setter
    def MaximumBandwidth(self, value):
        self._MaximumBandwidth = value
        self.edit(MaximumBandwidth=value)

    @EnableReservedBandwidth.setter
    def EnableReservedBandwidth(self, value):
        self._EnableReservedBandwidth = value
        self.edit(EnableReservedBandwidth=value)

    @ReservableBandwidth.setter
    def ReservableBandwidth(self, value):
        self._ReservableBandwidth = value
        self.edit(ReservableBandwidth=value)

    @EnableUnreservedBandwidth.setter
    def EnableUnreservedBandwidth(self, value):
        self._EnableUnreservedBandwidth = value
        self.edit(EnableUnreservedBandwidth=value)

    @UnreservedBandwidth0.setter
    def UnreservedBandwidth0(self, value):
        self._UnreservedBandwidth0 = value
        self.edit(UnreservedBandwidth0=value)

    @UnreservedBandwidth1.setter
    def UnreservedBandwidth1(self, value):
        self._UnreservedBandwidth1 = value
        self.edit(UnreservedBandwidth1=value)

    @UnreservedBandwidth2.setter
    def UnreservedBandwidth2(self, value):
        self._UnreservedBandwidth2 = value
        self.edit(UnreservedBandwidth2=value)

    @UnreservedBandwidth3.setter
    def UnreservedBandwidth3(self, value):
        self._UnreservedBandwidth3 = value
        self.edit(UnreservedBandwidth3=value)

    @UnreservedBandwidth4.setter
    def UnreservedBandwidth4(self, value):
        self._UnreservedBandwidth4 = value
        self.edit(UnreservedBandwidth4=value)

    @UnreservedBandwidth5.setter
    def UnreservedBandwidth5(self, value):
        self._UnreservedBandwidth5 = value
        self.edit(UnreservedBandwidth5=value)

    @UnreservedBandwidth6.setter
    def UnreservedBandwidth6(self, value):
        self._UnreservedBandwidth6 = value
        self.edit(UnreservedBandwidth6=value)

    @UnreservedBandwidth7.setter
    def UnreservedBandwidth7(self, value):
        self._UnreservedBandwidth7 = value
        self.edit(UnreservedBandwidth7=value)

    def _set_enablelocalip_with_str(self, value):
        self._EnableLocalIp = (value == 'True')

    def _set_localip_with_str(self, value):
        self._LocalIp = value

    def _set_enableremoteip_with_str(self, value):
        self._EnableRemoteIp = (value == 'True')

    def _set_remoteip_with_str(self, value):
        self._RemoteIp = value

    def _set_enablegroup_with_str(self, value):
        self._EnableGroup = (value == 'True')

    def _set_group_with_str(self, value):
        try:
            self._Group = int(value)
        except ValueError:
            self._Group = hex(int(value, 16))

    def _set_enablemaxbandwidth_with_str(self, value):
        self._EnableMaxBandwidth = (value == 'True')

    def _set_maximumbandwidth_with_str(self, value):
        try:
            self._MaximumBandwidth = int(value)
        except ValueError:
            self._MaximumBandwidth = hex(int(value, 16))

    def _set_enablereservedbandwidth_with_str(self, value):
        self._EnableReservedBandwidth = (value == 'True')

    def _set_reservablebandwidth_with_str(self, value):
        try:
            self._ReservableBandwidth = int(value)
        except ValueError:
            self._ReservableBandwidth = hex(int(value, 16))

    def _set_enableunreservedbandwidth_with_str(self, value):
        self._EnableUnreservedBandwidth = (value == 'True')

    def _set_unreservedbandwidth0_with_str(self, value):
        try:
            self._UnreservedBandwidth0 = int(value)
        except ValueError:
            self._UnreservedBandwidth0 = hex(int(value, 16))

    def _set_unreservedbandwidth1_with_str(self, value):
        try:
            self._UnreservedBandwidth1 = int(value)
        except ValueError:
            self._UnreservedBandwidth1 = hex(int(value, 16))

    def _set_unreservedbandwidth2_with_str(self, value):
        try:
            self._UnreservedBandwidth2 = int(value)
        except ValueError:
            self._UnreservedBandwidth2 = hex(int(value, 16))

    def _set_unreservedbandwidth3_with_str(self, value):
        try:
            self._UnreservedBandwidth3 = int(value)
        except ValueError:
            self._UnreservedBandwidth3 = hex(int(value, 16))

    def _set_unreservedbandwidth4_with_str(self, value):
        try:
            self._UnreservedBandwidth4 = int(value)
        except ValueError:
            self._UnreservedBandwidth4 = hex(int(value, 16))

    def _set_unreservedbandwidth5_with_str(self, value):
        try:
            self._UnreservedBandwidth5 = int(value)
        except ValueError:
            self._UnreservedBandwidth5 = hex(int(value, 16))

    def _set_unreservedbandwidth6_with_str(self, value):
        try:
            self._UnreservedBandwidth6 = int(value)
        except ValueError:
            self._UnreservedBandwidth6 = hex(int(value, 16))

    def _set_unreservedbandwidth7_with_str(self, value):
        try:
            self._UnreservedBandwidth7 = int(value)
        except ValueError:
            self._UnreservedBandwidth7 = hex(int(value, 16))

