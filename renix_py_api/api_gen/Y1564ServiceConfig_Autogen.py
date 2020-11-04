"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Y1564ServiceConfig(ROMObject):
    def __init__(self, TrafficType=None, StreamTemplateHandles=None, LoadUnit=None, FrameSize=None, Cir=None, CirTolerance=None, Eir=None, Cbs=None, Ebs=None, FrameDelay=None, FrameDelayTolerance=None, FrameDelayVariation=None, FrameDelayVariationTolerance=None, FrameLossRatio=None, AcceptableFrameLoss=None, ProfileType=None, MeshType=None, **kwargs):
        self._TrafficType = TrafficType  # Traffic Type
        self._StreamTemplateHandles = StreamTemplateHandles  # StreamTemplate Handles
        self._LoadUnit = LoadUnit  # Load Unit
        self._FrameSize = FrameSize  # Frame Size
        self._Cir = Cir  # CIR
        self._CirTolerance = CirTolerance  # CIR Tolerance (%)
        self._Eir = Eir  # EIR
        self._Cbs = Cbs  # CBS (byte)
        self._Ebs = Ebs  # EBS (byte)
        self._FrameDelay = FrameDelay  # Frame Delay (ns)
        self._FrameDelayTolerance = FrameDelayTolerance  # FD Tolerance (%)
        self._FrameDelayVariation = FrameDelayVariation  # Frame Delay Variation (ns)
        self._FrameDelayVariationTolerance = FrameDelayVariationTolerance  # FDV Tolerance (%)
        self._FrameLossRatio = FrameLossRatio  # Frame Loss Ratio (%)
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss
        self._ProfileType = ProfileType  # Profile Type
        self._MeshType = MeshType  # Mesh Type

        properties = kwargs.copy()
        if TrafficType is not None:
            properties['TrafficType'] = TrafficType
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if LoadUnit is not None:
            properties['LoadUnit'] = LoadUnit
        if FrameSize is not None:
            properties['FrameSize'] = FrameSize
        if Cir is not None:
            properties['Cir'] = Cir
        if CirTolerance is not None:
            properties['CirTolerance'] = CirTolerance
        if Eir is not None:
            properties['Eir'] = Eir
        if Cbs is not None:
            properties['Cbs'] = Cbs
        if Ebs is not None:
            properties['Ebs'] = Ebs
        if FrameDelay is not None:
            properties['FrameDelay'] = FrameDelay
        if FrameDelayTolerance is not None:
            properties['FrameDelayTolerance'] = FrameDelayTolerance
        if FrameDelayVariation is not None:
            properties['FrameDelayVariation'] = FrameDelayVariation
        if FrameDelayVariationTolerance is not None:
            properties['FrameDelayVariationTolerance'] = FrameDelayVariationTolerance
        if FrameLossRatio is not None:
            properties['FrameLossRatio'] = FrameLossRatio
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if ProfileType is not None:
            properties['ProfileType'] = ProfileType
        if MeshType is not None:
            properties['MeshType'] = MeshType

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564ServiceConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TrafficType=None, StreamTemplateHandles=None, LoadUnit=None, FrameSize=None, Cir=None, CirTolerance=None, Eir=None, Cbs=None, Ebs=None, FrameDelay=None, FrameDelayTolerance=None, FrameDelayVariation=None, FrameDelayVariationTolerance=None, FrameLossRatio=None, AcceptableFrameLoss=None, ProfileType=None, MeshType=None, **kwargs):
        properties = kwargs.copy()
        if TrafficType is not None:
            self._TrafficType = TrafficType
            properties['TrafficType'] = TrafficType
        if StreamTemplateHandles is not None:
            self._StreamTemplateHandles = StreamTemplateHandles
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if LoadUnit is not None:
            self._LoadUnit = LoadUnit
            properties['LoadUnit'] = LoadUnit
        if FrameSize is not None:
            self._FrameSize = FrameSize
            properties['FrameSize'] = FrameSize
        if Cir is not None:
            self._Cir = Cir
            properties['Cir'] = Cir
        if CirTolerance is not None:
            self._CirTolerance = CirTolerance
            properties['CirTolerance'] = CirTolerance
        if Eir is not None:
            self._Eir = Eir
            properties['Eir'] = Eir
        if Cbs is not None:
            self._Cbs = Cbs
            properties['Cbs'] = Cbs
        if Ebs is not None:
            self._Ebs = Ebs
            properties['Ebs'] = Ebs
        if FrameDelay is not None:
            self._FrameDelay = FrameDelay
            properties['FrameDelay'] = FrameDelay
        if FrameDelayTolerance is not None:
            self._FrameDelayTolerance = FrameDelayTolerance
            properties['FrameDelayTolerance'] = FrameDelayTolerance
        if FrameDelayVariation is not None:
            self._FrameDelayVariation = FrameDelayVariation
            properties['FrameDelayVariation'] = FrameDelayVariation
        if FrameDelayVariationTolerance is not None:
            self._FrameDelayVariationTolerance = FrameDelayVariationTolerance
            properties['FrameDelayVariationTolerance'] = FrameDelayVariationTolerance
        if FrameLossRatio is not None:
            self._FrameLossRatio = FrameLossRatio
            properties['FrameLossRatio'] = FrameLossRatio
        if AcceptableFrameLoss is not None:
            self._AcceptableFrameLoss = AcceptableFrameLoss
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if ProfileType is not None:
            self._ProfileType = ProfileType
            properties['ProfileType'] = ProfileType
        if MeshType is not None:
            self._MeshType = MeshType
            properties['MeshType'] = MeshType

        super(Y1564ServiceConfig, self).edit(**properties)

    @property
    def TrafficType(self):
        """
        get the value of property _TrafficType
        """
        if self.force_auto_sync:
            self.get('TrafficType')
        return self._TrafficType

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        if self.force_auto_sync:
            self.get('StreamTemplateHandles')
        return self._StreamTemplateHandles

    @property
    def LoadUnit(self):
        """
        get the value of property _LoadUnit
        """
        if self.force_auto_sync:
            self.get('LoadUnit')
        return self._LoadUnit

    @property
    def FrameSize(self):
        """
        get the value of property _FrameSize
        """
        if self.force_auto_sync:
            self.get('FrameSize')
        return self._FrameSize

    @property
    def Cir(self):
        """
        get the value of property _Cir
        """
        if self.force_auto_sync:
            self.get('Cir')
        return self._Cir

    @property
    def CirTolerance(self):
        """
        get the value of property _CirTolerance
        """
        if self.force_auto_sync:
            self.get('CirTolerance')
        return self._CirTolerance

    @property
    def Eir(self):
        """
        get the value of property _Eir
        """
        if self.force_auto_sync:
            self.get('Eir')
        return self._Eir

    @property
    def Cbs(self):
        """
        get the value of property _Cbs
        """
        if self.force_auto_sync:
            self.get('Cbs')
        return self._Cbs

    @property
    def Ebs(self):
        """
        get the value of property _Ebs
        """
        if self.force_auto_sync:
            self.get('Ebs')
        return self._Ebs

    @property
    def FrameDelay(self):
        """
        get the value of property _FrameDelay
        """
        if self.force_auto_sync:
            self.get('FrameDelay')
        return self._FrameDelay

    @property
    def FrameDelayTolerance(self):
        """
        get the value of property _FrameDelayTolerance
        """
        if self.force_auto_sync:
            self.get('FrameDelayTolerance')
        return self._FrameDelayTolerance

    @property
    def FrameDelayVariation(self):
        """
        get the value of property _FrameDelayVariation
        """
        if self.force_auto_sync:
            self.get('FrameDelayVariation')
        return self._FrameDelayVariation

    @property
    def FrameDelayVariationTolerance(self):
        """
        get the value of property _FrameDelayVariationTolerance
        """
        if self.force_auto_sync:
            self.get('FrameDelayVariationTolerance')
        return self._FrameDelayVariationTolerance

    @property
    def FrameLossRatio(self):
        """
        get the value of property _FrameLossRatio
        """
        if self.force_auto_sync:
            self.get('FrameLossRatio')
        return self._FrameLossRatio

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        if self.force_auto_sync:
            self.get('AcceptableFrameLoss')
        return self._AcceptableFrameLoss

    @property
    def ProfileType(self):
        """
        get the value of property _ProfileType
        """
        if self.force_auto_sync:
            self.get('ProfileType')
        return self._ProfileType

    @property
    def MeshType(self):
        """
        get the value of property _MeshType
        """
        if self.force_auto_sync:
            self.get('MeshType')
        return self._MeshType

    @TrafficType.setter
    def TrafficType(self, value):
        self._TrafficType = value
        self.edit(TrafficType=value)

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value
        self.edit(StreamTemplateHandles=value)

    @LoadUnit.setter
    def LoadUnit(self, value):
        self._LoadUnit = value
        self.edit(LoadUnit=value)

    @FrameSize.setter
    def FrameSize(self, value):
        self._FrameSize = value
        self.edit(FrameSize=value)

    @Cir.setter
    def Cir(self, value):
        self._Cir = value
        self.edit(Cir=value)

    @CirTolerance.setter
    def CirTolerance(self, value):
        self._CirTolerance = value
        self.edit(CirTolerance=value)

    @Eir.setter
    def Eir(self, value):
        self._Eir = value
        self.edit(Eir=value)

    @Cbs.setter
    def Cbs(self, value):
        self._Cbs = value
        self.edit(Cbs=value)

    @Ebs.setter
    def Ebs(self, value):
        self._Ebs = value
        self.edit(Ebs=value)

    @FrameDelay.setter
    def FrameDelay(self, value):
        self._FrameDelay = value
        self.edit(FrameDelay=value)

    @FrameDelayTolerance.setter
    def FrameDelayTolerance(self, value):
        self._FrameDelayTolerance = value
        self.edit(FrameDelayTolerance=value)

    @FrameDelayVariation.setter
    def FrameDelayVariation(self, value):
        self._FrameDelayVariation = value
        self.edit(FrameDelayVariation=value)

    @FrameDelayVariationTolerance.setter
    def FrameDelayVariationTolerance(self, value):
        self._FrameDelayVariationTolerance = value
        self.edit(FrameDelayVariationTolerance=value)

    @FrameLossRatio.setter
    def FrameLossRatio(self, value):
        self._FrameLossRatio = value
        self.edit(FrameLossRatio=value)

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value
        self.edit(AcceptableFrameLoss=value)

    @ProfileType.setter
    def ProfileType(self, value):
        self._ProfileType = value
        self.edit(ProfileType=value)

    @MeshType.setter
    def MeshType(self, value):
        self._MeshType = value
        self.edit(MeshType=value)

    def _set_traffictype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TrafficType = EnumTrafficType.%s' % value[:seperate])

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_loadunit_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadUnit = EnumY1564LoadUnit.%s' % value[:seperate])

    def _set_framesize_with_str(self, value):
        try:
            self._FrameSize = int(value)
        except ValueError:
            self._FrameSize = hex(int(value, 16))

    def _set_cir_with_str(self, value):
        self._Cir = float(value)

    def _set_cirtolerance_with_str(self, value):
        self._CirTolerance = float(value)

    def _set_eir_with_str(self, value):
        self._Eir = float(value)

    def _set_cbs_with_str(self, value):
        try:
            self._Cbs = int(value)
        except ValueError:
            self._Cbs = hex(int(value, 16))

    def _set_ebs_with_str(self, value):
        try:
            self._Ebs = int(value)
        except ValueError:
            self._Ebs = hex(int(value, 16))

    def _set_framedelay_with_str(self, value):
        try:
            self._FrameDelay = int(value)
        except ValueError:
            self._FrameDelay = hex(int(value, 16))

    def _set_framedelaytolerance_with_str(self, value):
        self._FrameDelayTolerance = float(value)

    def _set_framedelayvariation_with_str(self, value):
        try:
            self._FrameDelayVariation = int(value)
        except ValueError:
            self._FrameDelayVariation = hex(int(value, 16))

    def _set_framedelayvariationtolerance_with_str(self, value):
        self._FrameDelayVariationTolerance = float(value)

    def _set_framelossratio_with_str(self, value):
        self._FrameLossRatio = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        try:
            self._AcceptableFrameLoss = int(value)
        except ValueError:
            self._AcceptableFrameLoss = hex(int(value, 16))

    def _set_profiletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProfileType = EnumProfileType.%s' % value[:seperate])

    def _set_meshtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._MeshType = EnumMeshType.%s' % value[:seperate])

