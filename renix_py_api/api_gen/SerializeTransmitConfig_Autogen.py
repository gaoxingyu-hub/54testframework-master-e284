"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PortTransmitConfig_Autogen import PortTransmitConfig


@rom_manager.rom
class SerializeTransmitConfig(PortTransmitConfig):
    def __init__(self, LoopCount=None, LoopGap=None, LoopGapUnit=None, **kwargs):
        self._LoopCount = LoopCount  # Loop Count
        self._LoopGap = LoopGap  # Inter Loop Gap
        self._LoopGapUnit = LoopGapUnit  # Inter Loop Gap Unit

        properties = kwargs.copy()
        if LoopCount is not None:
            properties['LoopCount'] = LoopCount
        if LoopGap is not None:
            properties['LoopGap'] = LoopGap
        if LoopGapUnit is not None:
            properties['LoopGapUnit'] = LoopGapUnit

        # call base class function, and it will send message to renix server to create a class.
        super(SerializeTransmitConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LoopCount=None, LoopGap=None, LoopGapUnit=None, **kwargs):
        properties = kwargs.copy()
        if LoopCount is not None:
            self._LoopCount = LoopCount
            properties['LoopCount'] = LoopCount
        if LoopGap is not None:
            self._LoopGap = LoopGap
            properties['LoopGap'] = LoopGap
        if LoopGapUnit is not None:
            self._LoopGapUnit = LoopGapUnit
            properties['LoopGapUnit'] = LoopGapUnit

        super(SerializeTransmitConfig, self).edit(**properties)

    @property
    def LoopCount(self):
        """
        get the value of property _LoopCount
        """
        if self.force_auto_sync:
            self.get('LoopCount')
        return self._LoopCount

    @property
    def LoopGap(self):
        """
        get the value of property _LoopGap
        """
        if self.force_auto_sync:
            self.get('LoopGap')
        return self._LoopGap

    @property
    def LoopGapUnit(self):
        """
        get the value of property _LoopGapUnit
        """
        if self.force_auto_sync:
            self.get('LoopGapUnit')
        return self._LoopGapUnit

    @LoopCount.setter
    def LoopCount(self, value):
        self._LoopCount = value
        self.edit(LoopCount=value)

    @LoopGap.setter
    def LoopGap(self, value):
        self._LoopGap = value
        self.edit(LoopGap=value)

    @LoopGapUnit.setter
    def LoopGapUnit(self, value):
        self._LoopGapUnit = value
        self.edit(LoopGapUnit=value)

    def _set_loopcount_with_str(self, value):
        try:
            self._LoopCount = int(value)
        except ValueError:
            self._LoopCount = hex(int(value, 16))

    def _set_loopgap_with_str(self, value):
        try:
            self._LoopGap = int(value)
        except ValueError:
            self._LoopGap = hex(int(value, 16))

    def _set_loopgapunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoopGapUnit = EnumBurstGapUnit.%s' % value[:seperate])

