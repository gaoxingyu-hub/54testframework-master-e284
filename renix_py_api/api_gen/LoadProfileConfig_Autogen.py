"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LoadProfileConfig(ROMObject):
    def __init__(self, LoadType=None, ToFirstIteration=None, Iteration=None, TimeBetweenIteration=None, MaxOutstandingCon=None, MaxConcurrentCon=None, MaxConnectionsAttempted=None, MaxTransactionsAttempted=None, **kwargs):
        self._LoadType = LoadType  # Load Type
        self._ToFirstIteration = ToFirstIteration  # Time To First Iteration(sec.)
        self._Iteration = Iteration  # Iterations
        self._TimeBetweenIteration = TimeBetweenIteration  # Time Between Iteration(sec.)
        self._MaxOutstandingCon = MaxOutstandingCon  # Max. Outstanding Connections
        self._MaxConcurrentCon = MaxConcurrentCon  # Max. Concurrent Connections
        self._MaxConnectionsAttempted = MaxConnectionsAttempted  # Max. Connections Attempted
        self._MaxTransactionsAttempted = MaxTransactionsAttempted  # Max. Transactions Attempted

        properties = kwargs.copy()
        if LoadType is not None:
            properties['LoadType'] = LoadType
        if ToFirstIteration is not None:
            properties['ToFirstIteration'] = ToFirstIteration
        if Iteration is not None:
            properties['Iteration'] = Iteration
        if TimeBetweenIteration is not None:
            properties['TimeBetweenIteration'] = TimeBetweenIteration
        if MaxOutstandingCon is not None:
            properties['MaxOutstandingCon'] = MaxOutstandingCon
        if MaxConcurrentCon is not None:
            properties['MaxConcurrentCon'] = MaxConcurrentCon
        if MaxConnectionsAttempted is not None:
            properties['MaxConnectionsAttempted'] = MaxConnectionsAttempted
        if MaxTransactionsAttempted is not None:
            properties['MaxTransactionsAttempted'] = MaxTransactionsAttempted

        # call base class function, and it will send message to renix server to create a class.
        super(LoadProfileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LoadType=None, ToFirstIteration=None, Iteration=None, TimeBetweenIteration=None, MaxOutstandingCon=None, MaxConcurrentCon=None, MaxConnectionsAttempted=None, MaxTransactionsAttempted=None, **kwargs):
        properties = kwargs.copy()
        if LoadType is not None:
            self._LoadType = LoadType
            properties['LoadType'] = LoadType
        if ToFirstIteration is not None:
            self._ToFirstIteration = ToFirstIteration
            properties['ToFirstIteration'] = ToFirstIteration
        if Iteration is not None:
            self._Iteration = Iteration
            properties['Iteration'] = Iteration
        if TimeBetweenIteration is not None:
            self._TimeBetweenIteration = TimeBetweenIteration
            properties['TimeBetweenIteration'] = TimeBetweenIteration
        if MaxOutstandingCon is not None:
            self._MaxOutstandingCon = MaxOutstandingCon
            properties['MaxOutstandingCon'] = MaxOutstandingCon
        if MaxConcurrentCon is not None:
            self._MaxConcurrentCon = MaxConcurrentCon
            properties['MaxConcurrentCon'] = MaxConcurrentCon
        if MaxConnectionsAttempted is not None:
            self._MaxConnectionsAttempted = MaxConnectionsAttempted
            properties['MaxConnectionsAttempted'] = MaxConnectionsAttempted
        if MaxTransactionsAttempted is not None:
            self._MaxTransactionsAttempted = MaxTransactionsAttempted
            properties['MaxTransactionsAttempted'] = MaxTransactionsAttempted

        super(LoadProfileConfig, self).edit(**properties)

    @property
    def LoadType(self):
        """
        get the value of property _LoadType
        """
        if self.force_auto_sync:
            self.get('LoadType')
        return self._LoadType

    @property
    def ToFirstIteration(self):
        """
        get the value of property _ToFirstIteration
        """
        if self.force_auto_sync:
            self.get('ToFirstIteration')
        return self._ToFirstIteration

    @property
    def Iteration(self):
        """
        get the value of property _Iteration
        """
        if self.force_auto_sync:
            self.get('Iteration')
        return self._Iteration

    @property
    def TimeBetweenIteration(self):
        """
        get the value of property _TimeBetweenIteration
        """
        if self.force_auto_sync:
            self.get('TimeBetweenIteration')
        return self._TimeBetweenIteration

    @property
    def MaxOutstandingCon(self):
        """
        get the value of property _MaxOutstandingCon
        """
        if self.force_auto_sync:
            self.get('MaxOutstandingCon')
        return self._MaxOutstandingCon

    @property
    def MaxConcurrentCon(self):
        """
        get the value of property _MaxConcurrentCon
        """
        if self.force_auto_sync:
            self.get('MaxConcurrentCon')
        return self._MaxConcurrentCon

    @property
    def MaxConnectionsAttempted(self):
        """
        get the value of property _MaxConnectionsAttempted
        """
        if self.force_auto_sync:
            self.get('MaxConnectionsAttempted')
        return self._MaxConnectionsAttempted

    @property
    def MaxTransactionsAttempted(self):
        """
        get the value of property _MaxTransactionsAttempted
        """
        if self.force_auto_sync:
            self.get('MaxTransactionsAttempted')
        return self._MaxTransactionsAttempted

    @LoadType.setter
    def LoadType(self, value):
        self._LoadType = value
        self.edit(LoadType=value)

    @ToFirstIteration.setter
    def ToFirstIteration(self, value):
        self._ToFirstIteration = value
        self.edit(ToFirstIteration=value)

    @Iteration.setter
    def Iteration(self, value):
        self._Iteration = value
        self.edit(Iteration=value)

    @TimeBetweenIteration.setter
    def TimeBetweenIteration(self, value):
        self._TimeBetweenIteration = value
        self.edit(TimeBetweenIteration=value)

    @MaxOutstandingCon.setter
    def MaxOutstandingCon(self, value):
        self._MaxOutstandingCon = value
        self.edit(MaxOutstandingCon=value)

    @MaxConcurrentCon.setter
    def MaxConcurrentCon(self, value):
        self._MaxConcurrentCon = value
        self.edit(MaxConcurrentCon=value)

    @MaxConnectionsAttempted.setter
    def MaxConnectionsAttempted(self, value):
        self._MaxConnectionsAttempted = value
        self.edit(MaxConnectionsAttempted=value)

    @MaxTransactionsAttempted.setter
    def MaxTransactionsAttempted(self, value):
        self._MaxTransactionsAttempted = value
        self.edit(MaxTransactionsAttempted=value)

    def _set_loadtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadType = EnumLoadType.%s' % value[:seperate])

    def _set_tofirstiteration_with_str(self, value):
        try:
            self._ToFirstIteration = int(value)
        except ValueError:
            self._ToFirstIteration = hex(int(value, 16))

    def _set_iteration_with_str(self, value):
        try:
            self._Iteration = int(value)
        except ValueError:
            self._Iteration = hex(int(value, 16))

    def _set_timebetweeniteration_with_str(self, value):
        try:
            self._TimeBetweenIteration = int(value)
        except ValueError:
            self._TimeBetweenIteration = hex(int(value, 16))

    def _set_maxoutstandingcon_with_str(self, value):
        try:
            self._MaxOutstandingCon = int(value)
        except ValueError:
            self._MaxOutstandingCon = hex(int(value, 16))

    def _set_maxconcurrentcon_with_str(self, value):
        try:
            self._MaxConcurrentCon = int(value)
        except ValueError:
            self._MaxConcurrentCon = hex(int(value, 16))

    def _set_maxconnectionsattempted_with_str(self, value):
        try:
            self._MaxConnectionsAttempted = int(value)
        except ValueError:
            self._MaxConnectionsAttempted = hex(int(value, 16))

    def _set_maxtransactionsattempted_with_str(self, value):
        try:
            self._MaxTransactionsAttempted = int(value)
        except ValueError:
            self._MaxTransactionsAttempted = hex(int(value, 16))

