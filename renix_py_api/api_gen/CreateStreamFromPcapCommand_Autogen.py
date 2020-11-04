"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateStreamFromPcapCommand(ROMCommand):
    def __init__(self, PortList=None, FilePath=None, RxPortList=None, IncludeCrc=None, **kwargs):
        self._PortList = PortList  # Port Handles
        self._FilePath = FilePath  # Import Pcap File Path
        self._RxPortList = RxPortList  # Rx Port Handles
        self._IncludeCrc = IncludeCrc  # Include CRC in tail

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList
        if FilePath is not None:
            properties['FilePath'] = FilePath
        if RxPortList is not None:
            properties['RxPortList'] = RxPortList
        if IncludeCrc is not None:
            properties['IncludeCrc'] = IncludeCrc

        # call base class function, and it will send message to renix server to create a class.
        super(CreateStreamFromPcapCommand, self).__init__(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        return self._PortList

    @property
    def FilePath(self):
        """
        get the value of property _FilePath
        """
        return self._FilePath

    @property
    def RxPortList(self):
        """
        get the value of property _RxPortList
        """
        return self._RxPortList

    @property
    def IncludeCrc(self):
        """
        get the value of property _IncludeCrc
        """
        return self._IncludeCrc

    @PortList.setter
    def PortList(self, value):
        self._PortList = value

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value

    @RxPortList.setter
    def RxPortList(self, value):
        self._RxPortList = value

    @IncludeCrc.setter
    def IncludeCrc(self, value):
        self._IncludeCrc = value

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

    def _set_filepath_with_str(self, value):
        self._FilePath = value

    def _set_rxportlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RxPortList = tmp_value.split()

    def _set_includecrc_with_str(self, value):
        self._IncludeCrc = (value == 'True')

