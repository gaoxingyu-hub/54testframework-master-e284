"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ServerProfile_Autogen import L47ServerProfile


@rom_manager.rom
class HttpServerProfile(L47ServerProfile):
    def __init__(self, HttpVersion=None, ListenPort=None, RequestTimeout=None, EnableDelayResponse=None, MinDelayTime=None, MaxDelayTime=None, **kwargs):
        self._HttpVersion = HttpVersion  # HTTP Version
        self._ListenPort = ListenPort  # Listen Port
        self._RequestTimeout = RequestTimeout  # Request Timeout (ms)
        self._EnableDelayResponse = EnableDelayResponse  # Enable Delay Response
        self._MinDelayTime = MinDelayTime  # Min Response Delay Time
        self._MaxDelayTime = MaxDelayTime  # Max Response Delay Time

        properties = kwargs.copy()
        if HttpVersion is not None:
            properties['HttpVersion'] = HttpVersion
        if ListenPort is not None:
            properties['ListenPort'] = ListenPort
        if RequestTimeout is not None:
            properties['RequestTimeout'] = RequestTimeout
        if EnableDelayResponse is not None:
            properties['EnableDelayResponse'] = EnableDelayResponse
        if MinDelayTime is not None:
            properties['MinDelayTime'] = MinDelayTime
        if MaxDelayTime is not None:
            properties['MaxDelayTime'] = MaxDelayTime

        # call base class function, and it will send message to renix server to create a class.
        super(HttpServerProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HttpVersion=None, ListenPort=None, RequestTimeout=None, EnableDelayResponse=None, MinDelayTime=None, MaxDelayTime=None, **kwargs):
        properties = kwargs.copy()
        if HttpVersion is not None:
            self._HttpVersion = HttpVersion
            properties['HttpVersion'] = HttpVersion
        if ListenPort is not None:
            self._ListenPort = ListenPort
            properties['ListenPort'] = ListenPort
        if RequestTimeout is not None:
            self._RequestTimeout = RequestTimeout
            properties['RequestTimeout'] = RequestTimeout
        if EnableDelayResponse is not None:
            self._EnableDelayResponse = EnableDelayResponse
            properties['EnableDelayResponse'] = EnableDelayResponse
        if MinDelayTime is not None:
            self._MinDelayTime = MinDelayTime
            properties['MinDelayTime'] = MinDelayTime
        if MaxDelayTime is not None:
            self._MaxDelayTime = MaxDelayTime
            properties['MaxDelayTime'] = MaxDelayTime

        super(HttpServerProfile, self).edit(**properties)

    @property
    def HttpVersion(self):
        """
        get the value of property _HttpVersion
        """
        if self.force_auto_sync:
            self.get('HttpVersion')
        return self._HttpVersion

    @property
    def ListenPort(self):
        """
        get the value of property _ListenPort
        """
        if self.force_auto_sync:
            self.get('ListenPort')
        return self._ListenPort

    @property
    def RequestTimeout(self):
        """
        get the value of property _RequestTimeout
        """
        if self.force_auto_sync:
            self.get('RequestTimeout')
        return self._RequestTimeout

    @property
    def EnableDelayResponse(self):
        """
        get the value of property _EnableDelayResponse
        """
        if self.force_auto_sync:
            self.get('EnableDelayResponse')
        return self._EnableDelayResponse

    @property
    def MinDelayTime(self):
        """
        get the value of property _MinDelayTime
        """
        if self.force_auto_sync:
            self.get('MinDelayTime')
        return self._MinDelayTime

    @property
    def MaxDelayTime(self):
        """
        get the value of property _MaxDelayTime
        """
        if self.force_auto_sync:
            self.get('MaxDelayTime')
        return self._MaxDelayTime

    @HttpVersion.setter
    def HttpVersion(self, value):
        self._HttpVersion = value
        self.edit(HttpVersion=value)

    @ListenPort.setter
    def ListenPort(self, value):
        self._ListenPort = value
        self.edit(ListenPort=value)

    @RequestTimeout.setter
    def RequestTimeout(self, value):
        self._RequestTimeout = value
        self.edit(RequestTimeout=value)

    @EnableDelayResponse.setter
    def EnableDelayResponse(self, value):
        self._EnableDelayResponse = value
        self.edit(EnableDelayResponse=value)

    @MinDelayTime.setter
    def MinDelayTime(self, value):
        self._MinDelayTime = value
        self.edit(MinDelayTime=value)

    @MaxDelayTime.setter
    def MaxDelayTime(self, value):
        self._MaxDelayTime = value
        self.edit(MaxDelayTime=value)

    def _set_httpversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._HttpVersion = EnumHttpVersion.%s' % value[:seperate])

    def _set_listenport_with_str(self, value):
        try:
            self._ListenPort = int(value)
        except ValueError:
            self._ListenPort = hex(int(value, 16))

    def _set_requesttimeout_with_str(self, value):
        try:
            self._RequestTimeout = int(value)
        except ValueError:
            self._RequestTimeout = hex(int(value, 16))

    def _set_enabledelayresponse_with_str(self, value):
        self._EnableDelayResponse = (value == 'True')

    def _set_mindelaytime_with_str(self, value):
        try:
            self._MinDelayTime = int(value)
        except ValueError:
            self._MinDelayTime = hex(int(value, 16))

    def _set_maxdelaytime_with_str(self, value):
        try:
            self._MaxDelayTime = int(value)
        except ValueError:
            self._MaxDelayTime = hex(int(value, 16))

