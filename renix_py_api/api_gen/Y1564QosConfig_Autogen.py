"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Y1564QosConfig(ROMObject):
    def __init__(self, QosType=None, TosValue=None, TosCount=None, TosStep=None, DscpValue=None, DscpCount=None, DscpStep=None, TrafficClassValue=None, TrafficClassCount=None, TrafficClassStep=None, **kwargs):
        self._QosType = QosType  # Qos Type
        self._TosValue = TosValue  # Tos Value
        self._TosCount = TosCount  # Tos Count
        self._TosStep = TosStep  # Tos Step
        self._DscpValue = DscpValue  # Dscp Value
        self._DscpCount = DscpCount  # Dscp Count
        self._DscpStep = DscpStep  # Dscp Step
        self._TrafficClassValue = TrafficClassValue  # TrafficClass Value
        self._TrafficClassCount = TrafficClassCount  # TrafficClass Count
        self._TrafficClassStep = TrafficClassStep  # TrafficClass Step

        properties = kwargs.copy()
        if QosType is not None:
            properties['QosType'] = QosType
        if TosValue is not None:
            properties['TosValue'] = TosValue
        if TosCount is not None:
            properties['TosCount'] = TosCount
        if TosStep is not None:
            properties['TosStep'] = TosStep
        if DscpValue is not None:
            properties['DscpValue'] = DscpValue
        if DscpCount is not None:
            properties['DscpCount'] = DscpCount
        if DscpStep is not None:
            properties['DscpStep'] = DscpStep
        if TrafficClassValue is not None:
            properties['TrafficClassValue'] = TrafficClassValue
        if TrafficClassCount is not None:
            properties['TrafficClassCount'] = TrafficClassCount
        if TrafficClassStep is not None:
            properties['TrafficClassStep'] = TrafficClassStep

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564QosConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, QosType=None, TosValue=None, TosCount=None, TosStep=None, DscpValue=None, DscpCount=None, DscpStep=None, TrafficClassValue=None, TrafficClassCount=None, TrafficClassStep=None, **kwargs):
        properties = kwargs.copy()
        if QosType is not None:
            self._QosType = QosType
            properties['QosType'] = QosType
        if TosValue is not None:
            self._TosValue = TosValue
            properties['TosValue'] = TosValue
        if TosCount is not None:
            self._TosCount = TosCount
            properties['TosCount'] = TosCount
        if TosStep is not None:
            self._TosStep = TosStep
            properties['TosStep'] = TosStep
        if DscpValue is not None:
            self._DscpValue = DscpValue
            properties['DscpValue'] = DscpValue
        if DscpCount is not None:
            self._DscpCount = DscpCount
            properties['DscpCount'] = DscpCount
        if DscpStep is not None:
            self._DscpStep = DscpStep
            properties['DscpStep'] = DscpStep
        if TrafficClassValue is not None:
            self._TrafficClassValue = TrafficClassValue
            properties['TrafficClassValue'] = TrafficClassValue
        if TrafficClassCount is not None:
            self._TrafficClassCount = TrafficClassCount
            properties['TrafficClassCount'] = TrafficClassCount
        if TrafficClassStep is not None:
            self._TrafficClassStep = TrafficClassStep
            properties['TrafficClassStep'] = TrafficClassStep

        super(Y1564QosConfig, self).edit(**properties)

    @property
    def QosType(self):
        """
        get the value of property _QosType
        """
        if self.force_auto_sync:
            self.get('QosType')
        return self._QosType

    @property
    def TosValue(self):
        """
        get the value of property _TosValue
        """
        if self.force_auto_sync:
            self.get('TosValue')
        return self._TosValue

    @property
    def TosCount(self):
        """
        get the value of property _TosCount
        """
        if self.force_auto_sync:
            self.get('TosCount')
        return self._TosCount

    @property
    def TosStep(self):
        """
        get the value of property _TosStep
        """
        if self.force_auto_sync:
            self.get('TosStep')
        return self._TosStep

    @property
    def DscpValue(self):
        """
        get the value of property _DscpValue
        """
        if self.force_auto_sync:
            self.get('DscpValue')
        return self._DscpValue

    @property
    def DscpCount(self):
        """
        get the value of property _DscpCount
        """
        if self.force_auto_sync:
            self.get('DscpCount')
        return self._DscpCount

    @property
    def DscpStep(self):
        """
        get the value of property _DscpStep
        """
        if self.force_auto_sync:
            self.get('DscpStep')
        return self._DscpStep

    @property
    def TrafficClassValue(self):
        """
        get the value of property _TrafficClassValue
        """
        if self.force_auto_sync:
            self.get('TrafficClassValue')
        return self._TrafficClassValue

    @property
    def TrafficClassCount(self):
        """
        get the value of property _TrafficClassCount
        """
        if self.force_auto_sync:
            self.get('TrafficClassCount')
        return self._TrafficClassCount

    @property
    def TrafficClassStep(self):
        """
        get the value of property _TrafficClassStep
        """
        if self.force_auto_sync:
            self.get('TrafficClassStep')
        return self._TrafficClassStep

    @QosType.setter
    def QosType(self, value):
        self._QosType = value
        self.edit(QosType=value)

    @TosValue.setter
    def TosValue(self, value):
        self._TosValue = value
        self.edit(TosValue=value)

    @TosCount.setter
    def TosCount(self, value):
        self._TosCount = value
        self.edit(TosCount=value)

    @TosStep.setter
    def TosStep(self, value):
        self._TosStep = value
        self.edit(TosStep=value)

    @DscpValue.setter
    def DscpValue(self, value):
        self._DscpValue = value
        self.edit(DscpValue=value)

    @DscpCount.setter
    def DscpCount(self, value):
        self._DscpCount = value
        self.edit(DscpCount=value)

    @DscpStep.setter
    def DscpStep(self, value):
        self._DscpStep = value
        self.edit(DscpStep=value)

    @TrafficClassValue.setter
    def TrafficClassValue(self, value):
        self._TrafficClassValue = value
        self.edit(TrafficClassValue=value)

    @TrafficClassCount.setter
    def TrafficClassCount(self, value):
        self._TrafficClassCount = value
        self.edit(TrafficClassCount=value)

    @TrafficClassStep.setter
    def TrafficClassStep(self, value):
        self._TrafficClassStep = value
        self.edit(TrafficClassStep=value)

    def _set_qostype_with_str(self, value):
        seperate = value.find(':')
        exec('self._QosType = EnumQosType.%s' % value[:seperate])

    def _set_tosvalue_with_str(self, value):
        try:
            self._TosValue = int(value)
        except ValueError:
            self._TosValue = hex(int(value, 16))

    def _set_toscount_with_str(self, value):
        try:
            self._TosCount = int(value)
        except ValueError:
            self._TosCount = hex(int(value, 16))

    def _set_tosstep_with_str(self, value):
        try:
            self._TosStep = int(value)
        except ValueError:
            self._TosStep = hex(int(value, 16))

    def _set_dscpvalue_with_str(self, value):
        try:
            self._DscpValue = int(value)
        except ValueError:
            self._DscpValue = hex(int(value, 16))

    def _set_dscpcount_with_str(self, value):
        try:
            self._DscpCount = int(value)
        except ValueError:
            self._DscpCount = hex(int(value, 16))

    def _set_dscpstep_with_str(self, value):
        try:
            self._DscpStep = int(value)
        except ValueError:
            self._DscpStep = hex(int(value, 16))

    def _set_trafficclassvalue_with_str(self, value):
        try:
            self._TrafficClassValue = int(value)
        except ValueError:
            self._TrafficClassValue = hex(int(value, 16))

    def _set_trafficclasscount_with_str(self, value):
        try:
            self._TrafficClassCount = int(value)
        except ValueError:
            self._TrafficClassCount = hex(int(value, 16))

    def _set_trafficclassstep_with_str(self, value):
        try:
            self._TrafficClassStep = int(value)
        except ValueError:
            self._TrafficClassStep = hex(int(value, 16))

