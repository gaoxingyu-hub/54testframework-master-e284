"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ServerProfile_Autogen import L47ServerProfile


@rom_manager.rom
class DnsServerProfile(L47ServerProfile):
    def __init__(self, ListenPort=None, RequestTimeOut=None, **kwargs):
        self._ListenPort = ListenPort  # Listening Port
        self._RequestTimeOut = RequestTimeOut  # Request Timeout (sec)

        properties = kwargs.copy()
        if ListenPort is not None:
            properties['ListenPort'] = ListenPort
        if RequestTimeOut is not None:
            properties['RequestTimeOut'] = RequestTimeOut

        # call base class function, and it will send message to renix server to create a class.
        super(DnsServerProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ListenPort=None, RequestTimeOut=None, **kwargs):
        properties = kwargs.copy()
        if ListenPort is not None:
            self._ListenPort = ListenPort
            properties['ListenPort'] = ListenPort
        if RequestTimeOut is not None:
            self._RequestTimeOut = RequestTimeOut
            properties['RequestTimeOut'] = RequestTimeOut

        super(DnsServerProfile, self).edit(**properties)

    @property
    def ListenPort(self):
        """
        get the value of property _ListenPort
        """
        if self.force_auto_sync:
            self.get('ListenPort')
        return self._ListenPort

    @property
    def RequestTimeOut(self):
        """
        get the value of property _RequestTimeOut
        """
        if self.force_auto_sync:
            self.get('RequestTimeOut')
        return self._RequestTimeOut

    @ListenPort.setter
    def ListenPort(self, value):
        self._ListenPort = value
        self.edit(ListenPort=value)

    @RequestTimeOut.setter
    def RequestTimeOut(self, value):
        self._RequestTimeOut = value
        self.edit(RequestTimeOut=value)

    def _set_listenport_with_str(self, value):
        try:
            self._ListenPort = int(value)
        except ValueError:
            self._ListenPort = hex(int(value, 16))

    def _set_requesttimeout_with_str(self, value):
        try:
            self._RequestTimeOut = int(value)
        except ValueError:
            self._RequestTimeOut = hex(int(value, 16))

