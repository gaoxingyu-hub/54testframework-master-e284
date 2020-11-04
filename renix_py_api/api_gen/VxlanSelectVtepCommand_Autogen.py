"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class VxlanSelectVtepCommand(ROMCommand):
    def __init__(self, VxlanVtepHandle=None, VxlanVmHandle=None, **kwargs):
        self._VxlanVtepHandle = VxlanVtepHandle  # Vxlan VTEP configuration Handle
        self._VxlanVmHandle = VxlanVmHandle  # VM interface Handles

        properties = kwargs.copy()
        if VxlanVtepHandle is not None:
            properties['VxlanVtepHandle'] = VxlanVtepHandle
        if VxlanVmHandle is not None:
            properties['VxlanVmHandle'] = VxlanVmHandle

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanSelectVtepCommand, self).__init__(**properties)

    @property
    def VxlanVtepHandle(self):
        """
        get the value of property _VxlanVtepHandle
        """
        return self._VxlanVtepHandle

    @property
    def VxlanVmHandle(self):
        """
        get the value of property _VxlanVmHandle
        """
        return self._VxlanVmHandle

    @VxlanVtepHandle.setter
    def VxlanVtepHandle(self, value):
        self._VxlanVtepHandle = value

    @VxlanVmHandle.setter
    def VxlanVmHandle(self, value):
        self._VxlanVmHandle = value

    def _set_vxlanvtephandle_with_str(self, value):
        self._VxlanVtepHandle = value

    def _set_vxlanvmhandle_with_str(self, value):
        self._VxlanVmHandle = value

