"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisTEConfig(ROMObject):
    def __init__(self, EnableInterfaceIp=None, InterfaceIp=None, EnableNeighborIp=None, NeighborIp=None, EnableInterfaceIpv6=None, InterfaceIpv6=None, EnableNeighborIpv6=None, NeighborIpv6=None, EnableTeGroup=None, TeGroup=None, EnableMaxBandwidth=None, MaximunLink=None, EnableResBandwidth=None, MaximumReservableLink=None, EnableUnresBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
        self._EnableInterfaceIp = EnableInterfaceIp  # Enable Interface IP
        self._InterfaceIp = InterfaceIp  # Interface IP
        self._EnableNeighborIp = EnableNeighborIp  # Enable Neighbor IP
        self._NeighborIp = NeighborIp  # Neighbor IP
        self._EnableInterfaceIpv6 = EnableInterfaceIpv6  # Enable Interface IPv6
        self._InterfaceIpv6 = InterfaceIpv6  # Interface IPv6
        self._EnableNeighborIpv6 = EnableNeighborIpv6  # Enable Neighbor IPv6
        self._NeighborIpv6 = NeighborIpv6  # Neighbor IPv6
        self._EnableTeGroup = EnableTeGroup  # Enable TE Group
        self._TeGroup = TeGroup  # TE Group
        self._EnableMaxBandwidth = EnableMaxBandwidth  # Enable Max Bandwidth
        self._MaximunLink = MaximunLink  # Maximum Link (bytes/sec)
        self._EnableResBandwidth = EnableResBandwidth  # Enable Reserved Bandwidth
        self._MaximumReservableLink = MaximumReservableLink  # Maximum Reservable Link (bytes/sec)
        self._EnableUnresBandwidth = EnableUnresBandwidth  # Enable Unreserved Bandwidth
        self._UnreservedBandwidth0 = UnreservedBandwidth0  # Unreserved Bandwidth Priority0 (bytes/sec)
        self._UnreservedBandwidth1 = UnreservedBandwidth1  # Unreserved Bandwidth Priority1 (bytes/sec)
        self._UnreservedBandwidth2 = UnreservedBandwidth2  # Unreserved Bandwidth Priority2 (bytes/sec)
        self._UnreservedBandwidth3 = UnreservedBandwidth3  # Unreserved Bandwidth Priority3 (bytes/sec)
        self._UnreservedBandwidth4 = UnreservedBandwidth4  # Unreserved Bandwidth Priority4 (bytes/sec)
        self._UnreservedBandwidth5 = UnreservedBandwidth5  # Unreserved Bandwidth Priority5 (bytes/sec)
        self._UnreservedBandwidth6 = UnreservedBandwidth6  # Unreserved Bandwidth Priority6 (bytes/sec)
        self._UnreservedBandwidth7 = UnreservedBandwidth7  # Unreserved Bandwidth Priority7 (bytes/sec)

        properties = kwargs.copy()
        if EnableInterfaceIp is not None:
            properties['EnableInterfaceIp'] = EnableInterfaceIp
        if InterfaceIp is not None:
            properties['InterfaceIp'] = InterfaceIp
        if EnableNeighborIp is not None:
            properties['EnableNeighborIp'] = EnableNeighborIp
        if NeighborIp is not None:
            properties['NeighborIp'] = NeighborIp
        if EnableInterfaceIpv6 is not None:
            properties['EnableInterfaceIpv6'] = EnableInterfaceIpv6
        if InterfaceIpv6 is not None:
            properties['InterfaceIpv6'] = InterfaceIpv6
        if EnableNeighborIpv6 is not None:
            properties['EnableNeighborIpv6'] = EnableNeighborIpv6
        if NeighborIpv6 is not None:
            properties['NeighborIpv6'] = NeighborIpv6
        if EnableTeGroup is not None:
            properties['EnableTeGroup'] = EnableTeGroup
        if TeGroup is not None:
            properties['TeGroup'] = TeGroup
        if EnableMaxBandwidth is not None:
            properties['EnableMaxBandwidth'] = EnableMaxBandwidth
        if MaximunLink is not None:
            properties['MaximunLink'] = MaximunLink
        if EnableResBandwidth is not None:
            properties['EnableResBandwidth'] = EnableResBandwidth
        if MaximumReservableLink is not None:
            properties['MaximumReservableLink'] = MaximumReservableLink
        if EnableUnresBandwidth is not None:
            properties['EnableUnresBandwidth'] = EnableUnresBandwidth
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
        super(IsisTEConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableInterfaceIp=None, InterfaceIp=None, EnableNeighborIp=None, NeighborIp=None, EnableInterfaceIpv6=None, InterfaceIpv6=None, EnableNeighborIpv6=None, NeighborIpv6=None, EnableTeGroup=None, TeGroup=None, EnableMaxBandwidth=None, MaximunLink=None, EnableResBandwidth=None, MaximumReservableLink=None, EnableUnresBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
        properties = kwargs.copy()
        if EnableInterfaceIp is not None:
            self._EnableInterfaceIp = EnableInterfaceIp
            properties['EnableInterfaceIp'] = EnableInterfaceIp
        if InterfaceIp is not None:
            self._InterfaceIp = InterfaceIp
            properties['InterfaceIp'] = InterfaceIp
        if EnableNeighborIp is not None:
            self._EnableNeighborIp = EnableNeighborIp
            properties['EnableNeighborIp'] = EnableNeighborIp
        if NeighborIp is not None:
            self._NeighborIp = NeighborIp
            properties['NeighborIp'] = NeighborIp
        if EnableInterfaceIpv6 is not None:
            self._EnableInterfaceIpv6 = EnableInterfaceIpv6
            properties['EnableInterfaceIpv6'] = EnableInterfaceIpv6
        if InterfaceIpv6 is not None:
            self._InterfaceIpv6 = InterfaceIpv6
            properties['InterfaceIpv6'] = InterfaceIpv6
        if EnableNeighborIpv6 is not None:
            self._EnableNeighborIpv6 = EnableNeighborIpv6
            properties['EnableNeighborIpv6'] = EnableNeighborIpv6
        if NeighborIpv6 is not None:
            self._NeighborIpv6 = NeighborIpv6
            properties['NeighborIpv6'] = NeighborIpv6
        if EnableTeGroup is not None:
            self._EnableTeGroup = EnableTeGroup
            properties['EnableTeGroup'] = EnableTeGroup
        if TeGroup is not None:
            self._TeGroup = TeGroup
            properties['TeGroup'] = TeGroup
        if EnableMaxBandwidth is not None:
            self._EnableMaxBandwidth = EnableMaxBandwidth
            properties['EnableMaxBandwidth'] = EnableMaxBandwidth
        if MaximunLink is not None:
            self._MaximunLink = MaximunLink
            properties['MaximunLink'] = MaximunLink
        if EnableResBandwidth is not None:
            self._EnableResBandwidth = EnableResBandwidth
            properties['EnableResBandwidth'] = EnableResBandwidth
        if MaximumReservableLink is not None:
            self._MaximumReservableLink = MaximumReservableLink
            properties['MaximumReservableLink'] = MaximumReservableLink
        if EnableUnresBandwidth is not None:
            self._EnableUnresBandwidth = EnableUnresBandwidth
            properties['EnableUnresBandwidth'] = EnableUnresBandwidth
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

        super(IsisTEConfig, self).edit(**properties)

    @property
    def EnableInterfaceIp(self):
        """
        get the value of property _EnableInterfaceIp
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceIp')
        return self._EnableInterfaceIp

    @property
    def InterfaceIp(self):
        """
        get the value of property _InterfaceIp
        """
        if self.force_auto_sync:
            self.get('InterfaceIp')
        return self._InterfaceIp

    @property
    def EnableNeighborIp(self):
        """
        get the value of property _EnableNeighborIp
        """
        if self.force_auto_sync:
            self.get('EnableNeighborIp')
        return self._EnableNeighborIp

    @property
    def NeighborIp(self):
        """
        get the value of property _NeighborIp
        """
        if self.force_auto_sync:
            self.get('NeighborIp')
        return self._NeighborIp

    @property
    def EnableInterfaceIpv6(self):
        """
        get the value of property _EnableInterfaceIpv6
        """
        if self.force_auto_sync:
            self.get('EnableInterfaceIpv6')
        return self._EnableInterfaceIpv6

    @property
    def InterfaceIpv6(self):
        """
        get the value of property _InterfaceIpv6
        """
        if self.force_auto_sync:
            self.get('InterfaceIpv6')
        return self._InterfaceIpv6

    @property
    def EnableNeighborIpv6(self):
        """
        get the value of property _EnableNeighborIpv6
        """
        if self.force_auto_sync:
            self.get('EnableNeighborIpv6')
        return self._EnableNeighborIpv6

    @property
    def NeighborIpv6(self):
        """
        get the value of property _NeighborIpv6
        """
        if self.force_auto_sync:
            self.get('NeighborIpv6')
        return self._NeighborIpv6

    @property
    def EnableTeGroup(self):
        """
        get the value of property _EnableTeGroup
        """
        if self.force_auto_sync:
            self.get('EnableTeGroup')
        return self._EnableTeGroup

    @property
    def TeGroup(self):
        """
        get the value of property _TeGroup
        """
        if self.force_auto_sync:
            self.get('TeGroup')
        return self._TeGroup

    @property
    def EnableMaxBandwidth(self):
        """
        get the value of property _EnableMaxBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableMaxBandwidth')
        return self._EnableMaxBandwidth

    @property
    def MaximunLink(self):
        """
        get the value of property _MaximunLink
        """
        if self.force_auto_sync:
            self.get('MaximunLink')
        return self._MaximunLink

    @property
    def EnableResBandwidth(self):
        """
        get the value of property _EnableResBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableResBandwidth')
        return self._EnableResBandwidth

    @property
    def MaximumReservableLink(self):
        """
        get the value of property _MaximumReservableLink
        """
        if self.force_auto_sync:
            self.get('MaximumReservableLink')
        return self._MaximumReservableLink

    @property
    def EnableUnresBandwidth(self):
        """
        get the value of property _EnableUnresBandwidth
        """
        if self.force_auto_sync:
            self.get('EnableUnresBandwidth')
        return self._EnableUnresBandwidth

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

    @EnableInterfaceIp.setter
    def EnableInterfaceIp(self, value):
        self._EnableInterfaceIp = value
        self.edit(EnableInterfaceIp=value)

    @InterfaceIp.setter
    def InterfaceIp(self, value):
        self._InterfaceIp = value
        self.edit(InterfaceIp=value)

    @EnableNeighborIp.setter
    def EnableNeighborIp(self, value):
        self._EnableNeighborIp = value
        self.edit(EnableNeighborIp=value)

    @NeighborIp.setter
    def NeighborIp(self, value):
        self._NeighborIp = value
        self.edit(NeighborIp=value)

    @EnableInterfaceIpv6.setter
    def EnableInterfaceIpv6(self, value):
        self._EnableInterfaceIpv6 = value
        self.edit(EnableInterfaceIpv6=value)

    @InterfaceIpv6.setter
    def InterfaceIpv6(self, value):
        self._InterfaceIpv6 = value
        self.edit(InterfaceIpv6=value)

    @EnableNeighborIpv6.setter
    def EnableNeighborIpv6(self, value):
        self._EnableNeighborIpv6 = value
        self.edit(EnableNeighborIpv6=value)

    @NeighborIpv6.setter
    def NeighborIpv6(self, value):
        self._NeighborIpv6 = value
        self.edit(NeighborIpv6=value)

    @EnableTeGroup.setter
    def EnableTeGroup(self, value):
        self._EnableTeGroup = value
        self.edit(EnableTeGroup=value)

    @TeGroup.setter
    def TeGroup(self, value):
        self._TeGroup = value
        self.edit(TeGroup=value)

    @EnableMaxBandwidth.setter
    def EnableMaxBandwidth(self, value):
        self._EnableMaxBandwidth = value
        self.edit(EnableMaxBandwidth=value)

    @MaximunLink.setter
    def MaximunLink(self, value):
        self._MaximunLink = value
        self.edit(MaximunLink=value)

    @EnableResBandwidth.setter
    def EnableResBandwidth(self, value):
        self._EnableResBandwidth = value
        self.edit(EnableResBandwidth=value)

    @MaximumReservableLink.setter
    def MaximumReservableLink(self, value):
        self._MaximumReservableLink = value
        self.edit(MaximumReservableLink=value)

    @EnableUnresBandwidth.setter
    def EnableUnresBandwidth(self, value):
        self._EnableUnresBandwidth = value
        self.edit(EnableUnresBandwidth=value)

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

    def _set_enableinterfaceip_with_str(self, value):
        self._EnableInterfaceIp = (value == 'True')

    def _set_interfaceip_with_str(self, value):
        self._InterfaceIp = value

    def _set_enableneighborip_with_str(self, value):
        self._EnableNeighborIp = (value == 'True')

    def _set_neighborip_with_str(self, value):
        self._NeighborIp = value

    def _set_enableinterfaceipv6_with_str(self, value):
        self._EnableInterfaceIpv6 = (value == 'True')

    def _set_interfaceipv6_with_str(self, value):
        self._InterfaceIpv6 = value

    def _set_enableneighboripv6_with_str(self, value):
        self._EnableNeighborIpv6 = (value == 'True')

    def _set_neighboripv6_with_str(self, value):
        self._NeighborIpv6 = value

    def _set_enabletegroup_with_str(self, value):
        self._EnableTeGroup = (value == 'True')

    def _set_tegroup_with_str(self, value):
        try:
            self._TeGroup = int(value)
        except ValueError:
            self._TeGroup = hex(int(value, 16))

    def _set_enablemaxbandwidth_with_str(self, value):
        self._EnableMaxBandwidth = (value == 'True')

    def _set_maximunlink_with_str(self, value):
        try:
            self._MaximunLink = int(value)
        except ValueError:
            self._MaximunLink = hex(int(value, 16))

    def _set_enableresbandwidth_with_str(self, value):
        self._EnableResBandwidth = (value == 'True')

    def _set_maximumreservablelink_with_str(self, value):
        try:
            self._MaximumReservableLink = int(value)
        except ValueError:
            self._MaximumReservableLink = hex(int(value, 16))

    def _set_enableunresbandwidth_with_str(self, value):
        self._EnableUnresBandwidth = (value == 'True')

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

