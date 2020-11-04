"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class MldMembershipsConfig(ROMObject):
    def __init__(self, MldDeviceGroupMapping=None, MldSourceFilterMode=None, MldUserDefinedSources=None, MldSpecifySourcesAsList=None, MldSourceAddressList=None, MldNumberOfSources=None, MldStartingSourceIp=None, MldPrefixLength=None, MldIncrement=None, **kwargs):
        self._MldNumberOfGroups = 0  # Number of Groups, not editable
        self._MldDeviceGroupMapping = MldDeviceGroupMapping  # Device-Group Mapping
        self._MldSourceFilterMode = MldSourceFilterMode  # Source Filter Mode
        self._MldFilterNumberOfSources = 0  # Number of Sources, not editable
        self._MldUserDefinedSources = MldUserDefinedSources  # User Defined Sources
        self._MldSpecifySourcesAsList = MldSpecifySourcesAsList  # Specify Sources As List
        self._MldSourceAddressList = MldSourceAddressList  # Source Address List
        self._MldNumberOfSources = MldNumberOfSources  # Number Of Sources
        self._MldStartingSourceIp = MldStartingSourceIp  # Starting Source IP
        self._MldPrefixLength = MldPrefixLength  # Prefix Length
        self._MldIncrement = MldIncrement  # Increment
        self._SourceCount = 0  # Source Count, not editable

        properties = kwargs.copy()
        if MldDeviceGroupMapping is not None:
            properties['MldDeviceGroupMapping'] = MldDeviceGroupMapping
        if MldSourceFilterMode is not None:
            properties['MldSourceFilterMode'] = MldSourceFilterMode
        if MldUserDefinedSources is not None:
            properties['MldUserDefinedSources'] = MldUserDefinedSources
        if MldSpecifySourcesAsList is not None:
            properties['MldSpecifySourcesAsList'] = MldSpecifySourcesAsList
        if MldSourceAddressList is not None:
            properties['MldSourceAddressList'] = MldSourceAddressList
        if MldNumberOfSources is not None:
            properties['MldNumberOfSources'] = MldNumberOfSources
        if MldStartingSourceIp is not None:
            properties['MldStartingSourceIp'] = MldStartingSourceIp
        if MldPrefixLength is not None:
            properties['MldPrefixLength'] = MldPrefixLength
        if MldIncrement is not None:
            properties['MldIncrement'] = MldIncrement

        # call base class function, and it will send message to renix server to create a class.
        super(MldMembershipsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MldDeviceGroupMapping=None, MldSourceFilterMode=None, MldUserDefinedSources=None, MldSpecifySourcesAsList=None, MldSourceAddressList=None, MldNumberOfSources=None, MldStartingSourceIp=None, MldPrefixLength=None, MldIncrement=None, **kwargs):
        properties = kwargs.copy()
        if MldDeviceGroupMapping is not None:
            self._MldDeviceGroupMapping = MldDeviceGroupMapping
            properties['MldDeviceGroupMapping'] = MldDeviceGroupMapping
        if MldSourceFilterMode is not None:
            self._MldSourceFilterMode = MldSourceFilterMode
            properties['MldSourceFilterMode'] = MldSourceFilterMode
        if MldUserDefinedSources is not None:
            self._MldUserDefinedSources = MldUserDefinedSources
            properties['MldUserDefinedSources'] = MldUserDefinedSources
        if MldSpecifySourcesAsList is not None:
            self._MldSpecifySourcesAsList = MldSpecifySourcesAsList
            properties['MldSpecifySourcesAsList'] = MldSpecifySourcesAsList
        if MldSourceAddressList is not None:
            self._MldSourceAddressList = MldSourceAddressList
            properties['MldSourceAddressList'] = MldSourceAddressList
        if MldNumberOfSources is not None:
            self._MldNumberOfSources = MldNumberOfSources
            properties['MldNumberOfSources'] = MldNumberOfSources
        if MldStartingSourceIp is not None:
            self._MldStartingSourceIp = MldStartingSourceIp
            properties['MldStartingSourceIp'] = MldStartingSourceIp
        if MldPrefixLength is not None:
            self._MldPrefixLength = MldPrefixLength
            properties['MldPrefixLength'] = MldPrefixLength
        if MldIncrement is not None:
            self._MldIncrement = MldIncrement
            properties['MldIncrement'] = MldIncrement

        super(MldMembershipsConfig, self).edit(**properties)

    @property
    def MldNumberOfGroups(self):
        """
        get the value of property _MldNumberOfGroups
        """
        if self.force_auto_sync:
            self.get('MldNumberOfGroups')
        return self._MldNumberOfGroups

    @property
    def MldDeviceGroupMapping(self):
        """
        get the value of property _MldDeviceGroupMapping
        """
        if self.force_auto_sync:
            self.get('MldDeviceGroupMapping')
        return self._MldDeviceGroupMapping

    @property
    def MldSourceFilterMode(self):
        """
        get the value of property _MldSourceFilterMode
        """
        if self.force_auto_sync:
            self.get('MldSourceFilterMode')
        return self._MldSourceFilterMode

    @property
    def MldFilterNumberOfSources(self):
        """
        get the value of property _MldFilterNumberOfSources
        """
        if self.force_auto_sync:
            self.get('MldFilterNumberOfSources')
        return self._MldFilterNumberOfSources

    @property
    def MldUserDefinedSources(self):
        """
        get the value of property _MldUserDefinedSources
        """
        if self.force_auto_sync:
            self.get('MldUserDefinedSources')
        return self._MldUserDefinedSources

    @property
    def MldSpecifySourcesAsList(self):
        """
        get the value of property _MldSpecifySourcesAsList
        """
        if self.force_auto_sync:
            self.get('MldSpecifySourcesAsList')
        return self._MldSpecifySourcesAsList

    @property
    def MldSourceAddressList(self):
        """
        get the value of property _MldSourceAddressList
        """
        if self.force_auto_sync:
            self.get('MldSourceAddressList')
        return self._MldSourceAddressList

    @property
    def MldNumberOfSources(self):
        """
        get the value of property _MldNumberOfSources
        """
        if self.force_auto_sync:
            self.get('MldNumberOfSources')
        return self._MldNumberOfSources

    @property
    def MldStartingSourceIp(self):
        """
        get the value of property _MldStartingSourceIp
        """
        if self.force_auto_sync:
            self.get('MldStartingSourceIp')
        return self._MldStartingSourceIp

    @property
    def MldPrefixLength(self):
        """
        get the value of property _MldPrefixLength
        """
        if self.force_auto_sync:
            self.get('MldPrefixLength')
        return self._MldPrefixLength

    @property
    def MldIncrement(self):
        """
        get the value of property _MldIncrement
        """
        if self.force_auto_sync:
            self.get('MldIncrement')
        return self._MldIncrement

    @property
    def SourceCount(self):
        """
        get the value of property _SourceCount
        """
        if self.force_auto_sync:
            self.get('SourceCount')
        return self._SourceCount

    @MldDeviceGroupMapping.setter
    def MldDeviceGroupMapping(self, value):
        self._MldDeviceGroupMapping = value
        self.edit(MldDeviceGroupMapping=value)

    @MldSourceFilterMode.setter
    def MldSourceFilterMode(self, value):
        self._MldSourceFilterMode = value
        self.edit(MldSourceFilterMode=value)

    @MldUserDefinedSources.setter
    def MldUserDefinedSources(self, value):
        self._MldUserDefinedSources = value
        self.edit(MldUserDefinedSources=value)

    @MldSpecifySourcesAsList.setter
    def MldSpecifySourcesAsList(self, value):
        self._MldSpecifySourcesAsList = value
        self.edit(MldSpecifySourcesAsList=value)

    @MldSourceAddressList.setter
    def MldSourceAddressList(self, value):
        self._MldSourceAddressList = value
        self.edit(MldSourceAddressList=value)

    @MldNumberOfSources.setter
    def MldNumberOfSources(self, value):
        self._MldNumberOfSources = value
        self.edit(MldNumberOfSources=value)

    @MldStartingSourceIp.setter
    def MldStartingSourceIp(self, value):
        self._MldStartingSourceIp = value
        self.edit(MldStartingSourceIp=value)

    @MldPrefixLength.setter
    def MldPrefixLength(self, value):
        self._MldPrefixLength = value
        self.edit(MldPrefixLength=value)

    @MldIncrement.setter
    def MldIncrement(self, value):
        self._MldIncrement = value
        self.edit(MldIncrement=value)

    def _set_mldnumberofgroups_with_str(self, value):
        try:
            self._MldNumberOfGroups = int(value)
        except ValueError:
            self._MldNumberOfGroups = hex(int(value, 16))

    def _set_mlddevicegroupmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldDeviceGroupMapping = EnumMldDeviceGroupMapping.%s' % value[:seperate])

    def _set_mldsourcefiltermode_with_str(self, value):
        seperate = value.find(':')
        exec('self._MldSourceFilterMode = EnumMldSourceFilterMode.%s' % value[:seperate])

    def _set_mldfilternumberofsources_with_str(self, value):
        try:
            self._MldFilterNumberOfSources = int(value)
        except ValueError:
            self._MldFilterNumberOfSources = hex(int(value, 16))

    def _set_mlduserdefinedsources_with_str(self, value):
        self._MldUserDefinedSources = (value == 'True')

    def _set_mldspecifysourcesaslist_with_str(self, value):
        self._MldSpecifySourcesAsList = (value == 'True')

    def _set_mldsourceaddresslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldSourceAddressList = tmp_value.split()

    def _set_mldnumberofsources_with_str(self, value):
        try:
            self._MldNumberOfSources = int(value)
        except ValueError:
            self._MldNumberOfSources = hex(int(value, 16))

    def _set_mldstartingsourceip_with_str(self, value):
        self._MldStartingSourceIp = value

    def _set_mldprefixlength_with_str(self, value):
        try:
            self._MldPrefixLength = int(value)
        except ValueError:
            self._MldPrefixLength = hex(int(value, 16))

    def _set_mldincrement_with_str(self, value):
        try:
            self._MldIncrement = int(value)
        except ValueError:
            self._MldIncrement = hex(int(value, 16))

    def _set_sourcecount_with_str(self, value):
        try:
            self._SourceCount = int(value)
        except ValueError:
            self._SourceCount = hex(int(value, 16))

