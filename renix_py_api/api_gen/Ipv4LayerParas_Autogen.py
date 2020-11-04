"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayerParas_Autogen import NetworkLayerParas


@rom_manager.rom
class Ipv4LayerParas(NetworkLayerParas):
    def __init__(self, PrefixLength=None, Address=None, Step=None, PortStep=None, Gateway=None, GatewayStep=None, StepInBlock=None, GatewayCount=None, GatewayStepPerBlock=None, **kwargs):
        self._PrefixLength = PrefixLength  # Prefix Length
        self._Address = Address  # IPv4 Address Start
        self._Step = Step  # IPv4 Address Step
        self._PortStep = PortStep  # IPv4 Address Per Port Step
        self._Gateway = Gateway  # Gateway Address
        self._GatewayStep = GatewayStep  # Gateway Address Step
        self._StepInBlock = StepInBlock  # Step In Block
        self._GatewayCount = GatewayCount  # Number of Gateway Address Count
        self._GatewayStepPerBlock = GatewayStepPerBlock  # Gateway Address Step(per block)

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if Address is not None:
            properties['Address'] = Address
        if Step is not None:
            properties['Step'] = Step
        if PortStep is not None:
            properties['PortStep'] = PortStep
        if Gateway is not None:
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            properties['GatewayStep'] = GatewayStep
        if StepInBlock is not None:
            properties['StepInBlock'] = StepInBlock
        if GatewayCount is not None:
            properties['GatewayCount'] = GatewayCount
        if GatewayStepPerBlock is not None:
            properties['GatewayStepPerBlock'] = GatewayStepPerBlock

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv4LayerParas, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, Address=None, Step=None, PortStep=None, Gateway=None, GatewayStep=None, StepInBlock=None, GatewayCount=None, GatewayStepPerBlock=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if Address is not None:
            self._Address = Address
            properties['Address'] = Address
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if PortStep is not None:
            self._PortStep = PortStep
            properties['PortStep'] = PortStep
        if Gateway is not None:
            self._Gateway = Gateway
            properties['Gateway'] = Gateway
        if GatewayStep is not None:
            self._GatewayStep = GatewayStep
            properties['GatewayStep'] = GatewayStep
        if StepInBlock is not None:
            self._StepInBlock = StepInBlock
            properties['StepInBlock'] = StepInBlock
        if GatewayCount is not None:
            self._GatewayCount = GatewayCount
            properties['GatewayCount'] = GatewayCount
        if GatewayStepPerBlock is not None:
            self._GatewayStepPerBlock = GatewayStepPerBlock
            properties['GatewayStepPerBlock'] = GatewayStepPerBlock

        super(Ipv4LayerParas, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

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
    def StepInBlock(self):
        """
        get the value of property _StepInBlock
        """
        if self.force_auto_sync:
            self.get('StepInBlock')
        return self._StepInBlock

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

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @Address.setter
    def Address(self, value):
        self._Address = value
        self.edit(Address=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

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

    @StepInBlock.setter
    def StepInBlock(self, value):
        self._StepInBlock = value
        self.edit(StepInBlock=value)

    @GatewayCount.setter
    def GatewayCount(self, value):
        self._GatewayCount = value
        self.edit(GatewayCount=value)

    @GatewayStepPerBlock.setter
    def GatewayStepPerBlock(self, value):
        self._GatewayStepPerBlock = value
        self.edit(GatewayStepPerBlock=value)

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_address_with_str(self, value):
        self._Address = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_portstep_with_str(self, value):
        self._PortStep = value

    def _set_gateway_with_str(self, value):
        self._Gateway = value

    def _set_gatewaystep_with_str(self, value):
        self._GatewayStep = value

    def _set_stepinblock_with_str(self, value):
        self._StepInBlock = value

    def _set_gatewaycount_with_str(self, value):
        try:
            self._GatewayCount = int(value)
        except ValueError:
            self._GatewayCount = hex(int(value, 16))

    def _set_gatewaystepperblock_with_str(self, value):
        self._GatewayStepPerBlock = value

