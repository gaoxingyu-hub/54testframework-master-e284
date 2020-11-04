"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DotResultViewNode(ROMObject):
    def __init__(self, ViewNodeDescription=None, ResultViewType=None, ActionScript=None, AdditionalScript=None, **kwargs):
        self._ViewNodeDescription = ViewNodeDescription  # Description
        self._ResultViewType = ResultViewType  # Result Status
        self._ActionScript = ActionScript  # SQL to execute
        self._AdditionalScript = AdditionalScript  # Additional script to execute

        properties = kwargs.copy()
        if ViewNodeDescription is not None:
            properties['ViewNodeDescription'] = ViewNodeDescription
        if ResultViewType is not None:
            properties['ResultViewType'] = ResultViewType
        if ActionScript is not None:
            properties['ActionScript'] = ActionScript
        if AdditionalScript is not None:
            properties['AdditionalScript'] = AdditionalScript

        # call base class function, and it will send message to renix server to create a class.
        super(DotResultViewNode, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ViewNodeDescription=None, ResultViewType=None, ActionScript=None, AdditionalScript=None, **kwargs):
        properties = kwargs.copy()
        if ViewNodeDescription is not None:
            self._ViewNodeDescription = ViewNodeDescription
            properties['ViewNodeDescription'] = ViewNodeDescription
        if ResultViewType is not None:
            self._ResultViewType = ResultViewType
            properties['ResultViewType'] = ResultViewType
        if ActionScript is not None:
            self._ActionScript = ActionScript
            properties['ActionScript'] = ActionScript
        if AdditionalScript is not None:
            self._AdditionalScript = AdditionalScript
            properties['AdditionalScript'] = AdditionalScript

        super(DotResultViewNode, self).edit(**properties)

    @property
    def ViewNodeDescription(self):
        """
        get the value of property _ViewNodeDescription
        """
        if self.force_auto_sync:
            self.get('ViewNodeDescription')
        return self._ViewNodeDescription

    @property
    def ResultViewType(self):
        """
        get the value of property _ResultViewType
        """
        if self.force_auto_sync:
            self.get('ResultViewType')
        return self._ResultViewType

    @property
    def ActionScript(self):
        """
        get the value of property _ActionScript
        """
        if self.force_auto_sync:
            self.get('ActionScript')
        return self._ActionScript

    @property
    def AdditionalScript(self):
        """
        get the value of property _AdditionalScript
        """
        if self.force_auto_sync:
            self.get('AdditionalScript')
        return self._AdditionalScript

    @ViewNodeDescription.setter
    def ViewNodeDescription(self, value):
        self._ViewNodeDescription = value
        self.edit(ViewNodeDescription=value)

    @ResultViewType.setter
    def ResultViewType(self, value):
        self._ResultViewType = value
        self.edit(ResultViewType=value)

    @ActionScript.setter
    def ActionScript(self, value):
        self._ActionScript = value
        self.edit(ActionScript=value)

    @AdditionalScript.setter
    def AdditionalScript(self, value):
        self._AdditionalScript = value
        self.edit(AdditionalScript=value)

    def _set_viewnodedescription_with_str(self, value):
        self._ViewNodeDescription = value

    def _set_resultviewtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ResultViewType = EnumResultViewType.%s' % value[:seperate])

    def _set_actionscript_with_str(self, value):
        self._ActionScript = value

    def _set_additionalscript_with_str(self, value):
        self._AdditionalScript = value

