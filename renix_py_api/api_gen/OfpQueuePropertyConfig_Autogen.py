"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpQueuePropertyConfig(ROMObject):
    def __init__(self, Type=None, Rate=None, ExperimenterID=None, ExperimenterData=None, **kwargs):
        self._Type = Type  # Type
        self._Rate = Rate  # Rate(1/1000)
        self._ExperimenterID = ExperimenterID  # Experimenter ID
        self._ExperimenterData = ExperimenterData  # Experimenter Data

        properties = kwargs.copy()
        if Type is not None:
            properties['Type'] = Type
        if Rate is not None:
            properties['Rate'] = Rate
        if ExperimenterID is not None:
            properties['ExperimenterID'] = ExperimenterID
        if ExperimenterData is not None:
            properties['ExperimenterData'] = ExperimenterData

        # call base class function, and it will send message to renix server to create a class.
        super(OfpQueuePropertyConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Type=None, Rate=None, ExperimenterID=None, ExperimenterData=None, **kwargs):
        properties = kwargs.copy()
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type
        if Rate is not None:
            self._Rate = Rate
            properties['Rate'] = Rate
        if ExperimenterID is not None:
            self._ExperimenterID = ExperimenterID
            properties['ExperimenterID'] = ExperimenterID
        if ExperimenterData is not None:
            self._ExperimenterData = ExperimenterData
            properties['ExperimenterData'] = ExperimenterData

        super(OfpQueuePropertyConfig, self).edit(**properties)

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @property
    def Rate(self):
        """
        get the value of property _Rate
        """
        if self.force_auto_sync:
            self.get('Rate')
        return self._Rate

    @property
    def ExperimenterID(self):
        """
        get the value of property _ExperimenterID
        """
        if self.force_auto_sync:
            self.get('ExperimenterID')
        return self._ExperimenterID

    @property
    def ExperimenterData(self):
        """
        get the value of property _ExperimenterData
        """
        if self.force_auto_sync:
            self.get('ExperimenterData')
        return self._ExperimenterData

    @Type.setter
    def Type(self, value):
        self._Type = value
        self.edit(Type=value)

    @Rate.setter
    def Rate(self, value):
        self._Rate = value
        self.edit(Rate=value)

    @ExperimenterID.setter
    def ExperimenterID(self, value):
        self._ExperimenterID = value
        self.edit(ExperimenterID=value)

    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._ExperimenterData = value
        self.edit(ExperimenterData=value)

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpQueue.%s' % value[:seperate])

    def _set_rate_with_str(self, value):
        try:
            self._Rate = int(value)
        except ValueError:
            self._Rate = hex(int(value, 16))

    def _set_experimenterid_with_str(self, value):
        try:
            self._ExperimenterID = int(value)
        except ValueError:
            self._ExperimenterID = hex(int(value, 16))

    def _set_experimenterdata_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ExperimenterData = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._ExperimenterData.append(int(str_value))
            except ValueError:
                self._ExperimenterData.append(hex(int(str_value, 16)))

