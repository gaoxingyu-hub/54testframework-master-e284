"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrafficItem(ROMObject):
    def __init__(self, Bidirection=None, Direction=None, TopLayerType=None, TrafficMeshMode=None, EndpointMapping=None, StreamCreation=None, AllowSendingToSelf=None, **kwargs):
        self._Bidirection = Bidirection  # Bidirection
        self._Direction = Direction  # Traffic Direction
        self._TopLayerType = TopLayerType  # Traffic Top Layer Type
        self._TrafficMeshMode = TrafficMeshMode  # Traffic Mode
        self._EndpointMapping = EndpointMapping  # Traffic Mode
        self._StreamCreation = StreamCreation  # Endpoint New Strems
        self._AllowSendingToSelf = AllowSendingToSelf  # Allow Sending Traffic To Self

        properties = kwargs.copy()
        if Bidirection is not None:
            properties['Bidirection'] = Bidirection
        if Direction is not None:
            properties['Direction'] = Direction
        if TopLayerType is not None:
            properties['TopLayerType'] = TopLayerType
        if TrafficMeshMode is not None:
            properties['TrafficMeshMode'] = TrafficMeshMode
        if EndpointMapping is not None:
            properties['EndpointMapping'] = EndpointMapping
        if StreamCreation is not None:
            properties['StreamCreation'] = StreamCreation
        if AllowSendingToSelf is not None:
            properties['AllowSendingToSelf'] = AllowSendingToSelf

        # call base class function, and it will send message to renix server to create a class.
        super(TrafficItem, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Bidirection=None, Direction=None, TopLayerType=None, TrafficMeshMode=None, EndpointMapping=None, StreamCreation=None, AllowSendingToSelf=None, **kwargs):
        properties = kwargs.copy()
        if Bidirection is not None:
            self._Bidirection = Bidirection
            properties['Bidirection'] = Bidirection
        if Direction is not None:
            self._Direction = Direction
            properties['Direction'] = Direction
        if TopLayerType is not None:
            self._TopLayerType = TopLayerType
            properties['TopLayerType'] = TopLayerType
        if TrafficMeshMode is not None:
            self._TrafficMeshMode = TrafficMeshMode
            properties['TrafficMeshMode'] = TrafficMeshMode
        if EndpointMapping is not None:
            self._EndpointMapping = EndpointMapping
            properties['EndpointMapping'] = EndpointMapping
        if StreamCreation is not None:
            self._StreamCreation = StreamCreation
            properties['StreamCreation'] = StreamCreation
        if AllowSendingToSelf is not None:
            self._AllowSendingToSelf = AllowSendingToSelf
            properties['AllowSendingToSelf'] = AllowSendingToSelf

        super(TrafficItem, self).edit(**properties)

    @property
    def Bidirection(self):
        """
        get the value of property _Bidirection
        """
        if self.force_auto_sync:
            self.get('Bidirection')
        return self._Bidirection

    @property
    def Direction(self):
        """
        get the value of property _Direction
        """
        if self.force_auto_sync:
            self.get('Direction')
        return self._Direction

    @property
    def TopLayerType(self):
        """
        get the value of property _TopLayerType
        """
        if self.force_auto_sync:
            self.get('TopLayerType')
        return self._TopLayerType

    @property
    def TrafficMeshMode(self):
        """
        get the value of property _TrafficMeshMode
        """
        if self.force_auto_sync:
            self.get('TrafficMeshMode')
        return self._TrafficMeshMode

    @property
    def EndpointMapping(self):
        """
        get the value of property _EndpointMapping
        """
        if self.force_auto_sync:
            self.get('EndpointMapping')
        return self._EndpointMapping

    @property
    def StreamCreation(self):
        """
        get the value of property _StreamCreation
        """
        if self.force_auto_sync:
            self.get('StreamCreation')
        return self._StreamCreation

    @property
    def AllowSendingToSelf(self):
        """
        get the value of property _AllowSendingToSelf
        """
        if self.force_auto_sync:
            self.get('AllowSendingToSelf')
        return self._AllowSendingToSelf

    @Bidirection.setter
    def Bidirection(self, value):
        self._Bidirection = value
        self.edit(Bidirection=value)

    @Direction.setter
    def Direction(self, value):
        self._Direction = value
        self.edit(Direction=value)

    @TopLayerType.setter
    def TopLayerType(self, value):
        self._TopLayerType = value
        self.edit(TopLayerType=value)

    @TrafficMeshMode.setter
    def TrafficMeshMode(self, value):
        self._TrafficMeshMode = value
        self.edit(TrafficMeshMode=value)

    @EndpointMapping.setter
    def EndpointMapping(self, value):
        self._EndpointMapping = value
        self.edit(EndpointMapping=value)

    @StreamCreation.setter
    def StreamCreation(self, value):
        self._StreamCreation = value
        self.edit(StreamCreation=value)

    @AllowSendingToSelf.setter
    def AllowSendingToSelf(self, value):
        self._AllowSendingToSelf = value
        self.edit(AllowSendingToSelf=value)

    def _set_bidirection_with_str(self, value):
        self._Bidirection = (value == 'True')

    def _set_direction_with_str(self, value):
        seperate = value.find(':')
        exec('self._Direction = EnumTrafficDirection.%s' % value[:seperate])

    def _set_toplayertype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TopLayerType = EnumTrafficType.%s' % value[:seperate])

    def _set_trafficmeshmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficMeshMode = EnumTrafficMesh.%s' % value[:seperate])

    def _set_endpointmapping_with_str(self, value):
        seperate = value.find(':')
        exec('self._EndpointMapping = EnumEndpointMapping.%s' % value[:seperate])

    def _set_streamcreation_with_str(self, value):
        seperate = value.find(':')
        exec('self._StreamCreation = EnumStreamCreation.%s' % value[:seperate])

    def _set_allowsendingtoself_with_str(self, value):
        self._AllowSendingToSelf = (value == 'True')

