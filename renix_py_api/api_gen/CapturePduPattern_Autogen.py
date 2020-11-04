"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CapturePattern_Autogen import CapturePattern


@rom_manager.rom
class CapturePduPattern(CapturePattern):
    def __init__(self, TemplateString=None, **kwargs):
        self._PduPatternName = 'ethernetII_1.destMacAdd'  # Field Name, not editable
        self._Value = '00:00:02:02:01:02'  # Value, not editable
        self._TemplateString = TemplateString  # Template String

        properties = kwargs.copy()
        if TemplateString is not None:
            properties['TemplateString'] = TemplateString

        # call base class function, and it will send message to renix server to create a class.
        super(CapturePduPattern, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TemplateString=None, **kwargs):
        properties = kwargs.copy()
        if TemplateString is not None:
            self._TemplateString = TemplateString
            properties['TemplateString'] = TemplateString

        super(CapturePduPattern, self).edit(**properties)

    @property
    def PduPatternName(self):
        """
        get the value of property _PduPatternName
        """
        if self.force_auto_sync:
            self.get('PduPatternName')
        return self._PduPatternName

    @property
    def Value(self):
        """
        get the value of property _Value
        """
        if self.force_auto_sync:
            self.get('Value')
        return self._Value

    @property
    def TemplateString(self):
        """
        get the value of property _TemplateString
        """
        if self.force_auto_sync:
            self.get('TemplateString')
        return self._TemplateString

    @TemplateString.setter
    def TemplateString(self, value):
        self._TemplateString = value
        self.edit(TemplateString=value)

    def _set_pdupatternname_with_str(self, value):
        self._PduPatternName = value

    def _set_value_with_str(self, value):
        self._Value = value

    def _set_templatestring_with_str(self, value):
        self._TemplateString = value

