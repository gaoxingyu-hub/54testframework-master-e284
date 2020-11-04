"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EthMedia_Autogen import EthMedia


@rom_manager.rom
class EthFiber(EthMedia):
    def __init__(self, **kwargs):
        self._ModuleCpability = EnumModuleCapability.MOD_UNKNOWN  # Module Cpability, not editable
        self._PlugIn = False  # PlugIn, not editable
        self._RemoteFault = EnumRemoteFaultStatus.NORMAL  # Remote Fault Status, not editable
        self._PhyMode = EnumPhyMode.MODE_AUTO  # PHY Mode, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(EthFiber, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(EthFiber, self).edit(**properties)

    @property
    def ModuleCpability(self):
        """
        get the value of property _ModuleCpability
        """
        if self.force_auto_sync:
            self.get('ModuleCpability')
        return self._ModuleCpability

    @property
    def PlugIn(self):
        """
        get the value of property _PlugIn
        """
        if self.force_auto_sync:
            self.get('PlugIn')
        return self._PlugIn

    @property
    def RemoteFault(self):
        """
        get the value of property _RemoteFault
        """
        if self.force_auto_sync:
            self.get('RemoteFault')
        return self._RemoteFault

    @property
    def PhyMode(self):
        """
        get the value of property _PhyMode
        """
        if self.force_auto_sync:
            self.get('PhyMode')
        return self._PhyMode

    def _set_modulecpability_with_str(self, value):
        seperate = value.find(':')
        exec('self._ModuleCpability = EnumModuleCapability.%s' % value[:seperate])

    def _set_plugin_with_str(self, value):
        self._PlugIn = (value == 'True')

    def _set_remotefault_with_str(self, value):
        seperate = value.find(':')
        exec('self._RemoteFault = EnumRemoteFaultStatus.%s' % value[:seperate])

    def _set_phymode_with_str(self, value):
        seperate = value.find(':')
        exec('self._PhyMode = EnumPhyMode.%s' % value[:seperate])

