"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Vlan1Parameter(ROMObject):
    def __init__(self, VlanId=None, Priority=None, IsBound=None, **kwargs):
        self._VlanId = VlanId  # VLAN 1
        self._Priority = Priority  # VLAN 1 Priority
        self._IsBound = IsBound  # Current field is bound for interface

        properties = kwargs.copy()
        if VlanId is not None:
            properties['VlanId'] = VlanId
        if Priority is not None:
            properties['Priority'] = Priority
        if IsBound is not None:
            properties['IsBound'] = IsBound

        # call base class function, and it will send message to renix server to create a class.
        super(Vlan1Parameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, VlanId=None, Priority=None, IsBound=None, **kwargs):
        properties = kwargs.copy()
        if VlanId is not None:
            self._VlanId = VlanId
            properties['VlanId'] = VlanId
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if IsBound is not None:
            self._IsBound = IsBound
            properties['IsBound'] = IsBound

        super(Vlan1Parameter, self).edit(**properties)

    @property
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def IsBound(self):
        """
        get the value of property _IsBound
        """
        if self.force_auto_sync:
            self.get('IsBound')
        return self._IsBound

    @VlanId.setter
    def VlanId(self, value):
        self._VlanId = value
        self.edit(VlanId=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @IsBound.setter
    def IsBound(self, value):
        self._IsBound = value
        self.edit(IsBound=value)

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_isbound_with_str(self, value):
        self._IsBound = (value == 'True')

