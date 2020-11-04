"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47Command_Autogen import L47Command


@rom_manager.rom
class DnsQuery(L47Command):
    def __init__(self, QueryType=None, DestAddress=None, DestPort=None, HostName=None, RecursionDesired=None, DnsClientCmdExpectType=None, **kwargs):
        self._QueryType = QueryType  # Query Type
        self._DestAddress = DestAddress  # DNS Server Address
        self._DestPort = DestPort  # DNS Server Port
        self._HostName = HostName  # Host Name
        self._RecursionDesired = RecursionDesired  # Recursion Desired
        self._DnsClientCmdExpectType = DnsClientCmdExpectType  # Expect

        properties = kwargs.copy()
        if QueryType is not None:
            properties['QueryType'] = QueryType
        if DestAddress is not None:
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            properties['DestPort'] = DestPort
        if HostName is not None:
            properties['HostName'] = HostName
        if RecursionDesired is not None:
            properties['RecursionDesired'] = RecursionDesired
        if DnsClientCmdExpectType is not None:
            properties['DnsClientCmdExpectType'] = DnsClientCmdExpectType

        # call base class function, and it will send message to renix server to create a class.
        super(DnsQuery, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, QueryType=None, DestAddress=None, DestPort=None, HostName=None, RecursionDesired=None, DnsClientCmdExpectType=None, **kwargs):
        properties = kwargs.copy()
        if QueryType is not None:
            self._QueryType = QueryType
            properties['QueryType'] = QueryType
        if DestAddress is not None:
            self._DestAddress = DestAddress
            properties['DestAddress'] = DestAddress
        if DestPort is not None:
            self._DestPort = DestPort
            properties['DestPort'] = DestPort
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if RecursionDesired is not None:
            self._RecursionDesired = RecursionDesired
            properties['RecursionDesired'] = RecursionDesired
        if DnsClientCmdExpectType is not None:
            self._DnsClientCmdExpectType = DnsClientCmdExpectType
            properties['DnsClientCmdExpectType'] = DnsClientCmdExpectType

        super(DnsQuery, self).edit(**properties)

    @property
    def QueryType(self):
        """
        get the value of property _QueryType
        """
        if self.force_auto_sync:
            self.get('QueryType')
        return self._QueryType

    @property
    def DestAddress(self):
        """
        get the value of property _DestAddress
        """
        if self.force_auto_sync:
            self.get('DestAddress')
        return self._DestAddress

    @property
    def DestPort(self):
        """
        get the value of property _DestPort
        """
        if self.force_auto_sync:
            self.get('DestPort')
        return self._DestPort

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def RecursionDesired(self):
        """
        get the value of property _RecursionDesired
        """
        if self.force_auto_sync:
            self.get('RecursionDesired')
        return self._RecursionDesired

    @property
    def DnsClientCmdExpectType(self):
        """
        get the value of property _DnsClientCmdExpectType
        """
        if self.force_auto_sync:
            self.get('DnsClientCmdExpectType')
        return self._DnsClientCmdExpectType

    @QueryType.setter
    def QueryType(self, value):
        self._QueryType = value
        self.edit(QueryType=value)

    @DestAddress.setter
    def DestAddress(self, value):
        self._DestAddress = value
        self.edit(DestAddress=value)

    @DestPort.setter
    def DestPort(self, value):
        self._DestPort = value
        self.edit(DestPort=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @RecursionDesired.setter
    def RecursionDesired(self, value):
        self._RecursionDesired = value
        self.edit(RecursionDesired=value)

    @DnsClientCmdExpectType.setter
    def DnsClientCmdExpectType(self, value):
        self._DnsClientCmdExpectType = value
        self.edit(DnsClientCmdExpectType=value)

    def _set_querytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._QueryType = ClientCmdQueryType.%s' % value[:seperate])

    def _set_destaddress_with_str(self, value):
        self._DestAddress = value

    def _set_destport_with_str(self, value):
        try:
            self._DestPort = int(value)
        except ValueError:
            self._DestPort = hex(int(value, 16))

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_recursiondesired_with_str(self, value):
        self._RecursionDesired = (value == 'True')

    def _set_dnsclientcmdexpecttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._DnsClientCmdExpectType = ClientCmdExpectType.%s' % value[:seperate])

