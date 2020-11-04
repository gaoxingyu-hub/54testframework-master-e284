"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot3ahVarCommonConfig(ROMObject):
    def __init__(self, Branch=None, Leaf=None, **kwargs):
        self._Branch = Branch  # Branch
        self._Leaf = Leaf  # Leaf

        properties = kwargs.copy()
        if Branch is not None:
            properties['Branch'] = Branch
        if Leaf is not None:
            properties['Leaf'] = Leaf

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahVarCommonConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Branch=None, Leaf=None, **kwargs):
        properties = kwargs.copy()
        if Branch is not None:
            self._Branch = Branch
            properties['Branch'] = Branch
        if Leaf is not None:
            self._Leaf = Leaf
            properties['Leaf'] = Leaf

        super(Dot3ahVarCommonConfig, self).edit(**properties)

    @property
    def Branch(self):
        """
        get the value of property _Branch
        """
        if self.force_auto_sync:
            self.get('Branch')
        return self._Branch

    @property
    def Leaf(self):
        """
        get the value of property _Leaf
        """
        if self.force_auto_sync:
            self.get('Leaf')
        return self._Leaf

    @Branch.setter
    def Branch(self, value):
        self._Branch = value
        self.edit(Branch=value)

    @Leaf.setter
    def Leaf(self, value):
        self._Leaf = value
        self.edit(Leaf=value)

    def _set_branch_with_str(self, value):
        try:
            self._Branch = int(value)
        except ValueError:
            self._Branch = hex(int(value, 16))

    def _set_leaf_with_str(self, value):
        try:
            self._Leaf = int(value)
        except ValueError:
            self._Leaf = hex(int(value, 16))

