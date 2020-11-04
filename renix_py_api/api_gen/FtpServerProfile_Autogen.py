"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ServerProfile_Autogen import L47ServerProfile


@rom_manager.rom
class FtpServerProfile(L47ServerProfile):
    def __init__(self, ListenPort=None, VlanPriority=None, Tos=None, TrafficClass=None, **kwargs):
        self._ListenPort = ListenPort  # Listen Port
        self._VlanPriority = VlanPriority  # VLAN Priority
        self._Tos = Tos  # ToS/DSCP
        self._TrafficClass = TrafficClass  # Traffic Class

        properties = kwargs.copy()
        if ListenPort is not None:
            properties['ListenPort'] = ListenPort
        if VlanPriority is not None:
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            properties['Tos'] = Tos
        if TrafficClass is not None:
            properties['TrafficClass'] = TrafficClass

        # call base class function, and it will send message to renix server to create a class.
        super(FtpServerProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ListenPort=None, VlanPriority=None, Tos=None, TrafficClass=None, **kwargs):
        properties = kwargs.copy()
        if ListenPort is not None:
            self._ListenPort = ListenPort
            properties['ListenPort'] = ListenPort
        if VlanPriority is not None:
            self._VlanPriority = VlanPriority
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            self._Tos = Tos
            properties['Tos'] = Tos
        if TrafficClass is not None:
            self._TrafficClass = TrafficClass
            properties['TrafficClass'] = TrafficClass

        super(FtpServerProfile, self).edit(**properties)

    @property
    def ListenPort(self):
        """
        get the value of property _ListenPort
        """
        if self.force_auto_sync:
            self.get('ListenPort')
        return self._ListenPort

    @property
    def VlanPriority(self):
        """
        get the value of property _VlanPriority
        """
        if self.force_auto_sync:
            self.get('VlanPriority')
        return self._VlanPriority

    @property
    def Tos(self):
        """
        get the value of property _Tos
        """
        if self.force_auto_sync:
            self.get('Tos')
        return self._Tos

    @property
    def TrafficClass(self):
        """
        get the value of property _TrafficClass
        """
        if self.force_auto_sync:
            self.get('TrafficClass')
        return self._TrafficClass

    @ListenPort.setter
    def ListenPort(self, value):
        self._ListenPort = value
        self.edit(ListenPort=value)

    @VlanPriority.setter
    def VlanPriority(self, value):
        self._VlanPriority = value
        self.edit(VlanPriority=value)

    @Tos.setter
    def Tos(self, value):
        self._Tos = value
        self.edit(Tos=value)

    @TrafficClass.setter
    def TrafficClass(self, value):
        self._TrafficClass = value
        self.edit(TrafficClass=value)

    def _set_listenport_with_str(self, value):
        try:
            self._ListenPort = int(value)
        except ValueError:
            self._ListenPort = hex(int(value, 16))

    def _set_vlanpriority_with_str(self, value):
        try:
            self._VlanPriority = int(value)
        except ValueError:
            self._VlanPriority = hex(int(value, 16))

    def _set_tos_with_str(self, value):
        try:
            self._Tos = int(value)
        except ValueError:
            self._Tos = hex(int(value, 16))

    def _set_trafficclass_with_str(self, value):
        try:
            self._TrafficClass = int(value)
        except ValueError:
            self._TrafficClass = hex(int(value, 16))

