"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpInstructionConfig(ROMObject):
    def __init__(self, Type=None, FlowTableID=None, Metadata=None, MetadataMask=None, MeterID=None, ExperimenterID=None, **kwargs):
        self._Type = Type  # Type
        self._FlowTableID = FlowTableID  # Flow Table ID
        self._Metadata = Metadata  # Metadata
        self._MetadataMask = MetadataMask  # Metadata Mask
        self._MeterID = MeterID  # Meter Table ID
        self._ExperimenterID = ExperimenterID  # Experimenter ID

        properties = kwargs.copy()
        if Type is not None:
            properties['Type'] = Type
        if FlowTableID is not None:
            properties['FlowTableID'] = FlowTableID
        if Metadata is not None:
            properties['Metadata'] = Metadata
        if MetadataMask is not None:
            properties['MetadataMask'] = MetadataMask
        if MeterID is not None:
            properties['MeterID'] = MeterID
        if ExperimenterID is not None:
            properties['ExperimenterID'] = ExperimenterID

        # call base class function, and it will send message to renix server to create a class.
        super(OfpInstructionConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Type=None, FlowTableID=None, Metadata=None, MetadataMask=None, MeterID=None, ExperimenterID=None, **kwargs):
        properties = kwargs.copy()
        if Type is not None:
            self._Type = Type
            properties['Type'] = Type
        if FlowTableID is not None:
            self._FlowTableID = FlowTableID
            properties['FlowTableID'] = FlowTableID
        if Metadata is not None:
            self._Metadata = Metadata
            properties['Metadata'] = Metadata
        if MetadataMask is not None:
            self._MetadataMask = MetadataMask
            properties['MetadataMask'] = MetadataMask
        if MeterID is not None:
            self._MeterID = MeterID
            properties['MeterID'] = MeterID
        if ExperimenterID is not None:
            self._ExperimenterID = ExperimenterID
            properties['ExperimenterID'] = ExperimenterID

        super(OfpInstructionConfig, self).edit(**properties)

    @property
    def Type(self):
        """
        get the value of property _Type
        """
        if self.force_auto_sync:
            self.get('Type')
        return self._Type

    @property
    def FlowTableID(self):
        """
        get the value of property _FlowTableID
        """
        if self.force_auto_sync:
            self.get('FlowTableID')
        return self._FlowTableID

    @property
    def Metadata(self):
        """
        get the value of property _Metadata
        """
        if self.force_auto_sync:
            self.get('Metadata')
        return self._Metadata

    @property
    def MetadataMask(self):
        """
        get the value of property _MetadataMask
        """
        if self.force_auto_sync:
            self.get('MetadataMask')
        return self._MetadataMask

    @property
    def MeterID(self):
        """
        get the value of property _MeterID
        """
        if self.force_auto_sync:
            self.get('MeterID')
        return self._MeterID

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

    @FlowTableID.setter
    def FlowTableID(self, value):
        self._FlowTableID = value
        self.edit(FlowTableID=value)

    @Metadata.setter
    def Metadata(self, value):
        self._Metadata = value
        self.edit(Metadata=value)

    @MetadataMask.setter
    def MetadataMask(self, value):
        self._MetadataMask = value
        self.edit(MetadataMask=value)

    @MeterID.setter
    def MeterID(self, value):
        self._MeterID = value
        self.edit(MeterID=value)

    @ExperimenterID.setter
    def ExperimenterID(self, value):
        self._ExperimenterID = value
        self.edit(ExperimenterID=value)

    def _set_type_with_str(self, value):
        seperate = value.find(':')
        exec('self._Type = EnumOfpInstruction.%s' % value[:seperate])

    def _set_flowtableid_with_str(self, value):
        try:
            self._FlowTableID = int(value)
        except ValueError:
            self._FlowTableID = hex(int(value, 16))

    def _set_metadata_with_str(self, value):
        try:
            self._Metadata = int(value)
        except ValueError:
            self._Metadata = hex(int(value, 16))

    def _set_metadatamask_with_str(self, value):
        try:
            self._MetadataMask = int(value)
        except ValueError:
            self._MetadataMask = hex(int(value, 16))

    def _set_meterid_with_str(self, value):
        try:
            self._MeterID = int(value)
        except ValueError:
            self._MeterID = hex(int(value, 16))

    def _set_experimenterid_with_str(self, value):
        try:
            self._ExperimenterID = int(value)
        except ValueError:
            self._ExperimenterID = hex(int(value, 16))

