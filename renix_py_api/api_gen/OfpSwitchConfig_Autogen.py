"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpProtocolConfig_Autogen import OfpProtocolConfig


@rom_manager.rom
class OfpSwitchConfig(OfpProtocolConfig):
    def __init__(self, OpenFlowVersion=None, DPID=None, MaxBufferedPackets=None, MaxTableCount=None, Capabilities=None, **kwargs):
        self._OpenFlowVersion = swap_int_to_enum_flag(OpenFlowVersion, EnumOfpSwitchVersion)  # OpenFlow Version
        self._DPID = DPID  # DPID
        self._MaxBufferedPackets = MaxBufferedPackets  # Max Buffered Packets
        self._MaxTableCount = MaxTableCount  # Max Table Count
        self._Capabilities = Capabilities  # Capabilities

        properties = kwargs.copy()
        if OpenFlowVersion is not None:
            if isinstance(OpenFlowVersion, Flag):
                properties['OpenFlowVersion'] = OpenFlowVersion.value
            else:
                properties['OpenFlowVersion'] = OpenFlowVersion
        if DPID is not None:
            properties['DPID'] = DPID
        if MaxBufferedPackets is not None:
            properties['MaxBufferedPackets'] = MaxBufferedPackets
        if MaxTableCount is not None:
            properties['MaxTableCount'] = MaxTableCount
        if Capabilities is not None:
            properties['Capabilities'] = Capabilities

        # call base class function, and it will send message to renix server to create a class.
        super(OfpSwitchConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OpenFlowVersion=None, DPID=None, MaxBufferedPackets=None, MaxTableCount=None, Capabilities=None, **kwargs):
        properties = kwargs.copy()
        if OpenFlowVersion is not None:
            self._OpenFlowVersion = swap_int_to_enum_flag(OpenFlowVersion, EnumOfpSwitchVersion)
            if isinstance(OpenFlowVersion, Flag):
                properties['OpenFlowVersion'] = OpenFlowVersion.value
            else:
                properties['OpenFlowVersion'] = OpenFlowVersion
        if DPID is not None:
            self._DPID = DPID
            properties['DPID'] = DPID
        if MaxBufferedPackets is not None:
            self._MaxBufferedPackets = MaxBufferedPackets
            properties['MaxBufferedPackets'] = MaxBufferedPackets
        if MaxTableCount is not None:
            self._MaxTableCount = MaxTableCount
            properties['MaxTableCount'] = MaxTableCount
        if Capabilities is not None:
            self._Capabilities = Capabilities
            properties['Capabilities'] = Capabilities

        super(OfpSwitchConfig, self).edit(**properties)

    @property
    def OpenFlowVersion(self):
        """
        get the value of property _OpenFlowVersion
        """
        if self.force_auto_sync:
            self.get('OpenFlowVersion')
        return self._OpenFlowVersion

    @property
    def DPID(self):
        """
        get the value of property _DPID
        """
        if self.force_auto_sync:
            self.get('DPID')
        return self._DPID

    @property
    def MaxBufferedPackets(self):
        """
        get the value of property _MaxBufferedPackets
        """
        if self.force_auto_sync:
            self.get('MaxBufferedPackets')
        return self._MaxBufferedPackets

    @property
    def MaxTableCount(self):
        """
        get the value of property _MaxTableCount
        """
        if self.force_auto_sync:
            self.get('MaxTableCount')
        return self._MaxTableCount

    @property
    def Capabilities(self):
        """
        get the value of property _Capabilities
        """
        if self.force_auto_sync:
            self.get('Capabilities')
        return self._Capabilities

    @OpenFlowVersion.setter
    def OpenFlowVersion(self, value):
        self._OpenFlowVersion = swap_int_to_enum_flag(value, EnumOfpSwitchVersion)
        if isinstance(value, Flag):
            self.edit(OpenFlowVersion=value.value)
        else:
            self.edit(OpenFlowVersion=value)

    @DPID.setter
    def DPID(self, value):
        self._DPID = value
        self.edit(DPID=value)

    @MaxBufferedPackets.setter
    def MaxBufferedPackets(self, value):
        self._MaxBufferedPackets = value
        self.edit(MaxBufferedPackets=value)

    @MaxTableCount.setter
    def MaxTableCount(self, value):
        self._MaxTableCount = value
        self.edit(MaxTableCount=value)

    @Capabilities.setter
    def Capabilities(self, value):
        self._Capabilities = value
        self.edit(Capabilities=value)

    def _set_openflowversion_with_str(self, value):
        seperate = value.find(':')
        self._OpenFlowVersion = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOfpSwitchVersion)

    def _set_dpid_with_str(self, value):
        try:
            self._DPID = int(value)
        except ValueError:
            self._DPID = hex(int(value, 16))

    def _set_maxbufferedpackets_with_str(self, value):
        try:
            self._MaxBufferedPackets = int(value)
        except ValueError:
            self._MaxBufferedPackets = hex(int(value, 16))

    def _set_maxtablecount_with_str(self, value):
        try:
            self._MaxTableCount = int(value)
        except ValueError:
            self._MaxTableCount = hex(int(value, 16))

    def _set_capabilities_with_str(self, value):
        try:
            self._Capabilities = int(value)
        except ValueError:
            self._Capabilities = hex(int(value, 16))

