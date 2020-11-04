"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dot3ahOrgSpecConfig(ROMObject):
    def __init__(self, EnableOrgSpec=None, Period=None, OrgSpecOUI=None, Data=None, **kwargs):
        self._EnableOrgSpec = EnableOrgSpec  # Enable Organization Specific Event
        self._Period = Period  # Period (sec)
        self._OrgSpecOUI = OrgSpecOUI  # Organization Specific Event OUI
        self._Data = Data  # Organization Specific Data

        properties = kwargs.copy()
        if EnableOrgSpec is not None:
            properties['EnableOrgSpec'] = EnableOrgSpec
        if Period is not None:
            properties['Period'] = Period
        if OrgSpecOUI is not None:
            properties['OrgSpecOUI'] = OrgSpecOUI
        if Data is not None:
            properties['Data'] = Data

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahOrgSpecConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, EnableOrgSpec=None, Period=None, OrgSpecOUI=None, Data=None, **kwargs):
        properties = kwargs.copy()
        if EnableOrgSpec is not None:
            self._EnableOrgSpec = EnableOrgSpec
            properties['EnableOrgSpec'] = EnableOrgSpec
        if Period is not None:
            self._Period = Period
            properties['Period'] = Period
        if OrgSpecOUI is not None:
            self._OrgSpecOUI = OrgSpecOUI
            properties['OrgSpecOUI'] = OrgSpecOUI
        if Data is not None:
            self._Data = Data
            properties['Data'] = Data

        super(Dot3ahOrgSpecConfig, self).edit(**properties)

    @property
    def EnableOrgSpec(self):
        """
        get the value of property _EnableOrgSpec
        """
        if self.force_auto_sync:
            self.get('EnableOrgSpec')
        return self._EnableOrgSpec

    @property
    def Period(self):
        """
        get the value of property _Period
        """
        if self.force_auto_sync:
            self.get('Period')
        return self._Period

    @property
    def OrgSpecOUI(self):
        """
        get the value of property _OrgSpecOUI
        """
        if self.force_auto_sync:
            self.get('OrgSpecOUI')
        return self._OrgSpecOUI

    @property
    def Data(self):
        """
        get the value of property _Data
        """
        if self.force_auto_sync:
            self.get('Data')
        return self._Data

    @EnableOrgSpec.setter
    def EnableOrgSpec(self, value):
        self._EnableOrgSpec = value
        self.edit(EnableOrgSpec=value)

    @Period.setter
    def Period(self, value):
        self._Period = value
        self.edit(Period=value)

    @OrgSpecOUI.setter
    def OrgSpecOUI(self, value):
        self._OrgSpecOUI = value
        self.edit(OrgSpecOUI=value)

    @Data.setter
    def Data(self, value):
        self._Data = value
        self.edit(Data=value)

    def _set_enableorgspec_with_str(self, value):
        self._EnableOrgSpec = (value == 'True')

    def _set_period_with_str(self, value):
        try:
            self._Period = int(value)
        except ValueError:
            self._Period = hex(int(value, 16))

    def _set_orgspecoui_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OrgSpecOUI = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._OrgSpecOUI.append(int(str_value))
            except ValueError:
                self._OrgSpecOUI.append(hex(int(str_value, 16)))

    def _set_data_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Data = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._Data.append(int(str_value))
            except ValueError:
                self._Data.append(hex(int(str_value, 16)))

