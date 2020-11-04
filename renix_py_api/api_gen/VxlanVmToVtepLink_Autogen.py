"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .InterfaceBehindInterface_Autogen import InterfaceBehindInterface


@rom_manager.rom
class VxlanVmToVtepLink(InterfaceBehindInterface):
    def __init__(self, VniList=None, DestPort=None, VtepIpList=None, **kwargs):
        self._VniList = VniList  # VNI List
        self._SrcPortList = None  # Source Port List, not editable
        self._DestPort = DestPort  # Destination Port Number
        self._VtepIpList = VtepIpList  # Vtep IPv4 List

        properties = kwargs.copy()
        if VniList is not None:
            properties['VniList'] = VniList
        if DestPort is not None:
            properties['DestPort'] = DestPort
        if VtepIpList is not None:
            properties['VtepIpList'] = VtepIpList

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanVmToVtepLink, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, VniList=None, DestPort=None, VtepIpList=None, **kwargs):
        properties = kwargs.copy()
        if VniList is not None:
            self._VniList = VniList
            properties['VniList'] = VniList
        if DestPort is not None:
            self._DestPort = DestPort
            properties['DestPort'] = DestPort
        if VtepIpList is not None:
            self._VtepIpList = VtepIpList
            properties['VtepIpList'] = VtepIpList

        super(VxlanVmToVtepLink, self).edit(**properties)

    @property
    def VniList(self):
        """
        get the value of property _VniList
        """
        if self.force_auto_sync:
            self.get('VniList')
        return self._VniList

    @property
    def SrcPortList(self):
        """
        get the value of property _SrcPortList
        """
        if self.force_auto_sync:
            self.get('SrcPortList')
        return self._SrcPortList

    @property
    def DestPort(self):
        """
        get the value of property _DestPort
        """
        if self.force_auto_sync:
            self.get('DestPort')
        return self._DestPort

    @property
    def VtepIpList(self):
        """
        get the value of property _VtepIpList
        """
        if self.force_auto_sync:
            self.get('VtepIpList')
        return self._VtepIpList

    @VniList.setter
    def VniList(self, value):
        self._VniList = value
        self.edit(VniList=value)

    @DestPort.setter
    def DestPort(self, value):
        self._DestPort = value
        self.edit(DestPort=value)

    @VtepIpList.setter
    def VtepIpList(self, value):
        self._VtepIpList = value
        self.edit(VtepIpList=value)

    def _set_vnilist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VniList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._VniList.append(int(str_value))
            except ValueError:
                self._VniList.append(hex(int(str_value, 16)))

    def _set_srcportlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SrcPortList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._SrcPortList.append(int(str_value))
            except ValueError:
                self._SrcPortList.append(hex(int(str_value, 16)))

    def _set_destport_with_str(self, value):
        try:
            self._DestPort = int(value)
        except ValueError:
            self._DestPort = hex(int(value, 16))

    def _set_vtepiplist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VtepIpList = tmp_value.split()

