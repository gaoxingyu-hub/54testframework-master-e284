"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ChartResultSeries(ROMObject):
    def __init__(self, ResultSourceHandle=None, TreeListHandle=None, ObjectType=None, ObjectName=None, StatisticName=None, ParameterName=None, ParameterDisplayName=None, ResourceKey=None, Unit=None, Location=None, **kwargs):
        self._ResultSourceHandle = ResultSourceHandle  # Result Source
        self._TreeListHandle = TreeListHandle  # Tree List
        self._ObjectType = ObjectType  # Object Type
        self._ObjectName = ObjectName  # Object Name
        self._StatisticName = StatisticName  # Statistic Name
        self._ParameterName = ParameterName  # Parameter Name
        self._ParameterDisplayName = ParameterDisplayName  # Parameter Display Name
        self._ResourceKey = ResourceKey  # Resource Key
        self._Unit = Unit  # Unit
        self._Location = Location  # Location
        self._Value = 0.0  # Value, not editable

        properties = kwargs.copy()
        if ResultSourceHandle is not None:
            properties['ResultSourceHandle'] = ResultSourceHandle
        if TreeListHandle is not None:
            properties['TreeListHandle'] = TreeListHandle
        if ObjectType is not None:
            properties['ObjectType'] = ObjectType
        if ObjectName is not None:
            properties['ObjectName'] = ObjectName
        if StatisticName is not None:
            properties['StatisticName'] = StatisticName
        if ParameterName is not None:
            properties['ParameterName'] = ParameterName
        if ParameterDisplayName is not None:
            properties['ParameterDisplayName'] = ParameterDisplayName
        if ResourceKey is not None:
            properties['ResourceKey'] = ResourceKey
        if Unit is not None:
            properties['Unit'] = Unit
        if Location is not None:
            properties['Location'] = Location

        # call base class function, and it will send message to renix server to create a class.
        super(ChartResultSeries, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ResultSourceHandle=None, TreeListHandle=None, ObjectType=None, ObjectName=None, StatisticName=None, ParameterName=None, ParameterDisplayName=None, ResourceKey=None, Unit=None, Location=None, **kwargs):
        properties = kwargs.copy()
        if ResultSourceHandle is not None:
            self._ResultSourceHandle = ResultSourceHandle
            properties['ResultSourceHandle'] = ResultSourceHandle
        if TreeListHandle is not None:
            self._TreeListHandle = TreeListHandle
            properties['TreeListHandle'] = TreeListHandle
        if ObjectType is not None:
            self._ObjectType = ObjectType
            properties['ObjectType'] = ObjectType
        if ObjectName is not None:
            self._ObjectName = ObjectName
            properties['ObjectName'] = ObjectName
        if StatisticName is not None:
            self._StatisticName = StatisticName
            properties['StatisticName'] = StatisticName
        if ParameterName is not None:
            self._ParameterName = ParameterName
            properties['ParameterName'] = ParameterName
        if ParameterDisplayName is not None:
            self._ParameterDisplayName = ParameterDisplayName
            properties['ParameterDisplayName'] = ParameterDisplayName
        if ResourceKey is not None:
            self._ResourceKey = ResourceKey
            properties['ResourceKey'] = ResourceKey
        if Unit is not None:
            self._Unit = Unit
            properties['Unit'] = Unit
        if Location is not None:
            self._Location = Location
            properties['Location'] = Location

        super(ChartResultSeries, self).edit(**properties)

    @property
    def ResultSourceHandle(self):
        """
        get the value of property _ResultSourceHandle
        """
        if self.force_auto_sync:
            self.get('ResultSourceHandle')
        return self._ResultSourceHandle

    @property
    def TreeListHandle(self):
        """
        get the value of property _TreeListHandle
        """
        if self.force_auto_sync:
            self.get('TreeListHandle')
        return self._TreeListHandle

    @property
    def ObjectType(self):
        """
        get the value of property _ObjectType
        """
        if self.force_auto_sync:
            self.get('ObjectType')
        return self._ObjectType

    @property
    def ObjectName(self):
        """
        get the value of property _ObjectName
        """
        if self.force_auto_sync:
            self.get('ObjectName')
        return self._ObjectName

    @property
    def StatisticName(self):
        """
        get the value of property _StatisticName
        """
        if self.force_auto_sync:
            self.get('StatisticName')
        return self._StatisticName

    @property
    def ParameterName(self):
        """
        get the value of property _ParameterName
        """
        if self.force_auto_sync:
            self.get('ParameterName')
        return self._ParameterName

    @property
    def ParameterDisplayName(self):
        """
        get the value of property _ParameterDisplayName
        """
        if self.force_auto_sync:
            self.get('ParameterDisplayName')
        return self._ParameterDisplayName

    @property
    def ResourceKey(self):
        """
        get the value of property _ResourceKey
        """
        if self.force_auto_sync:
            self.get('ResourceKey')
        return self._ResourceKey

    @property
    def Unit(self):
        """
        get the value of property _Unit
        """
        if self.force_auto_sync:
            self.get('Unit')
        return self._Unit

    @property
    def Location(self):
        """
        get the value of property _Location
        """
        if self.force_auto_sync:
            self.get('Location')
        return self._Location

    @property
    def Value(self):
        """
        get the value of property _Value
        """
        if self.force_auto_sync:
            self.get('Value')
        return self._Value

    @ResultSourceHandle.setter
    def ResultSourceHandle(self, value):
        self._ResultSourceHandle = value
        self.edit(ResultSourceHandle=value)

    @TreeListHandle.setter
    def TreeListHandle(self, value):
        self._TreeListHandle = value
        self.edit(TreeListHandle=value)

    @ObjectType.setter
    def ObjectType(self, value):
        self._ObjectType = value
        self.edit(ObjectType=value)

    @ObjectName.setter
    def ObjectName(self, value):
        self._ObjectName = value
        self.edit(ObjectName=value)

    @StatisticName.setter
    def StatisticName(self, value):
        self._StatisticName = value
        self.edit(StatisticName=value)

    @ParameterName.setter
    def ParameterName(self, value):
        self._ParameterName = value
        self.edit(ParameterName=value)

    @ParameterDisplayName.setter
    def ParameterDisplayName(self, value):
        self._ParameterDisplayName = value
        self.edit(ParameterDisplayName=value)

    @ResourceKey.setter
    def ResourceKey(self, value):
        self._ResourceKey = value
        self.edit(ResourceKey=value)

    @Unit.setter
    def Unit(self, value):
        self._Unit = value
        self.edit(Unit=value)

    @Location.setter
    def Location(self, value):
        self._Location = value
        self.edit(Location=value)

    def _set_resultsourcehandle_with_str(self, value):
        self._ResultSourceHandle = value

    def _set_treelisthandle_with_str(self, value):
        self._TreeListHandle = value

    def _set_objecttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ObjectType = EnumChartObjectType.%s' % value[:seperate])

    def _set_objectname_with_str(self, value):
        self._ObjectName = value

    def _set_statisticname_with_str(self, value):
        self._StatisticName = value

    def _set_parametername_with_str(self, value):
        self._ParameterName = value

    def _set_parameterdisplayname_with_str(self, value):
        self._ParameterDisplayName = value

    def _set_resourcekey_with_str(self, value):
        self._ResourceKey = value

    def _set_unit_with_str(self, value):
        self._Unit = value

    def _set_location_with_str(self, value):
        self._Location = value

    def _set_value_with_str(self, value):
        self._Value = float(value)

