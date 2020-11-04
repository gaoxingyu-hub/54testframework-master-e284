"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class VerifyStatsValueCondition(ROMObject):
    def __init__(self, LeftStatsHandle=None, LeftObjectHandles=None, LeftDataClassName=None, LeftColumnName=None, NotOperator=None, CompareOperator=None, CompareTarget=None, CompareValue=None, StringCompareValue=None, RightStatsHandle=None, RightObjectHandles=None, RightDataClassName=None, RightColumnName=None, BoolOperator=None, **kwargs):
        self._LeftStatsHandle = LeftStatsHandle  # Left Statistic Object Handle
        self._LeftObjectHandles = LeftObjectHandles  # Object Handles
        self._LeftDataClassName = LeftDataClassName  # Result Class Name
        self._LeftColumnName = LeftColumnName  # Result Column Name
        self._NotOperator = NotOperator  # NOT
        self._CompareOperator = CompareOperator  # Operator
        self._CompareTarget = CompareTarget  # Compare Target
        self._CompareValue = CompareValue  # Value
        self._StringCompareValue = StringCompareValue  # Value
        self._RightStatsHandle = RightStatsHandle  # Right Statistic Object Handle
        self._RightObjectHandles = RightObjectHandles  # Object Handles
        self._RightDataClassName = RightDataClassName  # Result Class Name
        self._RightColumnName = RightColumnName  # Result Column Name
        self._BoolOperator = BoolOperator  # Boolean Operator

        properties = kwargs.copy()
        if LeftStatsHandle is not None:
            properties['LeftStatsHandle'] = LeftStatsHandle
        if LeftObjectHandles is not None:
            properties['LeftObjectHandles'] = LeftObjectHandles
        if LeftDataClassName is not None:
            properties['LeftDataClassName'] = LeftDataClassName
        if LeftColumnName is not None:
            properties['LeftColumnName'] = LeftColumnName
        if NotOperator is not None:
            properties['NotOperator'] = NotOperator
        if CompareOperator is not None:
            properties['CompareOperator'] = CompareOperator
        if CompareTarget is not None:
            properties['CompareTarget'] = CompareTarget
        if CompareValue is not None:
            properties['CompareValue'] = CompareValue
        if StringCompareValue is not None:
            properties['StringCompareValue'] = StringCompareValue
        if RightStatsHandle is not None:
            properties['RightStatsHandle'] = RightStatsHandle
        if RightObjectHandles is not None:
            properties['RightObjectHandles'] = RightObjectHandles
        if RightDataClassName is not None:
            properties['RightDataClassName'] = RightDataClassName
        if RightColumnName is not None:
            properties['RightColumnName'] = RightColumnName
        if BoolOperator is not None:
            properties['BoolOperator'] = BoolOperator

        # call base class function, and it will send message to renix server to create a class.
        super(VerifyStatsValueCondition, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LeftStatsHandle=None, LeftObjectHandles=None, LeftDataClassName=None, LeftColumnName=None, NotOperator=None, CompareOperator=None, CompareTarget=None, CompareValue=None, StringCompareValue=None, RightStatsHandle=None, RightObjectHandles=None, RightDataClassName=None, RightColumnName=None, BoolOperator=None, **kwargs):
        properties = kwargs.copy()
        if LeftStatsHandle is not None:
            self._LeftStatsHandle = LeftStatsHandle
            properties['LeftStatsHandle'] = LeftStatsHandle
        if LeftObjectHandles is not None:
            self._LeftObjectHandles = LeftObjectHandles
            properties['LeftObjectHandles'] = LeftObjectHandles
        if LeftDataClassName is not None:
            self._LeftDataClassName = LeftDataClassName
            properties['LeftDataClassName'] = LeftDataClassName
        if LeftColumnName is not None:
            self._LeftColumnName = LeftColumnName
            properties['LeftColumnName'] = LeftColumnName
        if NotOperator is not None:
            self._NotOperator = NotOperator
            properties['NotOperator'] = NotOperator
        if CompareOperator is not None:
            self._CompareOperator = CompareOperator
            properties['CompareOperator'] = CompareOperator
        if CompareTarget is not None:
            self._CompareTarget = CompareTarget
            properties['CompareTarget'] = CompareTarget
        if CompareValue is not None:
            self._CompareValue = CompareValue
            properties['CompareValue'] = CompareValue
        if StringCompareValue is not None:
            self._StringCompareValue = StringCompareValue
            properties['StringCompareValue'] = StringCompareValue
        if RightStatsHandle is not None:
            self._RightStatsHandle = RightStatsHandle
            properties['RightStatsHandle'] = RightStatsHandle
        if RightObjectHandles is not None:
            self._RightObjectHandles = RightObjectHandles
            properties['RightObjectHandles'] = RightObjectHandles
        if RightDataClassName is not None:
            self._RightDataClassName = RightDataClassName
            properties['RightDataClassName'] = RightDataClassName
        if RightColumnName is not None:
            self._RightColumnName = RightColumnName
            properties['RightColumnName'] = RightColumnName
        if BoolOperator is not None:
            self._BoolOperator = BoolOperator
            properties['BoolOperator'] = BoolOperator

        super(VerifyStatsValueCondition, self).edit(**properties)

    @property
    def LeftStatsHandle(self):
        """
        get the value of property _LeftStatsHandle
        """
        if self.force_auto_sync:
            self.get('LeftStatsHandle')
        return self._LeftStatsHandle

    @property
    def LeftObjectHandles(self):
        """
        get the value of property _LeftObjectHandles
        """
        if self.force_auto_sync:
            self.get('LeftObjectHandles')
        return self._LeftObjectHandles

    @property
    def LeftDataClassName(self):
        """
        get the value of property _LeftDataClassName
        """
        if self.force_auto_sync:
            self.get('LeftDataClassName')
        return self._LeftDataClassName

    @property
    def LeftColumnName(self):
        """
        get the value of property _LeftColumnName
        """
        if self.force_auto_sync:
            self.get('LeftColumnName')
        return self._LeftColumnName

    @property
    def NotOperator(self):
        """
        get the value of property _NotOperator
        """
        if self.force_auto_sync:
            self.get('NotOperator')
        return self._NotOperator

    @property
    def CompareOperator(self):
        """
        get the value of property _CompareOperator
        """
        if self.force_auto_sync:
            self.get('CompareOperator')
        return self._CompareOperator

    @property
    def CompareTarget(self):
        """
        get the value of property _CompareTarget
        """
        if self.force_auto_sync:
            self.get('CompareTarget')
        return self._CompareTarget

    @property
    def CompareValue(self):
        """
        get the value of property _CompareValue
        """
        if self.force_auto_sync:
            self.get('CompareValue')
        return self._CompareValue

    @property
    def StringCompareValue(self):
        """
        get the value of property _StringCompareValue
        """
        if self.force_auto_sync:
            self.get('StringCompareValue')
        return self._StringCompareValue

    @property
    def RightStatsHandle(self):
        """
        get the value of property _RightStatsHandle
        """
        if self.force_auto_sync:
            self.get('RightStatsHandle')
        return self._RightStatsHandle

    @property
    def RightObjectHandles(self):
        """
        get the value of property _RightObjectHandles
        """
        if self.force_auto_sync:
            self.get('RightObjectHandles')
        return self._RightObjectHandles

    @property
    def RightDataClassName(self):
        """
        get the value of property _RightDataClassName
        """
        if self.force_auto_sync:
            self.get('RightDataClassName')
        return self._RightDataClassName

    @property
    def RightColumnName(self):
        """
        get the value of property _RightColumnName
        """
        if self.force_auto_sync:
            self.get('RightColumnName')
        return self._RightColumnName

    @property
    def BoolOperator(self):
        """
        get the value of property _BoolOperator
        """
        if self.force_auto_sync:
            self.get('BoolOperator')
        return self._BoolOperator

    @LeftStatsHandle.setter
    def LeftStatsHandle(self, value):
        self._LeftStatsHandle = value
        self.edit(LeftStatsHandle=value)

    @LeftObjectHandles.setter
    def LeftObjectHandles(self, value):
        self._LeftObjectHandles = value
        self.edit(LeftObjectHandles=value)

    @LeftDataClassName.setter
    def LeftDataClassName(self, value):
        self._LeftDataClassName = value
        self.edit(LeftDataClassName=value)

    @LeftColumnName.setter
    def LeftColumnName(self, value):
        self._LeftColumnName = value
        self.edit(LeftColumnName=value)

    @NotOperator.setter
    def NotOperator(self, value):
        self._NotOperator = value
        self.edit(NotOperator=value)

    @CompareOperator.setter
    def CompareOperator(self, value):
        self._CompareOperator = value
        self.edit(CompareOperator=value)

    @CompareTarget.setter
    def CompareTarget(self, value):
        self._CompareTarget = value
        self.edit(CompareTarget=value)

    @CompareValue.setter
    def CompareValue(self, value):
        self._CompareValue = value
        self.edit(CompareValue=value)

    @StringCompareValue.setter
    def StringCompareValue(self, value):
        self._StringCompareValue = value
        self.edit(StringCompareValue=value)

    @RightStatsHandle.setter
    def RightStatsHandle(self, value):
        self._RightStatsHandle = value
        self.edit(RightStatsHandle=value)

    @RightObjectHandles.setter
    def RightObjectHandles(self, value):
        self._RightObjectHandles = value
        self.edit(RightObjectHandles=value)

    @RightDataClassName.setter
    def RightDataClassName(self, value):
        self._RightDataClassName = value
        self.edit(RightDataClassName=value)

    @RightColumnName.setter
    def RightColumnName(self, value):
        self._RightColumnName = value
        self.edit(RightColumnName=value)

    @BoolOperator.setter
    def BoolOperator(self, value):
        self._BoolOperator = value
        self.edit(BoolOperator=value)

    def _set_leftstatshandle_with_str(self, value):
        self._LeftStatsHandle = value

    def _set_leftobjecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LeftObjectHandles = tmp_value.split()

    def _set_leftdataclassname_with_str(self, value):
        self._LeftDataClassName = value

    def _set_leftcolumnname_with_str(self, value):
        self._LeftColumnName = value

    def _set_notoperator_with_str(self, value):
        self._NotOperator = (value == 'True')

    def _set_compareoperator_with_str(self, value):
        seperate = value.find(':')
        exec('self._CompareOperator = EnumWaitOperator.%s' % value[:seperate])

    def _set_comparetarget_with_str(self, value):
        seperate = value.find(':')
        exec('self._CompareTarget = EnumCompareTarget.%s' % value[:seperate])

    def _set_comparevalue_with_str(self, value):
        self._CompareValue = float(value)

    def _set_stringcomparevalue_with_str(self, value):
        self._StringCompareValue = value

    def _set_rightstatshandle_with_str(self, value):
        self._RightStatsHandle = value

    def _set_rightobjecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RightObjectHandles = tmp_value.split()

    def _set_rightdataclassname_with_str(self, value):
        self._RightDataClassName = value

    def _set_rightcolumnname_with_str(self, value):
        self._RightColumnName = value

    def _set_booloperator_with_str(self, value):
        seperate = value.find(':')
        exec('self._BoolOperator = EnumBoolOperator.%s' % value[:seperate])

