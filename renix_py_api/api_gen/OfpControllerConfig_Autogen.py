"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpProtocolConfig_Autogen import OfpProtocolConfig


@rom_manager.rom
class OfpControllerConfig(OfpProtocolConfig):
    def __init__(self, OpenFlowVersion=None, BarrierRequestTimeout=None, MaxFlowRate=None, **kwargs):
        self._OpenFlowVersion = OpenFlowVersion  # OpenFlow Version
        self._BarrierRequestTimeout = BarrierRequestTimeout  # Barrier Request Timeout (ms)
        self._MaxFlowRate = MaxFlowRate  # Max Flow Rate

        properties = kwargs.copy()
        if OpenFlowVersion is not None:
            properties['OpenFlowVersion'] = OpenFlowVersion
        if BarrierRequestTimeout is not None:
            properties['BarrierRequestTimeout'] = BarrierRequestTimeout
        if MaxFlowRate is not None:
            properties['MaxFlowRate'] = MaxFlowRate

        # call base class function, and it will send message to renix server to create a class.
        super(OfpControllerConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OpenFlowVersion=None, BarrierRequestTimeout=None, MaxFlowRate=None, **kwargs):
        properties = kwargs.copy()
        if OpenFlowVersion is not None:
            self._OpenFlowVersion = OpenFlowVersion
            properties['OpenFlowVersion'] = OpenFlowVersion
        if BarrierRequestTimeout is not None:
            self._BarrierRequestTimeout = BarrierRequestTimeout
            properties['BarrierRequestTimeout'] = BarrierRequestTimeout
        if MaxFlowRate is not None:
            self._MaxFlowRate = MaxFlowRate
            properties['MaxFlowRate'] = MaxFlowRate

        super(OfpControllerConfig, self).edit(**properties)

    @property
    def OpenFlowVersion(self):
        """
        get the value of property _OpenFlowVersion
        """
        if self.force_auto_sync:
            self.get('OpenFlowVersion')
        return self._OpenFlowVersion

    @property
    def BarrierRequestTimeout(self):
        """
        get the value of property _BarrierRequestTimeout
        """
        if self.force_auto_sync:
            self.get('BarrierRequestTimeout')
        return self._BarrierRequestTimeout

    @property
    def MaxFlowRate(self):
        """
        get the value of property _MaxFlowRate
        """
        if self.force_auto_sync:
            self.get('MaxFlowRate')
        return self._MaxFlowRate

    @OpenFlowVersion.setter
    def OpenFlowVersion(self, value):
        self._OpenFlowVersion = value
        self.edit(OpenFlowVersion=value)

    @BarrierRequestTimeout.setter
    def BarrierRequestTimeout(self, value):
        self._BarrierRequestTimeout = value
        self.edit(BarrierRequestTimeout=value)

    @MaxFlowRate.setter
    def MaxFlowRate(self, value):
        self._MaxFlowRate = value
        self.edit(MaxFlowRate=value)

    def _set_openflowversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._OpenFlowVersion = EnumOfpControllerVersion.%s' % value[:seperate])

    def _set_barrierrequesttimeout_with_str(self, value):
        try:
            self._BarrierRequestTimeout = int(value)
        except ValueError:
            self._BarrierRequestTimeout = hex(int(value, 16))

    def _set_maxflowrate_with_str(self, value):
        try:
            self._MaxFlowRate = int(value)
        except ValueError:
            self._MaxFlowRate = hex(int(value, 16))

