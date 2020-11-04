"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpCommonConfig(ROMObject):
    def __init__(self, IntegrityCheck=None, VlanPriority=None, Tos=None, TrafficClass=None, TCPTearDown=None, EnableSSL=None, **kwargs):
        self._IntegrityCheck = IntegrityCheck  # Integrity Check
        self._VlanPriority = VlanPriority  # VLAN Priority
        self._Tos = Tos  # ToS/DSCP
        self._TrafficClass = TrafficClass  # Traffic Class
        self._TCPTearDown = TCPTearDown  # TCPTearDown
        self._EnableSSL = EnableSSL  # Enable SSL/TLS

        properties = kwargs.copy()
        if IntegrityCheck is not None:
            properties['IntegrityCheck'] = IntegrityCheck
        if VlanPriority is not None:
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            properties['Tos'] = Tos
        if TrafficClass is not None:
            properties['TrafficClass'] = TrafficClass
        if TCPTearDown is not None:
            properties['TCPTearDown'] = TCPTearDown
        if EnableSSL is not None:
            properties['EnableSSL'] = EnableSSL

        # call base class function, and it will send message to renix server to create a class.
        super(HttpCommonConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IntegrityCheck=None, VlanPriority=None, Tos=None, TrafficClass=None, TCPTearDown=None, EnableSSL=None, **kwargs):
        properties = kwargs.copy()
        if IntegrityCheck is not None:
            self._IntegrityCheck = IntegrityCheck
            properties['IntegrityCheck'] = IntegrityCheck
        if VlanPriority is not None:
            self._VlanPriority = VlanPriority
            properties['VlanPriority'] = VlanPriority
        if Tos is not None:
            self._Tos = Tos
            properties['Tos'] = Tos
        if TrafficClass is not None:
            self._TrafficClass = TrafficClass
            properties['TrafficClass'] = TrafficClass
        if TCPTearDown is not None:
            self._TCPTearDown = TCPTearDown
            properties['TCPTearDown'] = TCPTearDown
        if EnableSSL is not None:
            self._EnableSSL = EnableSSL
            properties['EnableSSL'] = EnableSSL

        super(HttpCommonConfig, self).edit(**properties)

    @property
    def IntegrityCheck(self):
        """
        get the value of property _IntegrityCheck
        """
        if self.force_auto_sync:
            self.get('IntegrityCheck')
        return self._IntegrityCheck

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

    @property
    def TCPTearDown(self):
        """
        get the value of property _TCPTearDown
        """
        if self.force_auto_sync:
            self.get('TCPTearDown')
        return self._TCPTearDown

    @property
    def EnableSSL(self):
        """
        get the value of property _EnableSSL
        """
        if self.force_auto_sync:
            self.get('EnableSSL')
        return self._EnableSSL

    @IntegrityCheck.setter
    def IntegrityCheck(self, value):
        self._IntegrityCheck = value
        self.edit(IntegrityCheck=value)

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

    @TCPTearDown.setter
    def TCPTearDown(self, value):
        self._TCPTearDown = value
        self.edit(TCPTearDown=value)

    @EnableSSL.setter
    def EnableSSL(self, value):
        self._EnableSSL = value
        self.edit(EnableSSL=value)

    def _set_integritycheck_with_str(self, value):
        self._IntegrityCheck = (value == 'True')

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

    def _set_tcpteardown_with_str(self, value):
        seperate = value.find(':')
        exec('self._TCPTearDown = EnumTCPTearDown.%s' % value[:seperate])

    def _set_enablessl_with_str(self, value):
        self._EnableSSL = (value == 'True')

