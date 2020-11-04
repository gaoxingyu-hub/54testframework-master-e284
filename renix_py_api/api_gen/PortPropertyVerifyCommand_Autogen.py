"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PortPropertyVerifyCommand(ROMCommand):
    def __init__(self, PortList=None, Media=None, AutoNegotiation=None, LineSpeed=None, Duplex=None, FlowControl=None, PhyMode=None, FecType=None, DataPathMode=None, RemoteFault=None, Master=None, AutoMDIX=None, FastRetrain=None, WanMode=None, **kwargs):
        self._PortList = PortList  # Port Handles
        self._Media = Media  # Media Type
        self._MediaList = None  # Media Type, not editable
        self._AutoNegotiation = AutoNegotiation  # Auto Negotiation
        self._AutoNegotiationList = None  # Auto Negotiation, not editable
        self._LineSpeed = LineSpeed  # Line Speed
        self._LineSpeedList = None  # Line Speed, not editable
        self._Duplex = Duplex  # Duplex
        self._DuplexList = None  # Duplex, not editable
        self._FlowControl = FlowControl  # Flow Control
        self._FlowControlList = None  # Flow Control, not editable
        self._PhyMode = PhyMode  # PhyMode
        self._PhyModeList = None  # PhyMode, not editable
        self._FecType = FecType  # FecType
        self._FecTypeList = None  # FecType, not editable
        self._DataPathMode = DataPathMode  # Data Path Mode
        self._DataPathModeList = None  # Data Path Mode, not editable
        self._RemoteFault = RemoteFault  # RemoteFault
        self._RemoteFaultList = None  # RemoteFault, not editable
        self._Master = Master  # Master
        self._MasterList = None  # Master, not editable
        self._AutoMDIX = AutoMDIX  # Auto MDIX
        self._AutoMDIXList = None  # Auto MDIX, not editable
        self._FastRetrain = FastRetrain  # FastRetrain
        self._FastRetrainList = None  # FastRetrain, not editable
        self._WanMode = WanMode  # WAN
        self._WanModeList = None  # WAN, not editable
        self._PpmValid = False  # PpmValid, not editable
        self._TxDiffTxPostTxPreValid = False  # PpmValid, not editable

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList
        if Media is not None:
            properties['Media'] = Media
        if AutoNegotiation is not None:
            properties['AutoNegotiation'] = AutoNegotiation
        if LineSpeed is not None:
            properties['LineSpeed'] = LineSpeed
        if Duplex is not None:
            properties['Duplex'] = Duplex
        if FlowControl is not None:
            properties['FlowControl'] = FlowControl
        if PhyMode is not None:
            properties['PhyMode'] = PhyMode
        if FecType is not None:
            properties['FecType'] = FecType
        if DataPathMode is not None:
            properties['DataPathMode'] = DataPathMode
        if RemoteFault is not None:
            properties['RemoteFault'] = RemoteFault
        if Master is not None:
            properties['Master'] = Master
        if AutoMDIX is not None:
            properties['AutoMDIX'] = AutoMDIX
        if FastRetrain is not None:
            properties['FastRetrain'] = FastRetrain
        if WanMode is not None:
            properties['WanMode'] = WanMode

        # call base class function, and it will send message to renix server to create a class.
        super(PortPropertyVerifyCommand, self).__init__(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        return self._PortList

    @property
    def Media(self):
        """
        get the value of property _Media
        """
        return self._Media

    @property
    def MediaList(self):
        """
        get the value of property _MediaList
        """
        return self._MediaList

    @property
    def AutoNegotiation(self):
        """
        get the value of property _AutoNegotiation
        """
        return self._AutoNegotiation

    @property
    def AutoNegotiationList(self):
        """
        get the value of property _AutoNegotiationList
        """
        return self._AutoNegotiationList

    @property
    def LineSpeed(self):
        """
        get the value of property _LineSpeed
        """
        return self._LineSpeed

    @property
    def LineSpeedList(self):
        """
        get the value of property _LineSpeedList
        """
        return self._LineSpeedList

    @property
    def Duplex(self):
        """
        get the value of property _Duplex
        """
        return self._Duplex

    @property
    def DuplexList(self):
        """
        get the value of property _DuplexList
        """
        return self._DuplexList

    @property
    def FlowControl(self):
        """
        get the value of property _FlowControl
        """
        return self._FlowControl

    @property
    def FlowControlList(self):
        """
        get the value of property _FlowControlList
        """
        return self._FlowControlList

    @property
    def PhyMode(self):
        """
        get the value of property _PhyMode
        """
        return self._PhyMode

    @property
    def PhyModeList(self):
        """
        get the value of property _PhyModeList
        """
        return self._PhyModeList

    @property
    def FecType(self):
        """
        get the value of property _FecType
        """
        return self._FecType

    @property
    def FecTypeList(self):
        """
        get the value of property _FecTypeList
        """
        return self._FecTypeList

    @property
    def DataPathMode(self):
        """
        get the value of property _DataPathMode
        """
        return self._DataPathMode

    @property
    def DataPathModeList(self):
        """
        get the value of property _DataPathModeList
        """
        return self._DataPathModeList

    @property
    def RemoteFault(self):
        """
        get the value of property _RemoteFault
        """
        return self._RemoteFault

    @property
    def RemoteFaultList(self):
        """
        get the value of property _RemoteFaultList
        """
        return self._RemoteFaultList

    @property
    def Master(self):
        """
        get the value of property _Master
        """
        return self._Master

    @property
    def MasterList(self):
        """
        get the value of property _MasterList
        """
        return self._MasterList

    @property
    def AutoMDIX(self):
        """
        get the value of property _AutoMDIX
        """
        return self._AutoMDIX

    @property
    def AutoMDIXList(self):
        """
        get the value of property _AutoMDIXList
        """
        return self._AutoMDIXList

    @property
    def FastRetrain(self):
        """
        get the value of property _FastRetrain
        """
        return self._FastRetrain

    @property
    def FastRetrainList(self):
        """
        get the value of property _FastRetrainList
        """
        return self._FastRetrainList

    @property
    def WanMode(self):
        """
        get the value of property _WanMode
        """
        return self._WanMode

    @property
    def WanModeList(self):
        """
        get the value of property _WanModeList
        """
        return self._WanModeList

    @property
    def PpmValid(self):
        """
        get the value of property _PpmValid
        """
        return self._PpmValid

    @property
    def TxDiffTxPostTxPreValid(self):
        """
        get the value of property _TxDiffTxPostTxPreValid
        """
        return self._TxDiffTxPostTxPreValid

    @PortList.setter
    def PortList(self, value):
        self._PortList = value

    @Media.setter
    def Media(self, value):
        self._Media = value

    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        self._AutoNegotiation = value

    @LineSpeed.setter
    def LineSpeed(self, value):
        self._LineSpeed = value

    @Duplex.setter
    def Duplex(self, value):
        self._Duplex = value

    @FlowControl.setter
    def FlowControl(self, value):
        self._FlowControl = value

    @PhyMode.setter
    def PhyMode(self, value):
        self._PhyMode = value

    @FecType.setter
    def FecType(self, value):
        self._FecType = value

    @DataPathMode.setter
    def DataPathMode(self, value):
        self._DataPathMode = value

    @RemoteFault.setter
    def RemoteFault(self, value):
        self._RemoteFault = value

    @Master.setter
    def Master(self, value):
        self._Master = value

    @AutoMDIX.setter
    def AutoMDIX(self, value):
        self._AutoMDIX = value

    @FastRetrain.setter
    def FastRetrain(self, value):
        self._FastRetrain = value

    @WanMode.setter
    def WanMode(self, value):
        self._WanMode = value

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

    def _set_media_with_str(self, value):
        if value == 'None':
            self._Media = None
            return
        seperate = value.find(':')
        exec('self._Media = EnumMediaType.%s' % value[:seperate])

    def _set_medialist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MediaList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumMediaType + '.' + str_value[:seperate]
            exec('self._MediaList.append(%s)' %(enum_value))

    def _set_autonegotiation_with_str(self, value):
        if value == 'None':
            self._AutoNegotiation = None
            return
        self._AutoNegotiation = (value == 'True')

    def _set_autonegotiationlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AutoNegotiationList = []
        values = tmp_value.split()
        for str_value in values:
            self._AutoNegotiationList.append((str_value == 'True'))

    def _set_linespeed_with_str(self, value):
        if value == 'None':
            self._LineSpeed = None
            return
        seperate = value.find(':')
        exec('self._LineSpeed = EnumLineSpeed.%s' % value[:seperate])

    def _set_linespeedlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LineSpeedList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumLineSpeed + '.' + str_value[:seperate]
            exec('self._LineSpeedList.append(%s)' %(enum_value))

    def _set_duplex_with_str(self, value):
        if value == 'None':
            self._Duplex = None
            return
        seperate = value.find(':')
        exec('self._Duplex = EnumDuplex.%s' % value[:seperate])

    def _set_duplexlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DuplexList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumDuplex + '.' + str_value[:seperate]
            exec('self._DuplexList.append(%s)' %(enum_value))

    def _set_flowcontrol_with_str(self, value):
        if value == 'None':
            self._FlowControl = None
            return
        seperate = value.find(':')
        exec('self._FlowControl = EnumFlowControl.%s' % value[:seperate])

    def _set_flowcontrollist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FlowControlList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumFlowControl + '.' + str_value[:seperate]
            exec('self._FlowControlList.append(%s)' %(enum_value))

    def _set_phymode_with_str(self, value):
        if value == 'None':
            self._PhyMode = None
            return
        seperate = value.find(':')
        exec('self._PhyMode = EnumPhyMode.%s' % value[:seperate])

    def _set_phymodelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PhyModeList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumPhyMode + '.' + str_value[:seperate]
            exec('self._PhyModeList.append(%s)' %(enum_value))

    def _set_fectype_with_str(self, value):
        if value == 'None':
            self._FecType = None
            return
        seperate = value.find(':')
        exec('self._FecType = EnumFecType.%s' % value[:seperate])

    def _set_fectypelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FecTypeList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumFecType + '.' + str_value[:seperate]
            exec('self._FecTypeList.append(%s)' %(enum_value))

    def _set_datapathmode_with_str(self, value):
        if value == 'None':
            self._DataPathMode = None
            return
        seperate = value.find(':')
        exec('self._DataPathMode = EnumDataPath.%s' % value[:seperate])

    def _set_datapathmodelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DataPathModeList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumDataPath + '.' + str_value[:seperate]
            exec('self._DataPathModeList.append(%s)' %(enum_value))

    def _set_remotefault_with_str(self, value):
        if value == 'None':
            self._RemoteFault = None
            return
        seperate = value.find(':')
        exec('self._RemoteFault = EnumRemoteFault.%s' % value[:seperate])

    def _set_remotefaultlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RemoteFaultList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumRemoteFault + '.' + str_value[:seperate]
            exec('self._RemoteFaultList.append(%s)' %(enum_value))

    def _set_master_with_str(self, value):
        if value == 'None':
            self._Master = None
            return
        seperate = value.find(':')
        exec('self._Master = EnumMaster.%s' % value[:seperate])

    def _set_masterlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MasterList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumMaster + '.' + str_value[:seperate]
            exec('self._MasterList.append(%s)' %(enum_value))

    def _set_automdix_with_str(self, value):
        if value == 'None':
            self._AutoMDIX = None
            return
        self._AutoMDIX = (value == 'True')

    def _set_automdixlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AutoMDIXList = []
        values = tmp_value.split()
        for str_value in values:
            self._AutoMDIXList.append((str_value == 'True'))

    def _set_fastretrain_with_str(self, value):
        if value == 'None':
            self._FastRetrain = None
            return
        self._FastRetrain = (value == 'True')

    def _set_fastretrainlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FastRetrainList = []
        values = tmp_value.split()
        for str_value in values:
            self._FastRetrainList.append((str_value == 'True'))

    def _set_wanmode_with_str(self, value):
        if value == 'None':
            self._WanMode = None
            return
        seperate = value.find(':')
        exec('self._WanMode = EnumWanMode.%s' % value[:seperate])

    def _set_wanmodelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._WanModeList = []
        values = tmp_value.split()
        for str_value in values:
            seperate = str_value.find(':')
            enum_value = EnumWanMode + '.' + str_value[:seperate]
            exec('self._WanModeList.append(%s)' %(enum_value))

    def _set_ppmvalid_with_str(self, value):
        self._PpmValid = (value == 'True')

    def _set_txdifftxposttxprevalid_with_str(self, value):
        self._TxDiffTxPostTxPreValid = (value == 'True')

