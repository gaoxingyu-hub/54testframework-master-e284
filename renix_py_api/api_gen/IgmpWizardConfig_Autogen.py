"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class IgmpWizardConfig(ProtocolWizardConfig):
    def __init__(self, IgmpVersion=None, IgmpNumberOfGroups=None, IgmpStartingGroupIp=None, IgmpDeviceGroupMapping=None, IgmpStepPerPort=None, IgmpFilterMode=None, IgmpFilteredSources=None, IgmpExistingDevice=None, IgmpStart=None, IgmpStep=None, IgmpPrefix=None, IgmpCount=None, **kwargs):
        self._IgmpVersion = IgmpVersion  # Version
        self._IgmpNumberOfGroups = IgmpNumberOfGroups  # Number of groups
        self._IgmpStartingGroupIp = IgmpStartingGroupIp  # Starting group IP:
        self._IgmpDeviceGroupMapping = IgmpDeviceGroupMapping  # Device-Group Mapping:
        self._IgmpStepPerPort = IgmpStepPerPort  # Step per port:
        self._IgmpFilterMode = IgmpFilterMode  # Filter Mode:
        self._IgmpFilteredSources = IgmpFilteredSources  # Filtered Sources:
        self._IgmpExistingDevice = IgmpExistingDevice  # Interface Handle
        self._IgmpStart = IgmpStart  # Start
        self._IgmpStep = IgmpStep  # Step
        self._IgmpPrefix = IgmpPrefix  # Prefix
        self._IgmpCount = IgmpCount  # Count

        properties = kwargs.copy()
        if IgmpVersion is not None:
            properties['IgmpVersion'] = IgmpVersion
        if IgmpNumberOfGroups is not None:
            properties['IgmpNumberOfGroups'] = IgmpNumberOfGroups
        if IgmpStartingGroupIp is not None:
            properties['IgmpStartingGroupIp'] = IgmpStartingGroupIp
        if IgmpDeviceGroupMapping is not None:
            properties['IgmpDeviceGroupMapping'] = IgmpDeviceGroupMapping
        if IgmpStepPerPort is not None:
            properties['IgmpStepPerPort'] = IgmpStepPerPort
        if IgmpFilterMode is not None:
            properties['IgmpFilterMode'] = IgmpFilterMode
        if IgmpFilteredSources is not None:
            properties['IgmpFilteredSources'] = IgmpFilteredSources
        if IgmpExistingDevice is not None:
            properties['IgmpExistingDevice'] = IgmpExistingDevice
        if IgmpStart is not None:
            properties['IgmpStart'] = IgmpStart
        if IgmpStep is not None:
            properties['IgmpStep'] = IgmpStep
        if IgmpPrefix is not None:
            properties['IgmpPrefix'] = IgmpPrefix
        if IgmpCount is not None:
            properties['IgmpCount'] = IgmpCount

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IgmpVersion=None, IgmpNumberOfGroups=None, IgmpStartingGroupIp=None, IgmpDeviceGroupMapping=None, IgmpStepPerPort=None, IgmpFilterMode=None, IgmpFilteredSources=None, IgmpExistingDevice=None, IgmpStart=None, IgmpStep=None, IgmpPrefix=None, IgmpCount=None, **kwargs):
        properties = kwargs.copy()
        if IgmpVersion is not None:
            self._IgmpVersion = IgmpVersion
            properties['IgmpVersion'] = IgmpVersion
        if IgmpNumberOfGroups is not None:
            self._IgmpNumberOfGroups = IgmpNumberOfGroups
            properties['IgmpNumberOfGroups'] = IgmpNumberOfGroups
        if IgmpStartingGroupIp is not None:
            self._IgmpStartingGroupIp = IgmpStartingGroupIp
            properties['IgmpStartingGroupIp'] = IgmpStartingGroupIp
        if IgmpDeviceGroupMapping is not None:
            self._IgmpDeviceGroupMapping = IgmpDeviceGroupMapping
            properties['IgmpDeviceGroupMapping'] = IgmpDeviceGroupMapping
        if IgmpStepPerPort is not None:
            self._IgmpStepPerPort = IgmpStepPerPort
            properties['IgmpStepPerPort'] = IgmpStepPerPort
        if IgmpFilterMode is not None:
            self._IgmpFilterMode = IgmpFilterMode
            properties['IgmpFilterMode'] = IgmpFilterMode
        if IgmpFilteredSources is not None:
            self._IgmpFilteredSources = IgmpFilteredSources
            properties['IgmpFilteredSources'] = IgmpFilteredSources
        if IgmpExistingDevice is not None:
            self._IgmpExistingDevice = IgmpExistingDevice
            properties['IgmpExistingDevice'] = IgmpExistingDevice
        if IgmpStart is not None:
            self._IgmpStart = IgmpStart
            properties['IgmpStart'] = IgmpStart
        if IgmpStep is not None:
            self._IgmpStep = IgmpStep
            properties['IgmpStep'] = IgmpStep
        if IgmpPrefix is not None:
            self._IgmpPrefix = IgmpPrefix
            properties['IgmpPrefix'] = IgmpPrefix
        if IgmpCount is not None:
            self._IgmpCount = IgmpCount
            properties['IgmpCount'] = IgmpCount

        super(IgmpWizardConfig, self).edit(**properties)

    @property
    def IgmpVersion(self):
        """
        get the value of property _IgmpVersion
        """
        if self.force_auto_sync:
            self.get('IgmpVersion')
        return self._IgmpVersion

    @property
    def IgmpNumberOfGroups(self):
        """
        get the value of property _IgmpNumberOfGroups
        """
        if self.force_auto_sync:
            self.get('IgmpNumberOfGroups')
        return self._IgmpNumberOfGroups

    @property
    def IgmpStartingGroupIp(self):
        """
        get the value of property _IgmpStartingGroupIp
        """
        if self.force_auto_sync:
            self.get('IgmpStartingGroupIp')
        return self._IgmpStartingGroupIp

    @property
    def IgmpDeviceGroupMapping(self):
        """
        get the value of property _IgmpDeviceGroupMapping
        """
        if self.force_auto_sync:
            self.get('IgmpDeviceGroupMapping')
        return self._IgmpDeviceGroupMapping

    @property
    def IgmpStepPerPort(self):
        """
        get the value of property _IgmpStepPerPort
        """
        if self.force_auto_sync:
            self.get('IgmpStepPerPort')
        return self._IgmpStepPerPort

    @property
    def IgmpFilterMode(self):
        """
        get the value of property _IgmpFilterMode
        """
        if self.force_auto_sync:
            self.get('IgmpFilterMode')
        return self._IgmpFilterMode

    @property
    def IgmpFilteredSources(self):
        """
        get the value of property _IgmpFilteredSources
        """
        if self.force_auto_sync:
            self.get('IgmpFilteredSources')
        return self._IgmpFilteredSources

    @property
    def IgmpExistingDevice(self):
        """
        get the value of property _IgmpExistingDevice
        """
        if self.force_auto_sync:
            self.get('IgmpExistingDevice')
        return self._IgmpExistingDevice

    @property
    def IgmpStart(self):
        """
        get the value of property _IgmpStart
        """
        if self.force_auto_sync:
            self.get('IgmpStart')
        return self._IgmpStart

    @property
    def IgmpStep(self):
        """
        get the value of property _IgmpStep
        """
        if self.force_auto_sync:
            self.get('IgmpStep')
        return self._IgmpStep

    @property
    def IgmpPrefix(self):
        """
        get the value of property _IgmpPrefix
        """
        if self.force_auto_sync:
            self.get('IgmpPrefix')
        return self._IgmpPrefix

    @property
    def IgmpCount(self):
        """
        get the value of property _IgmpCount
        """
        if self.force_auto_sync:
            self.get('IgmpCount')
        return self._IgmpCount

    @IgmpVersion.setter
    def IgmpVersion(self, value):
        self._IgmpVersion = value
        self.edit(IgmpVersion=value)

    @IgmpNumberOfGroups.setter
    def IgmpNumberOfGroups(self, value):
        self._IgmpNumberOfGroups = value
        self.edit(IgmpNumberOfGroups=value)

    @IgmpStartingGroupIp.setter
    def IgmpStartingGroupIp(self, value):
        self._IgmpStartingGroupIp = value
        self.edit(IgmpStartingGroupIp=value)

    @IgmpDeviceGroupMapping.setter
    def IgmpDeviceGroupMapping(self, value):
        self._IgmpDeviceGroupMapping = value
        self.edit(IgmpDeviceGroupMapping=value)

    @IgmpStepPerPort.setter
    def IgmpStepPerPort(self, value):
        self._IgmpStepPerPort = value
        self.edit(IgmpStepPerPort=value)

    @IgmpFilterMode.setter
    def IgmpFilterMode(self, value):
        self._IgmpFilterMode = value
        self.edit(IgmpFilterMode=value)

    @IgmpFilteredSources.setter
    def IgmpFilteredSources(self, value):
        self._IgmpFilteredSources = value
        self.edit(IgmpFilteredSources=value)

    @IgmpExistingDevice.setter
    def IgmpExistingDevice(self, value):
        self._IgmpExistingDevice = value
        self.edit(IgmpExistingDevice=value)

    @IgmpStart.setter
    def IgmpStart(self, value):
        self._IgmpStart = value
        self.edit(IgmpStart=value)

    @IgmpStep.setter
    def IgmpStep(self, value):
        self._IgmpStep = value
        self.edit(IgmpStep=value)

    @IgmpPrefix.setter
    def IgmpPrefix(self, value):
        self._IgmpPrefix = value
        self.edit(IgmpPrefix=value)

    @IgmpCount.setter
    def IgmpCount(self, value):
        self._IgmpCount = value
        self.edit(IgmpCount=value)

    def _set_igmpversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpVersion = EnumIgmpMulticastVersion.%s' % value[:seperate])

    def _set_igmpnumberofgroups_with_str(self, value):
        try:
            self._IgmpNumberOfGroups = int(value)
        except ValueError:
            self._IgmpNumberOfGroups = hex(int(value, 16))

    def _set_igmpstartinggroupip_with_str(self, value):
        self._IgmpStartingGroupIp = value

    def _set_igmpdevicegroupmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpDeviceGroupMapping = EnumIgmpDeviceGroupMapping.%s' % value[:seperate])

    def _set_igmpstepperport_with_str(self, value):
        self._IgmpStepPerPort = value

    def _set_igmpfiltermode_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpFilterMode = EnumIgmpSourceFilterMode.%s' % value[:seperate])

    def _set_igmpfilteredsources_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpFilteredSources = EnumIgmpFilteredSources.%s' % value[:seperate])

    def _set_igmpexistingdevice_with_str(self, value):
        self._IgmpExistingDevice = value

    def _set_igmpstart_with_str(self, value):
        self._IgmpStart = value

    def _set_igmpstep_with_str(self, value):
        try:
            self._IgmpStep = int(value)
        except ValueError:
            self._IgmpStep = hex(int(value, 16))

    def _set_igmpprefix_with_str(self, value):
        try:
            self._IgmpPrefix = int(value)
        except ValueError:
            self._IgmpPrefix = hex(int(value, 16))

    def _set_igmpcount_with_str(self, value):
        try:
            self._IgmpCount = int(value)
        except ValueError:
            self._IgmpCount = hex(int(value, 16))

