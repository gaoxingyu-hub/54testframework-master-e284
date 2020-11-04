"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BaseMstInstanceConfig(ROMObject):
    def __init__(self, RegionRootType=None, RegionRootPriority=None, RegionRootMac=None, RegionRootPathCost=None, RegionRemainHops=None, **kwargs):
        self._InstanceNumber = 0  # Instance Number, not editable
        self._RegionElectedRootID = '00:00:00:00:00:00:00'  # Region Elected Root ID, not editable
        self._RegionRootType = RegionRootType  # Region Root Type
        self._RegionRootPriority = RegionRootPriority  # Region Root Priority
        self._RegionRootMac = RegionRootMac  # Region Root MAC
        self._RegionRootPathCost = RegionRootPathCost  # Region Root Path Cost
        self._RegionRemainHops = RegionRemainHops  # Remain Hops

        properties = kwargs.copy()
        if RegionRootType is not None:
            properties['RegionRootType'] = RegionRootType
        if RegionRootPriority is not None:
            properties['RegionRootPriority'] = RegionRootPriority
        if RegionRootMac is not None:
            properties['RegionRootMac'] = RegionRootMac
        if RegionRootPathCost is not None:
            properties['RegionRootPathCost'] = RegionRootPathCost
        if RegionRemainHops is not None:
            properties['RegionRemainHops'] = RegionRemainHops

        # call base class function, and it will send message to renix server to create a class.
        super(BaseMstInstanceConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RegionRootType=None, RegionRootPriority=None, RegionRootMac=None, RegionRootPathCost=None, RegionRemainHops=None, **kwargs):
        properties = kwargs.copy()
        if RegionRootType is not None:
            self._RegionRootType = RegionRootType
            properties['RegionRootType'] = RegionRootType
        if RegionRootPriority is not None:
            self._RegionRootPriority = RegionRootPriority
            properties['RegionRootPriority'] = RegionRootPriority
        if RegionRootMac is not None:
            self._RegionRootMac = RegionRootMac
            properties['RegionRootMac'] = RegionRootMac
        if RegionRootPathCost is not None:
            self._RegionRootPathCost = RegionRootPathCost
            properties['RegionRootPathCost'] = RegionRootPathCost
        if RegionRemainHops is not None:
            self._RegionRemainHops = RegionRemainHops
            properties['RegionRemainHops'] = RegionRemainHops

        super(BaseMstInstanceConfig, self).edit(**properties)

    @property
    def InstanceNumber(self):
        """
        get the value of property _InstanceNumber
        """
        if self.force_auto_sync:
            self.get('InstanceNumber')
        return self._InstanceNumber

    @property
    def RegionElectedRootID(self):
        """
        get the value of property _RegionElectedRootID
        """
        if self.force_auto_sync:
            self.get('RegionElectedRootID')
        return self._RegionElectedRootID

    @property
    def RegionRootType(self):
        """
        get the value of property _RegionRootType
        """
        if self.force_auto_sync:
            self.get('RegionRootType')
        return self._RegionRootType

    @property
    def RegionRootPriority(self):
        """
        get the value of property _RegionRootPriority
        """
        if self.force_auto_sync:
            self.get('RegionRootPriority')
        return self._RegionRootPriority

    @property
    def RegionRootMac(self):
        """
        get the value of property _RegionRootMac
        """
        if self.force_auto_sync:
            self.get('RegionRootMac')
        return self._RegionRootMac

    @property
    def RegionRootPathCost(self):
        """
        get the value of property _RegionRootPathCost
        """
        if self.force_auto_sync:
            self.get('RegionRootPathCost')
        return self._RegionRootPathCost

    @property
    def RegionRemainHops(self):
        """
        get the value of property _RegionRemainHops
        """
        if self.force_auto_sync:
            self.get('RegionRemainHops')
        return self._RegionRemainHops

    @RegionRootType.setter
    def RegionRootType(self, value):
        self._RegionRootType = value
        self.edit(RegionRootType=value)

    @RegionRootPriority.setter
    def RegionRootPriority(self, value):
        self._RegionRootPriority = value
        self.edit(RegionRootPriority=value)

    @RegionRootMac.setter
    def RegionRootMac(self, value):
        self._RegionRootMac = value
        self.edit(RegionRootMac=value)

    @RegionRootPathCost.setter
    def RegionRootPathCost(self, value):
        self._RegionRootPathCost = value
        self.edit(RegionRootPathCost=value)

    @RegionRemainHops.setter
    def RegionRemainHops(self, value):
        self._RegionRemainHops = value
        self.edit(RegionRemainHops=value)

    def _set_instancenumber_with_str(self, value):
        try:
            self._InstanceNumber = int(value)
        except ValueError:
            self._InstanceNumber = hex(int(value, 16))

    def _set_regionelectedrootid_with_str(self, value):
        self._RegionElectedRootID = value

    def _set_regionroottype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RegionRootType = EnumStpRootType.%s' % value[:seperate])

    def _set_regionrootpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._RegionRootPriority = EnumRootPriority.%s' % value[:seperate])

    def _set_regionrootmac_with_str(self, value):
        self._RegionRootMac = value

    def _set_regionrootpathcost_with_str(self, value):
        try:
            self._RegionRootPathCost = int(value)
        except ValueError:
            self._RegionRootPathCost = hex(int(value, 16))

    def _set_regionremainhops_with_str(self, value):
        try:
            self._RegionRemainHops = int(value)
        except ValueError:
            self._RegionRemainHops = hex(int(value, 16))

