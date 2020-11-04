"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2889AddressLearningWriteDbCommand_Autogen import Rfc2889AddressLearningWriteDbCommand


@rom_manager.rom
class AddressLearningRateWriteDbCommand(Rfc2889AddressLearningWriteDbCommand):
    def __init__(self, NumberOfAddresses=None, **kwargs):
        self._NumberOfAddresses = NumberOfAddresses  # Number Of Addresses

        properties = kwargs.copy()
        if NumberOfAddresses is not None:
            properties['NumberOfAddresses'] = NumberOfAddresses

        # call base class function, and it will send message to renix server to create a class.
        super(AddressLearningRateWriteDbCommand, self).__init__(**properties)

    @property
    def NumberOfAddresses(self):
        """
        get the value of property _NumberOfAddresses
        """
        return self._NumberOfAddresses

    @NumberOfAddresses.setter
    def NumberOfAddresses(self, value):
        self._NumberOfAddresses = value

    def _set_numberofaddresses_with_str(self, value):
        try:
            self._NumberOfAddresses = int(value)
        except ValueError:
            self._NumberOfAddresses = hex(int(value, 16))

