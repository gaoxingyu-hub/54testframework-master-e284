"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class UpgradeHardwareCommand(ROMCommand):
    def __init__(self, HardwareList=None, UpgradeFilePath=None, ForceUpgrade=None, **kwargs):
        self._HardwareList = HardwareList  # Hardware Handles
        self._UpgradeFilePath = UpgradeFilePath  # Upgrade File Name
        self._ForceUpgrade = ForceUpgrade  # Force Upgrade

        properties = kwargs.copy()
        if HardwareList is not None:
            properties['HardwareList'] = HardwareList
        if UpgradeFilePath is not None:
            properties['UpgradeFilePath'] = UpgradeFilePath
        if ForceUpgrade is not None:
            properties['ForceUpgrade'] = ForceUpgrade

        # call base class function, and it will send message to renix server to create a class.
        super(UpgradeHardwareCommand, self).__init__(**properties)

    @property
    def HardwareList(self):
        """
        get the value of property _HardwareList
        """
        return self._HardwareList

    @property
    def UpgradeFilePath(self):
        """
        get the value of property _UpgradeFilePath
        """
        return self._UpgradeFilePath

    @property
    def ForceUpgrade(self):
        """
        get the value of property _ForceUpgrade
        """
        return self._ForceUpgrade

    @HardwareList.setter
    def HardwareList(self, value):
        self._HardwareList = value

    @UpgradeFilePath.setter
    def UpgradeFilePath(self, value):
        self._UpgradeFilePath = value

    @ForceUpgrade.setter
    def ForceUpgrade(self, value):
        self._ForceUpgrade = value

    def _set_hardwarelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HardwareList = tmp_value.split()

    def _set_upgradefilepath_with_str(self, value):
        self._UpgradeFilePath = value

    def _set_forceupgrade_with_str(self, value):
        self._ForceUpgrade = (value == 'True')

