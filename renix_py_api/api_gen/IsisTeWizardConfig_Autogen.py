"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisTeWizardConfig(ROMObject):
    def __init__(self, EnableTeGroup=None, TeGroup=None, EnableMaxBandwidth=None, MaximunLink=None, EnableResBandwidth=None, MaximumReservableLink=None, EnableUnresBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
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
        super(IsisTeWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableTeGroup=None, TeGroup=None, EnableMaxBandwidth=None, MaximunLink=None, EnableResBandwidth=None, MaximumReservableLink=None, EnableUnresBandwidth=None, UnreservedBandwidth0=None, UnreservedBandwidth1=None, UnreservedBandwidth2=None, UnreservedBandwidth3=None, UnreservedBandwidth4=None, UnreservedBandwidth5=None, UnreservedBandwidth6=None, UnreservedBandwidth7=None, **kwargs):
        properties = kwargs.copy()
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

        super(IsisTeWizardConfig, self).edit(**properties)

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

