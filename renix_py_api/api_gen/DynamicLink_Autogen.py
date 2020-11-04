"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DynamicLink(ROMObject):
    def __init__(self, Source=None, Target=None, MinOccur=None, MaxOccur=None, Cloneable=None, **kwargs):
        self._Source = Source  # Link Source
        self._Target = Target  # Link Target
        self._MinOccur = MinOccur  # Min Occur
        self._MaxOccur = MaxOccur  # Max Occur
        self._Cloneable = Cloneable  # Cloneable

        properties = kwargs.copy()
        if Source is not None:
            properties['Source'] = Source
        if Target is not None:
            properties['Target'] = Target
        if MinOccur is not None:
            properties['MinOccur'] = MinOccur
        if MaxOccur is not None:
            properties['MaxOccur'] = MaxOccur
        if Cloneable is not None:
            properties['Cloneable'] = Cloneable

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicLink, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Source=None, Target=None, MinOccur=None, MaxOccur=None, Cloneable=None, **kwargs):
        properties = kwargs.copy()
        if Source is not None:
            self._Source = Source
            properties['Source'] = Source
        if Target is not None:
            self._Target = Target
            properties['Target'] = Target
        if MinOccur is not None:
            self._MinOccur = MinOccur
            properties['MinOccur'] = MinOccur
        if MaxOccur is not None:
            self._MaxOccur = MaxOccur
            properties['MaxOccur'] = MaxOccur
        if Cloneable is not None:
            self._Cloneable = Cloneable
            properties['Cloneable'] = Cloneable

        super(DynamicLink, self).edit(**properties)

    @property
    def Source(self):
        """
        get the value of property _Source
        """
        if self.force_auto_sync:
            self.get('Source')
        return self._Source

    @property
    def Target(self):
        """
        get the value of property _Target
        """
        if self.force_auto_sync:
            self.get('Target')
        return self._Target

    @property
    def MinOccur(self):
        """
        get the value of property _MinOccur
        """
        if self.force_auto_sync:
            self.get('MinOccur')
        return self._MinOccur

    @property
    def MaxOccur(self):
        """
        get the value of property _MaxOccur
        """
        if self.force_auto_sync:
            self.get('MaxOccur')
        return self._MaxOccur

    @property
    def Cloneable(self):
        """
        get the value of property _Cloneable
        """
        if self.force_auto_sync:
            self.get('Cloneable')
        return self._Cloneable

    @Source.setter
    def Source(self, value):
        self._Source = value
        self.edit(Source=value)

    @Target.setter
    def Target(self, value):
        self._Target = value
        self.edit(Target=value)

    @MinOccur.setter
    def MinOccur(self, value):
        self._MinOccur = value
        self.edit(MinOccur=value)

    @MaxOccur.setter
    def MaxOccur(self, value):
        self._MaxOccur = value
        self.edit(MaxOccur=value)

    @Cloneable.setter
    def Cloneable(self, value):
        self._Cloneable = value
        self.edit(Cloneable=value)

    def _set_source_with_str(self, value):
        self._Source = value

    def _set_target_with_str(self, value):
        self._Target = value

    def _set_minoccur_with_str(self, value):
        try:
            self._MinOccur = int(value)
        except ValueError:
            self._MinOccur = hex(int(value, 16))

    def _set_maxoccur_with_str(self, value):
        try:
            self._MaxOccur = int(value)
        except ValueError:
            self._MaxOccur = hex(int(value, 16))

    def _set_cloneable_with_str(self, value):
        self._Cloneable = (value == 'True')

