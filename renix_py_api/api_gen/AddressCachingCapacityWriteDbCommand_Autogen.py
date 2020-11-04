"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889AddressLearningWriteDbCommand_Autogen import Rfc2889AddressLearningWriteDbCommand


@rom_manager.rom
class AddressCachingCapacityWriteDbCommand(Rfc2889AddressLearningWriteDbCommand):
    def __init__(self, LearnRate=None, **kwargs):
        self._LearnRate = LearnRate  # Learning Rate (frames/sec)

        properties = kwargs.copy()
        if LearnRate is not None:
            properties['LearnRate'] = LearnRate

        # call base class function, and it will send message to renix server to create a class.
        super(AddressCachingCapacityWriteDbCommand, self).__init__(**properties)

    @property
    def LearnRate(self):
        """
        get the value of property _LearnRate
        """
        return self._LearnRate

    @LearnRate.setter
    def LearnRate(self, value):
        self._LearnRate = value

    def _set_learnrate_with_str(self, value):
        try:
            self._LearnRate = int(value)
        except ValueError:
            self._LearnRate = hex(int(value, 16))

