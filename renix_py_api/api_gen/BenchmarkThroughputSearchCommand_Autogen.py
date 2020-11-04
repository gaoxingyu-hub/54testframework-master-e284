"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BenchmarkThroughputSearchCommand(ROMCommand):
    def __init__(self, SearchMode=None, LowerBoundLimit=None, UpperBoundLimit=None, InitValue=None, Resolution=None, Backoff=None, ValueStep=None, AcceptableFrameLoss=None, IgnoreMinMaxLimit=None, CurrentLoad=None, **kwargs):
        self._SearchMode = SearchMode  # Traffic load search mode
        self._LowerBoundLimit = LowerBoundLimit  # Lowest Rate(%)
        self._UpperBoundLimit = UpperBoundLimit  # Uppermost Rate(%)
        self._InitValue = InitValue  # Initial Value
        self._Resolution = Resolution  # Resolution
        self._Backoff = Backoff  # Back Off
        self._ValueStep = ValueStep  # Step Value
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss(%)
        self._IgnoreMinMaxLimit = IgnoreMinMaxLimit  # Ignore Min and Max limit
        self._CurrentLoad = CurrentLoad  # Current Load(%)

        properties = kwargs.copy()
        if SearchMode is not None:
            properties['SearchMode'] = SearchMode
        if LowerBoundLimit is not None:
            properties['LowerBoundLimit'] = LowerBoundLimit
        if UpperBoundLimit is not None:
            properties['UpperBoundLimit'] = UpperBoundLimit
        if InitValue is not None:
            properties['InitValue'] = InitValue
        if Resolution is not None:
            properties['Resolution'] = Resolution
        if Backoff is not None:
            properties['Backoff'] = Backoff
        if ValueStep is not None:
            properties['ValueStep'] = ValueStep
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if IgnoreMinMaxLimit is not None:
            properties['IgnoreMinMaxLimit'] = IgnoreMinMaxLimit
        if CurrentLoad is not None:
            properties['CurrentLoad'] = CurrentLoad

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkThroughputSearchCommand, self).__init__(**properties)

    @property
    def SearchMode(self):
        """
        get the value of property _SearchMode
        """
        return self._SearchMode

    @property
    def LowerBoundLimit(self):
        """
        get the value of property _LowerBoundLimit
        """
        return self._LowerBoundLimit

    @property
    def UpperBoundLimit(self):
        """
        get the value of property _UpperBoundLimit
        """
        return self._UpperBoundLimit

    @property
    def InitValue(self):
        """
        get the value of property _InitValue
        """
        return self._InitValue

    @property
    def Resolution(self):
        """
        get the value of property _Resolution
        """
        return self._Resolution

    @property
    def Backoff(self):
        """
        get the value of property _Backoff
        """
        return self._Backoff

    @property
    def ValueStep(self):
        """
        get the value of property _ValueStep
        """
        return self._ValueStep

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        return self._AcceptableFrameLoss

    @property
    def IgnoreMinMaxLimit(self):
        """
        get the value of property _IgnoreMinMaxLimit
        """
        return self._IgnoreMinMaxLimit

    @property
    def CurrentLoad(self):
        """
        get the value of property _CurrentLoad
        """
        return self._CurrentLoad

    @SearchMode.setter
    def SearchMode(self, value):
        self._SearchMode = value

    @LowerBoundLimit.setter
    def LowerBoundLimit(self, value):
        self._LowerBoundLimit = value

    @UpperBoundLimit.setter
    def UpperBoundLimit(self, value):
        self._UpperBoundLimit = value

    @InitValue.setter
    def InitValue(self, value):
        self._InitValue = value

    @Resolution.setter
    def Resolution(self, value):
        self._Resolution = value

    @Backoff.setter
    def Backoff(self, value):
        self._Backoff = value

    @ValueStep.setter
    def ValueStep(self, value):
        self._ValueStep = value

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value

    @IgnoreMinMaxLimit.setter
    def IgnoreMinMaxLimit(self, value):
        self._IgnoreMinMaxLimit = value

    @CurrentLoad.setter
    def CurrentLoad(self, value):
        self._CurrentLoad = value

    def _set_searchmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SearchMode = EnumSearchMode.%s' % value[:seperate])

    def _set_lowerboundlimit_with_str(self, value):
        self._LowerBoundLimit = float(value)

    def _set_upperboundlimit_with_str(self, value):
        self._UpperBoundLimit = float(value)

    def _set_initvalue_with_str(self, value):
        self._InitValue = float(value)

    def _set_resolution_with_str(self, value):
        self._Resolution = float(value)

    def _set_backoff_with_str(self, value):
        self._Backoff = float(value)

    def _set_valuestep_with_str(self, value):
        self._ValueStep = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        self._AcceptableFrameLoss = float(value)

    def _set_ignoreminmaxlimit_with_str(self, value):
        self._IgnoreMinMaxLimit = (value == 'True')

    def _set_currentload_with_str(self, value):
        self._CurrentLoad = float(value)

