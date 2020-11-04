"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class AdvertiseBgpRouteBlockCommand(ROMCommand):
    def __init__(self, BgpRouteBlockHandles=None, **kwargs):
        self._BgpRouteBlockHandles = BgpRouteBlockHandles  # BGP Route Block Configs

        properties = kwargs.copy()
        if BgpRouteBlockHandles is not None:
            properties['BgpRouteBlockHandles'] = BgpRouteBlockHandles

        # call base class function, and it will send message to renix server to create a class.
        super(AdvertiseBgpRouteBlockCommand, self).__init__(**properties)

    @property
    def BgpRouteBlockHandles(self):
        """
        get the value of property _BgpRouteBlockHandles
        """
        return self._BgpRouteBlockHandles

    @BgpRouteBlockHandles.setter
    def BgpRouteBlockHandles(self, value):
        self._BgpRouteBlockHandles = value

    def _set_bgprouteblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BgpRouteBlockHandles = tmp_value.split()

