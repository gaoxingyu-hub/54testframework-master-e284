"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayerParas_Autogen import NetworkLayerParas


@rom_manager.rom
class VlanLayerParas(NetworkLayerParas):
    def __init__(self, VlanId=None, VlanStep=None, StepInBlock=None, Priority=None, PriorityStep=None, PriorityList=None, Tpid=None, **kwargs):
        self._VlanId = VlanId  # VLAN Id Start
        self._VlanStep = VlanStep  # VLAN Id Step
        self._StepInBlock = StepInBlock  # VLAN Id Step In Block
        self._Priority = Priority  # Priority
        self._PriorityStep = PriorityStep  # VLAN Priority Step
        self._PriorityList = PriorityList  # VLAN Priority List
        self._Tpid = Tpid  # TPID

        properties = kwargs.copy()
        if VlanId is not None:
            properties['VlanId'] = VlanId
        if VlanStep is not None:
            properties['VlanStep'] = VlanStep
        if StepInBlock is not None:
            properties['StepInBlock'] = StepInBlock
        if Priority is not None:
            properties['Priority'] = Priority
        if PriorityStep is not None:
            properties['PriorityStep'] = PriorityStep
        if PriorityList is not None:
            properties['PriorityList'] = PriorityList
        if Tpid is not None:
            properties['Tpid'] = Tpid

        # call base class function, and it will send message to renix server to create a class.
        super(VlanLayerParas, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, VlanId=None, VlanStep=None, StepInBlock=None, Priority=None, PriorityStep=None, PriorityList=None, Tpid=None, **kwargs):
        properties = kwargs.copy()
        if VlanId is not None:
            self._VlanId = VlanId
            properties['VlanId'] = VlanId
        if VlanStep is not None:
            self._VlanStep = VlanStep
            properties['VlanStep'] = VlanStep
        if StepInBlock is not None:
            self._StepInBlock = StepInBlock
            properties['StepInBlock'] = StepInBlock
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if PriorityStep is not None:
            self._PriorityStep = PriorityStep
            properties['PriorityStep'] = PriorityStep
        if PriorityList is not None:
            self._PriorityList = PriorityList
            properties['PriorityList'] = PriorityList
        if Tpid is not None:
            self._Tpid = Tpid
            properties['Tpid'] = Tpid

        super(VlanLayerParas, self).edit(**properties)

    @property
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def VlanStep(self):
        """
        get the value of property _VlanStep
        """
        if self.force_auto_sync:
            self.get('VlanStep')
        return self._VlanStep

    @property
    def StepInBlock(self):
        """
        get the value of property _StepInBlock
        """
        if self.force_auto_sync:
            self.get('StepInBlock')
        return self._StepInBlock

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def PriorityStep(self):
        """
        get the value of property _PriorityStep
        """
        if self.force_auto_sync:
            self.get('PriorityStep')
        return self._PriorityStep

    @property
    def PriorityList(self):
        """
        get the value of property _PriorityList
        """
        if self.force_auto_sync:
            self.get('PriorityList')
        return self._PriorityList

    @property
    def Tpid(self):
        """
        get the value of property _Tpid
        """
        if self.force_auto_sync:
            self.get('Tpid')
        return self._Tpid

    @VlanId.setter
    def VlanId(self, value):
        self._VlanId = value
        self.edit(VlanId=value)

    @VlanStep.setter
    def VlanStep(self, value):
        self._VlanStep = value
        self.edit(VlanStep=value)

    @StepInBlock.setter
    def StepInBlock(self, value):
        self._StepInBlock = value
        self.edit(StepInBlock=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @PriorityStep.setter
    def PriorityStep(self, value):
        self._PriorityStep = value
        self.edit(PriorityStep=value)

    @PriorityList.setter
    def PriorityList(self, value):
        self._PriorityList = value
        self.edit(PriorityList=value)

    @Tpid.setter
    def Tpid(self, value):
        self._Tpid = value
        self.edit(Tpid=value)

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_vlanstep_with_str(self, value):
        try:
            self._VlanStep = int(value)
        except ValueError:
            self._VlanStep = hex(int(value, 16))

    def _set_stepinblock_with_str(self, value):
        try:
            self._StepInBlock = int(value)
        except ValueError:
            self._StepInBlock = hex(int(value, 16))

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_prioritystep_with_str(self, value):
        try:
            self._PriorityStep = int(value)
        except ValueError:
            self._PriorityStep = hex(int(value, 16))

    def _set_prioritylist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PriorityList = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._PriorityList.append(int(str_value))
            except ValueError:
                self._PriorityList.append(hex(int(str_value, 16)))

    def _set_tpid_with_str(self, value):
        try:
            self._Tpid = int(value)
        except ValueError:
            self._Tpid = hex(int(value, 16))

