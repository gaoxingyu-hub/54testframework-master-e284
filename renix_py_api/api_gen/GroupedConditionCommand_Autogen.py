"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .GroupCommand_Autogen import GroupCommand


@rom_manager.rom
class GroupedConditionCommand(GroupCommand):
    def __init__(self, ExpectCondition=None, **kwargs):
        self._ExpectCondition = ExpectCondition  # Expect Condition

        properties = kwargs.copy()
        if ExpectCondition is not None:
            properties['ExpectCondition'] = ExpectCondition

        # call base class function, and it will send message to renix server to create a class.
        super(GroupedConditionCommand, self).__init__(**properties)

    @property
    def ExpectCondition(self):
        """
        get the value of property _ExpectCondition
        """
        return self._ExpectCondition

    @ExpectCondition.setter
    def ExpectCondition(self, value):
        self._ExpectCondition = value

    def _set_expectcondition_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExpectCondition = EnumExpectCondition.%s' % value[:seperate])

