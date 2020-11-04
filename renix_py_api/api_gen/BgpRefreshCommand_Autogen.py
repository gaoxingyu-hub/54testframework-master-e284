"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BgpRefreshCommand(ROMCommand):
    def __init__(self, BgpSessionBlockHandles=None, Afi=None, SubAfi=None, **kwargs):
        self._BgpSessionBlockHandles = BgpSessionBlockHandles  # BGP Protocol Configs
        self._Afi = Afi  # Refresh AFI
        self._SubAfi = SubAfi  # Refresh Sub-AFI

        properties = kwargs.copy()
        if BgpSessionBlockHandles is not None:
            properties['BgpSessionBlockHandles'] = BgpSessionBlockHandles
        if Afi is not None:
            properties['Afi'] = Afi
        if SubAfi is not None:
            properties['SubAfi'] = SubAfi

        # call base class function, and it will send message to renix server to create a class.
        super(BgpRefreshCommand, self).__init__(**properties)

    @property
    def BgpSessionBlockHandles(self):
        """
        get the value of property _BgpSessionBlockHandles
        """
        return self._BgpSessionBlockHandles

    @property
    def Afi(self):
        """
        get the value of property _Afi
        """
        return self._Afi

    @property
    def SubAfi(self):
        """
        get the value of property _SubAfi
        """
        return self._SubAfi

    @BgpSessionBlockHandles.setter
    def BgpSessionBlockHandles(self, value):
        self._BgpSessionBlockHandles = value

    @Afi.setter
    def Afi(self, value):
        self._Afi = value

    @SubAfi.setter
    def SubAfi(self, value):
        self._SubAfi = value

    def _set_bgpsessionblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BgpSessionBlockHandles = tmp_value.split()

    def _set_afi_with_str(self, value):
        seperate = value.find(':')
        exec('self._Afi = EnumBgpAfi.%s' % value[:seperate])

    def _set_subafi_with_str(self, value):
        seperate = value.find(':')
        exec('self._SubAfi = EnumBgpSubAfi.%s' % value[:seperate])

