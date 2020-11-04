"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisNeighborConfig(ROMObject):
    def __init__(self, SystemId=None, PseudonodeSystemId=None, NarrowMetric=None, WideMetric=None, **kwargs):
        self._SystemId = SystemId  # Neighbor System ID
        self._PseudonodeSystemId = PseudonodeSystemId  # Pseudonode System ID
        self._NarrowMetric = NarrowMetric  # Narrow Metric
        self._WideMetric = WideMetric  # Wide Metric

        properties = kwargs.copy()
        if SystemId is not None:
            properties['SystemId'] = SystemId
        if PseudonodeSystemId is not None:
            properties['PseudonodeSystemId'] = PseudonodeSystemId
        if NarrowMetric is not None:
            properties['NarrowMetric'] = NarrowMetric
        if WideMetric is not None:
            properties['WideMetric'] = WideMetric

        # call base class function, and it will send message to renix server to create a class.
        super(IsisNeighborConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SystemId=None, PseudonodeSystemId=None, NarrowMetric=None, WideMetric=None, **kwargs):
        properties = kwargs.copy()
        if SystemId is not None:
            self._SystemId = SystemId
            properties['SystemId'] = SystemId
        if PseudonodeSystemId is not None:
            self._PseudonodeSystemId = PseudonodeSystemId
            properties['PseudonodeSystemId'] = PseudonodeSystemId
        if NarrowMetric is not None:
            self._NarrowMetric = NarrowMetric
            properties['NarrowMetric'] = NarrowMetric
        if WideMetric is not None:
            self._WideMetric = WideMetric
            properties['WideMetric'] = WideMetric

        super(IsisNeighborConfig, self).edit(**properties)

    @property
    def SystemId(self):
        """
        get the value of property _SystemId
        """
        if self.force_auto_sync:
            self.get('SystemId')
        return self._SystemId

    @property
    def PseudonodeSystemId(self):
        """
        get the value of property _PseudonodeSystemId
        """
        if self.force_auto_sync:
            self.get('PseudonodeSystemId')
        return self._PseudonodeSystemId

    @property
    def NarrowMetric(self):
        """
        get the value of property _NarrowMetric
        """
        if self.force_auto_sync:
            self.get('NarrowMetric')
        return self._NarrowMetric

    @property
    def WideMetric(self):
        """
        get the value of property _WideMetric
        """
        if self.force_auto_sync:
            self.get('WideMetric')
        return self._WideMetric

    @SystemId.setter
    def SystemId(self, value):
        self._SystemId = value
        self.edit(SystemId=value)

    @PseudonodeSystemId.setter
    def PseudonodeSystemId(self, value):
        self._PseudonodeSystemId = value
        self.edit(PseudonodeSystemId=value)

    @NarrowMetric.setter
    def NarrowMetric(self, value):
        self._NarrowMetric = value
        self.edit(NarrowMetric=value)

    @WideMetric.setter
    def WideMetric(self, value):
        self._WideMetric = value
        self.edit(WideMetric=value)

    def _set_systemid_with_str(self, value):
        self._SystemId = value

    def _set_pseudonodesystemid_with_str(self, value):
        try:
            self._PseudonodeSystemId = int(value)
        except ValueError:
            self._PseudonodeSystemId = hex(int(value, 16))

    def _set_narrowmetric_with_str(self, value):
        try:
            self._NarrowMetric = int(value)
        except ValueError:
            self._NarrowMetric = hex(int(value, 16))

    def _set_widemetric_with_str(self, value):
        try:
            self._WideMetric = int(value)
        except ValueError:
            self._WideMetric = hex(int(value, 16))

