"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class PcapStreamWizardConfig(WizardConfigBase):
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
        super(PcapStreamWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PortList=None, FilePath=None, RxPortList=None, IncludeCrc=None, **kwargs):
        properties = kwargs.copy()
        if PortList is not None:
            self._PortList = PortList
            properties['PortList'] = PortList
        if FilePath is not None:
            self._FilePath = FilePath
            properties['FilePath'] = FilePath
        if RxPortList is not None:
            self._RxPortList = RxPortList
            properties['RxPortList'] = RxPortList
        if IncludeCrc is not None:
            self._IncludeCrc = IncludeCrc
            properties['IncludeCrc'] = IncludeCrc

        super(PcapStreamWizardConfig, self).edit(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        if self.force_auto_sync:
            self.get('PortList')
        return self._PortList

    @property
    def FilePath(self):
        """
        get the value of property _FilePath
        """
        if self.force_auto_sync:
            self.get('FilePath')
        return self._FilePath

    @property
    def RxPortList(self):
        """
        get the value of property _RxPortList
        """
        if self.force_auto_sync:
            self.get('RxPortList')
        return self._RxPortList

    @property
    def IncludeCrc(self):
        """
        get the value of property _IncludeCrc
        """
        if self.force_auto_sync:
            self.get('IncludeCrc')
        return self._IncludeCrc

    @PortList.setter
    def PortList(self, value):
        self._PortList = value
        self.edit(PortList=value)

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value
        self.edit(FilePath=value)

    @RxPortList.setter
    def RxPortList(self, value):
        self._RxPortList = value
        self.edit(RxPortList=value)

    @IncludeCrc.setter
    def IncludeCrc(self, value):
        self._IncludeCrc = value
        self.edit(IncludeCrc=value)

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

