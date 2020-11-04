"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class VerifyStatsValueCommand(ROMCommand):
    def __init__(self, QueryCount=None, ExpectCondition=None, **kwargs):
        self._QueryCount = QueryCount  # Query Count
        self._ExpectCondition = ExpectCondition  # Expect Condition

        properties = kwargs.copy()
        if QueryCount is not None:
            properties['QueryCount'] = QueryCount
        if ExpectCondition is not None:
            properties['ExpectCondition'] = ExpectCondition

        # call base class function, and it will send message to renix server to create a class.
        super(VerifyStatsValueCommand, self).__init__(**properties)

    @property
    def QueryCount(self):
        """
        get the value of property _QueryCount
        """
        return self._QueryCount

    @property
    def ExpectCondition(self):
        """
        get the value of property _ExpectCondition
        """
        return self._ExpectCondition

    @QueryCount.setter
    def QueryCount(self, value):
        self._QueryCount = value

    @ExpectCondition.setter
    def ExpectCondition(self, value):
        self._ExpectCondition = value

    def _set_querycount_with_str(self, value):
        try:
            self._QueryCount = int(value)
        except ValueError:
            self._QueryCount = hex(int(value, 16))

    def _set_expectcondition_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExpectCondition = EnumBoolean.%s' % value[:seperate])

