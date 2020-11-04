"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class RelocateWizardConfig(WizardConfigBase):
    def __init__(self, PortList=None, HardwarePortList=None, WaitForPortStatusUp=None, **kwargs):
        self._PortList = PortList  # HardwarePort Handles
        self._HardwarePortList = HardwarePortList  # HardwarePort Handles
        self._WaitForPortStatusUp = WaitForPortStatusUp  # Wait for the port status to be up

        properties = kwargs.copy()
        if PortList is not None:
            properties['PortList'] = PortList
        if HardwarePortList is not None:
            properties['HardwarePortList'] = HardwarePortList
        if WaitForPortStatusUp is not None:
            properties['WaitForPortStatusUp'] = WaitForPortStatusUp

        # call base class function, and it will send message to renix server to create a class.
        super(RelocateWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PortList=None, HardwarePortList=None, WaitForPortStatusUp=None, **kwargs):
        properties = kwargs.copy()
        if PortList is not None:
            self._PortList = PortList
            properties['PortList'] = PortList
        if HardwarePortList is not None:
            self._HardwarePortList = HardwarePortList
            properties['HardwarePortList'] = HardwarePortList
        if WaitForPortStatusUp is not None:
            self._WaitForPortStatusUp = WaitForPortStatusUp
            properties['WaitForPortStatusUp'] = WaitForPortStatusUp

        super(RelocateWizardConfig, self).edit(**properties)

    @property
    def PortList(self):
        """
        get the value of property _PortList
        """
        if self.force_auto_sync:
            self.get('PortList')
        return self._PortList

    @property
    def HardwarePortList(self):
        """
        get the value of property _HardwarePortList
        """
        if self.force_auto_sync:
            self.get('HardwarePortList')
        return self._HardwarePortList

    @property
    def WaitForPortStatusUp(self):
        """
        get the value of property _WaitForPortStatusUp
        """
        if self.force_auto_sync:
            self.get('WaitForPortStatusUp')
        return self._WaitForPortStatusUp

    @PortList.setter
    def PortList(self, value):
        self._PortList = value
        self.edit(PortList=value)

    @HardwarePortList.setter
    def HardwarePortList(self, value):
        self._HardwarePortList = value
        self.edit(HardwarePortList=value)

    @WaitForPortStatusUp.setter
    def WaitForPortStatusUp(self, value):
        self._WaitForPortStatusUp = value
        self.edit(WaitForPortStatusUp=value)

    def _set_portlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortList = tmp_value.split()

    def _set_hardwareportlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HardwarePortList = tmp_value.split()

    def _set_waitforportstatusup_with_str(self, value):
        self._WaitForPortStatusUp = (value == 'True')

