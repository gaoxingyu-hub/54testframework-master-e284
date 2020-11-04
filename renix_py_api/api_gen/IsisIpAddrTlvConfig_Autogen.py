"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisIpAddrTlvConfig(ROMObject):
    def __init__(self, Handle=None, RouteType=None, RouteCount=None, Increment=None, MetricType=None, WideMetric=None, UpDownBit=None, **kwargs):
        self._Handle = Handle  # Handle
        self._RouteType = RouteType  # Route Type
        self._RouteCount = RouteCount  # Number of Routes
        self._Increment = Increment  # Increment
        self._MetricType = MetricType  # Metric Type
        self._WideMetric = WideMetric  # Wide Metric
        self._UpDownBit = UpDownBit  # Up/Down Bit

        properties = kwargs.copy()
        if Handle is not None:
            properties['Handle'] = Handle
        if RouteType is not None:
            properties['RouteType'] = RouteType
        if RouteCount is not None:
            properties['RouteCount'] = RouteCount
        if Increment is not None:
            properties['Increment'] = Increment
        if MetricType is not None:
            properties['MetricType'] = MetricType
        if WideMetric is not None:
            properties['WideMetric'] = WideMetric
        if UpDownBit is not None:
            properties['UpDownBit'] = UpDownBit

        # call base class function, and it will send message to renix server to create a class.
        super(IsisIpAddrTlvConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Handle=None, RouteType=None, RouteCount=None, Increment=None, MetricType=None, WideMetric=None, UpDownBit=None, **kwargs):
        properties = kwargs.copy()
        if Handle is not None:
            self._Handle = Handle
            properties['Handle'] = Handle
        if RouteType is not None:
            self._RouteType = RouteType
            properties['RouteType'] = RouteType
        if RouteCount is not None:
            self._RouteCount = RouteCount
            properties['RouteCount'] = RouteCount
        if Increment is not None:
            self._Increment = Increment
            properties['Increment'] = Increment
        if MetricType is not None:
            self._MetricType = MetricType
            properties['MetricType'] = MetricType
        if WideMetric is not None:
            self._WideMetric = WideMetric
            properties['WideMetric'] = WideMetric
        if UpDownBit is not None:
            self._UpDownBit = UpDownBit
            properties['UpDownBit'] = UpDownBit

        super(IsisIpAddrTlvConfig, self).edit(**properties)

    @property
    def Handle(self):
        """
        get the value of property _Handle
        """
        if self.force_auto_sync:
            self.get('Handle')
        return self._Handle

    @property
    def RouteType(self):
        """
        get the value of property _RouteType
        """
        if self.force_auto_sync:
            self.get('RouteType')
        return self._RouteType

    @property
    def RouteCount(self):
        """
        get the value of property _RouteCount
        """
        if self.force_auto_sync:
            self.get('RouteCount')
        return self._RouteCount

    @property
    def Increment(self):
        """
        get the value of property _Increment
        """
        if self.force_auto_sync:
            self.get('Increment')
        return self._Increment

    @property
    def MetricType(self):
        """
        get the value of property _MetricType
        """
        if self.force_auto_sync:
            self.get('MetricType')
        return self._MetricType

    @property
    def WideMetric(self):
        """
        get the value of property _WideMetric
        """
        if self.force_auto_sync:
            self.get('WideMetric')
        return self._WideMetric

    @property
    def UpDownBit(self):
        """
        get the value of property _UpDownBit
        """
        if self.force_auto_sync:
            self.get('UpDownBit')
        return self._UpDownBit

    @Handle.setter
    def Handle(self, value):
        self._Handle = value
        self.edit(Handle=value)

    @RouteType.setter
    def RouteType(self, value):
        self._RouteType = value
        self.edit(RouteType=value)

    @RouteCount.setter
    def RouteCount(self, value):
        self._RouteCount = value
        self.edit(RouteCount=value)

    @Increment.setter
    def Increment(self, value):
        self._Increment = value
        self.edit(Increment=value)

    @MetricType.setter
    def MetricType(self, value):
        self._MetricType = value
        self.edit(MetricType=value)

    @WideMetric.setter
    def WideMetric(self, value):
        self._WideMetric = value
        self.edit(WideMetric=value)

    @UpDownBit.setter
    def UpDownBit(self, value):
        self._UpDownBit = value
        self.edit(UpDownBit=value)

    def _set_handle_with_str(self, value):
        try:
            self._Handle = int(value)
        except ValueError:
            self._Handle = hex(int(value, 16))

    def _set_routetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RouteType = EnumRouteMeTricType.%s' % value[:seperate])

    def _set_routecount_with_str(self, value):
        try:
            self._RouteCount = int(value)
        except ValueError:
            self._RouteCount = hex(int(value, 16))

    def _set_increment_with_str(self, value):
        try:
            self._Increment = int(value)
        except ValueError:
            self._Increment = hex(int(value, 16))

    def _set_metrictype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MetricType = EnumRouteMeTricType.%s' % value[:seperate])

    def _set_widemetric_with_str(self, value):
        try:
            self._WideMetric = int(value)
        except ValueError:
            self._WideMetric = hex(int(value, 16))

    def _set_updownbit_with_str(self, value):
        self._UpDownBit = (value == 'True')

