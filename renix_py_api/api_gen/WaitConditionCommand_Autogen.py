"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class WaitConditionCommand(ROMCommand):
    def __init__(self, WaitTime=None, ObjectHandles=None, PropertyName=None, ExpectValue=None, WaitOperator=None, **kwargs):
        self._WaitTime = WaitTime  # Wait Time (sec)
        self._ObjectHandles = ObjectHandles  # Object Handles
        self._PropertyName = PropertyName  # Property Name
        self._ExpectValue = ExpectValue  # Expect Value
        self._WaitOperator = WaitOperator  # Wait Operator

        properties = kwargs.copy()
        if WaitTime is not None:
            properties['WaitTime'] = WaitTime
        if ObjectHandles is not None:
            properties['ObjectHandles'] = ObjectHandles
        if PropertyName is not None:
            properties['PropertyName'] = PropertyName
        if ExpectValue is not None:
            properties['ExpectValue'] = ExpectValue
        if WaitOperator is not None:
            properties['WaitOperator'] = WaitOperator

        # call base class function, and it will send message to renix server to create a class.
        super(WaitConditionCommand, self).__init__(**properties)

    @property
    def WaitTime(self):
        """
        get the value of property _WaitTime
        """
        return self._WaitTime

    @property
    def ObjectHandles(self):
        """
        get the value of property _ObjectHandles
        """
        return self._ObjectHandles

    @property
    def PropertyName(self):
        """
        get the value of property _PropertyName
        """
        return self._PropertyName

    @property
    def ExpectValue(self):
        """
        get the value of property _ExpectValue
        """
        return self._ExpectValue

    @property
    def WaitOperator(self):
        """
        get the value of property _WaitOperator
        """
        return self._WaitOperator

    @WaitTime.setter
    def WaitTime(self, value):
        self._WaitTime = value

    @ObjectHandles.setter
    def ObjectHandles(self, value):
        self._ObjectHandles = value

    @PropertyName.setter
    def PropertyName(self, value):
        self._PropertyName = value

    @ExpectValue.setter
    def ExpectValue(self, value):
        self._ExpectValue = value

    @WaitOperator.setter
    def WaitOperator(self, value):
        self._WaitOperator = value

    def _set_waittime_with_str(self, value):
        try:
            self._WaitTime = int(value)
        except ValueError:
            self._WaitTime = hex(int(value, 16))

    def _set_objecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectHandles = tmp_value.split()

    def _set_propertyname_with_str(self, value):
        self._PropertyName = value

    def _set_expectvalue_with_str(self, value):
        self._ExpectValue = value

    def _set_waitoperator_with_str(self, value):
        seperate = value.find(':')
        exec('self._WaitOperator = EnumWaitOperator.%s' % value[:seperate])

