"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class OfpProtocolConfig(L23ProtocolConfig):
    def __init__(self, TcpPort=None, ConnectionType=None, EnableEchoRequest=None, EchoRequestInterval=None, **kwargs):
        self._State = EnumOfpSessionState.DISABLED  # State, not editable
        self._TcpPort = TcpPort  # TCP Port
        self._ConnectionType = ConnectionType  # Connection Type
        self._EnableEchoRequest = EnableEchoRequest  # Enable Echo Request
        self._EchoRequestInterval = EchoRequestInterval  # Echo Request Interval (sec)

        properties = kwargs.copy()
        if TcpPort is not None:
            properties['TcpPort'] = TcpPort
        if ConnectionType is not None:
            properties['ConnectionType'] = ConnectionType
        if EnableEchoRequest is not None:
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            properties['EchoRequestInterval'] = EchoRequestInterval

        # call base class function, and it will send message to renix server to create a class.
        super(OfpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TcpPort=None, ConnectionType=None, EnableEchoRequest=None, EchoRequestInterval=None, **kwargs):
        properties = kwargs.copy()
        if TcpPort is not None:
            self._TcpPort = TcpPort
            properties['TcpPort'] = TcpPort
        if ConnectionType is not None:
            self._ConnectionType = ConnectionType
            properties['ConnectionType'] = ConnectionType
        if EnableEchoRequest is not None:
            self._EnableEchoRequest = EnableEchoRequest
            properties['EnableEchoRequest'] = EnableEchoRequest
        if EchoRequestInterval is not None:
            self._EchoRequestInterval = EchoRequestInterval
            properties['EchoRequestInterval'] = EchoRequestInterval

        super(OfpProtocolConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def TcpPort(self):
        """
        get the value of property _TcpPort
        """
        if self.force_auto_sync:
            self.get('TcpPort')
        return self._TcpPort

    @property
    def ConnectionType(self):
        """
        get the value of property _ConnectionType
        """
        if self.force_auto_sync:
            self.get('ConnectionType')
        return self._ConnectionType

    @property
    def EnableEchoRequest(self):
        """
        get the value of property _EnableEchoRequest
        """
        if self.force_auto_sync:
            self.get('EnableEchoRequest')
        return self._EnableEchoRequest

    @property
    def EchoRequestInterval(self):
        """
        get the value of property _EchoRequestInterval
        """
        if self.force_auto_sync:
            self.get('EchoRequestInterval')
        return self._EchoRequestInterval

    @TcpPort.setter
    def TcpPort(self, value):
        self._TcpPort = value
        self.edit(TcpPort=value)

    @ConnectionType.setter
    def ConnectionType(self, value):
        self._ConnectionType = value
        self.edit(ConnectionType=value)

    @EnableEchoRequest.setter
    def EnableEchoRequest(self, value):
        self._EnableEchoRequest = value
        self.edit(EnableEchoRequest=value)

    @EchoRequestInterval.setter
    def EchoRequestInterval(self, value):
        self._EchoRequestInterval = value
        self.edit(EchoRequestInterval=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumOfpSessionState.%s' % value[:seperate])

    def _set_tcpport_with_str(self, value):
        try:
            self._TcpPort = int(value)
        except ValueError:
            self._TcpPort = hex(int(value, 16))

    def _set_connectiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ConnectionType = EnumOfpConnection.%s' % value[:seperate])

    def _set_enableechorequest_with_str(self, value):
        self._EnableEchoRequest = (value == 'True')

    def _set_echorequestinterval_with_str(self, value):
        try:
            self._EchoRequestInterval = int(value)
        except ValueError:
            self._EchoRequestInterval = hex(int(value, 16))

