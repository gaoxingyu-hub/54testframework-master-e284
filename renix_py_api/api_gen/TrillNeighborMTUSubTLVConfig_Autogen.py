"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillNeighborMTUSubTLVConfig(ROMObject):
    def __init__(self, MTU=None, FailedBitSet=None, **kwargs):
        self._MTU = MTU  # MTU
        self._FailedBitSet = FailedBitSet  # Failed Bit Set

        properties = kwargs.copy()
        if MTU is not None:
            properties['MTU'] = MTU
        if FailedBitSet is not None:
            properties['FailedBitSet'] = FailedBitSet

        # call base class function, and it will send message to renix server to create a class.
        super(TrillNeighborMTUSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MTU=None, FailedBitSet=None, **kwargs):
        properties = kwargs.copy()
        if MTU is not None:
            self._MTU = MTU
            properties['MTU'] = MTU
        if FailedBitSet is not None:
            self._FailedBitSet = FailedBitSet
            properties['FailedBitSet'] = FailedBitSet

        super(TrillNeighborMTUSubTLVConfig, self).edit(**properties)

    @property
    def MTU(self):
        """
        get the value of property _MTU
        """
        if self.force_auto_sync:
            self.get('MTU')
        return self._MTU

    @property
    def FailedBitSet(self):
        """
        get the value of property _FailedBitSet
        """
        if self.force_auto_sync:
            self.get('FailedBitSet')
        return self._FailedBitSet

    @MTU.setter
    def MTU(self, value):
        self._MTU = value
        self.edit(MTU=value)

    @FailedBitSet.setter
    def FailedBitSet(self, value):
        self._FailedBitSet = value
        self.edit(FailedBitSet=value)

    def _set_mtu_with_str(self, value):
        try:
            self._MTU = int(value)
        except ValueError:
            self._MTU = hex(int(value, 16))

    def _set_failedbitset_with_str(self, value):
        self._FailedBitSet = (value == 'True')

