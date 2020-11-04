"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateBindingStreamCommand(ROMCommand):
    def __init__(self, SrcEndpointHandles=None, DstEndpointHandles=None, Bidirection=None, Direction=None, TopLayerType=None, TrafficMeshMode=None, EndpointMapping=None, **kwargs):
        self._SrcEndpointHandles = SrcEndpointHandles  # Source Endpoints
        self._DstEndpointHandles = DstEndpointHandles  # Destination Endpoints
        self._BindingStreams = None  # Generated Bind StreamTemplate, not editable
        self._Bidirection = Bidirection  # Bidirection
        self._Direction = Direction  # Traffic Direction
        self._TopLayerType = TopLayerType  # Traffic Top Layer Type
        self._TrafficMeshMode = TrafficMeshMode  # Traffic Mode
        self._EndpointMapping = EndpointMapping  # Endpoint Mapping

        properties = kwargs.copy()
        if SrcEndpointHandles is not None:
            properties['SrcEndpointHandles'] = SrcEndpointHandles
        if DstEndpointHandles is not None:
            properties['DstEndpointHandles'] = DstEndpointHandles
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

        # call base class function, and it will send message to renix server to create a class.
        super(CreateBindingStreamCommand, self).__init__(**properties)

    @property
    def SrcEndpointHandles(self):
        """
        get the value of property _SrcEndpointHandles
        """
        return self._SrcEndpointHandles

    @property
    def DstEndpointHandles(self):
        """
        get the value of property _DstEndpointHandles
        """
        return self._DstEndpointHandles

    @property
    def BindingStreams(self):
        """
        get the value of property _BindingStreams
        """
        return self._BindingStreams

    @property
    def Bidirection(self):
        """
        get the value of property _Bidirection
        """
        return self._Bidirection

    @property
    def Direction(self):
        """
        get the value of property _Direction
        """
        return self._Direction

    @property
    def TopLayerType(self):
        """
        get the value of property _TopLayerType
        """
        return self._TopLayerType

    @property
    def TrafficMeshMode(self):
        """
        get the value of property _TrafficMeshMode
        """
        return self._TrafficMeshMode

    @property
    def EndpointMapping(self):
        """
        get the value of property _EndpointMapping
        """
        return self._EndpointMapping

    @SrcEndpointHandles.setter
    def SrcEndpointHandles(self, value):
        self._SrcEndpointHandles = value

    @DstEndpointHandles.setter
    def DstEndpointHandles(self, value):
        self._DstEndpointHandles = value

    @Bidirection.setter
    def Bidirection(self, value):
        self._Bidirection = value

    @Direction.setter
    def Direction(self, value):
        self._Direction = value

    @TopLayerType.setter
    def TopLayerType(self, value):
        self._TopLayerType = value

    @TrafficMeshMode.setter
    def TrafficMeshMode(self, value):
        self._TrafficMeshMode = value

    @EndpointMapping.setter
    def EndpointMapping(self, value):
        self._EndpointMapping = value

    def _set_srcendpointhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SrcEndpointHandles = tmp_value.split()

    def _set_dstendpointhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DstEndpointHandles = tmp_value.split()

    def _set_bindingstreams_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BindingStreams = tmp_value.split()

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

    def _set_output_property(self, value):
        self._set_bindingstreams_with_str(value)

