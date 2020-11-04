"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpActionConfig(ROMObject):
    def __init__(self, Type=None, PortNumber=None, ControllerMaxLength=None, GroupID=None, QueueID=None, TTL=None, Ethertype=None, FieldType=None, FieldValue=None, ExperimenterID=None, **kwargs):
        self._Type = Type  # Type
        self._PortNumber = PortNumber  # Port Number
        self._ControllerMaxLength = ControllerMaxLength  # Controller Max Length
        self._GroupID = GroupID  # Group ID
        self._QueueID = QueueID  # Queue ID
        self._TTL = TTL  # TTL
        self._Ethertype = Ethertype  # TTL
        self._FieldType = FieldType  # Field Type
        self._FieldValue = FieldValue  # Field Value
        self._ExperimenterID = ExperimenterID  # Experimenter ID

        properties = kwargs.copy()
        if Type is not None:
            properties['Type'] = Type
        if PortNumber is not None:
            properties['PortNumber'] = PortNumber
        if ControllerMaxLength is not None:
            properties['ControllerMaxLength'] = ControllerMaxLength
        if GroupID is not None:
            properties['GroupID'] = GroupID
        if QueueID is not None:
            properties['QueueID'] = QueueID
        if TTL is not None:
            properties['TTL'] = TTL
        if Ethertype is not None:
            properties['Ethertype'] = Ethertype
        if FieldType is not None:
            properties['FieldType'] = FieldType
        if FieldValue is not None:
            properties['FieldValue'] = FieldValue
        if ExperimenterID is not None:
            properties['ExperimenterID'] = ExperimenterID

        # call base class function, and it will send message to renix server to create a class.
        super(OfpActionConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Type=None, PortNumber=None, ControllerMaxLength=None, GroupID=None, QueueID=None, TTL=None, Ethertype=None, FieldType=None, FieldValue=None, ExperimenterID=None, **kwargs):
        properties = kwargs.copy()
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type
        if PortNumber is not None:
            self._PortNumber = PortNumber
            properties['PortNumber'] = PortNumber
        if ControllerMaxLength is not None:
            self._ControllerMaxLength = ControllerMaxLength
            properties['ControllerMaxLength'] = ControllerMaxLength
        if GroupID is not None:
            self._GroupID = GroupID
            properties['GroupID'] = GroupID
        if QueueID is not None:
            self._QueueID = QueueID
            properties['QueueID'] = QueueID
        if TTL is not None:
            self._TTL = TTL
            properties['TTL'] = TTL
        if Ethertype is not None:
            self._Ethertype = Ethertype
            properties['Ethertype'] = Ethertype
        if FieldType is not None:
            self._FieldType = FieldType
            properties['FieldType'] = FieldType
        if FieldValue is not None:
            self._FieldValue = FieldValue
            properties['FieldValue'] = FieldValue
        if ExperimenterID is not None:
            self._ExperimenterID = ExperimenterID
            properties['ExperimenterID'] = ExperimenterID

        super(OfpActionConfig, self).edit(**properties)

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @property
    def PortNumber(self):
        """
        get the value of property _PortNumber
        """
        if self.force_auto_sync:
            self.get('PortNumber')
        return self._PortNumber

    @property
    def ControllerMaxLength(self):
        """
        get the value of property _ControllerMaxLength
        """
        if self.force_auto_sync:
            self.get('ControllerMaxLength')
        return self._ControllerMaxLength

    @property
    def GroupID(self):
        """
        get the value of property _GroupID
        """
        if self.force_auto_sync:
            self.get('GroupID')
        return self._GroupID

    @property
    def QueueID(self):
        """
        get the value of property _QueueID
        """
        if self.force_auto_sync:
            self.get('QueueID')
        return self._QueueID

    @property
    def TTL(self):
        """
        get the value of property _TTL
        """
        if self.force_auto_sync:
            self.get('TTL')
        return self._TTL

    @property
    def Ethertype(self):
        """
        get the value of property _Ethertype
        """
        if self.force_auto_sync:
            self.get('Ethertype')
        return self._Ethertype

    @property
    def FieldType(self):
        """
        get the value of property _FieldType
        """
        if self.force_auto_sync:
            self.get('FieldType')
        return self._FieldType

    @property
    def FieldValue(self):
        """
        get the value of property _FieldValue
        """
        if self.force_auto_sync:
            self.get('FieldValue')
        return self._FieldValue

    @property
    def ExperimenterID(self):
        """
        get the value of property _ExperimenterID
        """
        if self.force_auto_sync:
            self.get('ExperimenterID')
        return self._ExperimenterID

    @Type.setter
    def Type(self, value):
        self._Type = value
        self.edit(Type=value)

    @PortNumber.setter
    def PortNumber(self, value):
        self._PortNumber = value
        self.edit(PortNumber=value)

    @ControllerMaxLength.setter
    def ControllerMaxLength(self, value):
        self._ControllerMaxLength = value
        self.edit(ControllerMaxLength=value)

    @GroupID.setter
    def GroupID(self, value):
        self._GroupID = value
        self.edit(GroupID=value)

    @QueueID.setter
    def QueueID(self, value):
        self._QueueID = value
        self.edit(QueueID=value)

    @TTL.setter
    def TTL(self, value):
        self._TTL = value
        self.edit(TTL=value)

    @Ethertype.setter
    def Ethertype(self, value):
        self._Ethertype = value
        self.edit(Ethertype=value)

    @FieldType.setter
    def FieldType(self, value):
        self._FieldType = value
        self.edit(FieldType=value)

    @FieldValue.setter
    def FieldValue(self, value):
        self._FieldValue = value
        self.edit(FieldValue=value)

    @ExperimenterID.setter
    def ExperimenterID(self, value):
        self._ExperimenterID = value
        self.edit(ExperimenterID=value)

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpAction.%s' % value[:seperate])

    def _set_portnumber_with_str(self, value):
        try:
            self._PortNumber = int(value)
        except ValueError:
            self._PortNumber = hex(int(value, 16))

    def _set_controllermaxlength_with_str(self, value):
        try:
            self._ControllerMaxLength = int(value)
        except ValueError:
            self._ControllerMaxLength = hex(int(value, 16))

    def _set_groupid_with_str(self, value):
        try:
            self._GroupID = int(value)
        except ValueError:
            self._GroupID = hex(int(value, 16))

    def _set_queueid_with_str(self, value):
        try:
            self._QueueID = int(value)
        except ValueError:
            self._QueueID = hex(int(value, 16))

    def _set_ttl_with_str(self, value):
        try:
            self._TTL = int(value)
        except ValueError:
            self._TTL = hex(int(value, 16))

    def _set_ethertype_with_str(self, value):
        try:
            self._Ethertype = int(value)
        except ValueError:
            self._Ethertype = hex(int(value, 16))

    def _set_fieldtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FieldType = EnumOfpField.%s' % value[:seperate])

    def _set_fieldvalue_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FieldValue = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._FieldValue.append(int(str_value))
            except ValueError:
                self._FieldValue.append(hex(int(str_value, 16)))

    def _set_experimenterid_with_str(self, value):
        try:
            self._ExperimenterID = int(value)
        except ValueError:
            self._ExperimenterID = hex(int(value, 16))

