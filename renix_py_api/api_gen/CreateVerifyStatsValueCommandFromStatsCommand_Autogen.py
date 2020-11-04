"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateVerifyStatsValueCommandFromStatsCommand(ROMCommand):
    def __init__(self, ConditionHandle=None, StatsHandle=None, ColumnName=None, **kwargs):
        self._ConditionHandle = ConditionHandle  # Existing Condition Handle
        self._StatsHandle = StatsHandle  # Statistic Object Handle
        self._ColumnName = ColumnName  # Result Column Name
        self._CreatedObject = ''  # Created Object Handle, not editable

        properties = kwargs.copy()
        if ConditionHandle is not None:
            properties['ConditionHandle'] = ConditionHandle
        if StatsHandle is not None:
            properties['StatsHandle'] = StatsHandle
        if ColumnName is not None:
            properties['ColumnName'] = ColumnName

        # call base class function, and it will send message to renix server to create a class.
        super(CreateVerifyStatsValueCommandFromStatsCommand, self).__init__(**properties)

    @property
    def ConditionHandle(self):
        """
        get the value of property _ConditionHandle
        """
        return self._ConditionHandle

    @property
    def StatsHandle(self):
        """
        get the value of property _StatsHandle
        """
        return self._StatsHandle

    @property
    def ColumnName(self):
        """
        get the value of property _ColumnName
        """
        return self._ColumnName

    @property
    def CreatedObject(self):
        """
        get the value of property _CreatedObject
        """
        return self._CreatedObject

    @ConditionHandle.setter
    def ConditionHandle(self, value):
        self._ConditionHandle = value

    @StatsHandle.setter
    def StatsHandle(self, value):
        self._StatsHandle = value

    @ColumnName.setter
    def ColumnName(self, value):
        self._ColumnName = value

    def _set_conditionhandle_with_str(self, value):
        self._ConditionHandle = value

    def _set_statshandle_with_str(self, value):
        self._StatsHandle = value

    def _set_columnname_with_str(self, value):
        self._ColumnName = value

    def _set_createdobject_with_str(self, value):
        self._CreatedObject = value

    def _set_output_property(self, value):
        self._set_createdobject_with_str(value)

