"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpActionBucketConfig(ROMObject):
    def __init__(self, Weight=None, WatchGroup=None, WatchPort=None, **kwargs):
        self._Weight = Weight  # Weight
        self._WatchGroup = WatchGroup  # Watch Group
        self._WatchPort = WatchPort  # Watch Port

        properties = kwargs.copy()
        if Weight is not None:
            properties['Weight'] = Weight
        if WatchGroup is not None:
            properties['WatchGroup'] = WatchGroup
        if WatchPort is not None:
            properties['WatchPort'] = WatchPort

        # call base class function, and it will send message to renix server to create a class.
        super(OfpActionBucketConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Weight=None, WatchGroup=None, WatchPort=None, **kwargs):
        properties = kwargs.copy()
        if Weight is not None:
            self._Weight = Weight
            properties['Weight'] = Weight
        if WatchGroup is not None:
            self._WatchGroup = WatchGroup
            properties['WatchGroup'] = WatchGroup
        if WatchPort is not None:
            self._WatchPort = WatchPort
            properties['WatchPort'] = WatchPort

        super(OfpActionBucketConfig, self).edit(**properties)

    @property
    def Weight(self):
        """
        get the value of property _Weight
        """
        if self.force_auto_sync:
            self.get('Weight')
        return self._Weight

    @property
    def WatchGroup(self):
        """
        get the value of property _WatchGroup
        """
        if self.force_auto_sync:
            self.get('WatchGroup')
        return self._WatchGroup

    @property
    def WatchPort(self):
        """
        get the value of property _WatchPort
        """
        if self.force_auto_sync:
            self.get('WatchPort')
        return self._WatchPort

    @Weight.setter
    def Weight(self, value):
        self._Weight = value
        self.edit(Weight=value)

    @WatchGroup.setter
    def WatchGroup(self, value):
        self._WatchGroup = value
        self.edit(WatchGroup=value)

    @WatchPort.setter
    def WatchPort(self, value):
        self._WatchPort = value
        self.edit(WatchPort=value)

    def _set_weight_with_str(self, value):
        try:
            self._Weight = int(value)
        except ValueError:
            self._Weight = hex(int(value, 16))

    def _set_watchgroup_with_str(self, value):
        try:
            self._WatchGroup = int(value)
        except ValueError:
            self._WatchGroup = hex(int(value, 16))

    def _set_watchport_with_str(self, value):
        try:
            self._WatchPort = int(value)
        except ValueError:
            self._WatchPort = hex(int(value, 16))

