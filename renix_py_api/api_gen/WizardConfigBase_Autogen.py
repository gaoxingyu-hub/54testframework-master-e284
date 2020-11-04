"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class WizardConfigBase(ROMObject):
    def __init__(self, IsAppended=None, PortType=None, **kwargs):
        self._PreviewUpperLimit = 1000  # Max preview count, not editable
        self._IsAppended = IsAppended  # Append to existing config
        self._PortType = PortType  # Port Type

        properties = kwargs.copy()
        if IsAppended is not None:
            properties['IsAppended'] = IsAppended
        if PortType is not None:
            properties['PortType'] = PortType

        # call base class function, and it will send message to renix server to create a class.
        super(WizardConfigBase, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IsAppended=None, PortType=None, **kwargs):
        properties = kwargs.copy()
        if IsAppended is not None:
            self._IsAppended = IsAppended
            properties['IsAppended'] = IsAppended
        if PortType is not None:
            self._PortType = PortType
            properties['PortType'] = PortType

        super(WizardConfigBase, self).edit(**properties)

    @property
    def PreviewUpperLimit(self):
        """
        get the value of property _PreviewUpperLimit
        """
        if self.force_auto_sync:
            self.get('PreviewUpperLimit')
        return self._PreviewUpperLimit

    @property
    def IsAppended(self):
        """
        get the value of property _IsAppended
        """
        if self.force_auto_sync:
            self.get('IsAppended')
        return self._IsAppended

    @property
    def PortType(self):
        """
        get the value of property _PortType
        """
        if self.force_auto_sync:
            self.get('PortType')
        return self._PortType

    @IsAppended.setter
    def IsAppended(self, value):
        self._IsAppended = value
        self.edit(IsAppended=value)

    @PortType.setter
    def PortType(self, value):
        self._PortType = value
        self.edit(PortType=value)

    def _set_previewupperlimit_with_str(self, value):
        try:
            self._PreviewUpperLimit = int(value)
        except ValueError:
            self._PreviewUpperLimit = hex(int(value, 16))

    def _set_isappended_with_str(self, value):
        self._IsAppended = (value == 'True')

    def _set_porttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._PortType = EnumPortType.%s' % value[:seperate])

