"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayer_Autogen import NetworkLayer


@rom_manager.rom
class EthIILayer(NetworkLayer):
    def __init__(self, Address=None, Step=None, AddressList=None, **kwargs):
        self._Address = Address  # Source MAC Address
        self._Step = Step  # Source MAC Address Step
        self._AddressList = AddressList  # Source MAC Address List

        properties = kwargs.copy()
        if Address is not None:
            properties['Address'] = Address
        if Step is not None:
            properties['Step'] = Step
        if AddressList is not None:
            properties['AddressList'] = AddressList

        # call base class function, and it will send message to renix server to create a class.
        super(EthIILayer, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Address=None, Step=None, AddressList=None, **kwargs):
        properties = kwargs.copy()
        if Address is not None:
            self._Address = Address
            properties['Address'] = Address
        if Step is not None:
            self._Step = Step
            properties['Step'] = Step
        if AddressList is not None:
            self._AddressList = AddressList
            properties['AddressList'] = AddressList

        super(EthIILayer, self).edit(**properties)

    @property
    def Address(self):
        """
        get the value of property _Address
        """
        if self.force_auto_sync:
            self.get('Address')
        return self._Address

    @property
    def Step(self):
        """
        get the value of property _Step
        """
        if self.force_auto_sync:
            self.get('Step')
        return self._Step

    @property
    def AddressList(self):
        """
        get the value of property _AddressList
        """
        if self.force_auto_sync:
            self.get('AddressList')
        return self._AddressList

    @Address.setter
    def Address(self, value):
        self._Address = value
        self.edit(Address=value)

    @Step.setter
    def Step(self, value):
        self._Step = value
        self.edit(Step=value)

    @AddressList.setter
    def AddressList(self, value):
        self._AddressList = value
        self.edit(AddressList=value)

    def _set_address_with_str(self, value):
        self._Address = value

    def _set_step_with_str(self, value):
        self._Step = value

    def _set_addresslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._AddressList = tmp_value.split()

