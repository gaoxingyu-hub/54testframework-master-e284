"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Ospfv2BfdSessionResult(Result):
    def __init__(self, **kwargs):
        self._Ipv4SessionKeyID = 0  # Ipv4 Session Key ID, not editable
        self._Ipv4SessionID = ''  # OSPFv2 Session Name, not editable
        self._SessionID = ''  # BFD Session Name, not editable
        self._SessionIndex = 0  # BFD Session Index, not editable
        self._Ipv4SourceAddress = '0.0.0.0'  # IPv4 Source Address, not editable
        self._Ipv4DestinationAddress = '0.0.0.0'  # IPv4 Destination Address, not editable
        self._BfdSessionState = 'Down'  # BFD Session State, not editable
        self._MyDiscriminator = ''  # My Discriminator, not editable
        self._YourDiscriminator = ''  # Your Discriminator, not editable
        self._BfdDiagnostic = 'No Diagnostic'  # BFD Diagnostic, not editable
        self._LastBfdDiagnosticErrorRx = 'No Diagnostic'  # Last BFD Diagnostic Error Rx, not editable
        self._BfdControlBits_PFCADM = '000000'  # BFD Control Bits (PFCADM), not editable
        self._ReceiveCount = 0  # Receive Count, not editable
        self._TransmitCount = 0  # Transmit Count, not editable
        self._TransmitInterval = 0  # Transmit Interval (us), not editable
        self._ReceivedRequiredMinRXInterval = 0  # Received Required Min Rx Interval (us), not editable
        self._ReceivedRequiredMinEchoRXInterval = 0  # Received Required Min Echo Rx Interval (us), not editable
        self._FlapsDetected = 0  # Flaps Detected, not editable
        self._TimeoutsDetected = 0  # Timeouts Detected, not editable
        self._RXAvgRate = 0  # Rx Avg Rate (packets/sec), not editable
        self._RXMaxRate = 0  # Rx Max Rate (packets/sec), not editable
        self._RXMinRate = 0  # Rx Min Rate (packets/sec), not editable
        self._TXAvgRate = 0  # Tx Avg Rate (packets/sec), not editable
        self._TXMaxRate = 0  # Tx Max Rate (packets/sec), not editable
        self._TXMinRate = 0  # Tx Min Rate (packets/sec), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2BfdSessionResult, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Ipv4SessionKeyID(self):
        """
        get the value of property _Ipv4SessionKeyID
        """
        if self.force_auto_sync:
            self.get('Ipv4SessionKeyID')
        return self._Ipv4SessionKeyID

    @property
    def Ipv4SessionID(self):
        """
        get the value of property _Ipv4SessionID
        """
        if self.force_auto_sync:
            self.get('Ipv4SessionID')
        return self._Ipv4SessionID

    @property
    def SessionID(self):
        """
        get the value of property _SessionID
        """
        if self.force_auto_sync:
            self.get('SessionID')
        return self._SessionID

    @property
    def SessionIndex(self):
        """
        get the value of property _SessionIndex
        """
        if self.force_auto_sync:
            self.get('SessionIndex')
        return self._SessionIndex

    @property
    def Ipv4SourceAddress(self):
        """
        get the value of property _Ipv4SourceAddress
        """
        if self.force_auto_sync:
            self.get('Ipv4SourceAddress')
        return self._Ipv4SourceAddress

    @property
    def Ipv4DestinationAddress(self):
        """
        get the value of property _Ipv4DestinationAddress
        """
        if self.force_auto_sync:
            self.get('Ipv4DestinationAddress')
        return self._Ipv4DestinationAddress

    @property
    def BfdSessionState(self):
        """
        get the value of property _BfdSessionState
        """
        if self.force_auto_sync:
            self.get('BfdSessionState')
        return self._BfdSessionState

    @property
    def MyDiscriminator(self):
        """
        get the value of property _MyDiscriminator
        """
        if self.force_auto_sync:
            self.get('MyDiscriminator')
        return self._MyDiscriminator

    @property
    def YourDiscriminator(self):
        """
        get the value of property _YourDiscriminator
        """
        if self.force_auto_sync:
            self.get('YourDiscriminator')
        return self._YourDiscriminator

    @property
    def BfdDiagnostic(self):
        """
        get the value of property _BfdDiagnostic
        """
        if self.force_auto_sync:
            self.get('BfdDiagnostic')
        return self._BfdDiagnostic

    @property
    def LastBfdDiagnosticErrorRx(self):
        """
        get the value of property _LastBfdDiagnosticErrorRx
        """
        if self.force_auto_sync:
            self.get('LastBfdDiagnosticErrorRx')
        return self._LastBfdDiagnosticErrorRx

    @property
    def BfdControlBits_PFCADM(self):
        """
        get the value of property _BfdControlBits_PFCADM
        """
        if self.force_auto_sync:
            self.get('BfdControlBits_PFCADM')
        return self._BfdControlBits_PFCADM

    @property
    def ReceiveCount(self):
        """
        get the value of property _ReceiveCount
        """
        if self.force_auto_sync:
            self.get('ReceiveCount')
        return self._ReceiveCount

    @property
    def TransmitCount(self):
        """
        get the value of property _TransmitCount
        """
        if self.force_auto_sync:
            self.get('TransmitCount')
        return self._TransmitCount

    @property
    def TransmitInterval(self):
        """
        get the value of property _TransmitInterval
        """
        if self.force_auto_sync:
            self.get('TransmitInterval')
        return self._TransmitInterval

    @property
    def ReceivedRequiredMinRXInterval(self):
        """
        get the value of property _ReceivedRequiredMinRXInterval
        """
        if self.force_auto_sync:
            self.get('ReceivedRequiredMinRXInterval')
        return self._ReceivedRequiredMinRXInterval

    @property
    def ReceivedRequiredMinEchoRXInterval(self):
        """
        get the value of property _ReceivedRequiredMinEchoRXInterval
        """
        if self.force_auto_sync:
            self.get('ReceivedRequiredMinEchoRXInterval')
        return self._ReceivedRequiredMinEchoRXInterval

    @property
    def FlapsDetected(self):
        """
        get the value of property _FlapsDetected
        """
        if self.force_auto_sync:
            self.get('FlapsDetected')
        return self._FlapsDetected

    @property
    def TimeoutsDetected(self):
        """
        get the value of property _TimeoutsDetected
        """
        if self.force_auto_sync:
            self.get('TimeoutsDetected')
        return self._TimeoutsDetected

    @property
    def RXAvgRate(self):
        """
        get the value of property _RXAvgRate
        """
        if self.force_auto_sync:
            self.get('RXAvgRate')
        return self._RXAvgRate

    @property
    def RXMaxRate(self):
        """
        get the value of property _RXMaxRate
        """
        if self.force_auto_sync:
            self.get('RXMaxRate')
        return self._RXMaxRate

    @property
    def RXMinRate(self):
        """
        get the value of property _RXMinRate
        """
        if self.force_auto_sync:
            self.get('RXMinRate')
        return self._RXMinRate

    @property
    def TXAvgRate(self):
        """
        get the value of property _TXAvgRate
        """
        if self.force_auto_sync:
            self.get('TXAvgRate')
        return self._TXAvgRate

    @property
    def TXMaxRate(self):
        """
        get the value of property _TXMaxRate
        """
        if self.force_auto_sync:
            self.get('TXMaxRate')
        return self._TXMaxRate

    @property
    def TXMinRate(self):
        """
        get the value of property _TXMinRate
        """
        if self.force_auto_sync:
            self.get('TXMinRate')
        return self._TXMinRate

    def _set_ipv4sessionkeyid_with_str(self, value):
        try:
            self._Ipv4SessionKeyID = int(value)
        except ValueError:
            self._Ipv4SessionKeyID = hex(int(value, 16))

    def _set_ipv4sessionid_with_str(self, value):
        self._Ipv4SessionID = value

    def _set_sessionid_with_str(self, value):
        self._SessionID = value

    def _set_sessionindex_with_str(self, value):
        try:
            self._SessionIndex = int(value)
        except ValueError:
            self._SessionIndex = hex(int(value, 16))

    def _set_ipv4sourceaddress_with_str(self, value):
        self._Ipv4SourceAddress = value

    def _set_ipv4destinationaddress_with_str(self, value):
        self._Ipv4DestinationAddress = value

    def _set_bfdsessionstate_with_str(self, value):
        self._BfdSessionState = value

    def _set_mydiscriminator_with_str(self, value):
        self._MyDiscriminator = value

    def _set_yourdiscriminator_with_str(self, value):
        self._YourDiscriminator = value

    def _set_bfddiagnostic_with_str(self, value):
        self._BfdDiagnostic = value

    def _set_lastbfddiagnosticerrorrx_with_str(self, value):
        self._LastBfdDiagnosticErrorRx = value

    def _set_bfdcontrolbits_pfcadm_with_str(self, value):
        self._BfdControlBits_PFCADM = value

    def _set_receivecount_with_str(self, value):
        try:
            self._ReceiveCount = int(value)
        except ValueError:
            self._ReceiveCount = hex(int(value, 16))

    def _set_transmitcount_with_str(self, value):
        try:
            self._TransmitCount = int(value)
        except ValueError:
            self._TransmitCount = hex(int(value, 16))

    def _set_transmitinterval_with_str(self, value):
        try:
            self._TransmitInterval = int(value)
        except ValueError:
            self._TransmitInterval = hex(int(value, 16))

    def _set_receivedrequiredminrxinterval_with_str(self, value):
        try:
            self._ReceivedRequiredMinRXInterval = int(value)
        except ValueError:
            self._ReceivedRequiredMinRXInterval = hex(int(value, 16))

    def _set_receivedrequiredminechorxinterval_with_str(self, value):
        try:
            self._ReceivedRequiredMinEchoRXInterval = int(value)
        except ValueError:
            self._ReceivedRequiredMinEchoRXInterval = hex(int(value, 16))

    def _set_flapsdetected_with_str(self, value):
        try:
            self._FlapsDetected = int(value)
        except ValueError:
            self._FlapsDetected = hex(int(value, 16))

    def _set_timeoutsdetected_with_str(self, value):
        try:
            self._TimeoutsDetected = int(value)
        except ValueError:
            self._TimeoutsDetected = hex(int(value, 16))

    def _set_rxavgrate_with_str(self, value):
        try:
            self._RXAvgRate = int(value)
        except ValueError:
            self._RXAvgRate = hex(int(value, 16))

    def _set_rxmaxrate_with_str(self, value):
        try:
            self._RXMaxRate = int(value)
        except ValueError:
            self._RXMaxRate = hex(int(value, 16))

    def _set_rxminrate_with_str(self, value):
        try:
            self._RXMinRate = int(value)
        except ValueError:
            self._RXMinRate = hex(int(value, 16))

    def _set_txavgrate_with_str(self, value):
        try:
            self._TXAvgRate = int(value)
        except ValueError:
            self._TXAvgRate = hex(int(value, 16))

    def _set_txmaxrate_with_str(self, value):
        try:
            self._TXMaxRate = int(value)
        except ValueError:
            self._TXMaxRate = hex(int(value, 16))

    def _set_txminrate_with_str(self, value):
        try:
            self._TXMinRate = int(value)
        except ValueError:
            self._TXMinRate = hex(int(value, 16))

