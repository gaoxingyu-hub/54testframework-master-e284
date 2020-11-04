"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class UdpParameter(ROMObject):
    def __init__(self, UdpSourcePort=None, UdpDestinationPort=None, **kwargs):
        self._UdpSourcePort = UdpSourcePort  # Source UDP Port
        self._UdpDestinationPort = UdpDestinationPort  # Destination UDP Port

        properties = kwargs.copy()
        if UdpSourcePort is not None:
            properties['UdpSourcePort'] = UdpSourcePort
        if UdpDestinationPort is not None:
            properties['UdpDestinationPort'] = UdpDestinationPort

        # call base class function, and it will send message to renix server to create a class.
        super(UdpParameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, UdpSourcePort=None, UdpDestinationPort=None, **kwargs):
        properties = kwargs.copy()
        if UdpSourcePort is not None:
            self._UdpSourcePort = UdpSourcePort
            properties['UdpSourcePort'] = UdpSourcePort
        if UdpDestinationPort is not None:
            self._UdpDestinationPort = UdpDestinationPort
            properties['UdpDestinationPort'] = UdpDestinationPort

        super(UdpParameter, self).edit(**properties)

    @property
    def UdpSourcePort(self):
        """
        get the value of property _UdpSourcePort
        """
        if self.force_auto_sync:
            self.get('UdpSourcePort')
        return self._UdpSourcePort

    @property
    def UdpDestinationPort(self):
        """
        get the value of property _UdpDestinationPort
        """
        if self.force_auto_sync:
            self.get('UdpDestinationPort')
        return self._UdpDestinationPort

    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._UdpSourcePort = value
        self.edit(UdpSourcePort=value)

    @UdpDestinationPort.setter
    def UdpDestinationPort(self, value):
        self._UdpDestinationPort = value
        self.edit(UdpDestinationPort=value)

    def _set_udpsourceport_with_str(self, value):
        try:
            self._UdpSourcePort = int(value)
        except ValueError:
            self._UdpSourcePort = hex(int(value, 16))

    def _set_udpdestinationport_with_str(self, value):
        try:
            self._UdpDestinationPort = int(value)
        except ValueError:
            self._UdpDestinationPort = hex(int(value, 16))

