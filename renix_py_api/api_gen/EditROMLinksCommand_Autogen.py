"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class EditROMLinksCommand(ROMCommand):
    def __init__(self, Sources=None, Targets=None, TargetClassName=None, LinkName=None, LinkEditType=None, SrcTargetMapType=None, **kwargs):
        self._Sources = Sources  # Source Object
        self._Targets = Targets  # Target Objects
        self._TargetClassName = TargetClassName  # Target Class Name
        self._LinkName = LinkName  # Link Name
        self._LinkEditType = LinkEditType  # Link Edit Type
        self._SrcTargetMapType = SrcTargetMapType  # Source To Target map type

        properties = kwargs.copy()
        if Sources is not None:
            properties['Sources'] = Sources
        if Targets is not None:
            properties['Targets'] = Targets
        if TargetClassName is not None:
            properties['TargetClassName'] = TargetClassName
        if LinkName is not None:
            properties['LinkName'] = LinkName
        if LinkEditType is not None:
            properties['LinkEditType'] = LinkEditType
        if SrcTargetMapType is not None:
            properties['SrcTargetMapType'] = SrcTargetMapType

        # call base class function, and it will send message to renix server to create a class.
        super(EditROMLinksCommand, self).__init__(**properties)

    @property
    def Sources(self):
        """
        get the value of property _Sources
        """
        return self._Sources

    @property
    def Targets(self):
        """
        get the value of property _Targets
        """
        return self._Targets

    @property
    def TargetClassName(self):
        """
        get the value of property _TargetClassName
        """
        return self._TargetClassName

    @property
    def LinkName(self):
        """
        get the value of property _LinkName
        """
        return self._LinkName

    @property
    def LinkEditType(self):
        """
        get the value of property _LinkEditType
        """
        return self._LinkEditType

    @property
    def SrcTargetMapType(self):
        """
        get the value of property _SrcTargetMapType
        """
        return self._SrcTargetMapType

    @Sources.setter
    def Sources(self, value):
        self._Sources = value

    @Targets.setter
    def Targets(self, value):
        self._Targets = value

    @TargetClassName.setter
    def TargetClassName(self, value):
        self._TargetClassName = value

    @LinkName.setter
    def LinkName(self, value):
        self._LinkName = value

    @LinkEditType.setter
    def LinkEditType(self, value):
        self._LinkEditType = value

    @SrcTargetMapType.setter
    def SrcTargetMapType(self, value):
        self._SrcTargetMapType = value

    def _set_sources_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Sources = tmp_value.split()

    def _set_targets_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Targets = tmp_value.split()

    def _set_targetclassname_with_str(self, value):
        self._TargetClassName = value

    def _set_linkname_with_str(self, value):
        self._LinkName = value

    def _set_linkedittype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkEditType = EnumLinkEditType.%s' % value[:seperate])

    def _set_srctargetmaptype_with_str(self, value):
        seperate = value.find(':')
        exec('self._SrcTargetMapType = EnumSrcDstMapType.%s' % value[:seperate])

