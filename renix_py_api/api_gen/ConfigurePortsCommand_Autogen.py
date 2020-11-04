"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ConfigurePortsCommand(ROMCommand):
    def __init__(self, PortList=None, Media=None, AutoNegotiation=None, LineSpeed=None, Duplex=None, FlowControl=None, PhyMode=None, FecType=None, PpmAdjust=None, DataPathMode=None, RemoteFault=None, Master=None, NoParam=None, Mtu=None, **kwargs):
        self._PortList = PortList  # Port Handles
        self._Media = Media  # Media Type
        self._AutoNegotiation = AutoNegotiation  # Auto Negotiation
        self._LineSpeed = LineSpeed  # Line Speed
        self._Duplex = Duplex  # Duplex
        self._FlowControl = FlowControl  # Flow Control
        self._PhyMode = PhyMode  # PhyMode
        self._FecType = FecType  # FecType
        self._PpmAdjust = PpmAdjust  # PPM Adjustment
        self._DataPathMode = DataPathMode  # Data Path Mode
        self._RemoteFault = RemoteFault  # RemoteFault
        self._Master = Master  # Master
        self._NoParam = NoParam  # No Parameter
        self._Mtu = Mtu  # MTU

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
        if PpmAdjust is not None:
            properties['PpmAdjust'] = PpmAdjust
        if DataPathMode is not None:
            properties['DataPathMode'] = DataPathMode
        if RemoteFault is not None:
            properties['RemoteFault'] = RemoteFault
        if Master is not None:
            properties['Master'] = Master
        if NoParam is not None:
            properties['NoParam'] = NoParam
        if Mtu is not None:
            properties['Mtu'] = Mtu

        # call base class function, and it will send message to renix server to create a class.
        super(ConfigurePortsCommand, self).__init__(**properties)

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
    def AutoNegotiation(self):
        """
        get the value of property _AutoNegotiation
        """
        return self._AutoNegotiation

    @property
    def LineSpeed(self):
        """
        get the value of property _LineSpeed
        """
        return self._LineSpeed

    @property
    def Duplex(self):
        """
        get the value of property _Duplex
        """
        return self._Duplex

    @property
    def FlowControl(self):
        """
        get the value of property _FlowControl
        """
        return self._FlowControl

    @property
    def PhyMode(self):
        """
        get the value of property _PhyMode
        """
        return self._PhyMode

    @property
    def FecType(self):
        """
        get the value of property _FecType
        """
        return self._FecType

    @property
    def PpmAdjust(self):
        """
        get the value of property _PpmAdjust
        """
        return self._PpmAdjust

    @property
    def DataPathMode(self):
        """
        get the value of property _DataPathMode
        """
        return self._DataPathMode

    @property
    def RemoteFault(self):
        """
        get the value of property _RemoteFault
        """
        return self._RemoteFault

    @property
    def Master(self):
        """
        get the value of property _Master
        """
        return self._Master

    @property
    def NoParam(self):
        """
        get the value of property _NoParam
        """
        return self._NoParam

    @property
    def Mtu(self):
        """
        get the value of property _Mtu
        """
        return self._Mtu

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

    @PpmAdjust.setter
    def PpmAdjust(self, value):
        self._PpmAdjust = value

    @DataPathMode.setter
    def DataPathMode(self, value):
        self._DataPathMode = value

    @RemoteFault.setter
    def RemoteFault(self, value):
        self._RemoteFault = value

    @Master.setter
    def Master(self, value):
        self._Master = value

    @NoParam.setter
    def NoParam(self, value):
        self._NoParam = value

    @Mtu.setter
    def Mtu(self, value):
        self._Mtu = value

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

    def _set_autonegotiation_with_str(self, value):
        if value == 'None':
            self._AutoNegotiation = None
            return
        self._AutoNegotiation = (value == 'True')

    def _set_linespeed_with_str(self, value):
        if value == 'None':
            self._LineSpeed = None
            return
        seperate = value.find(':')
        exec('self._LineSpeed = EnumLineSpeed.%s' % value[:seperate])

    def _set_duplex_with_str(self, value):
        if value == 'None':
            self._Duplex = None
            return
        seperate = value.find(':')
        exec('self._Duplex = EnumDuplex.%s' % value[:seperate])

    def _set_flowcontrol_with_str(self, value):
        if value == 'None':
            self._FlowControl = None
            return
        seperate = value.find(':')
        exec('self._FlowControl = EnumFlowControl.%s' % value[:seperate])

    def _set_phymode_with_str(self, value):
        if value == 'None':
            self._PhyMode = None
            return
        seperate = value.find(':')
        exec('self._PhyMode = EnumPhyMode.%s' % value[:seperate])

    def _set_fectype_with_str(self, value):
        if value == 'None':
            self._FecType = None
            return
        seperate = value.find(':')
        exec('self._FecType = EnumFecType.%s' % value[:seperate])

    def _set_ppmadjust_with_str(self, value):
        if value == 'None':
            self._PpmAdjust = None
            return
        try:
            self._PpmAdjust = int(value)
        except ValueError:
            self._PpmAdjust = hex(int(value, 16))

    def _set_datapathmode_with_str(self, value):
        if value == 'None':
            self._DataPathMode = None
            return
        seperate = value.find(':')
        exec('self._DataPathMode = EnumDataPath.%s' % value[:seperate])

    def _set_remotefault_with_str(self, value):
        if value == 'None':
            self._RemoteFault = None
            return
        seperate = value.find(':')
        exec('self._RemoteFault = EnumRemoteFault.%s' % value[:seperate])

    def _set_master_with_str(self, value):
        if value == 'None':
            self._Master = None
            return
        seperate = value.find(':')
        exec('self._Master = EnumMaster.%s' % value[:seperate])

    def _set_noparam_with_str(self, value):
        self._NoParam = (value == 'True')

    def _set_mtu_with_str(self, value):
        if value == 'None':
            self._Mtu = None
            return
        try:
            self._Mtu = int(value)
        except ValueError:
            self._Mtu = hex(int(value, 16))

