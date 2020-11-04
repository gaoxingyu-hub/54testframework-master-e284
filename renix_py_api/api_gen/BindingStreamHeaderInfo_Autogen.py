"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BindingStreamHeaderInfo(ROMObject):
    def __init__(self, L3forwarding=None, Direction=None, HeaderName=None, HeaderName1=None, EthHeaderName=None, UsingDestInterfaceMac=None, **kwargs):
        self._L3forwarding = L3forwarding  # Only used by L3 forwarding Ip Layer
        self._Direction = Direction  # Template String
        self._HeaderName = HeaderName  # binding to stream header Name
        self._HeaderName1 = HeaderName1  # binding to stream header1 Name
        self._EthHeaderName = EthHeaderName  # binding to stream Ether Header for dest ip layer use
        self._UsingDestInterfaceMac = UsingDestInterfaceMac  # For ip layer signal the bidirection is same network 

        properties = kwargs.copy()
        if L3forwarding is not None:
            properties['L3forwarding'] = L3forwarding
        if Direction is not None:
            properties['Direction'] = Direction
        if HeaderName is not None:
            properties['HeaderName'] = HeaderName
        if HeaderName1 is not None:
            properties['HeaderName1'] = HeaderName1
        if EthHeaderName is not None:
            properties['EthHeaderName'] = EthHeaderName
        if UsingDestInterfaceMac is not None:
            properties['UsingDestInterfaceMac'] = UsingDestInterfaceMac

        # call base class function, and it will send message to renix server to create a class.
        super(BindingStreamHeaderInfo, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, L3forwarding=None, Direction=None, HeaderName=None, HeaderName1=None, EthHeaderName=None, UsingDestInterfaceMac=None, **kwargs):
        properties = kwargs.copy()
        if L3forwarding is not None:
            self._L3forwarding = L3forwarding
            properties['L3forwarding'] = L3forwarding
        if Direction is not None:
            self._Direction = Direction
            properties['Direction'] = Direction
        if HeaderName is not None:
            self._HeaderName = HeaderName
            properties['HeaderName'] = HeaderName
        if HeaderName1 is not None:
            self._HeaderName1 = HeaderName1
            properties['HeaderName1'] = HeaderName1
        if EthHeaderName is not None:
            self._EthHeaderName = EthHeaderName
            properties['EthHeaderName'] = EthHeaderName
        if UsingDestInterfaceMac is not None:
            self._UsingDestInterfaceMac = UsingDestInterfaceMac
            properties['UsingDestInterfaceMac'] = UsingDestInterfaceMac

        super(BindingStreamHeaderInfo, self).edit(**properties)

    @property
    def L3forwarding(self):
        """
        get the value of property _L3forwarding
        """
        if self.force_auto_sync:
            self.get('L3forwarding')
        return self._L3forwarding

    @property
    def Direction(self):
        """
        get the value of property _Direction
        """
        if self.force_auto_sync:
            self.get('Direction')
        return self._Direction

    @property
    def HeaderName(self):
        """
        get the value of property _HeaderName
        """
        if self.force_auto_sync:
            self.get('HeaderName')
        return self._HeaderName

    @property
    def HeaderName1(self):
        """
        get the value of property _HeaderName1
        """
        if self.force_auto_sync:
            self.get('HeaderName1')
        return self._HeaderName1

    @property
    def EthHeaderName(self):
        """
        get the value of property _EthHeaderName
        """
        if self.force_auto_sync:
            self.get('EthHeaderName')
        return self._EthHeaderName

    @property
    def UsingDestInterfaceMac(self):
        """
        get the value of property _UsingDestInterfaceMac
        """
        if self.force_auto_sync:
            self.get('UsingDestInterfaceMac')
        return self._UsingDestInterfaceMac

    @L3forwarding.setter
    def L3forwarding(self, value):
        self._L3forwarding = value
        self.edit(L3forwarding=value)

    @Direction.setter
    def Direction(self, value):
        self._Direction = value
        self.edit(Direction=value)

    @HeaderName.setter
    def HeaderName(self, value):
        self._HeaderName = value
        self.edit(HeaderName=value)

    @HeaderName1.setter
    def HeaderName1(self, value):
        self._HeaderName1 = value
        self.edit(HeaderName1=value)

    @EthHeaderName.setter
    def EthHeaderName(self, value):
        self._EthHeaderName = value
        self.edit(EthHeaderName=value)

    @UsingDestInterfaceMac.setter
    def UsingDestInterfaceMac(self, value):
        self._UsingDestInterfaceMac = value
        self.edit(UsingDestInterfaceMac=value)

    def _set_l3forwarding_with_str(self, value):
        self._L3forwarding = (value == 'True')

    def _set_direction_with_str(self, value):
        self._Direction = value

    def _set_headername_with_str(self, value):
        self._HeaderName = value

    def _set_headername1_with_str(self, value):
        self._HeaderName1 = value

    def _set_ethheadername_with_str(self, value):
        self._EthHeaderName = value

    def _set_usingdestinterfacemac_with_str(self, value):
        self._UsingDestInterfaceMac = (value == 'True')

