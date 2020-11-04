"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Y1564WriteDbCommand_Autogen import Y1564WriteDbCommand


@rom_manager.rom
class Y1564ConfigurationTestWriteDbCommand(Y1564WriteDbCommand):
    def __init__(self, StreamTemplateHandles=None, ServiceConfigName=None, Cir=None, CirTolerance=None, Eir=None, FrameLossRatio=None, AcceptableFrameLoss=None, FrameDelay=None, FrameDelayTolerance=None, FrameDelayVariation=None, FrameDelayVariationTolerance=None, **kwargs):
        self._StreamTemplateHandles = StreamTemplateHandles  # Stream Config Handle
        self._ServiceConfigName = ServiceConfigName  # Service Config Name
        self._Cir = Cir  # CIR
        self._CirTolerance = CirTolerance  # CIR Tolerance (%)
        self._Eir = Eir  # EIR
        self._FrameLossRatio = FrameLossRatio  # Frame Loss Ratio (%)
        self._AcceptableFrameLoss = AcceptableFrameLoss  # Acceptable Frame Loss
        self._FrameDelay = FrameDelay  # Frame Delay (ns)
        self._FrameDelayTolerance = FrameDelayTolerance  # FD Tolerance (%)
        self._FrameDelayVariation = FrameDelayVariation  # Frame Delay Variation (ns)
        self._FrameDelayVariationTolerance = FrameDelayVariationTolerance  # FDV Tolerance (%)

        properties = kwargs.copy()
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if ServiceConfigName is not None:
            properties['ServiceConfigName'] = ServiceConfigName
        if Cir is not None:
            properties['Cir'] = Cir
        if CirTolerance is not None:
            properties['CirTolerance'] = CirTolerance
        if Eir is not None:
            properties['Eir'] = Eir
        if FrameLossRatio is not None:
            properties['FrameLossRatio'] = FrameLossRatio
        if AcceptableFrameLoss is not None:
            properties['AcceptableFrameLoss'] = AcceptableFrameLoss
        if FrameDelay is not None:
            properties['FrameDelay'] = FrameDelay
        if FrameDelayTolerance is not None:
            properties['FrameDelayTolerance'] = FrameDelayTolerance
        if FrameDelayVariation is not None:
            properties['FrameDelayVariation'] = FrameDelayVariation
        if FrameDelayVariationTolerance is not None:
            properties['FrameDelayVariationTolerance'] = FrameDelayVariationTolerance

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564ConfigurationTestWriteDbCommand, self).__init__(**properties)

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        return self._StreamTemplateHandles

    @property
    def ServiceConfigName(self):
        """
        get the value of property _ServiceConfigName
        """
        return self._ServiceConfigName

    @property
    def Cir(self):
        """
        get the value of property _Cir
        """
        return self._Cir

    @property
    def CirTolerance(self):
        """
        get the value of property _CirTolerance
        """
        return self._CirTolerance

    @property
    def Eir(self):
        """
        get the value of property _Eir
        """
        return self._Eir

    @property
    def FrameLossRatio(self):
        """
        get the value of property _FrameLossRatio
        """
        return self._FrameLossRatio

    @property
    def AcceptableFrameLoss(self):
        """
        get the value of property _AcceptableFrameLoss
        """
        return self._AcceptableFrameLoss

    @property
    def FrameDelay(self):
        """
        get the value of property _FrameDelay
        """
        return self._FrameDelay

    @property
    def FrameDelayTolerance(self):
        """
        get the value of property _FrameDelayTolerance
        """
        return self._FrameDelayTolerance

    @property
    def FrameDelayVariation(self):
        """
        get the value of property _FrameDelayVariation
        """
        return self._FrameDelayVariation

    @property
    def FrameDelayVariationTolerance(self):
        """
        get the value of property _FrameDelayVariationTolerance
        """
        return self._FrameDelayVariationTolerance

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value

    @ServiceConfigName.setter
    def ServiceConfigName(self, value):
        self._ServiceConfigName = value

    @Cir.setter
    def Cir(self, value):
        self._Cir = value

    @CirTolerance.setter
    def CirTolerance(self, value):
        self._CirTolerance = value

    @Eir.setter
    def Eir(self, value):
        self._Eir = value

    @FrameLossRatio.setter
    def FrameLossRatio(self, value):
        self._FrameLossRatio = value

    @AcceptableFrameLoss.setter
    def AcceptableFrameLoss(self, value):
        self._AcceptableFrameLoss = value

    @FrameDelay.setter
    def FrameDelay(self, value):
        self._FrameDelay = value

    @FrameDelayTolerance.setter
    def FrameDelayTolerance(self, value):
        self._FrameDelayTolerance = value

    @FrameDelayVariation.setter
    def FrameDelayVariation(self, value):
        self._FrameDelayVariation = value

    @FrameDelayVariationTolerance.setter
    def FrameDelayVariationTolerance(self, value):
        self._FrameDelayVariationTolerance = value

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

    def _set_serviceconfigname_with_str(self, value):
        self._ServiceConfigName = value

    def _set_cir_with_str(self, value):
        self._Cir = float(value)

    def _set_cirtolerance_with_str(self, value):
        self._CirTolerance = float(value)

    def _set_eir_with_str(self, value):
        self._Eir = float(value)

    def _set_framelossratio_with_str(self, value):
        self._FrameLossRatio = float(value)

    def _set_acceptableframeloss_with_str(self, value):
        try:
            self._AcceptableFrameLoss = int(value)
        except ValueError:
            self._AcceptableFrameLoss = hex(int(value, 16))

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

