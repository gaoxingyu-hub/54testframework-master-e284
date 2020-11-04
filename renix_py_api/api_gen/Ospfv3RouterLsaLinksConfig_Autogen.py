"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3RouterLsaLinksConfig(ROMObject):
    def __init__(self, LinkType=None, InterfaceId=None, NeighborInterfaceId=None, NeighborRouterId=None, Metric=None, **kwargs):
        self._LinkType = LinkType  # Link Type
        self._InterfaceId = InterfaceId  # Interface ID
        self._NeighborInterfaceId = NeighborInterfaceId  # Neighbor Interface ID
        self._NeighborRouterId = NeighborRouterId  # Neighbor Router ID
        self._Metric = Metric  # Metric

        properties = kwargs.copy()
        if LinkType is not None:
            properties['LinkType'] = LinkType
        if InterfaceId is not None:
            properties['InterfaceId'] = InterfaceId
        if NeighborInterfaceId is not None:
            properties['NeighborInterfaceId'] = NeighborInterfaceId
        if NeighborRouterId is not None:
            properties['NeighborRouterId'] = NeighborRouterId
        if Metric is not None:
            properties['Metric'] = Metric

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3RouterLsaLinksConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LinkType=None, InterfaceId=None, NeighborInterfaceId=None, NeighborRouterId=None, Metric=None, **kwargs):
        properties = kwargs.copy()
        if LinkType is not None:
            self._LinkType = LinkType
            properties['LinkType'] = LinkType
        if InterfaceId is not None:
            self._InterfaceId = InterfaceId
            properties['InterfaceId'] = InterfaceId
        if NeighborInterfaceId is not None:
            self._NeighborInterfaceId = NeighborInterfaceId
            properties['NeighborInterfaceId'] = NeighborInterfaceId
        if NeighborRouterId is not None:
            self._NeighborRouterId = NeighborRouterId
            properties['NeighborRouterId'] = NeighborRouterId
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric

        super(Ospfv3RouterLsaLinksConfig, self).edit(**properties)

    @property
    def LinkType(self):
        """
        get the value of property _LinkType
        """
        if self.force_auto_sync:
            self.get('LinkType')
        return self._LinkType

    @property
    def InterfaceId(self):
        """
        get the value of property _InterfaceId
        """
        if self.force_auto_sync:
            self.get('InterfaceId')
        return self._InterfaceId

    @property
    def NeighborInterfaceId(self):
        """
        get the value of property _NeighborInterfaceId
        """
        if self.force_auto_sync:
            self.get('NeighborInterfaceId')
        return self._NeighborInterfaceId

    @property
    def NeighborRouterId(self):
        """
        get the value of property _NeighborRouterId
        """
        if self.force_auto_sync:
            self.get('NeighborRouterId')
        return self._NeighborRouterId

    @property
    def Metric(self):
        """
        get the value of property _Metric
        """
        if self.force_auto_sync:
            self.get('Metric')
        return self._Metric

    @LinkType.setter
    def LinkType(self, value):
        self._LinkType = value
        self.edit(LinkType=value)

    @InterfaceId.setter
    def InterfaceId(self, value):
        self._InterfaceId = value
        self.edit(InterfaceId=value)

    @NeighborInterfaceId.setter
    def NeighborInterfaceId(self, value):
        self._NeighborInterfaceId = value
        self.edit(NeighborInterfaceId=value)

    @NeighborRouterId.setter
    def NeighborRouterId(self, value):
        self._NeighborRouterId = value
        self.edit(NeighborRouterId=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    def _set_linktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkType = EnumOspfv3RouteLinkType.%s' % value[:seperate])

    def _set_interfaceid_with_str(self, value):
        try:
            self._InterfaceId = int(value)
        except ValueError:
            self._InterfaceId = hex(int(value, 16))

    def _set_neighborinterfaceid_with_str(self, value):
        try:
            self._NeighborInterfaceId = int(value)
        except ValueError:
            self._NeighborInterfaceId = hex(int(value, 16))

    def _set_neighborrouterid_with_str(self, value):
        self._NeighborRouterId = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

