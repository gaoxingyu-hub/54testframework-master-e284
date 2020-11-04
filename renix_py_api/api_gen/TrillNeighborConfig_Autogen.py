"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillNeighborConfig(ROMObject):
    def __init__(self, NeighborSystemID=None, PseudonodeSystemID=None, LinkMetric=None, **kwargs):
        self._NeighborSystemID = NeighborSystemID  # Neighbor System ID
        self._PseudonodeSystemID = PseudonodeSystemID  # Pseudonode System ID
        self._LinkMetric = LinkMetric  # Link Metric

        properties = kwargs.copy()
        if NeighborSystemID is not None:
            properties['NeighborSystemID'] = NeighborSystemID
        if PseudonodeSystemID is not None:
            properties['PseudonodeSystemID'] = PseudonodeSystemID
        if LinkMetric is not None:
            properties['LinkMetric'] = LinkMetric

        # call base class function, and it will send message to renix server to create a class.
        super(TrillNeighborConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NeighborSystemID=None, PseudonodeSystemID=None, LinkMetric=None, **kwargs):
        properties = kwargs.copy()
        if NeighborSystemID is not None:
            self._NeighborSystemID = NeighborSystemID
            properties['NeighborSystemID'] = NeighborSystemID
        if PseudonodeSystemID is not None:
            self._PseudonodeSystemID = PseudonodeSystemID
            properties['PseudonodeSystemID'] = PseudonodeSystemID
        if LinkMetric is not None:
            self._LinkMetric = LinkMetric
            properties['LinkMetric'] = LinkMetric

        super(TrillNeighborConfig, self).edit(**properties)

    @property
    def NeighborSystemID(self):
        """
        get the value of property _NeighborSystemID
        """
        if self.force_auto_sync:
            self.get('NeighborSystemID')
        return self._NeighborSystemID

    @property
    def PseudonodeSystemID(self):
        """
        get the value of property _PseudonodeSystemID
        """
        if self.force_auto_sync:
            self.get('PseudonodeSystemID')
        return self._PseudonodeSystemID

    @property
    def LinkMetric(self):
        """
        get the value of property _LinkMetric
        """
        if self.force_auto_sync:
            self.get('LinkMetric')
        return self._LinkMetric

    @NeighborSystemID.setter
    def NeighborSystemID(self, value):
        self._NeighborSystemID = value
        self.edit(NeighborSystemID=value)

    @PseudonodeSystemID.setter
    def PseudonodeSystemID(self, value):
        self._PseudonodeSystemID = value
        self.edit(PseudonodeSystemID=value)

    @LinkMetric.setter
    def LinkMetric(self, value):
        self._LinkMetric = value
        self.edit(LinkMetric=value)

    def _set_neighborsystemid_with_str(self, value):
        self._NeighborSystemID = value

    def _set_pseudonodesystemid_with_str(self, value):
        try:
            self._PseudonodeSystemID = int(value)
        except ValueError:
            self._PseudonodeSystemID = hex(int(value, 16))

    def _set_linkmetric_with_str(self, value):
        try:
            self._LinkMetric = int(value)
        except ValueError:
            self._LinkMetric = hex(int(value, 16))

