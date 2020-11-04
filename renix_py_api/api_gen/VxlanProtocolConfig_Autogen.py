"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class VxlanProtocolConfig(L23ProtocolConfig):
    def __init__(self, AutoUdpSourcePort=None, UdpSourcePort=None, EnableUdpChecksum=None, EvpnLearning=None, OvsdbLearning=None, MulticastType=None, VtepTunnelIp=None, **kwargs):
        self._VtepState = EnumVtepState.STOPPED  # VTEP State, not editable
        self._AutoUdpSourcePort = AutoUdpSourcePort  # Auto UDP Source Port
        self._UdpSourcePort = UdpSourcePort  # UDP Source Port
        self._EnableUdpChecksum = EnableUdpChecksum  # Enable UDP Checksum
        self._AssociatedVmCount = 0  # Associated VM Devices, not editable
        self._AssociatedSegments = None  # Associated VXLAN Segments, not editable
        self._EvpnLearning = EvpnLearning  # EVPN Learning
        self._OvsdbLearning = OvsdbLearning  # OVSDB Learning
        self._MulticastType = MulticastType  # Multicast Type
        self._VtepTunnelIp = VtepTunnelIp  # Vtep Tunnel Ip Address

        properties = kwargs.copy()
        if AutoUdpSourcePort is not None:
            properties['AutoUdpSourcePort'] = AutoUdpSourcePort
        if UdpSourcePort is not None:
            properties['UdpSourcePort'] = UdpSourcePort
        if EnableUdpChecksum is not None:
            properties['EnableUdpChecksum'] = EnableUdpChecksum
        if EvpnLearning is not None:
            properties['EvpnLearning'] = EvpnLearning
        if OvsdbLearning is not None:
            properties['OvsdbLearning'] = OvsdbLearning
        if MulticastType is not None:
            properties['MulticastType'] = MulticastType
        if VtepTunnelIp is not None:
            properties['VtepTunnelIp'] = VtepTunnelIp

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AutoUdpSourcePort=None, UdpSourcePort=None, EnableUdpChecksum=None, EvpnLearning=None, OvsdbLearning=None, MulticastType=None, VtepTunnelIp=None, **kwargs):
        properties = kwargs.copy()
        if AutoUdpSourcePort is not None:
            self._AutoUdpSourcePort = AutoUdpSourcePort
            properties['AutoUdpSourcePort'] = AutoUdpSourcePort
        if UdpSourcePort is not None:
            self._UdpSourcePort = UdpSourcePort
            properties['UdpSourcePort'] = UdpSourcePort
        if EnableUdpChecksum is not None:
            self._EnableUdpChecksum = EnableUdpChecksum
            properties['EnableUdpChecksum'] = EnableUdpChecksum
        if EvpnLearning is not None:
            self._EvpnLearning = EvpnLearning
            properties['EvpnLearning'] = EvpnLearning
        if OvsdbLearning is not None:
            self._OvsdbLearning = OvsdbLearning
            properties['OvsdbLearning'] = OvsdbLearning
        if MulticastType is not None:
            self._MulticastType = MulticastType
            properties['MulticastType'] = MulticastType
        if VtepTunnelIp is not None:
            self._VtepTunnelIp = VtepTunnelIp
            properties['VtepTunnelIp'] = VtepTunnelIp

        super(VxlanProtocolConfig, self).edit(**properties)

    @property
    def VtepState(self):
        """
        get the value of property _VtepState
        """
        if self.force_auto_sync:
            self.get('VtepState')
        return self._VtepState

    @property
    def AutoUdpSourcePort(self):
        """
        get the value of property _AutoUdpSourcePort
        """
        if self.force_auto_sync:
            self.get('AutoUdpSourcePort')
        return self._AutoUdpSourcePort

    @property
    def UdpSourcePort(self):
        """
        get the value of property _UdpSourcePort
        """
        if self.force_auto_sync:
            self.get('UdpSourcePort')
        return self._UdpSourcePort

    @property
    def EnableUdpChecksum(self):
        """
        get the value of property _EnableUdpChecksum
        """
        if self.force_auto_sync:
            self.get('EnableUdpChecksum')
        return self._EnableUdpChecksum

    @property
    def AssociatedVmCount(self):
        """
        get the value of property _AssociatedVmCount
        """
        if self.force_auto_sync:
            self.get('AssociatedVmCount')
        return self._AssociatedVmCount

    @property
    def AssociatedSegments(self):
        """
        get the value of property _AssociatedSegments
        """
        if self.force_auto_sync:
            self.get('AssociatedSegments')
        return self._AssociatedSegments

    @property
    def EvpnLearning(self):
        """
        get the value of property _EvpnLearning
        """
        if self.force_auto_sync:
            self.get('EvpnLearning')
        return self._EvpnLearning

    @property
    def OvsdbLearning(self):
        """
        get the value of property _OvsdbLearning
        """
        if self.force_auto_sync:
            self.get('OvsdbLearning')
        return self._OvsdbLearning

    @property
    def MulticastType(self):
        """
        get the value of property _MulticastType
        """
        if self.force_auto_sync:
            self.get('MulticastType')
        return self._MulticastType

    @property
    def VtepTunnelIp(self):
        """
        get the value of property _VtepTunnelIp
        """
        if self.force_auto_sync:
            self.get('VtepTunnelIp')
        return self._VtepTunnelIp

    @AutoUdpSourcePort.setter
    def AutoUdpSourcePort(self, value):
        self._AutoUdpSourcePort = value
        self.edit(AutoUdpSourcePort=value)

    @UdpSourcePort.setter
    def UdpSourcePort(self, value):
        self._UdpSourcePort = value
        self.edit(UdpSourcePort=value)

    @EnableUdpChecksum.setter
    def EnableUdpChecksum(self, value):
        self._EnableUdpChecksum = value
        self.edit(EnableUdpChecksum=value)

    @EvpnLearning.setter
    def EvpnLearning(self, value):
        self._EvpnLearning = value
        self.edit(EvpnLearning=value)

    @OvsdbLearning.setter
    def OvsdbLearning(self, value):
        self._OvsdbLearning = value
        self.edit(OvsdbLearning=value)

    @MulticastType.setter
    def MulticastType(self, value):
        self._MulticastType = value
        self.edit(MulticastType=value)

    @VtepTunnelIp.setter
    def VtepTunnelIp(self, value):
        self._VtepTunnelIp = value
        self.edit(VtepTunnelIp=value)

    def _set_vtepstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._VtepState = EnumVtepState.%s' % value[:seperate])

    def _set_autoudpsourceport_with_str(self, value):
        self._AutoUdpSourcePort = (value == 'True')

    def _set_udpsourceport_with_str(self, value):
        try:
            self._UdpSourcePort = int(value)
        except ValueError:
            self._UdpSourcePort = hex(int(value, 16))

    def _set_enableudpchecksum_with_str(self, value):
        self._EnableUdpChecksum = (value == 'True')

    def _set_associatedvmcount_with_str(self, value):
        try:
            self._AssociatedVmCount = int(value)
        except ValueError:
            self._AssociatedVmCount = hex(int(value, 16))

    def _set_associatedsegments_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AssociatedSegments = tmp_value.split()

    def _set_evpnlearning_with_str(self, value):
        self._EvpnLearning = (value == 'True')

    def _set_ovsdblearning_with_str(self, value):
        self._OvsdbLearning = (value == 'True')

    def _set_multicasttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MulticastType = EnumMulticastType.%s' % value[:seperate])

    def _set_vteptunnelip_with_str(self, value):
        seperate = value.find(':')
        exec('self._VtepTunnelIp = EnumTunnelIpAddress.%s' % value[:seperate])

