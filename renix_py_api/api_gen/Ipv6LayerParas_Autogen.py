"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayerParas_Autogen import NetworkLayerParas


@rom_manager.rom
class Ipv6LayerParas(NetworkLayerParas):
    def __init__(self, PrefixLength=None, AddrType=None, Address=None, Step=None, StepInBlock=None, PortStep=None, Gateway=None, GatewayStep=None, GatewayCount=None, GatewayStepPerBlock=None, LinkLocalGenType=None, LinkLocal=None, LinkLocalStep=None, LinkLocalPortStep=None, **kwargs):
        self._PrefixLength = PrefixLength  # Prefix Length
        self._AddrType = AddrType  # Address Type
        self._Address = Address  # IPv6 Address Start
        self._Step = Step  # IPv6 Address Step
        self._StepInBlock = StepInBlock  # Step In Block
        self._PortStep = PortStep  # IPv6 Address Per Port Step
        self._Gateway = Gateway  # IPv6 Gateway Address
        self._GatewayStep = GatewayStep  # IPv6 Gateway Address Step
        self._GatewayCount = GatewayCount  # Number of Gateway Address Count
        self._GatewayStepPerBlock = GatewayStepPerBlock  # IPv6 Gateway Address Step(in block)
        self._LinkLocalGenType = LinkLocalGenType  # Link Local Generation Type
        self._LinkLocal = LinkLocal  # IPv6 Link Local Address
        self._LinkLocalStep = LinkLocalStep  # IPv6 Link Local Address Step
        self._LinkLocalPortStep = LinkLocalPortStep  # IPv6 Link Local Address Port Step

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if AddrType is not None:
            properties['AddrType'] = AddrType
        if Address is not None:
            properties['Address'] = Address
        if Step is not None:
            properties['Step'] = Step
        if StepInBlock is not None:
            properties['StepInBlock'] = StepInBlock
        if PortStep is not None:
            properties['PortStep'] = PortStep
        if Gateway is not None:
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            properties['GatewayStep'] = GatewayStep
        if GatewayCount is not None:
            properties['GatewayCount'] = GatewayCount
        if GatewayStepPerBlock is not None:
            properties['GatewayStepPerBlock'] = GatewayStepPerBlock
        if LinkLocalGenType is not None:
            properties['LinkLocalGenType'] = LinkLocalGenType
        if LinkLocal is not None:
            properties['LinkLocal'] = LinkLocal
        if LinkLocalStep is not None:
            properties['LinkLocalStep'] = LinkLocalStep
        if LinkLocalPortStep is not None:
            properties['LinkLocalPortStep'] = LinkLocalPortStep

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv6LayerParas, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, AddrType=None, Address=None, Step=None, StepInBlock=None, PortStep=None, Gateway=None, GatewayStep=None, GatewayCount=None, GatewayStepPerBlock=None, LinkLocalGenType=None, LinkLocal=None, LinkLocalStep=None, LinkLocalPortStep=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if AddrType is not None:
            self._AddrType = AddrType
            properties['AddrType'] = AddrType
        if Address is not None:
            self._Address = Address
            properties['Address'] = Address
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if StepInBlock is not None:
            self._StepInBlock = StepInBlock
            properties['StepInBlock'] = StepInBlock
        if PortStep is not None:
            self._PortStep = PortStep
            properties['PortStep'] = PortStep
        if Gateway is not None:
            self._Gateway = Gateway
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            self._GatewayStep = GatewayStep
            properties['GatewayStep'] = GatewayStep
        if GatewayCount is not None:
            self._GatewayCount = GatewayCount
            properties['GatewayCount'] = GatewayCount
        if GatewayStepPerBlock is not None:
            self._GatewayStepPerBlock = GatewayStepPerBlock
            properties['GatewayStepPerBlock'] = GatewayStepPerBlock
        if LinkLocalGenType is not None:
            self._LinkLocalGenType = LinkLocalGenType
            properties['LinkLocalGenType'] = LinkLocalGenType
        if LinkLocal is not None:
            self._LinkLocal = LinkLocal
            properties['LinkLocal'] = LinkLocal
        if LinkLocalStep is not None:
            self._LinkLocalStep = LinkLocalStep
            properties['LinkLocalStep'] = LinkLocalStep
        if LinkLocalPortStep is not None:
            self._LinkLocalPortStep = LinkLocalPortStep
            properties['LinkLocalPortStep'] = LinkLocalPortStep

        super(Ipv6LayerParas, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def AddrType(self):
        """
        get the value of property _AddrType
        """
        if self.force_auto_sync:
            self.get('AddrType')
        return self._AddrType

    @property
    def Address(self):
        """
        get the value of property _Address
        """
        if self.force_auto_sync:
            self.get('Address')
        return self._Address

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def StepInBlock(self):
        """
        get the value of property _StepInBlock
        """
        if self.force_auto_sync:
            self.get('StepInBlock')
        return self._StepInBlock

    @property
    def PortStep(self):
        """
        get the value of property _PortStep
        """
        if self.force_auto_sync:
            self.get('PortStep')
        return self._PortStep

    @property
    def Gateway(self):
        """
        get the value of property _Gateway
        """
        if self.force_auto_sync:
            self.get('Gateway')
        return self._Gateway

    @property
    def GatewayStep(self):
        """
        get the value of property _GatewayStep
        """
        if self.force_auto_sync:
            self.get('GatewayStep')
        return self._GatewayStep

    @property
    def GatewayCount(self):
        """
        get the value of property _GatewayCount
        """
        if self.force_auto_sync:
            self.get('GatewayCount')
        return self._GatewayCount

    @property
    def GatewayStepPerBlock(self):
        """
        get the value of property _GatewayStepPerBlock
        """
        if self.force_auto_sync:
            self.get('GatewayStepPerBlock')
        return self._GatewayStepPerBlock

    @property
    def LinkLocalGenType(self):
        """
        get the value of property _LinkLocalGenType
        """
        if self.force_auto_sync:
            self.get('LinkLocalGenType')
        return self._LinkLocalGenType

    @property
    def LinkLocal(self):
        """
        get the value of property _LinkLocal
        """
        if self.force_auto_sync:
            self.get('LinkLocal')
        return self._LinkLocal

    @property
    def LinkLocalStep(self):
        """
        get the value of property _LinkLocalStep
        """
        if self.force_auto_sync:
            self.get('LinkLocalStep')
        return self._LinkLocalStep

    @property
    def LinkLocalPortStep(self):
        """
        get the value of property _LinkLocalPortStep
        """
        if self.force_auto_sync:
            self.get('LinkLocalPortStep')
        return self._LinkLocalPortStep

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @AddrType.setter
    def AddrType(self, value):
        self._AddrType = value
        self.edit(AddrType=value)

    @Address.setter
    def Address(self, value):
        self._Address = value
        self.edit(Address=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @StepInBlock.setter
    def StepInBlock(self, value):
        self._StepInBlock = value
        self.edit(StepInBlock=value)

    @PortStep.setter
    def PortStep(self, value):
        self._PortStep = value
        self.edit(PortStep=value)

    @Gateway.setter
    def Gateway(self, value):
        self._Gateway = value
        self.edit(Gateway=value)

    @GatewayStep.setter
    def GatewayStep(self, value):
        self._GatewayStep = value
        self.edit(GatewayStep=value)

    @GatewayCount.setter
    def GatewayCount(self, value):
        self._GatewayCount = value
        self.edit(GatewayCount=value)

    @GatewayStepPerBlock.setter
    def GatewayStepPerBlock(self, value):
        self._GatewayStepPerBlock = value
        self.edit(GatewayStepPerBlock=value)

    @LinkLocalGenType.setter
    def LinkLocalGenType(self, value):
        self._LinkLocalGenType = value
        self.edit(LinkLocalGenType=value)

    @LinkLocal.setter
    def LinkLocal(self, value):
        self._LinkLocal = value
        self.edit(LinkLocal=value)

    @LinkLocalStep.setter
    def LinkLocalStep(self, value):
        self._LinkLocalStep = value
        self.edit(LinkLocalStep=value)

    @LinkLocalPortStep.setter
    def LinkLocalPortStep(self, value):
        self._LinkLocalPortStep = value
        self.edit(LinkLocalPortStep=value)

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_addrtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AddrType = EnumIPv6AddrType.%s' % value[:seperate])

    def _set_address_with_str(self, value):
        self._Address = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_stepinblock_with_str(self, value):
        self._StepInBlock = value

    def _set_portstep_with_str(self, value):
        self._PortStep = value

    def _set_gateway_with_str(self, value):
        self._Gateway = value

    def _set_gatewaystep_with_str(self, value):
        self._GatewayStep = value

    def _set_gatewaycount_with_str(self, value):
        try:
            self._GatewayCount = int(value)
        except ValueError:
            self._GatewayCount = hex(int(value, 16))

    def _set_gatewaystepperblock_with_str(self, value):
        self._GatewayStepPerBlock = value

    def _set_linklocalgentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkLocalGenType = LinkLocalGenTypeEnum.%s' % value[:seperate])

    def _set_linklocal_with_str(self, value):
        self._LinkLocal = value

    def _set_linklocalstep_with_str(self, value):
        self._LinkLocalStep = value

    def _set_linklocalportstep_with_str(self, value):
        self._LinkLocalPortStep = value

