"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillTreesSubTLVConfig(ROMObject):
    def __init__(self, NumberOfTreesToCompute=None, MaximumTreesAbleToCompute=None, NumberOfTreesToUse=None, **kwargs):
        self._NumberOfTreesToCompute = NumberOfTreesToCompute  # Number of Trees to Compute
        self._MaximumTreesAbleToCompute = MaximumTreesAbleToCompute  # Maximum Trees Able to Compute
        self._NumberOfTreesToUse = NumberOfTreesToUse  # Number of Trees to Use

        properties = kwargs.copy()
        if NumberOfTreesToCompute is not None:
            properties['NumberOfTreesToCompute'] = NumberOfTreesToCompute
        if MaximumTreesAbleToCompute is not None:
            properties['MaximumTreesAbleToCompute'] = MaximumTreesAbleToCompute
        if NumberOfTreesToUse is not None:
            properties['NumberOfTreesToUse'] = NumberOfTreesToUse

        # call base class function, and it will send message to renix server to create a class.
        super(TrillTreesSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NumberOfTreesToCompute=None, MaximumTreesAbleToCompute=None, NumberOfTreesToUse=None, **kwargs):
        properties = kwargs.copy()
        if NumberOfTreesToCompute is not None:
            self._NumberOfTreesToCompute = NumberOfTreesToCompute
            properties['NumberOfTreesToCompute'] = NumberOfTreesToCompute
        if MaximumTreesAbleToCompute is not None:
            self._MaximumTreesAbleToCompute = MaximumTreesAbleToCompute
            properties['MaximumTreesAbleToCompute'] = MaximumTreesAbleToCompute
        if NumberOfTreesToUse is not None:
            self._NumberOfTreesToUse = NumberOfTreesToUse
            properties['NumberOfTreesToUse'] = NumberOfTreesToUse

        super(TrillTreesSubTLVConfig, self).edit(**properties)

    @property
    def NumberOfTreesToCompute(self):
        """
        get the value of property _NumberOfTreesToCompute
        """
        if self.force_auto_sync:
            self.get('NumberOfTreesToCompute')
        return self._NumberOfTreesToCompute

    @property
    def MaximumTreesAbleToCompute(self):
        """
        get the value of property _MaximumTreesAbleToCompute
        """
        if self.force_auto_sync:
            self.get('MaximumTreesAbleToCompute')
        return self._MaximumTreesAbleToCompute

    @property
    def NumberOfTreesToUse(self):
        """
        get the value of property _NumberOfTreesToUse
        """
        if self.force_auto_sync:
            self.get('NumberOfTreesToUse')
        return self._NumberOfTreesToUse

    @NumberOfTreesToCompute.setter
    def NumberOfTreesToCompute(self, value):
        self._NumberOfTreesToCompute = value
        self.edit(NumberOfTreesToCompute=value)

    @MaximumTreesAbleToCompute.setter
    def MaximumTreesAbleToCompute(self, value):
        self._MaximumTreesAbleToCompute = value
        self.edit(MaximumTreesAbleToCompute=value)

    @NumberOfTreesToUse.setter
    def NumberOfTreesToUse(self, value):
        self._NumberOfTreesToUse = value
        self.edit(NumberOfTreesToUse=value)

    def _set_numberoftreestocompute_with_str(self, value):
        try:
            self._NumberOfTreesToCompute = int(value)
        except ValueError:
            self._NumberOfTreesToCompute = hex(int(value, 16))

    def _set_maximumtreesabletocompute_with_str(self, value):
        try:
            self._MaximumTreesAbleToCompute = int(value)
        except ValueError:
            self._MaximumTreesAbleToCompute = hex(int(value, 16))

    def _set_numberoftreestouse_with_str(self, value):
        try:
            self._NumberOfTreesToUse = int(value)
        except ValueError:
            self._NumberOfTreesToUse = hex(int(value, 16))

