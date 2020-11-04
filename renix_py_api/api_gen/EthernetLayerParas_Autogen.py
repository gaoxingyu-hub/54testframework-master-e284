"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayerParas_Autogen import NetworkLayerParas


@rom_manager.rom
class EthernetLayerParas(NetworkLayerParas):
    def __init__(self, Address=None, Step=None, PortStep=None, StepInBlock=None, **kwargs):
        self._Address = Address  # Source MAC Address Start
        self._Step = Step  # Source MAC Address Step
        self._PortStep = PortStep  # Source MAC Per Port Step
        self._StepInBlock = StepInBlock  # Source MAC Block Step

        properties = kwargs.copy()
        if Address is not None:
            properties['Address'] = Address
        if Step is not None:
            properties['Step'] = Step
        if PortStep is not None:
            properties['PortStep'] = PortStep
        if StepInBlock is not None:
            properties['StepInBlock'] = StepInBlock

        # call base class function, and it will send message to renix server to create a class.
        super(EthernetLayerParas, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Address=None, Step=None, PortStep=None, StepInBlock=None, **kwargs):
        properties = kwargs.copy()
        if Address is not None:
            self._Address = Address
            properties['Address'] = Address
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if PortStep is not None:
            self._PortStep = PortStep
            properties['PortStep'] = PortStep
        if StepInBlock is not None:
            self._StepInBlock = StepInBlock
            properties['StepInBlock'] = StepInBlock

        super(EthernetLayerParas, self).edit(**properties)

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
    def StepInBlock(self):
        """
        get the value of property _StepInBlock
        """
        if self.force_auto_sync:
            self.get('StepInBlock')
        return self._StepInBlock

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

    @StepInBlock.setter
    def StepInBlock(self, value):
        self._StepInBlock = value
        self.edit(StepInBlock=value)

    def _set_address_with_str(self, value):
        self._Address = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_portstep_with_str(self, value):
        self._PortStep = value

    def _set_stepinblock_with_str(self, value):
        self._StepInBlock = value

