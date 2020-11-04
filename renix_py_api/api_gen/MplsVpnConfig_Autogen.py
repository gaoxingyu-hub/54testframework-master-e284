"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class MplsVpnConfig(ROMObject):
    def __init__(self, PortHandles=None, InterfaceHandles=None, StreamTemplateHandles=None, DutRouterId=None, DutRouterIdOnly=None, DutAsNumber=None, Enable4ByteDutAs=None, Dut4ByteAsNumber=None, IgpProtocolHandle=None, MplsProtocolHandle=None, EnablePRouters=None, PRoutersPerInterface=None, PRoutersStartIp=None, PRoutersPrefixLength=None, PRoutersIdStart=None, PRoutersIdStep=None, PeRoutersPerInterface=None, PeRoutersIdStart=None, PeRoutersIdStep=None, TrafficLoadPercentProvider=None, TrafficLoadPercentCustomer=None, HasLspPing=None, CoreTunnelEnableLspPing=None, VpnTunnelEnablePeToDutLspPing=None, **kwargs):
        self._PortHandles = PortHandles  # Port Handles
        self._InterfaceHandles = InterfaceHandles  # Interface Handles
        self._StreamTemplateHandles = StreamTemplateHandles  # Stream Template Handles
        self._DutRouterId = DutRouterId  # DUT Router ID
        self._DutRouterIdOnly = DutRouterIdOnly  # DUT Router ID only
        self._DutAsNumber = DutAsNumber  # DUT AS Number
        self._Enable4ByteDutAs = Enable4ByteDutAs  # Enable 4-Byte DUT AS Number
        self._Dut4ByteAsNumber = Dut4ByteAsNumber  # DUT 4-Bytes AS Number
        self._IgpProtocol = EnumMplsIgpProtocols.OSPF  # IGP, not editable
        self._IgpProtocolHandle = IgpProtocolHandle  # IGP Protocol Handle
        self._MplsProtocol = EnumMplsMplsProtocols.LDP  # MPLS, not editable
        self._MplsProtocolHandle = MplsProtocolHandle  # MPLS Protocol Handle
        self._EnablePRouters = EnablePRouters  # Enable P routers
        self._PRoutersPerInterface = PRoutersPerInterface  # P Routers Per Interface
        self._TopologyType = EnumMplsTopologyType.Tree  # Topology Type, not editable
        self._PRoutersStartIp = PRoutersStartIp  # Start IP
        self._PRoutersPrefixLength = PRoutersPrefixLength  # Prefix Length
        self._PRoutersIdStart = PRoutersIdStart  # Start
        self._PRoutersIdStep = PRoutersIdStep  # Step
        self._PeRoutersPerInterface = PeRoutersPerInterface  # PE Routers Per Interface
        self._PeRoutersIdStart = PeRoutersIdStart  # Start
        self._PeRoutersIdStep = PeRoutersIdStep  # Step
        self._TrafficFlow = EnumMplsTrafficFlowType.CustomerProviderBoth  # Traffic Flow, not editable
        self._TrafficLoadPercentProvider = TrafficLoadPercentProvider  # Load Percent from Provider Ports
        self._TrafficLoadPercentCustomer = TrafficLoadPercentCustomer  # Load Percent from Customer Ports
        self._HasLspPing = HasLspPing  # HasLspPing
        self._CoreTunnelEnableLspPing = CoreTunnelEnableLspPing  # Enable LSP Ping
        self._VpnTunnelEnablePeToDutLspPing = VpnTunnelEnablePeToDutLspPing  # Enable PE to DUT VPN Tunnel LSP Ping

        properties = kwargs.copy()
        if PortHandles is not None:
            properties['PortHandles'] = PortHandles
        if InterfaceHandles is not None:
            properties['InterfaceHandles'] = InterfaceHandles
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if DutRouterId is not None:
            properties['DutRouterId'] = DutRouterId
        if DutRouterIdOnly is not None:
            properties['DutRouterIdOnly'] = DutRouterIdOnly
        if DutAsNumber is not None:
            properties['DutAsNumber'] = DutAsNumber
        if Enable4ByteDutAs is not None:
            properties['Enable4ByteDutAs'] = Enable4ByteDutAs
        if Dut4ByteAsNumber is not None:
            properties['Dut4ByteAsNumber'] = Dut4ByteAsNumber
        if IgpProtocolHandle is not None:
            properties['IgpProtocolHandle'] = IgpProtocolHandle
        if MplsProtocolHandle is not None:
            properties['MplsProtocolHandle'] = MplsProtocolHandle
        if EnablePRouters is not None:
            properties['EnablePRouters'] = EnablePRouters
        if PRoutersPerInterface is not None:
            properties['PRoutersPerInterface'] = PRoutersPerInterface
        if PRoutersStartIp is not None:
            properties['PRoutersStartIp'] = PRoutersStartIp
        if PRoutersPrefixLength is not None:
            properties['PRoutersPrefixLength'] = PRoutersPrefixLength
        if PRoutersIdStart is not None:
            properties['PRoutersIdStart'] = PRoutersIdStart
        if PRoutersIdStep is not None:
            properties['PRoutersIdStep'] = PRoutersIdStep
        if PeRoutersPerInterface is not None:
            properties['PeRoutersPerInterface'] = PeRoutersPerInterface
        if PeRoutersIdStart is not None:
            properties['PeRoutersIdStart'] = PeRoutersIdStart
        if PeRoutersIdStep is not None:
            properties['PeRoutersIdStep'] = PeRoutersIdStep
        if TrafficLoadPercentProvider is not None:
            properties['TrafficLoadPercentProvider'] = TrafficLoadPercentProvider
        if TrafficLoadPercentCustomer is not None:
            properties['TrafficLoadPercentCustomer'] = TrafficLoadPercentCustomer
        if HasLspPing is not None:
            properties['HasLspPing'] = HasLspPing
        if CoreTunnelEnableLspPing is not None:
            properties['CoreTunnelEnableLspPing'] = CoreTunnelEnableLspPing
        if VpnTunnelEnablePeToDutLspPing is not None:
            properties['VpnTunnelEnablePeToDutLspPing'] = VpnTunnelEnablePeToDutLspPing

        # call base class function, and it will send message to renix server to create a class.
        super(MplsVpnConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PortHandles=None, InterfaceHandles=None, StreamTemplateHandles=None, DutRouterId=None, DutRouterIdOnly=None, DutAsNumber=None, Enable4ByteDutAs=None, Dut4ByteAsNumber=None, IgpProtocolHandle=None, MplsProtocolHandle=None, EnablePRouters=None, PRoutersPerInterface=None, PRoutersStartIp=None, PRoutersPrefixLength=None, PRoutersIdStart=None, PRoutersIdStep=None, PeRoutersPerInterface=None, PeRoutersIdStart=None, PeRoutersIdStep=None, TrafficLoadPercentProvider=None, TrafficLoadPercentCustomer=None, HasLspPing=None, CoreTunnelEnableLspPing=None, VpnTunnelEnablePeToDutLspPing=None, **kwargs):
        properties = kwargs.copy()
        if PortHandles is not None:
            self._PortHandles = PortHandles
            properties['PortHandles'] = PortHandles
        if InterfaceHandles is not None:
            self._InterfaceHandles = InterfaceHandles
            properties['InterfaceHandles'] = InterfaceHandles
        if StreamTemplateHandles is not None:
            self._StreamTemplateHandles = StreamTemplateHandles
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if DutRouterId is not None:
            self._DutRouterId = DutRouterId
            properties['DutRouterId'] = DutRouterId
        if DutRouterIdOnly is not None:
            self._DutRouterIdOnly = DutRouterIdOnly
            properties['DutRouterIdOnly'] = DutRouterIdOnly
        if DutAsNumber is not None:
            self._DutAsNumber = DutAsNumber
            properties['DutAsNumber'] = DutAsNumber
        if Enable4ByteDutAs is not None:
            self._Enable4ByteDutAs = Enable4ByteDutAs
            properties['Enable4ByteDutAs'] = Enable4ByteDutAs
        if Dut4ByteAsNumber is not None:
            self._Dut4ByteAsNumber = Dut4ByteAsNumber
            properties['Dut4ByteAsNumber'] = Dut4ByteAsNumber
        if IgpProtocolHandle is not None:
            self._IgpProtocolHandle = IgpProtocolHandle
            properties['IgpProtocolHandle'] = IgpProtocolHandle
        if MplsProtocolHandle is not None:
            self._MplsProtocolHandle = MplsProtocolHandle
            properties['MplsProtocolHandle'] = MplsProtocolHandle
        if EnablePRouters is not None:
            self._EnablePRouters = EnablePRouters
            properties['EnablePRouters'] = EnablePRouters
        if PRoutersPerInterface is not None:
            self._PRoutersPerInterface = PRoutersPerInterface
            properties['PRoutersPerInterface'] = PRoutersPerInterface
        if PRoutersStartIp is not None:
            self._PRoutersStartIp = PRoutersStartIp
            properties['PRoutersStartIp'] = PRoutersStartIp
        if PRoutersPrefixLength is not None:
            self._PRoutersPrefixLength = PRoutersPrefixLength
            properties['PRoutersPrefixLength'] = PRoutersPrefixLength
        if PRoutersIdStart is not None:
            self._PRoutersIdStart = PRoutersIdStart
            properties['PRoutersIdStart'] = PRoutersIdStart
        if PRoutersIdStep is not None:
            self._PRoutersIdStep = PRoutersIdStep
            properties['PRoutersIdStep'] = PRoutersIdStep
        if PeRoutersPerInterface is not None:
            self._PeRoutersPerInterface = PeRoutersPerInterface
            properties['PeRoutersPerInterface'] = PeRoutersPerInterface
        if PeRoutersIdStart is not None:
            self._PeRoutersIdStart = PeRoutersIdStart
            properties['PeRoutersIdStart'] = PeRoutersIdStart
        if PeRoutersIdStep is not None:
            self._PeRoutersIdStep = PeRoutersIdStep
            properties['PeRoutersIdStep'] = PeRoutersIdStep
        if TrafficLoadPercentProvider is not None:
            self._TrafficLoadPercentProvider = TrafficLoadPercentProvider
            properties['TrafficLoadPercentProvider'] = TrafficLoadPercentProvider
        if TrafficLoadPercentCustomer is not None:
            self._TrafficLoadPercentCustomer = TrafficLoadPercentCustomer
            properties['TrafficLoadPercentCustomer'] = TrafficLoadPercentCustomer
        if HasLspPing is not None:
            self._HasLspPing = HasLspPing
            properties['HasLspPing'] = HasLspPing
        if CoreTunnelEnableLspPing is not None:
            self._CoreTunnelEnableLspPing = CoreTunnelEnableLspPing
            properties['CoreTunnelEnableLspPing'] = CoreTunnelEnableLspPing
        if VpnTunnelEnablePeToDutLspPing is not None:
            self._VpnTunnelEnablePeToDutLspPing = VpnTunnelEnablePeToDutLspPing
            properties['VpnTunnelEnablePeToDutLspPing'] = VpnTunnelEnablePeToDutLspPing

        super(MplsVpnConfig, self).edit(**properties)

    @property
    def PortHandles(self):
        """
        get the value of property _PortHandles
        """
        if self.force_auto_sync:
            self.get('PortHandles')
        return self._PortHandles

    @property
    def InterfaceHandles(self):
        """
        get the value of property _InterfaceHandles
        """
        if self.force_auto_sync:
            self.get('InterfaceHandles')
        return self._InterfaceHandles

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        if self.force_auto_sync:
            self.get('StreamTemplateHandles')
        return self._StreamTemplateHandles

    @property
    def DutRouterId(self):
        """
        get the value of property _DutRouterId
        """
        if self.force_auto_sync:
            self.get('DutRouterId')
        return self._DutRouterId

    @property
    def DutRouterIdOnly(self):
        """
        get the value of property _DutRouterIdOnly
        """
        if self.force_auto_sync:
            self.get('DutRouterIdOnly')
        return self._DutRouterIdOnly

    @property
    def DutAsNumber(self):
        """
        get the value of property _DutAsNumber
        """
        if self.force_auto_sync:
            self.get('DutAsNumber')
        return self._DutAsNumber

    @property
    def Enable4ByteDutAs(self):
        """
        get the value of property _Enable4ByteDutAs
        """
        if self.force_auto_sync:
            self.get('Enable4ByteDutAs')
        return self._Enable4ByteDutAs

    @property
    def Dut4ByteAsNumber(self):
        """
        get the value of property _Dut4ByteAsNumber
        """
        if self.force_auto_sync:
            self.get('Dut4ByteAsNumber')
        return self._Dut4ByteAsNumber

    @property
    def IgpProtocol(self):
        """
        get the value of property _IgpProtocol
        """
        if self.force_auto_sync:
            self.get('IgpProtocol')
        return self._IgpProtocol

    @property
    def IgpProtocolHandle(self):
        """
        get the value of property _IgpProtocolHandle
        """
        if self.force_auto_sync:
            self.get('IgpProtocolHandle')
        return self._IgpProtocolHandle

    @property
    def MplsProtocol(self):
        """
        get the value of property _MplsProtocol
        """
        if self.force_auto_sync:
            self.get('MplsProtocol')
        return self._MplsProtocol

    @property
    def MplsProtocolHandle(self):
        """
        get the value of property _MplsProtocolHandle
        """
        if self.force_auto_sync:
            self.get('MplsProtocolHandle')
        return self._MplsProtocolHandle

    @property
    def EnablePRouters(self):
        """
        get the value of property _EnablePRouters
        """
        if self.force_auto_sync:
            self.get('EnablePRouters')
        return self._EnablePRouters

    @property
    def PRoutersPerInterface(self):
        """
        get the value of property _PRoutersPerInterface
        """
        if self.force_auto_sync:
            self.get('PRoutersPerInterface')
        return self._PRoutersPerInterface

    @property
    def TopologyType(self):
        """
        get the value of property _TopologyType
        """
        if self.force_auto_sync:
            self.get('TopologyType')
        return self._TopologyType

    @property
    def PRoutersStartIp(self):
        """
        get the value of property _PRoutersStartIp
        """
        if self.force_auto_sync:
            self.get('PRoutersStartIp')
        return self._PRoutersStartIp

    @property
    def PRoutersPrefixLength(self):
        """
        get the value of property _PRoutersPrefixLength
        """
        if self.force_auto_sync:
            self.get('PRoutersPrefixLength')
        return self._PRoutersPrefixLength

    @property
    def PRoutersIdStart(self):
        """
        get the value of property _PRoutersIdStart
        """
        if self.force_auto_sync:
            self.get('PRoutersIdStart')
        return self._PRoutersIdStart

    @property
    def PRoutersIdStep(self):
        """
        get the value of property _PRoutersIdStep
        """
        if self.force_auto_sync:
            self.get('PRoutersIdStep')
        return self._PRoutersIdStep

    @property
    def PeRoutersPerInterface(self):
        """
        get the value of property _PeRoutersPerInterface
        """
        if self.force_auto_sync:
            self.get('PeRoutersPerInterface')
        return self._PeRoutersPerInterface

    @property
    def PeRoutersIdStart(self):
        """
        get the value of property _PeRoutersIdStart
        """
        if self.force_auto_sync:
            self.get('PeRoutersIdStart')
        return self._PeRoutersIdStart

    @property
    def PeRoutersIdStep(self):
        """
        get the value of property _PeRoutersIdStep
        """
        if self.force_auto_sync:
            self.get('PeRoutersIdStep')
        return self._PeRoutersIdStep

    @property
    def TrafficFlow(self):
        """
        get the value of property _TrafficFlow
        """
        if self.force_auto_sync:
            self.get('TrafficFlow')
        return self._TrafficFlow

    @property
    def TrafficLoadPercentProvider(self):
        """
        get the value of property _TrafficLoadPercentProvider
        """
        if self.force_auto_sync:
            self.get('TrafficLoadPercentProvider')
        return self._TrafficLoadPercentProvider

    @property
    def TrafficLoadPercentCustomer(self):
        """
        get the value of property _TrafficLoadPercentCustomer
        """
        if self.force_auto_sync:
            self.get('TrafficLoadPercentCustomer')
        return self._TrafficLoadPercentCustomer

    @property
    def HasLspPing(self):
        """
        get the value of property _HasLspPing
        """
        if self.force_auto_sync:
            self.get('HasLspPing')
        return self._HasLspPing

    @property
    def CoreTunnelEnableLspPing(self):
        """
        get the value of property _CoreTunnelEnableLspPing
        """
        if self.force_auto_sync:
            self.get('CoreTunnelEnableLspPing')
        return self._CoreTunnelEnableLspPing

    @property
    def VpnTunnelEnablePeToDutLspPing(self):
        """
        get the value of property _VpnTunnelEnablePeToDutLspPing
        """
        if self.force_auto_sync:
            self.get('VpnTunnelEnablePeToDutLspPing')
        return self._VpnTunnelEnablePeToDutLspPing

    @PortHandles.setter
    def PortHandles(self, value):
        self._PortHandles = value
        self.edit(PortHandles=value)

    @InterfaceHandles.setter
    def InterfaceHandles(self, value):
        self._InterfaceHandles = value
        self.edit(InterfaceHandles=value)

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value
        self.edit(StreamTemplateHandles=value)

    @DutRouterId.setter
    def DutRouterId(self, value):
        self._DutRouterId = value
        self.edit(DutRouterId=value)

    @DutRouterIdOnly.setter
    def DutRouterIdOnly(self, value):
        self._DutRouterIdOnly = value
        self.edit(DutRouterIdOnly=value)

    @DutAsNumber.setter
    def DutAsNumber(self, value):
        self._DutAsNumber = value
        self.edit(DutAsNumber=value)

    @Enable4ByteDutAs.setter
    def Enable4ByteDutAs(self, value):
        self._Enable4ByteDutAs = value
        self.edit(Enable4ByteDutAs=value)

    @Dut4ByteAsNumber.setter
    def Dut4ByteAsNumber(self, value):
        self._Dut4ByteAsNumber = value
        self.edit(Dut4ByteAsNumber=value)

    @IgpProtocolHandle.setter
    def IgpProtocolHandle(self, value):
        self._IgpProtocolHandle = value
        self.edit(IgpProtocolHandle=value)

    @MplsProtocolHandle.setter
    def MplsProtocolHandle(self, value):
        self._MplsProtocolHandle = value
        self.edit(MplsProtocolHandle=value)

    @EnablePRouters.setter
    def EnablePRouters(self, value):
        self._EnablePRouters = value
        self.edit(EnablePRouters=value)

    @PRoutersPerInterface.setter
    def PRoutersPerInterface(self, value):
        self._PRoutersPerInterface = value
        self.edit(PRoutersPerInterface=value)

    @PRoutersStartIp.setter
    def PRoutersStartIp(self, value):
        self._PRoutersStartIp = value
        self.edit(PRoutersStartIp=value)

    @PRoutersPrefixLength.setter
    def PRoutersPrefixLength(self, value):
        self._PRoutersPrefixLength = value
        self.edit(PRoutersPrefixLength=value)

    @PRoutersIdStart.setter
    def PRoutersIdStart(self, value):
        self._PRoutersIdStart = value
        self.edit(PRoutersIdStart=value)

    @PRoutersIdStep.setter
    def PRoutersIdStep(self, value):
        self._PRoutersIdStep = value
        self.edit(PRoutersIdStep=value)

    @PeRoutersPerInterface.setter
    def PeRoutersPerInterface(self, value):
        self._PeRoutersPerInterface = value
        self.edit(PeRoutersPerInterface=value)

    @PeRoutersIdStart.setter
    def PeRoutersIdStart(self, value):
        self._PeRoutersIdStart = value
        self.edit(PeRoutersIdStart=value)

    @PeRoutersIdStep.setter
    def PeRoutersIdStep(self, value):
        self._PeRoutersIdStep = value
        self.edit(PeRoutersIdStep=value)

    @TrafficLoadPercentProvider.setter
    def TrafficLoadPercentProvider(self, value):
        self._TrafficLoadPercentProvider = value
        self.edit(TrafficLoadPercentProvider=value)

    @TrafficLoadPercentCustomer.setter
    def TrafficLoadPercentCustomer(self, value):
        self._TrafficLoadPercentCustomer = value
        self.edit(TrafficLoadPercentCustomer=value)

    @HasLspPing.setter
    def HasLspPing(self, value):
        self._HasLspPing = value
        self.edit(HasLspPing=value)

    @CoreTunnelEnableLspPing.setter
    def CoreTunnelEnableLspPing(self, value):
        self._CoreTunnelEnableLspPing = value
        self.edit(CoreTunnelEnableLspPing=value)

    @VpnTunnelEnablePeToDutLspPing.setter
    def VpnTunnelEnablePeToDutLspPing(self, value):
        self._VpnTunnelEnablePeToDutLspPing = value
        self.edit(VpnTunnelEnablePeToDutLspPing=value)

    def _set_porthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortHandles = tmp_value.split()

    def _set_interfacehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceHandles = tmp_value.split()

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_dutrouterid_with_str(self, value):
        self._DutRouterId = value

    def _set_dutrouteridonly_with_str(self, value):
        self._DutRouterIdOnly = (value == 'True')

    def _set_dutasnumber_with_str(self, value):
        try:
            self._DutAsNumber = int(value)
        except ValueError:
            self._DutAsNumber = hex(int(value, 16))

    def _set_enable4bytedutas_with_str(self, value):
        self._Enable4ByteDutAs = (value == 'True')

    def _set_dut4byteasnumber_with_str(self, value):
        self._Dut4ByteAsNumber = value

    def _set_igpprotocol_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgpProtocol = EnumMplsIgpProtocols.%s' % value[:seperate])

    def _set_igpprotocolhandle_with_str(self, value):
        self._IgpProtocolHandle = value

    def _set_mplsprotocol_with_str(self, value):
        seperate = value.find(':')
        exec('self._MplsProtocol = EnumMplsMplsProtocols.%s' % value[:seperate])

    def _set_mplsprotocolhandle_with_str(self, value):
        self._MplsProtocolHandle = value

    def _set_enableprouters_with_str(self, value):
        self._EnablePRouters = (value == 'True')

    def _set_proutersperinterface_with_str(self, value):
        try:
            self._PRoutersPerInterface = int(value)
        except ValueError:
            self._PRoutersPerInterface = hex(int(value, 16))

    def _set_topologytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TopologyType = EnumMplsTopologyType.%s' % value[:seperate])

    def _set_proutersstartip_with_str(self, value):
        self._PRoutersStartIp = value

    def _set_proutersprefixlength_with_str(self, value):
        try:
            self._PRoutersPrefixLength = int(value)
        except ValueError:
            self._PRoutersPrefixLength = hex(int(value, 16))

    def _set_proutersidstart_with_str(self, value):
        self._PRoutersIdStart = value

    def _set_proutersidstep_with_str(self, value):
        self._PRoutersIdStep = value

    def _set_peroutersperinterface_with_str(self, value):
        try:
            self._PeRoutersPerInterface = int(value)
        except ValueError:
            self._PeRoutersPerInterface = hex(int(value, 16))

    def _set_peroutersidstart_with_str(self, value):
        self._PeRoutersIdStart = value

    def _set_peroutersidstep_with_str(self, value):
        self._PeRoutersIdStep = value

    def _set_trafficflow_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficFlow = EnumMplsTrafficFlowType.%s' % value[:seperate])

    def _set_trafficloadpercentprovider_with_str(self, value):
        try:
            self._TrafficLoadPercentProvider = int(value)
        except ValueError:
            self._TrafficLoadPercentProvider = hex(int(value, 16))

    def _set_trafficloadpercentcustomer_with_str(self, value):
        try:
            self._TrafficLoadPercentCustomer = int(value)
        except ValueError:
            self._TrafficLoadPercentCustomer = hex(int(value, 16))

    def _set_haslspping_with_str(self, value):
        self._HasLspPing = (value == 'True')

    def _set_coretunnelenablelspping_with_str(self, value):
        self._CoreTunnelEnableLspPing = (value == 'True')

    def _set_vpntunnelenablepetodutlspping_with_str(self, value):
        self._VpnTunnelEnablePeToDutLspPing = (value == 'True')

