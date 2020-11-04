"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class EditROMLinkCommand(ROMCommand):
    def __init__(self, Source=None, Targets=None, TargetClassName=None, LinkName=None, LinkEditType=None, **kwargs):
        self._Source = Source  # Source Object
        self._Targets = Targets  # Target Objects
        self._TargetClassName = TargetClassName  # Target Class Name
        self._LinkName = LinkName  # Link Name
        self._LinkEditType = LinkEditType  # Link Edit Type

        properties = kwargs.copy()
        if Source is not None:
            properties['Source'] = Source
        if Targets is not None:
            properties['Targets'] = Targets
        if TargetClassName is not None:
            properties['TargetClassName'] = TargetClassName
        if LinkName is not None:
            properties['LinkName'] = LinkName
        if LinkEditType is not None:
            properties['LinkEditType'] = LinkEditType

        # call base class function, and it will send message to renix server to create a class.
        super(EditROMLinkCommand, self).__init__(**properties)

    @property
    def Source(self):
        """
        get the value of property _Source
        """
        return self._Source

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

    @Source.setter
    def Source(self, value):
        self._Source = value

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

    def _set_source_with_str(self, value):
        self._Source = value

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

