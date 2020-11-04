"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from renix_py_api.core import Core


@rom_manager.rom
class ROMObject(Core):
    def __init__(self, Name=None, Enable=None, ROMTag=None, **kwargs):
        self._Name = Name  # Name
        self._Enable = Enable  # Enable
        self._ROMTag = ROMTag  # Tag

        properties = kwargs.copy()
        if Name is not None:
            properties['Name'] = Name
        if Enable is not None:
            properties['Enable'] = Enable
        if ROMTag is not None:
            properties['ROMTag'] = ROMTag

        # call base class function, and it will send message to renix server to create a class.
        from .ROMCommand_Autogen import ROMCommand
        if isinstance(self, ROMCommand):
            self.force_auto_sync = False
        else:
            super(ROMObject, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Name=None, Enable=None, ROMTag=None, **kwargs):
        properties = kwargs.copy()
        if Name is not None:
            self._Name = Name
            properties['Name'] = Name
        if Enable is not None:
            self._Enable = Enable
            properties['Enable'] = Enable
        if ROMTag is not None:
            self._ROMTag = ROMTag
            properties['ROMTag'] = ROMTag

        super(ROMObject, self).edit(**properties)

    @property
    def Name(self):
        """
        get the value of property _Name
        """
        if self.force_auto_sync:
            self.get('Name')
        return self._Name

    @property
    def Enable(self):
        """
        get the value of property _Enable
        """
        if self.force_auto_sync:
            self.get('Enable')
        return self._Enable

    @property
    def ROMTag(self):
        """
        get the value of property _ROMTag
        """
        if self.force_auto_sync:
            self.get('ROMTag')
        return self._ROMTag

    @Name.setter
    def Name(self, value):
        self._Name = value
        self.edit(Name=value)

    @Enable.setter
    def Enable(self, value):
        self._Enable = value
        self.edit(Enable=value)

    @ROMTag.setter
    def ROMTag(self, value):
        self._ROMTag = value
        self.edit(ROMTag=value)

    def _set_name_with_str(self, value):
        self._Name = value

    def _set_enable_with_str(self, value):
        self._Enable = (value == 'True')

    def _set_romtag_with_str(self, value):
        self._ROMTag = value

