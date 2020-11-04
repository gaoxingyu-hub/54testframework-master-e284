"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TcpConfig(ROMObject):
    def __init__(self, ReceiveWindowSize=None, SendWindowSize=None, RetransmissionTimeoutMin=None, RetransmissionTimeoutMax=None, KeepAliveInitTime=None, KeepAliveIdleTime=None, KeepAliveInterval=None, KeepAliveProbes=None, CongestionControl=None, MaxSegSize=None, MaxSegLifetime=None, FinWaitTimeout=None, SYNRetries=None, EnableHighperformanceTCP=None, EnableLimitedTransmitTCP=None, DelayAck=None, DelayAckTimeout=None, SelectAck=None, SackHoles=None, TotalSackHoles=None, **kwargs):
        self._ReceiveWindowSize = ReceiveWindowSize  # Receive Window Size
        self._SendWindowSize = SendWindowSize  # Send Window Size
        self._RetransmissionTimeoutMin = RetransmissionTimeoutMin  # Retransmission Timeout Min
        self._RetransmissionTimeoutMax = RetransmissionTimeoutMax  # Retransmission Timeout Max
        self._KeepAliveInitTime = KeepAliveInitTime  # Keep-Alive Initial Time
        self._KeepAliveIdleTime = KeepAliveIdleTime  # Keep-Alive Idle Time
        self._KeepAliveInterval = KeepAliveInterval  # Keep-Alive Interval
        self._KeepAliveProbes = KeepAliveProbes  # Keep-Alive Probes
        self._CongestionControl = CongestionControl  # Congestion Control
        self._MaxSegSize = MaxSegSize  # Max Segment Size (TX)
        self._MaxSegLifetime = MaxSegLifetime  # Max Segment Lifetime
        self._FinWaitTimeout = FinWaitTimeout  # Fin Wait Timeout
        self._SYNRetries = SYNRetries  # SYN Retries
        self._EnableHighperformanceTCP = EnableHighperformanceTCP  # Enable RFC1323 High Performance TCP
        self._EnableLimitedTransmitTCP = EnableLimitedTransmitTCP  # Enable RFC3042 Limited Transmit TCP
        self._DelayAck = DelayAck  # Delay ACK
        self._DelayAckTimeout = DelayAckTimeout  # Delay ACK Timeout
        self._SelectAck = SelectAck  # Selective ACK
        self._SackHoles = SackHoles  # Sack Holes Per TCP Connection
        self._TotalSackHoles = TotalSackHoles  # Total Sack Holes

        properties = kwargs.copy()
        if ReceiveWindowSize is not None:
            properties['ReceiveWindowSize'] = ReceiveWindowSize
        if SendWindowSize is not None:
            properties['SendWindowSize'] = SendWindowSize
        if RetransmissionTimeoutMin is not None:
            properties['RetransmissionTimeoutMin'] = RetransmissionTimeoutMin
        if RetransmissionTimeoutMax is not None:
            properties['RetransmissionTimeoutMax'] = RetransmissionTimeoutMax
        if KeepAliveInitTime is not None:
            properties['KeepAliveInitTime'] = KeepAliveInitTime
        if KeepAliveIdleTime is not None:
            properties['KeepAliveIdleTime'] = KeepAliveIdleTime
        if KeepAliveInterval is not None:
            properties['KeepAliveInterval'] = KeepAliveInterval
        if KeepAliveProbes is not None:
            properties['KeepAliveProbes'] = KeepAliveProbes
        if CongestionControl is not None:
            properties['CongestionControl'] = CongestionControl
        if MaxSegSize is not None:
            properties['MaxSegSize'] = MaxSegSize
        if MaxSegLifetime is not None:
            properties['MaxSegLifetime'] = MaxSegLifetime
        if FinWaitTimeout is not None:
            properties['FinWaitTimeout'] = FinWaitTimeout
        if SYNRetries is not None:
            properties['SYNRetries'] = SYNRetries
        if EnableHighperformanceTCP is not None:
            properties['EnableHighperformanceTCP'] = EnableHighperformanceTCP
        if EnableLimitedTransmitTCP is not None:
            properties['EnableLimitedTransmitTCP'] = EnableLimitedTransmitTCP
        if DelayAck is not None:
            properties['DelayAck'] = DelayAck
        if DelayAckTimeout is not None:
            properties['DelayAckTimeout'] = DelayAckTimeout
        if SelectAck is not None:
            properties['SelectAck'] = SelectAck
        if SackHoles is not None:
            properties['SackHoles'] = SackHoles
        if TotalSackHoles is not None:
            properties['TotalSackHoles'] = TotalSackHoles

        # call base class function, and it will send message to renix server to create a class.
        super(TcpConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ReceiveWindowSize=None, SendWindowSize=None, RetransmissionTimeoutMin=None, RetransmissionTimeoutMax=None, KeepAliveInitTime=None, KeepAliveIdleTime=None, KeepAliveInterval=None, KeepAliveProbes=None, CongestionControl=None, MaxSegSize=None, MaxSegLifetime=None, FinWaitTimeout=None, SYNRetries=None, EnableHighperformanceTCP=None, EnableLimitedTransmitTCP=None, DelayAck=None, DelayAckTimeout=None, SelectAck=None, SackHoles=None, TotalSackHoles=None, **kwargs):
        properties = kwargs.copy()
        if ReceiveWindowSize is not None:
            self._ReceiveWindowSize = ReceiveWindowSize
            properties['ReceiveWindowSize'] = ReceiveWindowSize
        if SendWindowSize is not None:
            self._SendWindowSize = SendWindowSize
            properties['SendWindowSize'] = SendWindowSize
        if RetransmissionTimeoutMin is not None:
            self._RetransmissionTimeoutMin = RetransmissionTimeoutMin
            properties['RetransmissionTimeoutMin'] = RetransmissionTimeoutMin
        if RetransmissionTimeoutMax is not None:
            self._RetransmissionTimeoutMax = RetransmissionTimeoutMax
            properties['RetransmissionTimeoutMax'] = RetransmissionTimeoutMax
        if KeepAliveInitTime is not None:
            self._KeepAliveInitTime = KeepAliveInitTime
            properties['KeepAliveInitTime'] = KeepAliveInitTime
        if KeepAliveIdleTime is not None:
            self._KeepAliveIdleTime = KeepAliveIdleTime
            properties['KeepAliveIdleTime'] = KeepAliveIdleTime
        if KeepAliveInterval is not None:
            self._KeepAliveInterval = KeepAliveInterval
            properties['KeepAliveInterval'] = KeepAliveInterval
        if KeepAliveProbes is not None:
            self._KeepAliveProbes = KeepAliveProbes
            properties['KeepAliveProbes'] = KeepAliveProbes
        if CongestionControl is not None:
            self._CongestionControl = CongestionControl
            properties['CongestionControl'] = CongestionControl
        if MaxSegSize is not None:
            self._MaxSegSize = MaxSegSize
            properties['MaxSegSize'] = MaxSegSize
        if MaxSegLifetime is not None:
            self._MaxSegLifetime = MaxSegLifetime
            properties['MaxSegLifetime'] = MaxSegLifetime
        if FinWaitTimeout is not None:
            self._FinWaitTimeout = FinWaitTimeout
            properties['FinWaitTimeout'] = FinWaitTimeout
        if SYNRetries is not None:
            self._SYNRetries = SYNRetries
            properties['SYNRetries'] = SYNRetries
        if EnableHighperformanceTCP is not None:
            self._EnableHighperformanceTCP = EnableHighperformanceTCP
            properties['EnableHighperformanceTCP'] = EnableHighperformanceTCP
        if EnableLimitedTransmitTCP is not None:
            self._EnableLimitedTransmitTCP = EnableLimitedTransmitTCP
            properties['EnableLimitedTransmitTCP'] = EnableLimitedTransmitTCP
        if DelayAck is not None:
            self._DelayAck = DelayAck
            properties['DelayAck'] = DelayAck
        if DelayAckTimeout is not None:
            self._DelayAckTimeout = DelayAckTimeout
            properties['DelayAckTimeout'] = DelayAckTimeout
        if SelectAck is not None:
            self._SelectAck = SelectAck
            properties['SelectAck'] = SelectAck
        if SackHoles is not None:
            self._SackHoles = SackHoles
            properties['SackHoles'] = SackHoles
        if TotalSackHoles is not None:
            self._TotalSackHoles = TotalSackHoles
            properties['TotalSackHoles'] = TotalSackHoles

        super(TcpConfig, self).edit(**properties)

    @property
    def ReceiveWindowSize(self):
        """
        get the value of property _ReceiveWindowSize
        """
        if self.force_auto_sync:
            self.get('ReceiveWindowSize')
        return self._ReceiveWindowSize

    @property
    def SendWindowSize(self):
        """
        get the value of property _SendWindowSize
        """
        if self.force_auto_sync:
            self.get('SendWindowSize')
        return self._SendWindowSize

    @property
    def RetransmissionTimeoutMin(self):
        """
        get the value of property _RetransmissionTimeoutMin
        """
        if self.force_auto_sync:
            self.get('RetransmissionTimeoutMin')
        return self._RetransmissionTimeoutMin

    @property
    def RetransmissionTimeoutMax(self):
        """
        get the value of property _RetransmissionTimeoutMax
        """
        if self.force_auto_sync:
            self.get('RetransmissionTimeoutMax')
        return self._RetransmissionTimeoutMax

    @property
    def KeepAliveInitTime(self):
        """
        get the value of property _KeepAliveInitTime
        """
        if self.force_auto_sync:
            self.get('KeepAliveInitTime')
        return self._KeepAliveInitTime

    @property
    def KeepAliveIdleTime(self):
        """
        get the value of property _KeepAliveIdleTime
        """
        if self.force_auto_sync:
            self.get('KeepAliveIdleTime')
        return self._KeepAliveIdleTime

    @property
    def KeepAliveInterval(self):
        """
        get the value of property _KeepAliveInterval
        """
        if self.force_auto_sync:
            self.get('KeepAliveInterval')
        return self._KeepAliveInterval

    @property
    def KeepAliveProbes(self):
        """
        get the value of property _KeepAliveProbes
        """
        if self.force_auto_sync:
            self.get('KeepAliveProbes')
        return self._KeepAliveProbes

    @property
    def CongestionControl(self):
        """
        get the value of property _CongestionControl
        """
        if self.force_auto_sync:
            self.get('CongestionControl')
        return self._CongestionControl

    @property
    def MaxSegSize(self):
        """
        get the value of property _MaxSegSize
        """
        if self.force_auto_sync:
            self.get('MaxSegSize')
        return self._MaxSegSize

    @property
    def MaxSegLifetime(self):
        """
        get the value of property _MaxSegLifetime
        """
        if self.force_auto_sync:
            self.get('MaxSegLifetime')
        return self._MaxSegLifetime

    @property
    def FinWaitTimeout(self):
        """
        get the value of property _FinWaitTimeout
        """
        if self.force_auto_sync:
            self.get('FinWaitTimeout')
        return self._FinWaitTimeout

    @property
    def SYNRetries(self):
        """
        get the value of property _SYNRetries
        """
        if self.force_auto_sync:
            self.get('SYNRetries')
        return self._SYNRetries

    @property
    def EnableHighperformanceTCP(self):
        """
        get the value of property _EnableHighperformanceTCP
        """
        if self.force_auto_sync:
            self.get('EnableHighperformanceTCP')
        return self._EnableHighperformanceTCP

    @property
    def EnableLimitedTransmitTCP(self):
        """
        get the value of property _EnableLimitedTransmitTCP
        """
        if self.force_auto_sync:
            self.get('EnableLimitedTransmitTCP')
        return self._EnableLimitedTransmitTCP

    @property
    def DelayAck(self):
        """
        get the value of property _DelayAck
        """
        if self.force_auto_sync:
            self.get('DelayAck')
        return self._DelayAck

    @property
    def DelayAckTimeout(self):
        """
        get the value of property _DelayAckTimeout
        """
        if self.force_auto_sync:
            self.get('DelayAckTimeout')
        return self._DelayAckTimeout

    @property
    def SelectAck(self):
        """
        get the value of property _SelectAck
        """
        if self.force_auto_sync:
            self.get('SelectAck')
        return self._SelectAck

    @property
    def SackHoles(self):
        """
        get the value of property _SackHoles
        """
        if self.force_auto_sync:
            self.get('SackHoles')
        return self._SackHoles

    @property
    def TotalSackHoles(self):
        """
        get the value of property _TotalSackHoles
        """
        if self.force_auto_sync:
            self.get('TotalSackHoles')
        return self._TotalSackHoles

    @ReceiveWindowSize.setter
    def ReceiveWindowSize(self, value):
        self._ReceiveWindowSize = value
        self.edit(ReceiveWindowSize=value)

    @SendWindowSize.setter
    def SendWindowSize(self, value):
        self._SendWindowSize = value
        self.edit(SendWindowSize=value)

    @RetransmissionTimeoutMin.setter
    def RetransmissionTimeoutMin(self, value):
        self._RetransmissionTimeoutMin = value
        self.edit(RetransmissionTimeoutMin=value)

    @RetransmissionTimeoutMax.setter
    def RetransmissionTimeoutMax(self, value):
        self._RetransmissionTimeoutMax = value
        self.edit(RetransmissionTimeoutMax=value)

    @KeepAliveInitTime.setter
    def KeepAliveInitTime(self, value):
        self._KeepAliveInitTime = value
        self.edit(KeepAliveInitTime=value)

    @KeepAliveIdleTime.setter
    def KeepAliveIdleTime(self, value):
        self._KeepAliveIdleTime = value
        self.edit(KeepAliveIdleTime=value)

    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value):
        self._KeepAliveInterval = value
        self.edit(KeepAliveInterval=value)

    @KeepAliveProbes.setter
    def KeepAliveProbes(self, value):
        self._KeepAliveProbes = value
        self.edit(KeepAliveProbes=value)

    @CongestionControl.setter
    def CongestionControl(self, value):
        self._CongestionControl = value
        self.edit(CongestionControl=value)

    @MaxSegSize.setter
    def MaxSegSize(self, value):
        self._MaxSegSize = value
        self.edit(MaxSegSize=value)

    @MaxSegLifetime.setter
    def MaxSegLifetime(self, value):
        self._MaxSegLifetime = value
        self.edit(MaxSegLifetime=value)

    @FinWaitTimeout.setter
    def FinWaitTimeout(self, value):
        self._FinWaitTimeout = value
        self.edit(FinWaitTimeout=value)

    @SYNRetries.setter
    def SYNRetries(self, value):
        self._SYNRetries = value
        self.edit(SYNRetries=value)

    @EnableHighperformanceTCP.setter
    def EnableHighperformanceTCP(self, value):
        self._EnableHighperformanceTCP = value
        self.edit(EnableHighperformanceTCP=value)

    @EnableLimitedTransmitTCP.setter
    def EnableLimitedTransmitTCP(self, value):
        self._EnableLimitedTransmitTCP = value
        self.edit(EnableLimitedTransmitTCP=value)

    @DelayAck.setter
    def DelayAck(self, value):
        self._DelayAck = value
        self.edit(DelayAck=value)

    @DelayAckTimeout.setter
    def DelayAckTimeout(self, value):
        self._DelayAckTimeout = value
        self.edit(DelayAckTimeout=value)

    @SelectAck.setter
    def SelectAck(self, value):
        self._SelectAck = value
        self.edit(SelectAck=value)

    @SackHoles.setter
    def SackHoles(self, value):
        self._SackHoles = value
        self.edit(SackHoles=value)

    @TotalSackHoles.setter
    def TotalSackHoles(self, value):
        self._TotalSackHoles = value
        self.edit(TotalSackHoles=value)

    def _set_receivewindowsize_with_str(self, value):
        try:
            self._ReceiveWindowSize = int(value)
        except ValueError:
            self._ReceiveWindowSize = hex(int(value, 16))

    def _set_sendwindowsize_with_str(self, value):
        try:
            self._SendWindowSize = int(value)
        except ValueError:
            self._SendWindowSize = hex(int(value, 16))

    def _set_retransmissiontimeoutmin_with_str(self, value):
        try:
            self._RetransmissionTimeoutMin = int(value)
        except ValueError:
            self._RetransmissionTimeoutMin = hex(int(value, 16))

    def _set_retransmissiontimeoutmax_with_str(self, value):
        try:
            self._RetransmissionTimeoutMax = int(value)
        except ValueError:
            self._RetransmissionTimeoutMax = hex(int(value, 16))

    def _set_keepaliveinittime_with_str(self, value):
        try:
            self._KeepAliveInitTime = int(value)
        except ValueError:
            self._KeepAliveInitTime = hex(int(value, 16))

    def _set_keepaliveidletime_with_str(self, value):
        try:
            self._KeepAliveIdleTime = int(value)
        except ValueError:
            self._KeepAliveIdleTime = hex(int(value, 16))

    def _set_keepaliveinterval_with_str(self, value):
        try:
            self._KeepAliveInterval = int(value)
        except ValueError:
            self._KeepAliveInterval = hex(int(value, 16))

    def _set_keepaliveprobes_with_str(self, value):
        try:
            self._KeepAliveProbes = int(value)
        except ValueError:
            self._KeepAliveProbes = hex(int(value, 16))

    def _set_congestioncontrol_with_str(self, value):
        seperate = value.find(':')
        exec('self._CongestionControl = EnumCongestionControl.%s' % value[:seperate])

    def _set_maxsegsize_with_str(self, value):
        try:
            self._MaxSegSize = int(value)
        except ValueError:
            self._MaxSegSize = hex(int(value, 16))

    def _set_maxseglifetime_with_str(self, value):
        try:
            self._MaxSegLifetime = int(value)
        except ValueError:
            self._MaxSegLifetime = hex(int(value, 16))

    def _set_finwaittimeout_with_str(self, value):
        try:
            self._FinWaitTimeout = int(value)
        except ValueError:
            self._FinWaitTimeout = hex(int(value, 16))

    def _set_synretries_with_str(self, value):
        try:
            self._SYNRetries = int(value)
        except ValueError:
            self._SYNRetries = hex(int(value, 16))

    def _set_enablehighperformancetcp_with_str(self, value):
        self._EnableHighperformanceTCP = (value == 'True')

    def _set_enablelimitedtransmittcp_with_str(self, value):
        self._EnableLimitedTransmitTCP = (value == 'True')

    def _set_delayack_with_str(self, value):
        self._DelayAck = (value == 'True')

    def _set_delayacktimeout_with_str(self, value):
        try:
            self._DelayAckTimeout = int(value)
        except ValueError:
            self._DelayAckTimeout = hex(int(value, 16))

    def _set_selectack_with_str(self, value):
        self._SelectAck = (value == 'True')

    def _set_sackholes_with_str(self, value):
        try:
            self._SackHoles = int(value)
        except ValueError:
            self._SackHoles = hex(int(value, 16))

    def _set_totalsackholes_with_str(self, value):
        try:
            self._TotalSackHoles = int(value)
        except ValueError:
            self._TotalSackHoles = hex(int(value, 16))

