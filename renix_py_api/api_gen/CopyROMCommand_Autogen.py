"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CopyROMCommand(ROMCommand):
    def __init__(self, SourceObjectHandles=None, TargetObjectHandle=None, CopyName=None, **kwargs):
        self._SourceObjectHandles = SourceObjectHandles  # Source Object Handles
        self._TargetObjectHandle = TargetObjectHandle  # Target Object Handle
        self._CopyName = CopyName  # Copy Object Name

        properties = kwargs.copy()
        if SourceObjectHandles is not None:
            properties['SourceObjectHandles'] = SourceObjectHandles
        if TargetObjectHandle is not None:
            properties['TargetObjectHandle'] = TargetObjectHandle
        if CopyName is not None:
            properties['CopyName'] = CopyName

        # call base class function, and it will send message to renix server to create a class.
        super(CopyROMCommand, self).__init__(**properties)

    @property
    def SourceObjectHandles(self):
        """
        get the value of property _SourceObjectHandles
        """
        return self._SourceObjectHandles

    @property
    def TargetObjectHandle(self):
        """
        get the value of property _TargetObjectHandle
        """
        return self._TargetObjectHandle

    @property
    def CopyName(self):
        """
        get the value of property _CopyName
        """
        return self._CopyName

    @SourceObjectHandles.setter
    def SourceObjectHandles(self, value):
        self._SourceObjectHandles = value

    @TargetObjectHandle.setter
    def TargetObjectHandle(self, value):
        self._TargetObjectHandle = value

    @CopyName.setter
    def CopyName(self, value):
        self._CopyName = value

    def _set_sourceobjecthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SourceObjectHandles = tmp_value.split()

    def _set_targetobjecthandle_with_str(self, value):
        self._TargetObjectHandle = value

    def _set_copyname_with_str(self, value):
        self._CopyName = (value == 'True')

