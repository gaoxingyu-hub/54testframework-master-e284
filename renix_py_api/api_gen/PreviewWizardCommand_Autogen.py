"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PreviewWizardCommand(ROMCommand):
    def __init__(self, WizardConfig=None, NameOffset=None, **kwargs):
        self._WizardConfig = WizardConfig  # Wizard Config Handle
        self._NameOffset = NameOffset  # Offset
        self._PreviewHeader = ''  # Preview Header, not editable
        self._PreviewValue = None  # Return Handles, not editable

        properties = kwargs.copy()
        if WizardConfig is not None:
            properties['WizardConfig'] = WizardConfig
        if NameOffset is not None:
            properties['NameOffset'] = NameOffset

        # call base class function, and it will send message to renix server to create a class.
        super(PreviewWizardCommand, self).__init__(**properties)

    @property
    def WizardConfig(self):
        """
        get the value of property _WizardConfig
        """
        return self._WizardConfig

    @property
    def NameOffset(self):
        """
        get the value of property _NameOffset
        """
        return self._NameOffset

    @property
    def PreviewHeader(self):
        """
        get the value of property _PreviewHeader
        """
        return self._PreviewHeader

    @property
    def PreviewValue(self):
        """
        get the value of property _PreviewValue
        """
        return self._PreviewValue

    @WizardConfig.setter
    def WizardConfig(self, value):
        self._WizardConfig = value

    @NameOffset.setter
    def NameOffset(self, value):
        self._NameOffset = value

    def _set_wizardconfig_with_str(self, value):
        self._WizardConfig = value

    def _set_nameoffset_with_str(self, value):
        try:
            self._NameOffset = int(value)
        except ValueError:
            self._NameOffset = hex(int(value, 16))

    def _set_previewheader_with_str(self, value):
        self._PreviewHeader = value

    def _set_previewvalue_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PreviewValue = tmp_value.split()

