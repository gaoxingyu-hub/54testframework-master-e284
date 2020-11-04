"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class VxlanVmProperty(ROMObject):
    def __init__(self, AttachedVtepAddr=None, **kwargs):
        self._AttachedVtepAddr = AttachedVtepAddr  # Attached VTEP IP address

        properties = kwargs.copy()
        if AttachedVtepAddr is not None:
            properties['AttachedVtepAddr'] = AttachedVtepAddr

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanVmProperty, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AttachedVtepAddr=None, **kwargs):
        properties = kwargs.copy()
        if AttachedVtepAddr is not None:
            self._AttachedVtepAddr = AttachedVtepAddr
            properties['AttachedVtepAddr'] = AttachedVtepAddr

        super(VxlanVmProperty, self).edit(**properties)

    @property
    def AttachedVtepAddr(self):
        """
        get the value of property _AttachedVtepAddr
        """
        if self.force_auto_sync:
            self.get('AttachedVtepAddr')
        return self._AttachedVtepAddr

    @AttachedVtepAddr.setter
    def AttachedVtepAddr(self, value):
        self._AttachedVtepAddr = value
        self.edit(AttachedVtepAddr=value)

    def _set_attachedvtepaddr_with_str(self, value):
        self._AttachedVtepAddr = value

