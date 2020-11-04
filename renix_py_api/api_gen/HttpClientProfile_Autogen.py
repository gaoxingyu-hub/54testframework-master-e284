"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ClientProfile_Autogen import L47ClientProfile


@rom_manager.rom
class HttpClientProfile(L47ClientProfile):
    def __init__(self, HttpVersion=None, ConcurrentConnPerUser=None, KeepAlive=None, MaximumPossible=None, TransactionPerConn=None, MaxPipelineDepth=None, **kwargs):
        self._HttpVersion = HttpVersion  # HTTP Version
        self._ConcurrentConnPerUser = ConcurrentConnPerUser  # Concurrent Connection Per User
        self._KeepAlive = KeepAlive  # Keep Alive
        self._MaximumPossible = MaximumPossible  # Maximum Possible
        self._TransactionPerConn = TransactionPerConn  # Transaction(s) per Connection
        self._MaxPipelineDepth = MaxPipelineDepth  # Max. Pipeline Depth

        properties = kwargs.copy()
        if HttpVersion is not None:
            properties['HttpVersion'] = HttpVersion
        if ConcurrentConnPerUser is not None:
            properties['ConcurrentConnPerUser'] = ConcurrentConnPerUser
        if KeepAlive is not None:
            properties['KeepAlive'] = KeepAlive
        if MaximumPossible is not None:
            properties['MaximumPossible'] = MaximumPossible
        if TransactionPerConn is not None:
            properties['TransactionPerConn'] = TransactionPerConn
        if MaxPipelineDepth is not None:
            properties['MaxPipelineDepth'] = MaxPipelineDepth

        # call base class function, and it will send message to renix server to create a class.
        super(HttpClientProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HttpVersion=None, ConcurrentConnPerUser=None, KeepAlive=None, MaximumPossible=None, TransactionPerConn=None, MaxPipelineDepth=None, **kwargs):
        properties = kwargs.copy()
        if HttpVersion is not None:
            self._HttpVersion = HttpVersion
            properties['HttpVersion'] = HttpVersion
        if ConcurrentConnPerUser is not None:
            self._ConcurrentConnPerUser = ConcurrentConnPerUser
            properties['ConcurrentConnPerUser'] = ConcurrentConnPerUser
        if KeepAlive is not None:
            self._KeepAlive = KeepAlive
            properties['KeepAlive'] = KeepAlive
        if MaximumPossible is not None:
            self._MaximumPossible = MaximumPossible
            properties['MaximumPossible'] = MaximumPossible
        if TransactionPerConn is not None:
            self._TransactionPerConn = TransactionPerConn
            properties['TransactionPerConn'] = TransactionPerConn
        if MaxPipelineDepth is not None:
            self._MaxPipelineDepth = MaxPipelineDepth
            properties['MaxPipelineDepth'] = MaxPipelineDepth

        super(HttpClientProfile, self).edit(**properties)

    @property
    def HttpVersion(self):
        """
        get the value of property _HttpVersion
        """
        if self.force_auto_sync:
            self.get('HttpVersion')
        return self._HttpVersion

    @property
    def ConcurrentConnPerUser(self):
        """
        get the value of property _ConcurrentConnPerUser
        """
        if self.force_auto_sync:
            self.get('ConcurrentConnPerUser')
        return self._ConcurrentConnPerUser

    @property
    def KeepAlive(self):
        """
        get the value of property _KeepAlive
        """
        if self.force_auto_sync:
            self.get('KeepAlive')
        return self._KeepAlive

    @property
    def MaximumPossible(self):
        """
        get the value of property _MaximumPossible
        """
        if self.force_auto_sync:
            self.get('MaximumPossible')
        return self._MaximumPossible

    @property
    def TransactionPerConn(self):
        """
        get the value of property _TransactionPerConn
        """
        if self.force_auto_sync:
            self.get('TransactionPerConn')
        return self._TransactionPerConn

    @property
    def MaxPipelineDepth(self):
        """
        get the value of property _MaxPipelineDepth
        """
        if self.force_auto_sync:
            self.get('MaxPipelineDepth')
        return self._MaxPipelineDepth

    @HttpVersion.setter
    def HttpVersion(self, value):
        self._HttpVersion = value
        self.edit(HttpVersion=value)

    @ConcurrentConnPerUser.setter
    def ConcurrentConnPerUser(self, value):
        self._ConcurrentConnPerUser = value
        self.edit(ConcurrentConnPerUser=value)

    @KeepAlive.setter
    def KeepAlive(self, value):
        self._KeepAlive = value
        self.edit(KeepAlive=value)

    @MaximumPossible.setter
    def MaximumPossible(self, value):
        self._MaximumPossible = value
        self.edit(MaximumPossible=value)

    @TransactionPerConn.setter
    def TransactionPerConn(self, value):
        self._TransactionPerConn = value
        self.edit(TransactionPerConn=value)

    @MaxPipelineDepth.setter
    def MaxPipelineDepth(self, value):
        self._MaxPipelineDepth = value
        self.edit(MaxPipelineDepth=value)

    def _set_httpversion_with_str(self, value):
        seperate = value.find(':')
        exec('self._HttpVersion = EnumHttpVersion.%s' % value[:seperate])

    def _set_concurrentconnperuser_with_str(self, value):
        try:
            self._ConcurrentConnPerUser = int(value)
        except ValueError:
            self._ConcurrentConnPerUser = hex(int(value, 16))

    def _set_keepalive_with_str(self, value):
        self._KeepAlive = (value == 'True')

    def _set_maximumpossible_with_str(self, value):
        self._MaximumPossible = (value == 'True')

    def _set_transactionperconn_with_str(self, value):
        try:
            self._TransactionPerConn = int(value)
        except ValueError:
            self._TransactionPerConn = hex(int(value, 16))

    def _set_maxpipelinedepth_with_str(self, value):
        try:
            self._MaxPipelineDepth = int(value)
        except ValueError:
            self._MaxPipelineDepth = hex(int(value, 16))

