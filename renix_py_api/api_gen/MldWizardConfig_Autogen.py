"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class MldWizardConfig(ProtocolWizardConfig):
    def __init__(self, MldVersion=None, MldNumberOfGroups=None, MldStartingGroupIp=None, MldDeviceGroupMapping=None, MldStepPerPort=None, MldFilterMode=None, MldFilteredSources=None, MldExistingDevice=None, MldStart=None, MldStep=None, MldPrefix=None, MldCount=None, **kwargs):
        self._MldVersion = MldVersion  # Version
        self._MldNumberOfGroups = MldNumberOfGroups  # Number of groups
        self._MldStartingGroupIp = MldStartingGroupIp  # Starting group IP:
        self._MldDeviceGroupMapping = MldDeviceGroupMapping  # Device-Group Mapping:
        self._MldStepPerPort = MldStepPerPort  # Step per port:
        self._MldFilterMode = MldFilterMode  # Filter Mode:
        self._MldFilteredSources = MldFilteredSources  # Filtered Sources:
        self._MldExistingDevice = MldExistingDevice  # Interface Handle
        self._MldStart = MldStart  # Start
        self._MldStep = MldStep  # Step
        self._MldPrefix = MldPrefix  # Prefix
        self._MldCount = MldCount  # Count

        properties = kwargs.copy()
        if MldVersion is not None:
            properties['MldVersion'] = MldVersion
        if MldNumberOfGroups is not None:
            properties['MldNumberOfGroups'] = MldNumberOfGroups
        if MldStartingGroupIp is not None:
            properties['MldStartingGroupIp'] = MldStartingGroupIp
        if MldDeviceGroupMapping is not None:
            properties['MldDeviceGroupMapping'] = MldDeviceGroupMapping
        if MldStepPerPort is not None:
            properties['MldStepPerPort'] = MldStepPerPort
        if MldFilterMode is not None:
            properties['MldFilterMode'] = MldFilterMode
        if MldFilteredSources is not None:
            properties['MldFilteredSources'] = MldFilteredSources
        if MldExistingDevice is not None:
            properties['MldExistingDevice'] = MldExistingDevice
        if MldStart is not None:
            properties['MldStart'] = MldStart
        if MldStep is not None:
            properties['MldStep'] = MldStep
        if MldPrefix is not None:
            properties['MldPrefix'] = MldPrefix
        if MldCount is not None:
            properties['MldCount'] = MldCount

        # call base class function, and it will send message to renix server to create a class.
        super(MldWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MldVersion=None, MldNumberOfGroups=None, MldStartingGroupIp=None, MldDeviceGroupMapping=None, MldStepPerPort=None, MldFilterMode=None, MldFilteredSources=None, MldExistingDevice=None, MldStart=None, MldStep=None, MldPrefix=None, MldCount=None, **kwargs):
        properties = kwargs.copy()
        if MldVersion is not None:
            self._MldVersion = MldVersion
            properties['MldVersion'] = MldVersion
        if MldNumberOfGroups is not None:
            self._MldNumberOfGroups = MldNumberOfGroups
            properties['MldNumberOfGroups'] = MldNumberOfGroups
        if MldStartingGroupIp is not None:
            self._MldStartingGroupIp = MldStartingGroupIp
            properties['MldStartingGroupIp'] = MldStartingGroupIp
        if MldDeviceGroupMapping is not None:
            self._MldDeviceGroupMapping = MldDeviceGroupMapping
            properties['MldDeviceGroupMapping'] = MldDeviceGroupMapping
        if MldStepPerPort is not None:
            self._MldStepPerPort = MldStepPerPort
            properties['MldStepPerPort'] = MldStepPerPort
        if MldFilterMode is not None:
            self._MldFilterMode = MldFilterMode
            properties['MldFilterMode'] = MldFilterMode
        if MldFilteredSources is not None:
            self._MldFilteredSources = MldFilteredSources
            properties['MldFilteredSources'] = MldFilteredSources
        if MldExistingDevice is not None:
            self._MldExistingDevice = MldExistingDevice
            properties['MldExistingDevice'] = MldExistingDevice
        if MldStart is not None:
            self._MldStart = MldStart
            properties['MldStart'] = MldStart
        if MldStep is not None:
            self._MldStep = MldStep
            properties['MldStep'] = MldStep
        if MldPrefix is not None:
            self._MldPrefix = MldPrefix
            properties['MldPrefix'] = MldPrefix
        if MldCount is not None:
            self._MldCount = MldCount
            properties['MldCount'] = MldCount

        super(MldWizardConfig, self).edit(**properties)

    @property
    def MldVersion(self):
        """
        get the value of property _MldVersion
        """
        if self.force_auto_sync:
            self.get('MldVersion')
        return self._MldVersion

    @property
    def MldNumberOfGroups(self):
        """
        get the value of property _MldNumberOfGroups
        """
        if self.force_auto_sync:
            self.get('MldNumberOfGroups')
        return self._MldNumberOfGroups

    @property
    def MldStartingGroupIp(self):
        """
        get the value of property _MldStartingGroupIp
        """
        if self.force_auto_sync:
            self.get('MldStartingGroupIp')
        return self._MldStartingGroupIp

    @property
    def MldDeviceGroupMapping(self):
        """
        get the value of property _MldDeviceGroupMapping
        """
        if self.force_auto_sync:
            self.get('MldDeviceGroupMapping')
        return self._MldDeviceGroupMapping

    @property
    def MldStepPerPort(self):
        """
        get the value of property _MldStepPerPort
        """
        if self.force_auto_sync:
            self.get('MldStepPerPort')
        return self._MldStepPerPort

    @property
    def MldFilterMode(self):
        """
        get the value of property _MldFilterMode
        """
        if self.force_auto_sync:
            self.get('MldFilterMode')
        return self._MldFilterMode

    @property
    def MldFilteredSources(self):
        """
        get the value of property _MldFilteredSources
        """
        if self.force_auto_sync:
            self.get('MldFilteredSources')
        return self._MldFilteredSources

    @property
    def MldExistingDevice(self):
        """
        get the value of property _MldExistingDevice
        """
        if self.force_auto_sync:
            self.get('MldExistingDevice')
        return self._MldExistingDevice

    @property
    def MldStart(self):
        """
        get the value of property _MldStart
        """
        if self.force_auto_sync:
            self.get('MldStart')
        return self._MldStart

    @property
    def MldStep(self):
        """
        get the value of property _MldStep
        """
        if self.force_auto_sync:
            self.get('MldStep')
        return self._MldStep

    @property
    def MldPrefix(self):
        """
        get the value of property _MldPrefix
        """
        if self.force_auto_sync:
            self.get('MldPrefix')
        return self._MldPrefix

    @property
    def MldCount(self):
        """
        get the value of property _MldCount
        """
        if self.force_auto_sync:
            self.get('MldCount')
        return self._MldCount

    @MldVersion.setter
    def MldVersion(self, value):
        self._MldVersion = value
        self.edit(MldVersion=value)

    @MldNumberOfGroups.setter
    def MldNumberOfGroups(self, value):
        self._MldNumberOfGroups = value
        self.edit(MldNumberOfGroups=value)

    @MldStartingGroupIp.setter
    def MldStartingGroupIp(self, value):
        self._MldStartingGroupIp = value
        self.edit(MldStartingGroupIp=value)

    @MldDeviceGroupMapping.setter
    def MldDeviceGroupMapping(self, value):
        self._MldDeviceGroupMapping = value
        self.edit(MldDeviceGroupMapping=value)

    @MldStepPerPort.setter
    def MldStepPerPort(self, value):
        self._MldStepPerPort = value
        self.edit(MldStepPerPort=value)

    @MldFilterMode.setter
    def MldFilterMode(self, value):
        self._MldFilterMode = value
        self.edit(MldFilterMode=value)

    @MldFilteredSources.setter
    def MldFilteredSources(self, value):
        self._MldFilteredSources = value
        self.edit(MldFilteredSources=value)

    @MldExistingDevice.setter
    def MldExistingDevice(self, value):
        self._MldExistingDevice = value
        self.edit(MldExistingDevice=value)

    @MldStart.setter
    def MldStart(self, value):
        self._MldStart = value
        self.edit(MldStart=value)

    @MldStep.setter
    def MldStep(self, value):
        self._MldStep = value
        self.edit(MldStep=value)

    @MldPrefix.setter
    def MldPrefix(self, value):
        self._MldPrefix = value
        self.edit(MldPrefix=value)

    @MldCount.setter
    def MldCount(self, value):
        self._MldCount = value
        self.edit(MldCount=value)

    def _set_mldversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldVersion = EnumMldMulticastVersion.%s' % value[:seperate])

    def _set_mldnumberofgroups_with_str(self, value):
        try:
            self._MldNumberOfGroups = int(value)
        except ValueError:
            self._MldNumberOfGroups = hex(int(value, 16))

    def _set_mldstartinggroupip_with_str(self, value):
        self._MldStartingGroupIp = value

    def _set_mlddevicegroupmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldDeviceGroupMapping = EnumMldDeviceGroupMapping.%s' % value[:seperate])

    def _set_mldstepperport_with_str(self, value):
        self._MldStepPerPort = value

    def _set_mldfiltermode_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldFilterMode = EnumMldSourceFilterMode.%s' % value[:seperate])

    def _set_mldfilteredsources_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldFilteredSources = EnumMldFilteredSources.%s' % value[:seperate])

    def _set_mldexistingdevice_with_str(self, value):
        self._MldExistingDevice = value

    def _set_mldstart_with_str(self, value):
        self._MldStart = value

    def _set_mldstep_with_str(self, value):
        try:
            self._MldStep = int(value)
        except ValueError:
            self._MldStep = hex(int(value, 16))

    def _set_mldprefix_with_str(self, value):
        try:
            self._MldPrefix = int(value)
        except ValueError:
            self._MldPrefix = hex(int(value, 16))

    def _set_mldcount_with_str(self, value):
        try:
            self._MldCount = int(value)
        except ValueError:
            self._MldCount = hex(int(value, 16))

