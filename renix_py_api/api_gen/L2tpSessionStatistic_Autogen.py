"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class L2tpSessionStatistic(Result):
    def __init__(self, **kwargs):
        self._L2tpBlockId = ''  # L2TP Block Name, not editable
        self._NodeIndexInBlock = 1  # Index in LAC/LNS Block, not editable
        self._LocalTunnelId = 0  # Local Tunnel ID, not editable
        self._RemoteTunnelId = 0  # Remote Tunnel ID, not editable
        self._LocalSessionId = 0  # Local Session ID, not editable
        self._RemoteSessionId = 0  # Remote Session ID, not editable
        self._SessionState = 'Idle'  # Session State, not editable
        self._LocalTunnelIpAddress = ''  # Local Tunnel IPv4 Address, not editable
        self._RemoteTunnelIpAddress = ''  # Remote Tunnel IPv4 Address, not editable
        self._LocalTunnelIpv6Address = ''  # Local Tunnel IPv6 Address, not editable
        self._RemoteTunnelIpv6Address = ''  # Remote Tunnel IPv6 Address, not editable
        self._TxIcrq = 0  # Tx ICRQ, not editable
        self._RxIcrq = 0  # Rx ICRQ, not editable
        self._TxIcrp = 0  # Tx ICRP, not editable
        self._RxIcrp = 0  # Rx ICRP, not editable
        self._TxIccn = 0  # Tx ICCN, not editable
        self._RxIccn = 0  # Rx ICCN, not editable
        self._TxCdn = 0  # Tx CDN, not editable
        self._RxCdn = 0  # Rx CDN, not editable
        self._ResultCode = 0  # Result Code, not editable
        self._ErrorCode = 0  # Error Code, not editable
        self._ErrorMessage = ''  # Error Message, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpSessionStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def L2tpBlockId(self):
        """
        get the value of property _L2tpBlockId
        """
        if self.force_auto_sync:
            self.get('L2tpBlockId')
        return self._L2tpBlockId

    @property
    def NodeIndexInBlock(self):
        """
        get the value of property _NodeIndexInBlock
        """
        if self.force_auto_sync:
            self.get('NodeIndexInBlock')
        return self._NodeIndexInBlock

    @property
    def LocalTunnelId(self):
        """
        get the value of property _LocalTunnelId
        """
        if self.force_auto_sync:
            self.get('LocalTunnelId')
        return self._LocalTunnelId

    @property
    def RemoteTunnelId(self):
        """
        get the value of property _RemoteTunnelId
        """
        if self.force_auto_sync:
            self.get('RemoteTunnelId')
        return self._RemoteTunnelId

    @property
    def LocalSessionId(self):
        """
        get the value of property _LocalSessionId
        """
        if self.force_auto_sync:
            self.get('LocalSessionId')
        return self._LocalSessionId

    @property
    def RemoteSessionId(self):
        """
        get the value of property _RemoteSessionId
        """
        if self.force_auto_sync:
            self.get('RemoteSessionId')
        return self._RemoteSessionId

    @property
    def SessionState(self):
        """
        get the value of property _SessionState
        """
        if self.force_auto_sync:
            self.get('SessionState')
        return self._SessionState

    @property
    def LocalTunnelIpAddress(self):
        """
        get the value of property _LocalTunnelIpAddress
        """
        if self.force_auto_sync:
            self.get('LocalTunnelIpAddress')
        return self._LocalTunnelIpAddress

    @property
    def RemoteTunnelIpAddress(self):
        """
        get the value of property _RemoteTunnelIpAddress
        """
        if self.force_auto_sync:
            self.get('RemoteTunnelIpAddress')
        return self._RemoteTunnelIpAddress

    @property
    def LocalTunnelIpv6Address(self):
        """
        get the value of property _LocalTunnelIpv6Address
        """
        if self.force_auto_sync:
            self.get('LocalTunnelIpv6Address')
        return self._LocalTunnelIpv6Address

    @property
    def RemoteTunnelIpv6Address(self):
        """
        get the value of property _RemoteTunnelIpv6Address
        """
        if self.force_auto_sync:
            self.get('RemoteTunnelIpv6Address')
        return self._RemoteTunnelIpv6Address

    @property
    def TxIcrq(self):
        """
        get the value of property _TxIcrq
        """
        if self.force_auto_sync:
            self.get('TxIcrq')
        return self._TxIcrq

    @property
    def RxIcrq(self):
        """
        get the value of property _RxIcrq
        """
        if self.force_auto_sync:
            self.get('RxIcrq')
        return self._RxIcrq

    @property
    def TxIcrp(self):
        """
        get the value of property _TxIcrp
        """
        if self.force_auto_sync:
            self.get('TxIcrp')
        return self._TxIcrp

    @property
    def RxIcrp(self):
        """
        get the value of property _RxIcrp
        """
        if self.force_auto_sync:
            self.get('RxIcrp')
        return self._RxIcrp

    @property
    def TxIccn(self):
        """
        get the value of property _TxIccn
        """
        if self.force_auto_sync:
            self.get('TxIccn')
        return self._TxIccn

    @property
    def RxIccn(self):
        """
        get the value of property _RxIccn
        """
        if self.force_auto_sync:
            self.get('RxIccn')
        return self._RxIccn

    @property
    def TxCdn(self):
        """
        get the value of property _TxCdn
        """
        if self.force_auto_sync:
            self.get('TxCdn')
        return self._TxCdn

    @property
    def RxCdn(self):
        """
        get the value of property _RxCdn
        """
        if self.force_auto_sync:
            self.get('RxCdn')
        return self._RxCdn

    @property
    def ResultCode(self):
        """
        get the value of property _ResultCode
        """
        if self.force_auto_sync:
            self.get('ResultCode')
        return self._ResultCode

    @property
    def ErrorCode(self):
        """
        get the value of property _ErrorCode
        """
        if self.force_auto_sync:
            self.get('ErrorCode')
        return self._ErrorCode

    @property
    def ErrorMessage(self):
        """
        get the value of property _ErrorMessage
        """
        if self.force_auto_sync:
            self.get('ErrorMessage')
        return self._ErrorMessage

    def _set_l2tpblockid_with_str(self, value):
        self._L2tpBlockId = value

    def _set_nodeindexinblock_with_str(self, value):
        try:
            self._NodeIndexInBlock = int(value)
        except ValueError:
            self._NodeIndexInBlock = hex(int(value, 16))

    def _set_localtunnelid_with_str(self, value):
        try:
            self._LocalTunnelId = int(value)
        except ValueError:
            self._LocalTunnelId = hex(int(value, 16))

    def _set_remotetunnelid_with_str(self, value):
        try:
            self._RemoteTunnelId = int(value)
        except ValueError:
            self._RemoteTunnelId = hex(int(value, 16))

    def _set_localsessionid_with_str(self, value):
        try:
            self._LocalSessionId = int(value)
        except ValueError:
            self._LocalSessionId = hex(int(value, 16))

    def _set_remotesessionid_with_str(self, value):
        try:
            self._RemoteSessionId = int(value)
        except ValueError:
            self._RemoteSessionId = hex(int(value, 16))

    def _set_sessionstate_with_str(self, value):
        self._SessionState = value

    def _set_localtunnelipaddress_with_str(self, value):
        self._LocalTunnelIpAddress = value

    def _set_remotetunnelipaddress_with_str(self, value):
        self._RemoteTunnelIpAddress = value

    def _set_localtunnelipv6address_with_str(self, value):
        self._LocalTunnelIpv6Address = value

    def _set_remotetunnelipv6address_with_str(self, value):
        self._RemoteTunnelIpv6Address = value

    def _set_txicrq_with_str(self, value):
        try:
            self._TxIcrq = int(value)
        except ValueError:
            self._TxIcrq = hex(int(value, 16))

    def _set_rxicrq_with_str(self, value):
        try:
            self._RxIcrq = int(value)
        except ValueError:
            self._RxIcrq = hex(int(value, 16))

    def _set_txicrp_with_str(self, value):
        try:
            self._TxIcrp = int(value)
        except ValueError:
            self._TxIcrp = hex(int(value, 16))

    def _set_rxicrp_with_str(self, value):
        try:
            self._RxIcrp = int(value)
        except ValueError:
            self._RxIcrp = hex(int(value, 16))

    def _set_txiccn_with_str(self, value):
        try:
            self._TxIccn = int(value)
        except ValueError:
            self._TxIccn = hex(int(value, 16))

    def _set_rxiccn_with_str(self, value):
        try:
            self._RxIccn = int(value)
        except ValueError:
            self._RxIccn = hex(int(value, 16))

    def _set_txcdn_with_str(self, value):
        try:
            self._TxCdn = int(value)
        except ValueError:
            self._TxCdn = hex(int(value, 16))

    def _set_rxcdn_with_str(self, value):
        try:
            self._RxCdn = int(value)
        except ValueError:
            self._RxCdn = hex(int(value, 16))

    def _set_resultcode_with_str(self, value):
        try:
            self._ResultCode = int(value)
        except ValueError:
            self._ResultCode = hex(int(value, 16))

    def _set_errorcode_with_str(self, value):
        try:
            self._ErrorCode = int(value)
        except ValueError:
            self._ErrorCode = hex(int(value, 16))

    def _set_errormessage_with_str(self, value):
        self._ErrorMessage = value

