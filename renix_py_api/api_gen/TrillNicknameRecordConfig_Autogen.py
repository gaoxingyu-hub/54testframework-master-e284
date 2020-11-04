"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillNicknameRecordConfig(ROMObject):
    def __init__(self, NicknamePriority=None, TreeRootPriority=None, RBridgeNickname=None, **kwargs):
        self._NicknamePriority = NicknamePriority  # Nickname Priority
        self._TreeRootPriority = TreeRootPriority  # Tree Root Priority
        self._RBridgeNickname = RBridgeNickname  # RBridge Nickname

        properties = kwargs.copy()
        if NicknamePriority is not None:
            properties['NicknamePriority'] = NicknamePriority
        if TreeRootPriority is not None:
            properties['TreeRootPriority'] = TreeRootPriority
        if RBridgeNickname is not None:
            properties['RBridgeNickname'] = RBridgeNickname

        # call base class function, and it will send message to renix server to create a class.
        super(TrillNicknameRecordConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NicknamePriority=None, TreeRootPriority=None, RBridgeNickname=None, **kwargs):
        properties = kwargs.copy()
        if NicknamePriority is not None:
            self._NicknamePriority = NicknamePriority
            properties['NicknamePriority'] = NicknamePriority
        if TreeRootPriority is not None:
            self._TreeRootPriority = TreeRootPriority
            properties['TreeRootPriority'] = TreeRootPriority
        if RBridgeNickname is not None:
            self._RBridgeNickname = RBridgeNickname
            properties['RBridgeNickname'] = RBridgeNickname

        super(TrillNicknameRecordConfig, self).edit(**properties)

    @property
    def NicknamePriority(self):
        """
        get the value of property _NicknamePriority
        """
        if self.force_auto_sync:
            self.get('NicknamePriority')
        return self._NicknamePriority

    @property
    def TreeRootPriority(self):
        """
        get the value of property _TreeRootPriority
        """
        if self.force_auto_sync:
            self.get('TreeRootPriority')
        return self._TreeRootPriority

    @property
    def RBridgeNickname(self):
        """
        get the value of property _RBridgeNickname
        """
        if self.force_auto_sync:
            self.get('RBridgeNickname')
        return self._RBridgeNickname

    @NicknamePriority.setter
    def NicknamePriority(self, value):
        self._NicknamePriority = value
        self.edit(NicknamePriority=value)

    @TreeRootPriority.setter
    def TreeRootPriority(self, value):
        self._TreeRootPriority = value
        self.edit(TreeRootPriority=value)

    @RBridgeNickname.setter
    def RBridgeNickname(self, value):
        self._RBridgeNickname = value
        self.edit(RBridgeNickname=value)

    def _set_nicknamepriority_with_str(self, value):
        try:
            self._NicknamePriority = int(value)
        except ValueError:
            self._NicknamePriority = hex(int(value, 16))

    def _set_treerootpriority_with_str(self, value):
        try:
            self._TreeRootPriority = int(value)
        except ValueError:
            self._TreeRootPriority = hex(int(value, 16))

    def _set_rbridgenickname_with_str(self, value):
        try:
            self._RBridgeNickname = int(value)
        except ValueError:
            self._RBridgeNickname = hex(int(value, 16))

