"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsL2VpnConfig_Autogen import MplsL2VpnConfig


@rom_manager.rom
class LdpVplsConfig(MplsL2VpnConfig):
    def __init__(self, EnableVplsScalability=None, **kwargs):
        self._EnableVplsScalability = EnableVplsScalability  # Enable VPLS Scalability

        properties = kwargs.copy()
        if EnableVplsScalability is not None:
            properties['EnableVplsScalability'] = EnableVplsScalability

        # call base class function, and it will send message to renix server to create a class.
        super(LdpVplsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableVplsScalability=None, **kwargs):
        properties = kwargs.copy()
        if EnableVplsScalability is not None:
            self._EnableVplsScalability = EnableVplsScalability
            properties['EnableVplsScalability'] = EnableVplsScalability

        super(LdpVplsConfig, self).edit(**properties)

    @property
    def EnableVplsScalability(self):
        """
        get the value of property _EnableVplsScalability
        """
        if self.force_auto_sync:
            self.get('EnableVplsScalability')
        return self._EnableVplsScalability

    @EnableVplsScalability.setter
    def EnableVplsScalability(self, value):
        self._EnableVplsScalability = value
        self.edit(EnableVplsScalability=value)

    def _set_enablevplsscalability_with_str(self, value):
        self._EnableVplsScalability = (value == 'True')

