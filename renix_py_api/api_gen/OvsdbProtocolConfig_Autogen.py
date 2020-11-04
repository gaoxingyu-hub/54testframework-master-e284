"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class OvsdbProtocolConfig(L23ProtocolConfig):
    def __init__(self, OvsdbControllerIpList=None, OvsdbContents=None, **kwargs):
        self._OvsdbState = EnumOvsdbState.STOPPED  # OVSDB State, not editable
        self._OvsdbControllerIpList = OvsdbControllerIpList  # OVSDB Controller IP List
        self._OvsdbConnectionPort = 6640  # OVSDB Connection Port, not editable
        self._OvsdbContents = OvsdbContents  # 

        properties = kwargs.copy()
        if OvsdbControllerIpList is not None:
            properties['OvsdbControllerIpList'] = OvsdbControllerIpList
        if OvsdbContents is not None:
            properties['OvsdbContents'] = OvsdbContents

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OvsdbControllerIpList=None, OvsdbContents=None, **kwargs):
        properties = kwargs.copy()
        if OvsdbControllerIpList is not None:
            self._OvsdbControllerIpList = OvsdbControllerIpList
            properties['OvsdbControllerIpList'] = OvsdbControllerIpList
        if OvsdbContents is not None:
            self._OvsdbContents = OvsdbContents
            properties['OvsdbContents'] = OvsdbContents

        super(OvsdbProtocolConfig, self).edit(**properties)

    @property
    def OvsdbState(self):
        """
        get the value of property _OvsdbState
        """
        if self.force_auto_sync:
            self.get('OvsdbState')
        return self._OvsdbState

    @property
    def OvsdbControllerIpList(self):
        """
        get the value of property _OvsdbControllerIpList
        """
        if self.force_auto_sync:
            self.get('OvsdbControllerIpList')
        return self._OvsdbControllerIpList

    @property
    def OvsdbConnectionPort(self):
        """
        get the value of property _OvsdbConnectionPort
        """
        if self.force_auto_sync:
            self.get('OvsdbConnectionPort')
        return self._OvsdbConnectionPort

    @property
    def OvsdbContents(self):
        """
        get the value of property _OvsdbContents
        """
        if self.force_auto_sync:
            self.get('OvsdbContents')
        return self._OvsdbContents

    @OvsdbControllerIpList.setter
    def OvsdbControllerIpList(self, value):
        self._OvsdbControllerIpList = value
        self.edit(OvsdbControllerIpList=value)

    @OvsdbContents.setter
    def OvsdbContents(self, value):
        self._OvsdbContents = value
        self.edit(OvsdbContents=value)

    def _set_ovsdbstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbState = EnumOvsdbState.%s' % value[:seperate])

    def _set_ovsdbcontrolleriplist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OvsdbControllerIpList = tmp_value.split()

    def _set_ovsdbconnectionport_with_str(self, value):
        try:
            self._OvsdbConnectionPort = int(value)
        except ValueError:
            self._OvsdbConnectionPort = hex(int(value, 16))

    def _set_ovsdbcontents_with_str(self, value):
        self._OvsdbContents = value

