"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ExpandWizardCommand(ROMCommand):
    def __init__(self, WizardConfig=None, **kwargs):
        self._WizardConfig = WizardConfig  # Wizard Config Handle
        self._ReturnList = None  # Return Handles, not editable

        properties = kwargs.copy()
        if WizardConfig is not None:
            properties['WizardConfig'] = WizardConfig

        # call base class function, and it will send message to renix server to create a class.
        super(ExpandWizardCommand, self).__init__(**properties)

    @property
    def WizardConfig(self):
        """
        get the value of property _WizardConfig
        """
        return self._WizardConfig

    @property
    def ReturnList(self):
        """
        get the value of property _ReturnList
        """
        return self._ReturnList

    @WizardConfig.setter
    def WizardConfig(self, value):
        self._WizardConfig = value

    def _set_wizardconfig_with_str(self, value):
        self._WizardConfig = value

    def _set_returnlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ReturnList = tmp_value.split()

    def _set_output_property(self, value):
        self._set_returnlist_with_str(value)

