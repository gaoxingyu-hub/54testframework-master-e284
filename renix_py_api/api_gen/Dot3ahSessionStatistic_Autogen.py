"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dot3ahSessionStatistic(Result):
    def __init__(self, **kwargs):
        self._SessionHandle = ''  # 802.3ah Session Name, not editable
        self._State = ''  # State, not editable
        self._LocalMultiplexerAction = ''  # Local Multiplexer Action, not editable
        self._LocalParserAction = ''  # Local Parser Action, not editable
        self._RemoteMultiplexerAction = ''  # Remote Multiplexer Action, not editable
        self._RemoteParserAction = ''  # Remote Parser Action, not editable
        self._RemoteMode = ''  # Remote Mode, not editable
        self._RemoteOamVersion = 0  # Remote OAM Version, not editable
        self._RemoteRevision = 0  # Remote Revision, not editable
        self._RemoteOui = ''  # Remote OUI, not editable
        self._RemoteEnableVarRetrieval = ''  # Remote Enable Variable Retrieval, not editable
        self._RemoteEnableInterpretLinkEvent = ''  # Remote Enable Interpret Link Event, not editable
        self._RemoteEnableLoopBack = ''  # Remote Enable Loopback, not editable
        self._RemoteEnableUnidirMode = ''  # Remote Enable Unidirectional Mode, not editable
        self._RemoteMaxPduSize = 0  # Remote Max PDU Size, not editable
        self._RemoteVendorSpecificInfo = 0  # Remote Vendor Specific Info, not editable
        self._TxDyingGaspCounter = 0  # Tx Dying Gasp Event, not editable
        self._RxDyingGaspCounter = 0  # Rx Dying Gasp Event, not editable
        self._TxLinkFaultCounter = 0  # Tx Link Fault Event, not editable
        self._RxLinkFaultCounter = 0  # Rx Link Fault Event, not editable
        self._TxCriticalCounter = 0  # Tx Critical Event, not editable
        self._RxCriticalCounter = 0  # Rx Critical Event, not editable
        self._TxEfeCounter = 0  # Tx Errored Frame Event, not editable
        self._RxEfeCounter = 0  # Rx Errored Frame Event, not editable
        self._TxEspeCounter = 0  # Tx Errored Symbol Period Event, not editable
        self._RxEspeCounter = 0  # Rx Errored Symbol Period Event, not editable
        self._TxEfpeCounter = 0  # Tx Errored Frame Period Event, not editable
        self._RxEfpeCounter = 0  # Rx Errored Frame Period Event, not editable
        self._TxEfsseCounter = 0  # Tx Errored Frame Seconds Summary Event, not editable
        self._RxEfsseCounter = 0  # Rx Errored Frame Seconds Summary Event, not editable
        self._TxOrgSpecEventCounter = 0  # Tx Organization Specific Event, not editable
        self._RxOrgSpecEventCounter = 0  # Rx Organization Specific Event, not editable
        self._TxInfoPduCounter = 0  # Tx Info PDU, not editable
        self._RxInfoPduCounter = 0  # Rx Info PDU, not editable
        self._TxEventNotificationPduCounter = 0  # Tx Event Notification, not editable
        self._RxEventNotificationPduCounter = 0  # Rx Event Notification, not editable
        self._TxLoopBackCounter = 0  # Tx Loopback, not editable
        self._RxLoopBackCounter = 0  # Rx Loopback, not editable
        self._TxVarReqCounter = 0  # Tx Variable Request, not editable
        self._RxVarReqCounter = 0  # Rx Variable Request, not editable
        self._TxVarRespCounter = 0  # Tx Variable Response, not editable
        self._RxVarRespCounter = 0  # Rx Variable Response, not editable
        self._TxOrgSpecPduCounter = 0  # Tx Organization Specific PDU, not editable
        self._RxOrgSpecPduCounter = 0  # Rx Organization Specific PDU, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahSessionStatistic, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SessionHandle(self):
        """
        get the value of property _SessionHandle
        """
        if self.force_auto_sync:
            self.get('SessionHandle')
        return self._SessionHandle

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def LocalMultiplexerAction(self):
        """
        get the value of property _LocalMultiplexerAction
        """
        if self.force_auto_sync:
            self.get('LocalMultiplexerAction')
        return self._LocalMultiplexerAction

    @property
    def LocalParserAction(self):
        """
        get the value of property _LocalParserAction
        """
        if self.force_auto_sync:
            self.get('LocalParserAction')
        return self._LocalParserAction

    @property
    def RemoteMultiplexerAction(self):
        """
        get the value of property _RemoteMultiplexerAction
        """
        if self.force_auto_sync:
            self.get('RemoteMultiplexerAction')
        return self._RemoteMultiplexerAction

    @property
    def RemoteParserAction(self):
        """
        get the value of property _RemoteParserAction
        """
        if self.force_auto_sync:
            self.get('RemoteParserAction')
        return self._RemoteParserAction

    @property
    def RemoteMode(self):
        """
        get the value of property _RemoteMode
        """
        if self.force_auto_sync:
            self.get('RemoteMode')
        return self._RemoteMode

    @property
    def RemoteOamVersion(self):
        """
        get the value of property _RemoteOamVersion
        """
        if self.force_auto_sync:
            self.get('RemoteOamVersion')
        return self._RemoteOamVersion

    @property
    def RemoteRevision(self):
        """
        get the value of property _RemoteRevision
        """
        if self.force_auto_sync:
            self.get('RemoteRevision')
        return self._RemoteRevision

    @property
    def RemoteOui(self):
        """
        get the value of property _RemoteOui
        """
        if self.force_auto_sync:
            self.get('RemoteOui')
        return self._RemoteOui

    @property
    def RemoteEnableVarRetrieval(self):
        """
        get the value of property _RemoteEnableVarRetrieval
        """
        if self.force_auto_sync:
            self.get('RemoteEnableVarRetrieval')
        return self._RemoteEnableVarRetrieval

    @property
    def RemoteEnableInterpretLinkEvent(self):
        """
        get the value of property _RemoteEnableInterpretLinkEvent
        """
        if self.force_auto_sync:
            self.get('RemoteEnableInterpretLinkEvent')
        return self._RemoteEnableInterpretLinkEvent

    @property
    def RemoteEnableLoopBack(self):
        """
        get the value of property _RemoteEnableLoopBack
        """
        if self.force_auto_sync:
            self.get('RemoteEnableLoopBack')
        return self._RemoteEnableLoopBack

    @property
    def RemoteEnableUnidirMode(self):
        """
        get the value of property _RemoteEnableUnidirMode
        """
        if self.force_auto_sync:
            self.get('RemoteEnableUnidirMode')
        return self._RemoteEnableUnidirMode

    @property
    def RemoteMaxPduSize(self):
        """
        get the value of property _RemoteMaxPduSize
        """
        if self.force_auto_sync:
            self.get('RemoteMaxPduSize')
        return self._RemoteMaxPduSize

    @property
    def RemoteVendorSpecificInfo(self):
        """
        get the value of property _RemoteVendorSpecificInfo
        """
        if self.force_auto_sync:
            self.get('RemoteVendorSpecificInfo')
        return self._RemoteVendorSpecificInfo

    @property
    def TxDyingGaspCounter(self):
        """
        get the value of property _TxDyingGaspCounter
        """
        if self.force_auto_sync:
            self.get('TxDyingGaspCounter')
        return self._TxDyingGaspCounter

    @property
    def RxDyingGaspCounter(self):
        """
        get the value of property _RxDyingGaspCounter
        """
        if self.force_auto_sync:
            self.get('RxDyingGaspCounter')
        return self._RxDyingGaspCounter

    @property
    def TxLinkFaultCounter(self):
        """
        get the value of property _TxLinkFaultCounter
        """
        if self.force_auto_sync:
            self.get('TxLinkFaultCounter')
        return self._TxLinkFaultCounter

    @property
    def RxLinkFaultCounter(self):
        """
        get the value of property _RxLinkFaultCounter
        """
        if self.force_auto_sync:
            self.get('RxLinkFaultCounter')
        return self._RxLinkFaultCounter

    @property
    def TxCriticalCounter(self):
        """
        get the value of property _TxCriticalCounter
        """
        if self.force_auto_sync:
            self.get('TxCriticalCounter')
        return self._TxCriticalCounter

    @property
    def RxCriticalCounter(self):
        """
        get the value of property _RxCriticalCounter
        """
        if self.force_auto_sync:
            self.get('RxCriticalCounter')
        return self._RxCriticalCounter

    @property
    def TxEfeCounter(self):
        """
        get the value of property _TxEfeCounter
        """
        if self.force_auto_sync:
            self.get('TxEfeCounter')
        return self._TxEfeCounter

    @property
    def RxEfeCounter(self):
        """
        get the value of property _RxEfeCounter
        """
        if self.force_auto_sync:
            self.get('RxEfeCounter')
        return self._RxEfeCounter

    @property
    def TxEspeCounter(self):
        """
        get the value of property _TxEspeCounter
        """
        if self.force_auto_sync:
            self.get('TxEspeCounter')
        return self._TxEspeCounter

    @property
    def RxEspeCounter(self):
        """
        get the value of property _RxEspeCounter
        """
        if self.force_auto_sync:
            self.get('RxEspeCounter')
        return self._RxEspeCounter

    @property
    def TxEfpeCounter(self):
        """
        get the value of property _TxEfpeCounter
        """
        if self.force_auto_sync:
            self.get('TxEfpeCounter')
        return self._TxEfpeCounter

    @property
    def RxEfpeCounter(self):
        """
        get the value of property _RxEfpeCounter
        """
        if self.force_auto_sync:
            self.get('RxEfpeCounter')
        return self._RxEfpeCounter

    @property
    def TxEfsseCounter(self):
        """
        get the value of property _TxEfsseCounter
        """
        if self.force_auto_sync:
            self.get('TxEfsseCounter')
        return self._TxEfsseCounter

    @property
    def RxEfsseCounter(self):
        """
        get the value of property _RxEfsseCounter
        """
        if self.force_auto_sync:
            self.get('RxEfsseCounter')
        return self._RxEfsseCounter

    @property
    def TxOrgSpecEventCounter(self):
        """
        get the value of property _TxOrgSpecEventCounter
        """
        if self.force_auto_sync:
            self.get('TxOrgSpecEventCounter')
        return self._TxOrgSpecEventCounter

    @property
    def RxOrgSpecEventCounter(self):
        """
        get the value of property _RxOrgSpecEventCounter
        """
        if self.force_auto_sync:
            self.get('RxOrgSpecEventCounter')
        return self._RxOrgSpecEventCounter

    @property
    def TxInfoPduCounter(self):
        """
        get the value of property _TxInfoPduCounter
        """
        if self.force_auto_sync:
            self.get('TxInfoPduCounter')
        return self._TxInfoPduCounter

    @property
    def RxInfoPduCounter(self):
        """
        get the value of property _RxInfoPduCounter
        """
        if self.force_auto_sync:
            self.get('RxInfoPduCounter')
        return self._RxInfoPduCounter

    @property
    def TxEventNotificationPduCounter(self):
        """
        get the value of property _TxEventNotificationPduCounter
        """
        if self.force_auto_sync:
            self.get('TxEventNotificationPduCounter')
        return self._TxEventNotificationPduCounter

    @property
    def RxEventNotificationPduCounter(self):
        """
        get the value of property _RxEventNotificationPduCounter
        """
        if self.force_auto_sync:
            self.get('RxEventNotificationPduCounter')
        return self._RxEventNotificationPduCounter

    @property
    def TxLoopBackCounter(self):
        """
        get the value of property _TxLoopBackCounter
        """
        if self.force_auto_sync:
            self.get('TxLoopBackCounter')
        return self._TxLoopBackCounter

    @property
    def RxLoopBackCounter(self):
        """
        get the value of property _RxLoopBackCounter
        """
        if self.force_auto_sync:
            self.get('RxLoopBackCounter')
        return self._RxLoopBackCounter

    @property
    def TxVarReqCounter(self):
        """
        get the value of property _TxVarReqCounter
        """
        if self.force_auto_sync:
            self.get('TxVarReqCounter')
        return self._TxVarReqCounter

    @property
    def RxVarReqCounter(self):
        """
        get the value of property _RxVarReqCounter
        """
        if self.force_auto_sync:
            self.get('RxVarReqCounter')
        return self._RxVarReqCounter

    @property
    def TxVarRespCounter(self):
        """
        get the value of property _TxVarRespCounter
        """
        if self.force_auto_sync:
            self.get('TxVarRespCounter')
        return self._TxVarRespCounter

    @property
    def RxVarRespCounter(self):
        """
        get the value of property _RxVarRespCounter
        """
        if self.force_auto_sync:
            self.get('RxVarRespCounter')
        return self._RxVarRespCounter

    @property
    def TxOrgSpecPduCounter(self):
        """
        get the value of property _TxOrgSpecPduCounter
        """
        if self.force_auto_sync:
            self.get('TxOrgSpecPduCounter')
        return self._TxOrgSpecPduCounter

    @property
    def RxOrgSpecPduCounter(self):
        """
        get the value of property _RxOrgSpecPduCounter
        """
        if self.force_auto_sync:
            self.get('RxOrgSpecPduCounter')
        return self._RxOrgSpecPduCounter

    def _set_sessionhandle_with_str(self, value):
        self._SessionHandle = value

    def _set_state_with_str(self, value):
        self._State = value

    def _set_localmultiplexeraction_with_str(self, value):
        self._LocalMultiplexerAction = value

    def _set_localparseraction_with_str(self, value):
        self._LocalParserAction = value

    def _set_remotemultiplexeraction_with_str(self, value):
        self._RemoteMultiplexerAction = value

    def _set_remoteparseraction_with_str(self, value):
        self._RemoteParserAction = value

    def _set_remotemode_with_str(self, value):
        self._RemoteMode = value

    def _set_remoteoamversion_with_str(self, value):
        try:
            self._RemoteOamVersion = int(value)
        except ValueError:
            self._RemoteOamVersion = hex(int(value, 16))

    def _set_remoterevision_with_str(self, value):
        try:
            self._RemoteRevision = int(value)
        except ValueError:
            self._RemoteRevision = hex(int(value, 16))

    def _set_remoteoui_with_str(self, value):
        self._RemoteOui = value

    def _set_remoteenablevarretrieval_with_str(self, value):
        self._RemoteEnableVarRetrieval = value

    def _set_remoteenableinterpretlinkevent_with_str(self, value):
        self._RemoteEnableInterpretLinkEvent = value

    def _set_remoteenableloopback_with_str(self, value):
        self._RemoteEnableLoopBack = value

    def _set_remoteenableunidirmode_with_str(self, value):
        self._RemoteEnableUnidirMode = value

    def _set_remotemaxpdusize_with_str(self, value):
        try:
            self._RemoteMaxPduSize = int(value)
        except ValueError:
            self._RemoteMaxPduSize = hex(int(value, 16))

    def _set_remotevendorspecificinfo_with_str(self, value):
        try:
            self._RemoteVendorSpecificInfo = int(value)
        except ValueError:
            self._RemoteVendorSpecificInfo = hex(int(value, 16))

    def _set_txdyinggaspcounter_with_str(self, value):
        try:
            self._TxDyingGaspCounter = int(value)
        except ValueError:
            self._TxDyingGaspCounter = hex(int(value, 16))

    def _set_rxdyinggaspcounter_with_str(self, value):
        try:
            self._RxDyingGaspCounter = int(value)
        except ValueError:
            self._RxDyingGaspCounter = hex(int(value, 16))

    def _set_txlinkfaultcounter_with_str(self, value):
        try:
            self._TxLinkFaultCounter = int(value)
        except ValueError:
            self._TxLinkFaultCounter = hex(int(value, 16))

    def _set_rxlinkfaultcounter_with_str(self, value):
        try:
            self._RxLinkFaultCounter = int(value)
        except ValueError:
            self._RxLinkFaultCounter = hex(int(value, 16))

    def _set_txcriticalcounter_with_str(self, value):
        try:
            self._TxCriticalCounter = int(value)
        except ValueError:
            self._TxCriticalCounter = hex(int(value, 16))

    def _set_rxcriticalcounter_with_str(self, value):
        try:
            self._RxCriticalCounter = int(value)
        except ValueError:
            self._RxCriticalCounter = hex(int(value, 16))

    def _set_txefecounter_with_str(self, value):
        try:
            self._TxEfeCounter = int(value)
        except ValueError:
            self._TxEfeCounter = hex(int(value, 16))

    def _set_rxefecounter_with_str(self, value):
        try:
            self._RxEfeCounter = int(value)
        except ValueError:
            self._RxEfeCounter = hex(int(value, 16))

    def _set_txespecounter_with_str(self, value):
        try:
            self._TxEspeCounter = int(value)
        except ValueError:
            self._TxEspeCounter = hex(int(value, 16))

    def _set_rxespecounter_with_str(self, value):
        try:
            self._RxEspeCounter = int(value)
        except ValueError:
            self._RxEspeCounter = hex(int(value, 16))

    def _set_txefpecounter_with_str(self, value):
        try:
            self._TxEfpeCounter = int(value)
        except ValueError:
            self._TxEfpeCounter = hex(int(value, 16))

    def _set_rxefpecounter_with_str(self, value):
        try:
            self._RxEfpeCounter = int(value)
        except ValueError:
            self._RxEfpeCounter = hex(int(value, 16))

    def _set_txefssecounter_with_str(self, value):
        try:
            self._TxEfsseCounter = int(value)
        except ValueError:
            self._TxEfsseCounter = hex(int(value, 16))

    def _set_rxefssecounter_with_str(self, value):
        try:
            self._RxEfsseCounter = int(value)
        except ValueError:
            self._RxEfsseCounter = hex(int(value, 16))

    def _set_txorgspeceventcounter_with_str(self, value):
        try:
            self._TxOrgSpecEventCounter = int(value)
        except ValueError:
            self._TxOrgSpecEventCounter = hex(int(value, 16))

    def _set_rxorgspeceventcounter_with_str(self, value):
        try:
            self._RxOrgSpecEventCounter = int(value)
        except ValueError:
            self._RxOrgSpecEventCounter = hex(int(value, 16))

    def _set_txinfopducounter_with_str(self, value):
        try:
            self._TxInfoPduCounter = int(value)
        except ValueError:
            self._TxInfoPduCounter = hex(int(value, 16))

    def _set_rxinfopducounter_with_str(self, value):
        try:
            self._RxInfoPduCounter = int(value)
        except ValueError:
            self._RxInfoPduCounter = hex(int(value, 16))

    def _set_txeventnotificationpducounter_with_str(self, value):
        try:
            self._TxEventNotificationPduCounter = int(value)
        except ValueError:
            self._TxEventNotificationPduCounter = hex(int(value, 16))

    def _set_rxeventnotificationpducounter_with_str(self, value):
        try:
            self._RxEventNotificationPduCounter = int(value)
        except ValueError:
            self._RxEventNotificationPduCounter = hex(int(value, 16))

    def _set_txloopbackcounter_with_str(self, value):
        try:
            self._TxLoopBackCounter = int(value)
        except ValueError:
            self._TxLoopBackCounter = hex(int(value, 16))

    def _set_rxloopbackcounter_with_str(self, value):
        try:
            self._RxLoopBackCounter = int(value)
        except ValueError:
            self._RxLoopBackCounter = hex(int(value, 16))

    def _set_txvarreqcounter_with_str(self, value):
        try:
            self._TxVarReqCounter = int(value)
        except ValueError:
            self._TxVarReqCounter = hex(int(value, 16))

    def _set_rxvarreqcounter_with_str(self, value):
        try:
            self._RxVarReqCounter = int(value)
        except ValueError:
            self._RxVarReqCounter = hex(int(value, 16))

    def _set_txvarrespcounter_with_str(self, value):
        try:
            self._TxVarRespCounter = int(value)
        except ValueError:
            self._TxVarRespCounter = hex(int(value, 16))

    def _set_rxvarrespcounter_with_str(self, value):
        try:
            self._RxVarRespCounter = int(value)
        except ValueError:
            self._RxVarRespCounter = hex(int(value, 16))

    def _set_txorgspecpducounter_with_str(self, value):
        try:
            self._TxOrgSpecPduCounter = int(value)
        except ValueError:
            self._TxOrgSpecPduCounter = hex(int(value, 16))

    def _set_rxorgspecpducounter_with_str(self, value):
        try:
            self._RxOrgSpecPduCounter = int(value)
        except ValueError:
            self._RxOrgSpecPduCounter = hex(int(value, 16))

