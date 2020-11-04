"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv2NetworkAtchRouterConfig(ROMObject):
    def __init__(self, AttachedRouter=None, **kwargs):
        self._AttachedRouter = AttachedRouter  # Attached Router

        properties = kwargs.copy()
        if AttachedRouter is not None:
            properties['AttachedRouter'] = AttachedRouter

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2NetworkAtchRouterConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AttachedRouter=None, **kwargs):
        properties = kwargs.copy()
        if AttachedRouter is not None:
            self._AttachedRouter = AttachedRouter
            properties['AttachedRouter'] = AttachedRouter

        super(Ospfv2NetworkAtchRouterConfig, self).edit(**properties)

    @property
    def AttachedRouter(self):
        """
        get the value of property _AttachedRouter
        """
        if self.force_auto_sync:
            self.get('AttachedRouter')
        return self._AttachedRouter

    @AttachedRouter.setter
    def AttachedRouter(self, value):
        self._AttachedRouter = value
        self.edit(AttachedRouter=value)

    def _set_attachedrouter_with_str(self, value):
        self._AttachedRouter = value

