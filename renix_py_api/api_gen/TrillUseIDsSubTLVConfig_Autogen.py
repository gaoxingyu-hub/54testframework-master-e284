"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillUseIDsSubTLVConfig(ROMObject):
    def __init__(self, TreeUseIDNicknameOfRoot=None, TreeUseIDStartingTreeNumber=None, **kwargs):
        self._TreeUseIDNicknameOfRoot = TreeUseIDNicknameOfRoot  # Tree Use ID Nickname of Root
        self._TreeUseIDStartingTreeNumber = TreeUseIDStartingTreeNumber  # Tree Use ID Starting Tree Number

        properties = kwargs.copy()
        if TreeUseIDNicknameOfRoot is not None:
            properties['TreeUseIDNicknameOfRoot'] = TreeUseIDNicknameOfRoot
        if TreeUseIDStartingTreeNumber is not None:
            properties['TreeUseIDStartingTreeNumber'] = TreeUseIDStartingTreeNumber

        # call base class function, and it will send message to renix server to create a class.
        super(TrillUseIDsSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TreeUseIDNicknameOfRoot=None, TreeUseIDStartingTreeNumber=None, **kwargs):
        properties = kwargs.copy()
        if TreeUseIDNicknameOfRoot is not None:
            self._TreeUseIDNicknameOfRoot = TreeUseIDNicknameOfRoot
            properties['TreeUseIDNicknameOfRoot'] = TreeUseIDNicknameOfRoot
        if TreeUseIDStartingTreeNumber is not None:
            self._TreeUseIDStartingTreeNumber = TreeUseIDStartingTreeNumber
            properties['TreeUseIDStartingTreeNumber'] = TreeUseIDStartingTreeNumber

        super(TrillUseIDsSubTLVConfig, self).edit(**properties)

    @property
    def TreeUseIDNicknameOfRoot(self):
        """
        get the value of property _TreeUseIDNicknameOfRoot
        """
        if self.force_auto_sync:
            self.get('TreeUseIDNicknameOfRoot')
        return self._TreeUseIDNicknameOfRoot

    @property
    def TreeUseIDStartingTreeNumber(self):
        """
        get the value of property _TreeUseIDStartingTreeNumber
        """
        if self.force_auto_sync:
            self.get('TreeUseIDStartingTreeNumber')
        return self._TreeUseIDStartingTreeNumber

    @TreeUseIDNicknameOfRoot.setter
    def TreeUseIDNicknameOfRoot(self, value):
        self._TreeUseIDNicknameOfRoot = value
        self.edit(TreeUseIDNicknameOfRoot=value)

    @TreeUseIDStartingTreeNumber.setter
    def TreeUseIDStartingTreeNumber(self, value):
        self._TreeUseIDStartingTreeNumber = value
        self.edit(TreeUseIDStartingTreeNumber=value)

    def _set_treeuseidnicknameofroot_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TreeUseIDNicknameOfRoot = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._TreeUseIDNicknameOfRoot.append(int(str_value))
            except ValueError:
                self._TreeUseIDNicknameOfRoot.append(hex(int(str_value, 16)))

    def _set_treeuseidstartingtreenumber_with_str(self, value):
        try:
            self._TreeUseIDStartingTreeNumber = int(value)
        except ValueError:
            self._TreeUseIDStartingTreeNumber = hex(int(value, 16))

