"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HardwareChassis(ROMObject):
    def __init__(self, Hostname=None, SyncClockRef=None, SyncClockMaster=None, **kwargs):
        self._Hostname = Hostname  # Chassis IP or Hostname
        self._PartNumber = ''  # Part Number, not editable
        self._Version = ''  # Chassis Version, not editable
        self._SerialNumber = ''  # Serial Number, not editable
        self._State = EnumChassisState.CHASSIS_DOWN  # Chassis State, not editable
        self._UpgradeState = EnumUpgradeState.UPGRADE_NOT_STARTED  # Upgrade State, not editable
        self._SyncClockRef = SyncClockRef  # SYNC Clock Ref
        self._SyncClockMaster = SyncClockMaster  # Sync Clock Master
        self._UpgradeProgress = 0  # Progress, not editable

        properties = kwargs.copy()
        if Hostname is not None:
            properties['Hostname'] = Hostname
        if SyncClockRef is not None:
            properties['SyncClockRef'] = SyncClockRef
        if SyncClockMaster is not None:
            properties['SyncClockMaster'] = SyncClockMaster

        # call base class function, and it will send message to renix server to create a class.
        super(HardwareChassis, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Hostname=None, SyncClockRef=None, SyncClockMaster=None, **kwargs):
        properties = kwargs.copy()
        if Hostname is not None:
            self._Hostname = Hostname
            properties['Hostname'] = Hostname
        if SyncClockRef is not None:
            self._SyncClockRef = SyncClockRef
            properties['SyncClockRef'] = SyncClockRef
        if SyncClockMaster is not None:
            self._SyncClockMaster = SyncClockMaster
            properties['SyncClockMaster'] = SyncClockMaster

        super(HardwareChassis, self).edit(**properties)

    @property
    def Hostname(self):
        """
        get the value of property _Hostname
        """
        if self.force_auto_sync:
            self.get('Hostname')
        return self._Hostname

    @property
    def PartNumber(self):
        """
        get the value of property _PartNumber
        """
        if self.force_auto_sync:
            self.get('PartNumber')
        return self._PartNumber

    @property
    def Version(self):
        """
        get the value of property _Version
        """
        if self.force_auto_sync:
            self.get('Version')
        return self._Version

    @property
    def SerialNumber(self):
        """
        get the value of property _SerialNumber
        """
        if self.force_auto_sync:
            self.get('SerialNumber')
        return self._SerialNumber

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def UpgradeState(self):
        """
        get the value of property _UpgradeState
        """
        if self.force_auto_sync:
            self.get('UpgradeState')
        return self._UpgradeState

    @property
    def SyncClockRef(self):
        """
        get the value of property _SyncClockRef
        """
        if self.force_auto_sync:
            self.get('SyncClockRef')
        return self._SyncClockRef

    @property
    def SyncClockMaster(self):
        """
        get the value of property _SyncClockMaster
        """
        if self.force_auto_sync:
            self.get('SyncClockMaster')
        return self._SyncClockMaster

    @property
    def UpgradeProgress(self):
        """
        get the value of property _UpgradeProgress
        """
        if self.force_auto_sync:
            self.get('UpgradeProgress')
        return self._UpgradeProgress

    @Hostname.setter
    def Hostname(self, value):
        self._Hostname = value
        self.edit(Hostname=value)

    @SyncClockRef.setter
    def SyncClockRef(self, value):
        self._SyncClockRef = value
        self.edit(SyncClockRef=value)

    @SyncClockMaster.setter
    def SyncClockMaster(self, value):
        self._SyncClockMaster = value
        self.edit(SyncClockMaster=value)

    def _set_hostname_with_str(self, value):
        self._Hostname = value

    def _set_partnumber_with_str(self, value):
        self._PartNumber = value

    def _set_version_with_str(self, value):
        self._Version = value

    def _set_serialnumber_with_str(self, value):
        self._SerialNumber = value

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumChassisState.%s' % value[:seperate])

    def _set_upgradestate_with_str(self, value):
        seperate = value.find(':')
        exec('self._UpgradeState = EnumUpgradeState.%s' % value[:seperate])

    def _set_syncclockref_with_str(self, value):
        seperate = value.find(':')
        exec('self._SyncClockRef = EnumSynClockRef.%s' % value[:seperate])

    def _set_syncclockmaster_with_str(self, value):
        self._SyncClockMaster = (value == 'True')

    def _set_upgradeprogress_with_str(self, value):
        try:
            self._UpgradeProgress = int(value)
        except ValueError:
            self._UpgradeProgress = hex(int(value, 16))

