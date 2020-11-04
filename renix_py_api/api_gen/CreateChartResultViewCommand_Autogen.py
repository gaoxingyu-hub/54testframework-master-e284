"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateChartResultViewCommand(ROMCommand):
    def __init__(self, ViewName=None, DataClassNames=None, ResultSourceHandles=None, TreeListHandles=None, ObjectTypes=None, ObjectNames=None, StatisticNames=None, ParameterNames=None, ParameterDisplayNames=None, ResourceKeys=None, Units=None, Locations=None, **kwargs):
        self._ViewName = ViewName  # View Name
        self._DataClassNames = DataClassNames  # Data Class Names
        self._ResultSourceHandles = ResultSourceHandles  # Result Source
        self._TreeListHandles = TreeListHandles  # Tree List
        self._ObjectTypes = ObjectTypes  # Object Types
        self._ObjectNames = ObjectNames  # Object Names
        self._StatisticNames = StatisticNames  # Statistic Names
        self._ParameterNames = ParameterNames  # Parameter Names
        self._ParameterDisplayNames = ParameterDisplayNames  # Parameter Display Names
        self._ResourceKeys = ResourceKeys  # Resource Keys
        self._Units = Units  # Units
        self._Locations = Locations  # Locations
        self._ResultViewHandles = None  # Result Views, not editable

        properties = kwargs.copy()
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if DataClassNames is not None:
            properties['DataClassNames'] = DataClassNames
        if ResultSourceHandles is not None:
            properties['ResultSourceHandles'] = ResultSourceHandles
        if TreeListHandles is not None:
            properties['TreeListHandles'] = TreeListHandles
        if ObjectTypes is not None:
            properties['ObjectTypes'] = ObjectTypes
        if ObjectNames is not None:
            properties['ObjectNames'] = ObjectNames
        if StatisticNames is not None:
            properties['StatisticNames'] = StatisticNames
        if ParameterNames is not None:
            properties['ParameterNames'] = ParameterNames
        if ParameterDisplayNames is not None:
            properties['ParameterDisplayNames'] = ParameterDisplayNames
        if ResourceKeys is not None:
            properties['ResourceKeys'] = ResourceKeys
        if Units is not None:
            properties['Units'] = Units
        if Locations is not None:
            properties['Locations'] = Locations

        # call base class function, and it will send message to renix server to create a class.
        super(CreateChartResultViewCommand, self).__init__(**properties)

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        return self._ViewName

    @property
    def DataClassNames(self):
        """
        get the value of property _DataClassNames
        """
        return self._DataClassNames

    @property
    def ResultSourceHandles(self):
        """
        get the value of property _ResultSourceHandles
        """
        return self._ResultSourceHandles

    @property
    def TreeListHandles(self):
        """
        get the value of property _TreeListHandles
        """
        return self._TreeListHandles

    @property
    def ObjectTypes(self):
        """
        get the value of property _ObjectTypes
        """
        return self._ObjectTypes

    @property
    def ObjectNames(self):
        """
        get the value of property _ObjectNames
        """
        return self._ObjectNames

    @property
    def StatisticNames(self):
        """
        get the value of property _StatisticNames
        """
        return self._StatisticNames

    @property
    def ParameterNames(self):
        """
        get the value of property _ParameterNames
        """
        return self._ParameterNames

    @property
    def ParameterDisplayNames(self):
        """
        get the value of property _ParameterDisplayNames
        """
        return self._ParameterDisplayNames

    @property
    def ResourceKeys(self):
        """
        get the value of property _ResourceKeys
        """
        return self._ResourceKeys

    @property
    def Units(self):
        """
        get the value of property _Units
        """
        return self._Units

    @property
    def Locations(self):
        """
        get the value of property _Locations
        """
        return self._Locations

    @property
    def ResultViewHandles(self):
        """
        get the value of property _ResultViewHandles
        """
        return self._ResultViewHandles

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value

    @DataClassNames.setter
    def DataClassNames(self, value):
        self._DataClassNames = value

    @ResultSourceHandles.setter
    def ResultSourceHandles(self, value):
        self._ResultSourceHandles = value

    @TreeListHandles.setter
    def TreeListHandles(self, value):
        self._TreeListHandles = value

    @ObjectTypes.setter
    def ObjectTypes(self, value):
        self._ObjectTypes = value

    @ObjectNames.setter
    def ObjectNames(self, value):
        self._ObjectNames = value

    @StatisticNames.setter
    def StatisticNames(self, value):
        self._StatisticNames = value

    @ParameterNames.setter
    def ParameterNames(self, value):
        self._ParameterNames = value

    @ParameterDisplayNames.setter
    def ParameterDisplayNames(self, value):
        self._ParameterDisplayNames = value

    @ResourceKeys.setter
    def ResourceKeys(self, value):
        self._ResourceKeys = value

    @Units.setter
    def Units(self, value):
        self._Units = value

    @Locations.setter
    def Locations(self, value):
        self._Locations = value

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_dataclassnames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DataClassNames = tmp_value.split()

    def _set_resultsourcehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ResultSourceHandles = tmp_value.split()

    def _set_treelisthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TreeListHandles = tmp_value.split()

    def _set_objecttypes_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectTypes = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumChartObjectType + '.' + str_value[:seperate]
            exec('self._ObjectTypes.append(%s)' %(enum_value))

    def _set_objectnames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectNames = tmp_value.split()

    def _set_statisticnames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StatisticNames = tmp_value.split()

    def _set_parameternames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ParameterNames = tmp_value.split()

    def _set_parameterdisplaynames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ParameterDisplayNames = tmp_value.split()

    def _set_resourcekeys_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ResourceKeys = tmp_value.split()

    def _set_units_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Units = tmp_value.split()

    def _set_locations_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Locations = tmp_value.split()

    def _set_resultviewhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ResultViewHandles = tmp_value.split()

    def _set_output_property(self, value):
        self._set_resultviewhandles_with_str(value)

