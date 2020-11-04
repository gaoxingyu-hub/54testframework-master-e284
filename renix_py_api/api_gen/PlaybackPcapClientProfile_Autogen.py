"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L47ClientProfile_Autogen import L47ClientProfile


@rom_manager.rom
class PlaybackPcapClientProfile(L47ClientProfile):
    def __init__(self, PcapFile=None, Loop=None, FirstIp=None, IpCount=None, Modifier=None, PacketInterval=None, CustomSettingMs=None, CloseType=None, **kwargs):
        self._PcapFile = PcapFile  # Pcap File
        self._Loop = Loop  # Loop
        self._FirstIp = FirstIp  # First IP
        self._IpCount = IpCount  # IP Count
        self._Modifier = Modifier  # Modifier
        self._PacketInterval = PacketInterval  # Packet Interval
        self._CustomSettingMs = CustomSettingMs  # Custom
        self._CloseType = CloseType  # Close Type

        properties = kwargs.copy()
        if PcapFile is not None:
            properties['PcapFile'] = PcapFile
        if Loop is not None:
            properties['Loop'] = Loop
        if FirstIp is not None:
            properties['FirstIp'] = FirstIp
        if IpCount is not None:
            properties['IpCount'] = IpCount
        if Modifier is not None:
            properties['Modifier'] = Modifier
        if PacketInterval is not None:
            properties['PacketInterval'] = PacketInterval
        if CustomSettingMs is not None:
            properties['CustomSettingMs'] = CustomSettingMs
        if CloseType is not None:
            properties['CloseType'] = CloseType

        # call base class function, and it will send message to renix server to create a class.
        super(PlaybackPcapClientProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PcapFile=None, Loop=None, FirstIp=None, IpCount=None, Modifier=None, PacketInterval=None, CustomSettingMs=None, CloseType=None, **kwargs):
        properties = kwargs.copy()
        if PcapFile is not None:
            self._PcapFile = PcapFile
            properties['PcapFile'] = PcapFile
        if Loop is not None:
            self._Loop = Loop
            properties['Loop'] = Loop
        if FirstIp is not None:
            self._FirstIp = FirstIp
            properties['FirstIp'] = FirstIp
        if IpCount is not None:
            self._IpCount = IpCount
            properties['IpCount'] = IpCount
        if Modifier is not None:
            self._Modifier = Modifier
            properties['Modifier'] = Modifier
        if PacketInterval is not None:
            self._PacketInterval = PacketInterval
            properties['PacketInterval'] = PacketInterval
        if CustomSettingMs is not None:
            self._CustomSettingMs = CustomSettingMs
            properties['CustomSettingMs'] = CustomSettingMs
        if CloseType is not None:
            self._CloseType = CloseType
            properties['CloseType'] = CloseType

        super(PlaybackPcapClientProfile, self).edit(**properties)

    @property
    def PcapFile(self):
        """
        get the value of property _PcapFile
        """
        if self.force_auto_sync:
            self.get('PcapFile')
        return self._PcapFile

    @property
    def Loop(self):
        """
        get the value of property _Loop
        """
        if self.force_auto_sync:
            self.get('Loop')
        return self._Loop

    @property
    def FirstIp(self):
        """
        get the value of property _FirstIp
        """
        if self.force_auto_sync:
            self.get('FirstIp')
        return self._FirstIp

    @property
    def IpCount(self):
        """
        get the value of property _IpCount
        """
        if self.force_auto_sync:
            self.get('IpCount')
        return self._IpCount

    @property
    def Modifier(self):
        """
        get the value of property _Modifier
        """
        if self.force_auto_sync:
            self.get('Modifier')
        return self._Modifier

    @property
    def PacketInterval(self):
        """
        get the value of property _PacketInterval
        """
        if self.force_auto_sync:
            self.get('PacketInterval')
        return self._PacketInterval

    @property
    def CustomSettingMs(self):
        """
        get the value of property _CustomSettingMs
        """
        if self.force_auto_sync:
            self.get('CustomSettingMs')
        return self._CustomSettingMs

    @property
    def CloseType(self):
        """
        get the value of property _CloseType
        """
        if self.force_auto_sync:
            self.get('CloseType')
        return self._CloseType

    @PcapFile.setter
    def PcapFile(self, value):
        self._PcapFile = value
        self.edit(PcapFile=value)

    @Loop.setter
    def Loop(self, value):
        self._Loop = value
        self.edit(Loop=value)

    @FirstIp.setter
    def FirstIp(self, value):
        self._FirstIp = value
        self.edit(FirstIp=value)

    @IpCount.setter
    def IpCount(self, value):
        self._IpCount = value
        self.edit(IpCount=value)

    @Modifier.setter
    def Modifier(self, value):
        self._Modifier = value
        self.edit(Modifier=value)

    @PacketInterval.setter
    def PacketInterval(self, value):
        self._PacketInterval = value
        self.edit(PacketInterval=value)

    @CustomSettingMs.setter
    def CustomSettingMs(self, value):
        self._CustomSettingMs = value
        self.edit(CustomSettingMs=value)

    @CloseType.setter
    def CloseType(self, value):
        self._CloseType = value
        self.edit(CloseType=value)

    def _set_pcapfile_with_str(self, value):
        self._PcapFile = value

    def _set_loop_with_str(self, value):
        try:
            self._Loop = int(value)
        except ValueError:
            self._Loop = hex(int(value, 16))

    def _set_firstip_with_str(self, value):
        self._FirstIp = value

    def _set_ipcount_with_str(self, value):
        try:
            self._IpCount = int(value)
        except ValueError:
            self._IpCount = hex(int(value, 16))

    def _set_modifier_with_str(self, value):
        try:
            self._Modifier = int(value)
        except ValueError:
            self._Modifier = hex(int(value, 16))

    def _set_packetinterval_with_str(self, value):
        seperate = value.find(':')
        exec('self._PacketInterval = EnumPacketInterval.%s' % value[:seperate])

    def _set_customsettingms_with_str(self, value):
        try:
            self._CustomSettingMs = int(value)
        except ValueError:
            self._CustomSettingMs = hex(int(value, 16))

    def _set_closetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CloseType = EnumCloseType.%s' % value[:seperate])

