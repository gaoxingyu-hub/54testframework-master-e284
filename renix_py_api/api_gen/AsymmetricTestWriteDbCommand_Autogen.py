"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Rfc2544WriteDbCommand_Autogen import Rfc2544WriteDbCommand


@rom_manager.rom
class AsymmetricTestWriteDbCommand(Rfc2544WriteDbCommand):
    def __init__(self, ProfileAllocation=None, **kwargs):
        self._ProfileAllocation = ProfileAllocation  # Profile Allocation

        properties = kwargs.copy()
        if ProfileAllocation is not None:
            properties['ProfileAllocation'] = ProfileAllocation

        # call base class function, and it will send message to renix server to create a class.
        super(AsymmetricTestWriteDbCommand, self).__init__(**properties)

    @property
    def ProfileAllocation(self):
        """
        get the value of property _ProfileAllocation
        """
        return self._ProfileAllocation

    @ProfileAllocation.setter
    def ProfileAllocation(self, value):
        self._ProfileAllocation = value

    def _set_profileallocation_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProfileAllocation = EnumProfileAllocation.%s' % value[:seperate])

