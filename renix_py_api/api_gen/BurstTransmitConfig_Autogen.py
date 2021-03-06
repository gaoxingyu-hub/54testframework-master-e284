"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PortTransmitConfig_Autogen import PortTransmitConfig


@rom_manager.rom
class BurstTransmitConfig(PortTransmitConfig):
    def __init__(self, FramePerBurst=None, BurstCount=None, BurstGap=None, BurstGapUnit=None, **kwargs):
        self._FramePerBurst = FramePerBurst  # Frames per Burst
        self._BurstCount = BurstCount  # Burst Count
        self._BurstGap = BurstGap  # Inter Burst Gap
        self._BurstGapUnit = BurstGapUnit  # Inter Burst Gap Unit

        properties = kwargs.copy()
        if FramePerBurst is not None:
            properties['FramePerBurst'] = FramePerBurst
        if BurstCount is not None:
            properties['BurstCount'] = BurstCount
        if BurstGap is not None:
            properties['BurstGap'] = BurstGap
        if BurstGapUnit is not None:
            properties['BurstGapUnit'] = BurstGapUnit

        # call base class function, and it will send message to renix server to create a class.
        super(BurstTransmitConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FramePerBurst=None, BurstCount=None, BurstGap=None, BurstGapUnit=None, **kwargs):
        properties = kwargs.copy()
        if FramePerBurst is not None:
            self._FramePerBurst = FramePerBurst
            properties['FramePerBurst'] = FramePerBurst
        if BurstCount is not None:
            self._BurstCount = BurstCount
            properties['BurstCount'] = BurstCount
        if BurstGap is not None:
            self._BurstGap = BurstGap
            properties['BurstGap'] = BurstGap
        if BurstGapUnit is not None:
            self._BurstGapUnit = BurstGapUnit
            properties['BurstGapUnit'] = BurstGapUnit

        super(BurstTransmitConfig, self).edit(**properties)

    @property
    def FramePerBurst(self):
        """
        get the value of property _FramePerBurst
        """
        if self.force_auto_sync:
            self.get('FramePerBurst')
        return self._FramePerBurst

    @property
    def BurstCount(self):
        """
        get the value of property _BurstCount
        """
        if self.force_auto_sync:
            self.get('BurstCount')
        return self._BurstCount

    @property
    def BurstGap(self):
        """
        get the value of property _BurstGap
        """
        if self.force_auto_sync:
            self.get('BurstGap')
        return self._BurstGap

    @property
    def BurstGapUnit(self):
        """
        get the value of property _BurstGapUnit
        """
        if self.force_auto_sync:
            self.get('BurstGapUnit')
        return self._BurstGapUnit

    @FramePerBurst.setter
    def FramePerBurst(self, value):
        self._FramePerBurst = value
        self.edit(FramePerBurst=value)

    @BurstCount.setter
    def BurstCount(self, value):
        self._BurstCount = value
        self.edit(BurstCount=value)

    @BurstGap.setter
    def BurstGap(self, value):
        self._BurstGap = value
        self.edit(BurstGap=value)

    @BurstGapUnit.setter
    def BurstGapUnit(self, value):
        self._BurstGapUnit = value
        self.edit(BurstGapUnit=value)

    def _set_frameperburst_with_str(self, value):
        try:
            self._FramePerBurst = int(value)
        except ValueError:
            self._FramePerBurst = hex(int(value, 16))

    def _set_burstcount_with_str(self, value):
        try:
            self._BurstCount = int(value)
        except ValueError:
            self._BurstCount = hex(int(value, 16))

    def _set_burstgap_with_str(self, value):
        try:
            self._BurstGap = int(value)
        except ValueError:
            self._BurstGap = hex(int(value, 16))

    def _set_burstgapunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._BurstGapUnit = EnumBurstGapUnit.%s' % value[:seperate])

