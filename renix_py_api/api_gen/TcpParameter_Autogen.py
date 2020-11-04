"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TcpParameter(ROMObject):
    def __init__(self, TcpSourcePort=None, TcpDestinationPort=None, **kwargs):
        self._TcpSourcePort = TcpSourcePort  # Source TCP Port
        self._TcpDestinationPort = TcpDestinationPort  # Destination TCP Port

        properties = kwargs.copy()
        if TcpSourcePort is not None:
            properties['TcpSourcePort'] = TcpSourcePort
        if TcpDestinationPort is not None:
            properties['TcpDestinationPort'] = TcpDestinationPort

        # call base class function, and it will send message to renix server to create a class.
        super(TcpParameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TcpSourcePort=None, TcpDestinationPort=None, **kwargs):
        properties = kwargs.copy()
        if TcpSourcePort is not None:
            self._TcpSourcePort = TcpSourcePort
            properties['TcpSourcePort'] = TcpSourcePort
        if TcpDestinationPort is not None:
            self._TcpDestinationPort = TcpDestinationPort
            properties['TcpDestinationPort'] = TcpDestinationPort

        super(TcpParameter, self).edit(**properties)

    @property
    def TcpSourcePort(self):
        """
        get the value of property _TcpSourcePort
        """
        if self.force_auto_sync:
            self.get('TcpSourcePort')
        return self._TcpSourcePort

    @property
    def TcpDestinationPort(self):
        """
        get the value of property _TcpDestinationPort
        """
        if self.force_auto_sync:
            self.get('TcpDestinationPort')
        return self._TcpDestinationPort

    @TcpSourcePort.setter
    def TcpSourcePort(self, value):
        self._TcpSourcePort = value
        self.edit(TcpSourcePort=value)

    @TcpDestinationPort.setter
    def TcpDestinationPort(self, value):
        self._TcpDestinationPort = value
        self.edit(TcpDestinationPort=value)

    def _set_tcpsourceport_with_str(self, value):
        try:
            self._TcpSourcePort = int(value)
        except ValueError:
            self._TcpSourcePort = hex(int(value, 16))

    def _set_tcpdestinationport_with_str(self, value):
        try:
            self._TcpDestinationPort = int(value)
        except ValueError:
            self._TcpDestinationPort = hex(int(value, 16))

