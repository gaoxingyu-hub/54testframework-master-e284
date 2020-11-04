"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class VxlanSelectVmCommand(ROMCommand):
    def __init__(self, VxlanSegmentHandles=None, VxlanVmHandles=None, **kwargs):
        self._VxlanSegmentHandles = VxlanSegmentHandles  # VXLAN Segment
        self._VxlanVmHandles = VxlanVmHandles  # VM

        properties = kwargs.copy()
        if VxlanSegmentHandles is not None:
            properties['VxlanSegmentHandles'] = VxlanSegmentHandles
        if VxlanVmHandles is not None:
            properties['VxlanVmHandles'] = VxlanVmHandles

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanSelectVmCommand, self).__init__(**properties)

    @property
    def VxlanSegmentHandles(self):
        """
        get the value of property _VxlanSegmentHandles
        """
        return self._VxlanSegmentHandles

    @property
    def VxlanVmHandles(self):
        """
        get the value of property _VxlanVmHandles
        """
        return self._VxlanVmHandles

    @VxlanSegmentHandles.setter
    def VxlanSegmentHandles(self, value):
        self._VxlanSegmentHandles = value

    @VxlanVmHandles.setter
    def VxlanVmHandles(self, value):
        self._VxlanVmHandles = value

    def _set_vxlansegmenthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VxlanSegmentHandles = tmp_value.split()

    def _set_vxlanvmhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VxlanVmHandles = tmp_value.split()

