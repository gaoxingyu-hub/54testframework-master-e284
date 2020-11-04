"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ClientProfile_Autogen import L47ClientProfile


@rom_manager.rom
class DnsClientProfile(L47ClientProfile):
    def __init__(self, Transport=None, RetryNum=None, EnableWaitResponse=None, QueryTimeout=None, **kwargs):
        self._Transport = Transport  # Transport Type
        self._RetryNum = RetryNum  # Number of Retries
        self._EnableWaitResponse = EnableWaitResponse  # Wait Response
        self._QueryTimeout = QueryTimeout  # Query Timeout (ms)

        properties = kwargs.copy()
        if Transport is not None:
            properties['Transport'] = Transport
        if RetryNum is not None:
            properties['RetryNum'] = RetryNum
        if EnableWaitResponse is not None:
            properties['EnableWaitResponse'] = EnableWaitResponse
        if QueryTimeout is not None:
            properties['QueryTimeout'] = QueryTimeout

        # call base class function, and it will send message to renix server to create a class.
        super(DnsClientProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Transport=None, RetryNum=None, EnableWaitResponse=None, QueryTimeout=None, **kwargs):
        properties = kwargs.copy()
        if Transport is not None:
            self._Transport = Transport
            properties['Transport'] = Transport
        if RetryNum is not None:
            self._RetryNum = RetryNum
            properties['RetryNum'] = RetryNum
        if EnableWaitResponse is not None:
            self._EnableWaitResponse = EnableWaitResponse
            properties['EnableWaitResponse'] = EnableWaitResponse
        if QueryTimeout is not None:
            self._QueryTimeout = QueryTimeout
            properties['QueryTimeout'] = QueryTimeout

        super(DnsClientProfile, self).edit(**properties)

    @property
    def Transport(self):
        """
        get the value of property _Transport
        """
        if self.force_auto_sync:
            self.get('Transport')
        return self._Transport

    @property
    def RetryNum(self):
        """
        get the value of property _RetryNum
        """
        if self.force_auto_sync:
            self.get('RetryNum')
        return self._RetryNum

    @property
    def EnableWaitResponse(self):
        """
        get the value of property _EnableWaitResponse
        """
        if self.force_auto_sync:
            self.get('EnableWaitResponse')
        return self._EnableWaitResponse

    @property
    def QueryTimeout(self):
        """
        get the value of property _QueryTimeout
        """
        if self.force_auto_sync:
            self.get('QueryTimeout')
        return self._QueryTimeout

    @Transport.setter
    def Transport(self, value):
        self._Transport = value
        self.edit(Transport=value)

    @RetryNum.setter
    def RetryNum(self, value):
        self._RetryNum = value
        self.edit(RetryNum=value)

    @EnableWaitResponse.setter
    def EnableWaitResponse(self, value):
        self._EnableWaitResponse = value
        self.edit(EnableWaitResponse=value)

    @QueryTimeout.setter
    def QueryTimeout(self, value):
        self._QueryTimeout = value
        self.edit(QueryTimeout=value)

    def _set_transport_with_str(self, value):
        seperate = value.find(':')
        exec('self._Transport = TransportType.%s' % value[:seperate])

    def _set_retrynum_with_str(self, value):
        try:
            self._RetryNum = int(value)
        except ValueError:
            self._RetryNum = hex(int(value, 16))

    def _set_enablewaitresponse_with_str(self, value):
        self._EnableWaitResponse = (value == 'True')

    def _set_querytimeout_with_str(self, value):
        try:
            self._QueryTimeout = int(value)
        except ValueError:
            self._QueryTimeout = hex(int(value, 16))

