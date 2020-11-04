"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillTreeRootIDSubTLVConfig(ROMObject):
    def __init__(self, TreeRootIDNicknameOfRoot=None, TreeRootIDStartingTreeNumber=None, **kwargs):
        self._TreeRootIDNicknameOfRoot = TreeRootIDNicknameOfRoot  # Tree Root ID Nickname of Root
        self._TreeRootIDStartingTreeNumber = TreeRootIDStartingTreeNumber  # Tree Root ID Starting Tree Number

        properties = kwargs.copy()
        if TreeRootIDNicknameOfRoot is not None:
            properties['TreeRootIDNicknameOfRoot'] = TreeRootIDNicknameOfRoot
        if TreeRootIDStartingTreeNumber is not None:
            properties['TreeRootIDStartingTreeNumber'] = TreeRootIDStartingTreeNumber

        # call base class function, and it will send message to renix server to create a class.
        super(TrillTreeRootIDSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TreeRootIDNicknameOfRoot=None, TreeRootIDStartingTreeNumber=None, **kwargs):
        properties = kwargs.copy()
        if TreeRootIDNicknameOfRoot is not None:
            self._TreeRootIDNicknameOfRoot = TreeRootIDNicknameOfRoot
            properties['TreeRootIDNicknameOfRoot'] = TreeRootIDNicknameOfRoot
        if TreeRootIDStartingTreeNumber is not None:
            self._TreeRootIDStartingTreeNumber = TreeRootIDStartingTreeNumber
            properties['TreeRootIDStartingTreeNumber'] = TreeRootIDStartingTreeNumber

        super(TrillTreeRootIDSubTLVConfig, self).edit(**properties)

    @property
    def TreeRootIDNicknameOfRoot(self):
        """
        get the value of property _TreeRootIDNicknameOfRoot
        """
        if self.force_auto_sync:
            self.get('TreeRootIDNicknameOfRoot')
        return self._TreeRootIDNicknameOfRoot

    @property
    def TreeRootIDStartingTreeNumber(self):
        """
        get the value of property _TreeRootIDStartingTreeNumber
        """
        if self.force_auto_sync:
            self.get('TreeRootIDStartingTreeNumber')
        return self._TreeRootIDStartingTreeNumber

    @TreeRootIDNicknameOfRoot.setter
    def TreeRootIDNicknameOfRoot(self, value):
        self._TreeRootIDNicknameOfRoot = value
        self.edit(TreeRootIDNicknameOfRoot=value)

    @TreeRootIDStartingTreeNumber.setter
    def TreeRootIDStartingTreeNumber(self, value):
        self._TreeRootIDStartingTreeNumber = value
        self.edit(TreeRootIDStartingTreeNumber=value)

    def _set_treerootidnicknameofroot_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TreeRootIDNicknameOfRoot = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._TreeRootIDNicknameOfRoot.append(int(str_value))
            except ValueError:
                self._TreeRootIDNicknameOfRoot.append(hex(int(str_value, 16)))

    def _set_treerootidstartingtreenumber_with_str(self, value):
        try:
            self._TreeRootIDStartingTreeNumber = int(value)
        except ValueError:
            self._TreeRootIDStartingTreeNumber = hex(int(value, 16))

