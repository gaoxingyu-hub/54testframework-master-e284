"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv2RouterLsaLinksConfig(ROMObject):
    def __init__(self, LinkType=None, LinkId=None, LinkData=None, Metric=None, **kwargs):
        self._LinkType = LinkType  # Link Type
        self._LinkId = LinkId  # Link ID
        self._LinkData = LinkData  # Link Data
        self._Metric = Metric  # Metric

        properties = kwargs.copy()
        if LinkType is not None:
            properties['LinkType'] = LinkType
        if LinkId is not None:
            properties['LinkId'] = LinkId
        if LinkData is not None:
            properties['LinkData'] = LinkData
        if Metric is not None:
            properties['Metric'] = Metric

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2RouterLsaLinksConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LinkType=None, LinkId=None, LinkData=None, Metric=None, **kwargs):
        properties = kwargs.copy()
        if LinkType is not None:
            self._LinkType = LinkType
            properties['LinkType'] = LinkType
        if LinkId is not None:
            self._LinkId = LinkId
            properties['LinkId'] = LinkId
        if LinkData is not None:
            self._LinkData = LinkData
            properties['LinkData'] = LinkData
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric

        super(Ospfv2RouterLsaLinksConfig, self).edit(**properties)

    @property
    def LinkType(self):
        """
        get the value of property _LinkType
        """
        if self.force_auto_sync:
            self.get('LinkType')
        return self._LinkType

    @property
    def LinkId(self):
        """
        get the value of property _LinkId
        """
        if self.force_auto_sync:
            self.get('LinkId')
        return self._LinkId

    @property
    def LinkData(self):
        """
        get the value of property _LinkData
        """
        if self.force_auto_sync:
            self.get('LinkData')
        return self._LinkData

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

    @LinkId.setter
    def LinkId(self, value):
        self._LinkId = value
        self.edit(LinkId=value)

    @LinkData.setter
    def LinkData(self, value):
        self._LinkData = value
        self.edit(LinkData=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    def _set_linktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkType = EnumRouterLsaLinkType.%s' % value[:seperate])

    def _set_linkid_with_str(self, value):
        self._LinkId = value

    def _set_linkdata_with_str(self, value):
        self._LinkData = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

