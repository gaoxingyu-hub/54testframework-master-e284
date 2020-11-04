"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class VxlanSelectMulticastGroupCommand(ROMCommand):
    def __init__(self, VxlanSegmentHandle=None, VxlanMulticastGroupHandle=None, **kwargs):
        self._VxlanSegmentHandle = VxlanSegmentHandle  # Vxlan Segment Handle
        self._VxlanMulticastGroupHandle = VxlanMulticastGroupHandle  # Multi-cast group Handle

        properties = kwargs.copy()
        if VxlanSegmentHandle is not None:
            properties['VxlanSegmentHandle'] = VxlanSegmentHandle
        if VxlanMulticastGroupHandle is not None:
            properties['VxlanMulticastGroupHandle'] = VxlanMulticastGroupHandle

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanSelectMulticastGroupCommand, self).__init__(**properties)

    @property
    def VxlanSegmentHandle(self):
        """
        get the value of property _VxlanSegmentHandle
        """
        return self._VxlanSegmentHandle

    @property
    def VxlanMulticastGroupHandle(self):
        """
        get the value of property _VxlanMulticastGroupHandle
        """
        return self._VxlanMulticastGroupHandle

    @VxlanSegmentHandle.setter
    def VxlanSegmentHandle(self, value):
        self._VxlanSegmentHandle = value

    @VxlanMulticastGroupHandle.setter
    def VxlanMulticastGroupHandle(self, value):
        self._VxlanMulticastGroupHandle = value

    def _set_vxlansegmenthandle_with_str(self, value):
        self._VxlanSegmentHandle = value

    def _set_vxlanmulticastgrouphandle_with_str(self, value):
        self._VxlanMulticastGroupHandle = value

