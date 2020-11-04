"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IgmpMembershipsConfig(ROMObject):
    def __init__(self, IgmpDeviceGroupMapping=None, IgmpSourceFilterMode=None, IgmpUserDefinedSources=None, IgmpSpecifySourcesAsList=None, IgmpSourceAddressList=None, IgmpNumberOfSources=None, IgmpStartingSourceIp=None, IgmpPrefixLength=None, IgmpIncrement=None, **kwargs):
        self._IgmpNumberOfGroups = 0  # Number of Groups, not editable
        self._IgmpDeviceGroupMapping = IgmpDeviceGroupMapping  # Device-Group Mapping
        self._IgmpSourceFilterMode = IgmpSourceFilterMode  # Source Filter Mode
        self._IgmpFilterNumberOfSources = 0  # Number of Sources, not editable
        self._IgmpUserDefinedSources = IgmpUserDefinedSources  # User Defined Sources
        self._IgmpSpecifySourcesAsList = IgmpSpecifySourcesAsList  # Specify Sources As List
        self._IgmpSourceAddressList = IgmpSourceAddressList  # Source Address List
        self._IgmpNumberOfSources = IgmpNumberOfSources  # Number Of Sources
        self._IgmpStartingSourceIp = IgmpStartingSourceIp  # Starting Source IP
        self._IgmpPrefixLength = IgmpPrefixLength  # Prefix Length
        self._IgmpIncrement = IgmpIncrement  # Increment
        self._SourceCount = 0  # Source Count, not editable

        properties = kwargs.copy()
        if IgmpDeviceGroupMapping is not None:
            properties['IgmpDeviceGroupMapping'] = IgmpDeviceGroupMapping
        if IgmpSourceFilterMode is not None:
            properties['IgmpSourceFilterMode'] = IgmpSourceFilterMode
        if IgmpUserDefinedSources is not None:
            properties['IgmpUserDefinedSources'] = IgmpUserDefinedSources
        if IgmpSpecifySourcesAsList is not None:
            properties['IgmpSpecifySourcesAsList'] = IgmpSpecifySourcesAsList
        if IgmpSourceAddressList is not None:
            properties['IgmpSourceAddressList'] = IgmpSourceAddressList
        if IgmpNumberOfSources is not None:
            properties['IgmpNumberOfSources'] = IgmpNumberOfSources
        if IgmpStartingSourceIp is not None:
            properties['IgmpStartingSourceIp'] = IgmpStartingSourceIp
        if IgmpPrefixLength is not None:
            properties['IgmpPrefixLength'] = IgmpPrefixLength
        if IgmpIncrement is not None:
            properties['IgmpIncrement'] = IgmpIncrement

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpMembershipsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IgmpDeviceGroupMapping=None, IgmpSourceFilterMode=None, IgmpUserDefinedSources=None, IgmpSpecifySourcesAsList=None, IgmpSourceAddressList=None, IgmpNumberOfSources=None, IgmpStartingSourceIp=None, IgmpPrefixLength=None, IgmpIncrement=None, **kwargs):
        properties = kwargs.copy()
        if IgmpDeviceGroupMapping is not None:
            self._IgmpDeviceGroupMapping = IgmpDeviceGroupMapping
            properties['IgmpDeviceGroupMapping'] = IgmpDeviceGroupMapping
        if IgmpSourceFilterMode is not None:
            self._IgmpSourceFilterMode = IgmpSourceFilterMode
            properties['IgmpSourceFilterMode'] = IgmpSourceFilterMode
        if IgmpUserDefinedSources is not None:
            self._IgmpUserDefinedSources = IgmpUserDefinedSources
            properties['IgmpUserDefinedSources'] = IgmpUserDefinedSources
        if IgmpSpecifySourcesAsList is not None:
            self._IgmpSpecifySourcesAsList = IgmpSpecifySourcesAsList
            properties['IgmpSpecifySourcesAsList'] = IgmpSpecifySourcesAsList
        if IgmpSourceAddressList is not None:
            self._IgmpSourceAddressList = IgmpSourceAddressList
            properties['IgmpSourceAddressList'] = IgmpSourceAddressList
        if IgmpNumberOfSources is not None:
            self._IgmpNumberOfSources = IgmpNumberOfSources
            properties['IgmpNumberOfSources'] = IgmpNumberOfSources
        if IgmpStartingSourceIp is not None:
            self._IgmpStartingSourceIp = IgmpStartingSourceIp
            properties['IgmpStartingSourceIp'] = IgmpStartingSourceIp
        if IgmpPrefixLength is not None:
            self._IgmpPrefixLength = IgmpPrefixLength
            properties['IgmpPrefixLength'] = IgmpPrefixLength
        if IgmpIncrement is not None:
            self._IgmpIncrement = IgmpIncrement
            properties['IgmpIncrement'] = IgmpIncrement

        super(IgmpMembershipsConfig, self).edit(**properties)

    @property
    def IgmpNumberOfGroups(self):
        """
        get the value of property _IgmpNumberOfGroups
        """
        if self.force_auto_sync:
            self.get('IgmpNumberOfGroups')
        return self._IgmpNumberOfGroups

    @property
    def IgmpDeviceGroupMapping(self):
        """
        get the value of property _IgmpDeviceGroupMapping
        """
        if self.force_auto_sync:
            self.get('IgmpDeviceGroupMapping')
        return self._IgmpDeviceGroupMapping

    @property
    def IgmpSourceFilterMode(self):
        """
        get the value of property _IgmpSourceFilterMode
        """
        if self.force_auto_sync:
            self.get('IgmpSourceFilterMode')
        return self._IgmpSourceFilterMode

    @property
    def IgmpFilterNumberOfSources(self):
        """
        get the value of property _IgmpFilterNumberOfSources
        """
        if self.force_auto_sync:
            self.get('IgmpFilterNumberOfSources')
        return self._IgmpFilterNumberOfSources

    @property
    def IgmpUserDefinedSources(self):
        """
        get the value of property _IgmpUserDefinedSources
        """
        if self.force_auto_sync:
            self.get('IgmpUserDefinedSources')
        return self._IgmpUserDefinedSources

    @property
    def IgmpSpecifySourcesAsList(self):
        """
        get the value of property _IgmpSpecifySourcesAsList
        """
        if self.force_auto_sync:
            self.get('IgmpSpecifySourcesAsList')
        return self._IgmpSpecifySourcesAsList

    @property
    def IgmpSourceAddressList(self):
        """
        get the value of property _IgmpSourceAddressList
        """
        if self.force_auto_sync:
            self.get('IgmpSourceAddressList')
        return self._IgmpSourceAddressList

    @property
    def IgmpNumberOfSources(self):
        """
        get the value of property _IgmpNumberOfSources
        """
        if self.force_auto_sync:
            self.get('IgmpNumberOfSources')
        return self._IgmpNumberOfSources

    @property
    def IgmpStartingSourceIp(self):
        """
        get the value of property _IgmpStartingSourceIp
        """
        if self.force_auto_sync:
            self.get('IgmpStartingSourceIp')
        return self._IgmpStartingSourceIp

    @property
    def IgmpPrefixLength(self):
        """
        get the value of property _IgmpPrefixLength
        """
        if self.force_auto_sync:
            self.get('IgmpPrefixLength')
        return self._IgmpPrefixLength

    @property
    def IgmpIncrement(self):
        """
        get the value of property _IgmpIncrement
        """
        if self.force_auto_sync:
            self.get('IgmpIncrement')
        return self._IgmpIncrement

    @property
    def SourceCount(self):
        """
        get the value of property _SourceCount
        """
        if self.force_auto_sync:
            self.get('SourceCount')
        return self._SourceCount

    @IgmpDeviceGroupMapping.setter
    def IgmpDeviceGroupMapping(self, value):
        self._IgmpDeviceGroupMapping = value
        self.edit(IgmpDeviceGroupMapping=value)

    @IgmpSourceFilterMode.setter
    def IgmpSourceFilterMode(self, value):
        self._IgmpSourceFilterMode = value
        self.edit(IgmpSourceFilterMode=value)

    @IgmpUserDefinedSources.setter
    def IgmpUserDefinedSources(self, value):
        self._IgmpUserDefinedSources = value
        self.edit(IgmpUserDefinedSources=value)

    @IgmpSpecifySourcesAsList.setter
    def IgmpSpecifySourcesAsList(self, value):
        self._IgmpSpecifySourcesAsList = value
        self.edit(IgmpSpecifySourcesAsList=value)

    @IgmpSourceAddressList.setter
    def IgmpSourceAddressList(self, value):
        self._IgmpSourceAddressList = value
        self.edit(IgmpSourceAddressList=value)

    @IgmpNumberOfSources.setter
    def IgmpNumberOfSources(self, value):
        self._IgmpNumberOfSources = value
        self.edit(IgmpNumberOfSources=value)

    @IgmpStartingSourceIp.setter
    def IgmpStartingSourceIp(self, value):
        self._IgmpStartingSourceIp = value
        self.edit(IgmpStartingSourceIp=value)

    @IgmpPrefixLength.setter
    def IgmpPrefixLength(self, value):
        self._IgmpPrefixLength = value
        self.edit(IgmpPrefixLength=value)

    @IgmpIncrement.setter
    def IgmpIncrement(self, value):
        self._IgmpIncrement = value
        self.edit(IgmpIncrement=value)

    def _set_igmpnumberofgroups_with_str(self, value):
        try:
            self._IgmpNumberOfGroups = int(value)
        except ValueError:
            self._IgmpNumberOfGroups = hex(int(value, 16))

    def _set_igmpdevicegroupmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpDeviceGroupMapping = EnumIgmpDeviceGroupMapping.%s' % value[:seperate])

    def _set_igmpsourcefiltermode_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgmpSourceFilterMode = EnumIgmpSourceFilterMode.%s' % value[:seperate])

    def _set_igmpfilternumberofsources_with_str(self, value):
        try:
            self._IgmpFilterNumberOfSources = int(value)
        except ValueError:
            self._IgmpFilterNumberOfSources = hex(int(value, 16))

    def _set_igmpuserdefinedsources_with_str(self, value):
        self._IgmpUserDefinedSources = (value == 'True')

    def _set_igmpspecifysourcesaslist_with_str(self, value):
        self._IgmpSpecifySourcesAsList = (value == 'True')

    def _set_igmpsourceaddresslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpSourceAddressList = tmp_value.split()

    def _set_igmpnumberofsources_with_str(self, value):
        try:
            self._IgmpNumberOfSources = int(value)
        except ValueError:
            self._IgmpNumberOfSources = hex(int(value, 16))

    def _set_igmpstartingsourceip_with_str(self, value):
        self._IgmpStartingSourceIp = value

    def _set_igmpprefixlength_with_str(self, value):
        try:
            self._IgmpPrefixLength = int(value)
        except ValueError:
            self._IgmpPrefixLength = hex(int(value, 16))

    def _set_igmpincrement_with_str(self, value):
        try:
            self._IgmpIncrement = int(value)
        except ValueError:
            self._IgmpIncrement = hex(int(value, 16))

    def _set_sourcecount_with_str(self, value):
        try:
            self._SourceCount = int(value)
        except ValueError:
            self._SourceCount = hex(int(value, 16))

