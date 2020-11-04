"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BfdIpv4SessionConfig(ROMObject):
    def __init__(self, NumberOfSessions=None, StartDestinationAddress=None, DestinationAddressIncrement=None, EnableMyDiscriminator=None, MyDiscriminator=None, MyDiscriminatorIncrement=None, **kwargs):
        self._SourceAddress = '0.0.0.0'  # Source Address, not editable
        self._NumberOfSessions = NumberOfSessions  # Number of Sessions
        self._StartDestinationAddress = StartDestinationAddress  # Start Destination Address
        self._EndDestinationAddress = '192.0.1.0'  # End Destination Address, not editable
        self._DestinationAddressIncrement = DestinationAddressIncrement  # Destination Address Increment
        self._EnableMyDiscriminator = EnableMyDiscriminator  # Enable My Discriminator
        self._MyDiscriminator = MyDiscriminator  # My Discriminator
        self._MyDiscriminatorIncrement = MyDiscriminatorIncrement  # My Discriminator Increment

        properties = kwargs.copy()
        if NumberOfSessions is not None:
            properties['NumberOfSessions'] = NumberOfSessions
        if StartDestinationAddress is not None:
            properties['StartDestinationAddress'] = StartDestinationAddress
        if DestinationAddressIncrement is not None:
            properties['DestinationAddressIncrement'] = DestinationAddressIncrement
        if EnableMyDiscriminator is not None:
            properties['EnableMyDiscriminator'] = EnableMyDiscriminator
        if MyDiscriminator is not None:
            properties['MyDiscriminator'] = MyDiscriminator
        if MyDiscriminatorIncrement is not None:
            properties['MyDiscriminatorIncrement'] = MyDiscriminatorIncrement

        # call base class function, and it will send message to renix server to create a class.
        super(BfdIpv4SessionConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NumberOfSessions=None, StartDestinationAddress=None, DestinationAddressIncrement=None, EnableMyDiscriminator=None, MyDiscriminator=None, MyDiscriminatorIncrement=None, **kwargs):
        properties = kwargs.copy()
        if NumberOfSessions is not None:
            self._NumberOfSessions = NumberOfSessions
            properties['NumberOfSessions'] = NumberOfSessions
        if StartDestinationAddress is not None:
            self._StartDestinationAddress = StartDestinationAddress
            properties['StartDestinationAddress'] = StartDestinationAddress
        if DestinationAddressIncrement is not None:
            self._DestinationAddressIncrement = DestinationAddressIncrement
            properties['DestinationAddressIncrement'] = DestinationAddressIncrement
        if EnableMyDiscriminator is not None:
            self._EnableMyDiscriminator = EnableMyDiscriminator
            properties['EnableMyDiscriminator'] = EnableMyDiscriminator
        if MyDiscriminator is not None:
            self._MyDiscriminator = MyDiscriminator
            properties['MyDiscriminator'] = MyDiscriminator
        if MyDiscriminatorIncrement is not None:
            self._MyDiscriminatorIncrement = MyDiscriminatorIncrement
            properties['MyDiscriminatorIncrement'] = MyDiscriminatorIncrement

        super(BfdIpv4SessionConfig, self).edit(**properties)

    @property
    def SourceAddress(self):
        """
        get the value of property _SourceAddress
        """
        if self.force_auto_sync:
            self.get('SourceAddress')
        return self._SourceAddress

    @property
    def NumberOfSessions(self):
        """
        get the value of property _NumberOfSessions
        """
        if self.force_auto_sync:
            self.get('NumberOfSessions')
        return self._NumberOfSessions

    @property
    def StartDestinationAddress(self):
        """
        get the value of property _StartDestinationAddress
        """
        if self.force_auto_sync:
            self.get('StartDestinationAddress')
        return self._StartDestinationAddress

    @property
    def EndDestinationAddress(self):
        """
        get the value of property _EndDestinationAddress
        """
        if self.force_auto_sync:
            self.get('EndDestinationAddress')
        return self._EndDestinationAddress

    @property
    def DestinationAddressIncrement(self):
        """
        get the value of property _DestinationAddressIncrement
        """
        if self.force_auto_sync:
            self.get('DestinationAddressIncrement')
        return self._DestinationAddressIncrement

    @property
    def EnableMyDiscriminator(self):
        """
        get the value of property _EnableMyDiscriminator
        """
        if self.force_auto_sync:
            self.get('EnableMyDiscriminator')
        return self._EnableMyDiscriminator

    @property
    def MyDiscriminator(self):
        """
        get the value of property _MyDiscriminator
        """
        if self.force_auto_sync:
            self.get('MyDiscriminator')
        return self._MyDiscriminator

    @property
    def MyDiscriminatorIncrement(self):
        """
        get the value of property _MyDiscriminatorIncrement
        """
        if self.force_auto_sync:
            self.get('MyDiscriminatorIncrement')
        return self._MyDiscriminatorIncrement

    @NumberOfSessions.setter
    def NumberOfSessions(self, value):
        self._NumberOfSessions = value
        self.edit(NumberOfSessions=value)

    @StartDestinationAddress.setter
    def StartDestinationAddress(self, value):
        self._StartDestinationAddress = value
        self.edit(StartDestinationAddress=value)

    @DestinationAddressIncrement.setter
    def DestinationAddressIncrement(self, value):
        self._DestinationAddressIncrement = value
        self.edit(DestinationAddressIncrement=value)

    @EnableMyDiscriminator.setter
    def EnableMyDiscriminator(self, value):
        self._EnableMyDiscriminator = value
        self.edit(EnableMyDiscriminator=value)

    @MyDiscriminator.setter
    def MyDiscriminator(self, value):
        self._MyDiscriminator = value
        self.edit(MyDiscriminator=value)

    @MyDiscriminatorIncrement.setter
    def MyDiscriminatorIncrement(self, value):
        self._MyDiscriminatorIncrement = value
        self.edit(MyDiscriminatorIncrement=value)

    def _set_sourceaddress_with_str(self, value):
        self._SourceAddress = value

    def _set_numberofsessions_with_str(self, value):
        try:
            self._NumberOfSessions = int(value)
        except ValueError:
            self._NumberOfSessions = hex(int(value, 16))

    def _set_startdestinationaddress_with_str(self, value):
        self._StartDestinationAddress = value

    def _set_enddestinationaddress_with_str(self, value):
        self._EndDestinationAddress = value

    def _set_destinationaddressincrement_with_str(self, value):
        self._DestinationAddressIncrement = value

    def _set_enablemydiscriminator_with_str(self, value):
        self._EnableMyDiscriminator = (value == 'True')

    def _set_mydiscriminator_with_str(self, value):
        try:
            self._MyDiscriminator = int(value)
        except ValueError:
            self._MyDiscriminator = hex(int(value, 16))

    def _set_mydiscriminatorincrement_with_str(self, value):
        try:
            self._MyDiscriminatorIncrement = int(value)
        except ValueError:
            self._MyDiscriminatorIncrement = hex(int(value, 16))

