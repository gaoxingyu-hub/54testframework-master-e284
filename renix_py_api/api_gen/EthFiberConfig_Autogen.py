"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EthMediaConfig_Autogen import EthMediaConfig


@rom_manager.rom
class EthFiberConfig(EthMediaConfig):
    def __init__(self, RemoteFault=None, WanMode=None, PhyMode=None, TxDiffCtrlLane0=None, TxDiffCtrlLane1=None, TxDiffCtrlLane2=None, TxDiffCtrlLane3=None, TxPostCursorLane0=None, TxPostCursorLane1=None, TxPostCursorLane2=None, TxPostCursorLane3=None, TxPreCursorLane0=None, TxPreCursorLane1=None, TxPreCursorLane2=None, TxPreCursorLane3=None, **kwargs):
        self._RemoteFault = RemoteFault  # RemoteFault
        self._WanMode = WanMode  # WAN
        self._PhyMode = PhyMode  # PHY Mode
        self._TxDiffCtrlLane0 = TxDiffCtrlLane0  # TxDiffCtrl Lane0
        self._TxDiffCtrlLane1 = TxDiffCtrlLane1  # TxDiffCtrl Lane1
        self._TxDiffCtrlLane2 = TxDiffCtrlLane2  # TxDiffCtrl Lane2
        self._TxDiffCtrlLane3 = TxDiffCtrlLane3  # TxDiffCtrl Lane3
        self._TxPostCursorLane0 = TxPostCursorLane0  # TxPostCursor Lane0
        self._TxPostCursorLane1 = TxPostCursorLane1  # TxPostCursor Lane1
        self._TxPostCursorLane2 = TxPostCursorLane2  # TxPostCursor Lane2
        self._TxPostCursorLane3 = TxPostCursorLane3  # TxPostCursor Lane3
        self._TxPreCursorLane0 = TxPreCursorLane0  # TxPreCursor Lane0
        self._TxPreCursorLane1 = TxPreCursorLane1  # TxPreCursor Lane1
        self._TxPreCursorLane2 = TxPreCursorLane2  # TxPreCursor Lane2
        self._TxPreCursorLane3 = TxPreCursorLane3  # TxPreCursor Lane3

        properties = kwargs.copy()
        if RemoteFault is not None:
            properties['RemoteFault'] = RemoteFault
        if WanMode is not None:
            properties['WanMode'] = WanMode
        if PhyMode is not None:
            properties['PhyMode'] = PhyMode
        if TxDiffCtrlLane0 is not None:
            properties['TxDiffCtrlLane0'] = TxDiffCtrlLane0
        if TxDiffCtrlLane1 is not None:
            properties['TxDiffCtrlLane1'] = TxDiffCtrlLane1
        if TxDiffCtrlLane2 is not None:
            properties['TxDiffCtrlLane2'] = TxDiffCtrlLane2
        if TxDiffCtrlLane3 is not None:
            properties['TxDiffCtrlLane3'] = TxDiffCtrlLane3
        if TxPostCursorLane0 is not None:
            properties['TxPostCursorLane0'] = TxPostCursorLane0
        if TxPostCursorLane1 is not None:
            properties['TxPostCursorLane1'] = TxPostCursorLane1
        if TxPostCursorLane2 is not None:
            properties['TxPostCursorLane2'] = TxPostCursorLane2
        if TxPostCursorLane3 is not None:
            properties['TxPostCursorLane3'] = TxPostCursorLane3
        if TxPreCursorLane0 is not None:
            properties['TxPreCursorLane0'] = TxPreCursorLane0
        if TxPreCursorLane1 is not None:
            properties['TxPreCursorLane1'] = TxPreCursorLane1
        if TxPreCursorLane2 is not None:
            properties['TxPreCursorLane2'] = TxPreCursorLane2
        if TxPreCursorLane3 is not None:
            properties['TxPreCursorLane3'] = TxPreCursorLane3

        # call base class function, and it will send message to renix server to create a class.
        super(EthFiberConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RemoteFault=None, WanMode=None, PhyMode=None, TxDiffCtrlLane0=None, TxDiffCtrlLane1=None, TxDiffCtrlLane2=None, TxDiffCtrlLane3=None, TxPostCursorLane0=None, TxPostCursorLane1=None, TxPostCursorLane2=None, TxPostCursorLane3=None, TxPreCursorLane0=None, TxPreCursorLane1=None, TxPreCursorLane2=None, TxPreCursorLane3=None, **kwargs):
        properties = kwargs.copy()
        if RemoteFault is not None:
            self._RemoteFault = RemoteFault
            properties['RemoteFault'] = RemoteFault
        if WanMode is not None:
            self._WanMode = WanMode
            properties['WanMode'] = WanMode
        if PhyMode is not None:
            self._PhyMode = PhyMode
            properties['PhyMode'] = PhyMode
        if TxDiffCtrlLane0 is not None:
            self._TxDiffCtrlLane0 = TxDiffCtrlLane0
            properties['TxDiffCtrlLane0'] = TxDiffCtrlLane0
        if TxDiffCtrlLane1 is not None:
            self._TxDiffCtrlLane1 = TxDiffCtrlLane1
            properties['TxDiffCtrlLane1'] = TxDiffCtrlLane1
        if TxDiffCtrlLane2 is not None:
            self._TxDiffCtrlLane2 = TxDiffCtrlLane2
            properties['TxDiffCtrlLane2'] = TxDiffCtrlLane2
        if TxDiffCtrlLane3 is not None:
            self._TxDiffCtrlLane3 = TxDiffCtrlLane3
            properties['TxDiffCtrlLane3'] = TxDiffCtrlLane3
        if TxPostCursorLane0 is not None:
            self._TxPostCursorLane0 = TxPostCursorLane0
            properties['TxPostCursorLane0'] = TxPostCursorLane0
        if TxPostCursorLane1 is not None:
            self._TxPostCursorLane1 = TxPostCursorLane1
            properties['TxPostCursorLane1'] = TxPostCursorLane1
        if TxPostCursorLane2 is not None:
            self._TxPostCursorLane2 = TxPostCursorLane2
            properties['TxPostCursorLane2'] = TxPostCursorLane2
        if TxPostCursorLane3 is not None:
            self._TxPostCursorLane3 = TxPostCursorLane3
            properties['TxPostCursorLane3'] = TxPostCursorLane3
        if TxPreCursorLane0 is not None:
            self._TxPreCursorLane0 = TxPreCursorLane0
            properties['TxPreCursorLane0'] = TxPreCursorLane0
        if TxPreCursorLane1 is not None:
            self._TxPreCursorLane1 = TxPreCursorLane1
            properties['TxPreCursorLane1'] = TxPreCursorLane1
        if TxPreCursorLane2 is not None:
            self._TxPreCursorLane2 = TxPreCursorLane2
            properties['TxPreCursorLane2'] = TxPreCursorLane2
        if TxPreCursorLane3 is not None:
            self._TxPreCursorLane3 = TxPreCursorLane3
            properties['TxPreCursorLane3'] = TxPreCursorLane3

        super(EthFiberConfig, self).edit(**properties)

    @property
    def RemoteFault(self):
        """
        get the value of property _RemoteFault
        """
        if self.force_auto_sync:
            self.get('RemoteFault')
        return self._RemoteFault

    @property
    def WanMode(self):
        """
        get the value of property _WanMode
        """
        if self.force_auto_sync:
            self.get('WanMode')
        return self._WanMode

    @property
    def PhyMode(self):
        """
        get the value of property _PhyMode
        """
        if self.force_auto_sync:
            self.get('PhyMode')
        return self._PhyMode

    @property
    def TxDiffCtrlLane0(self):
        """
        get the value of property _TxDiffCtrlLane0
        """
        if self.force_auto_sync:
            self.get('TxDiffCtrlLane0')
        return self._TxDiffCtrlLane0

    @property
    def TxDiffCtrlLane1(self):
        """
        get the value of property _TxDiffCtrlLane1
        """
        if self.force_auto_sync:
            self.get('TxDiffCtrlLane1')
        return self._TxDiffCtrlLane1

    @property
    def TxDiffCtrlLane2(self):
        """
        get the value of property _TxDiffCtrlLane2
        """
        if self.force_auto_sync:
            self.get('TxDiffCtrlLane2')
        return self._TxDiffCtrlLane2

    @property
    def TxDiffCtrlLane3(self):
        """
        get the value of property _TxDiffCtrlLane3
        """
        if self.force_auto_sync:
            self.get('TxDiffCtrlLane3')
        return self._TxDiffCtrlLane3

    @property
    def TxPostCursorLane0(self):
        """
        get the value of property _TxPostCursorLane0
        """
        if self.force_auto_sync:
            self.get('TxPostCursorLane0')
        return self._TxPostCursorLane0

    @property
    def TxPostCursorLane1(self):
        """
        get the value of property _TxPostCursorLane1
        """
        if self.force_auto_sync:
            self.get('TxPostCursorLane1')
        return self._TxPostCursorLane1

    @property
    def TxPostCursorLane2(self):
        """
        get the value of property _TxPostCursorLane2
        """
        if self.force_auto_sync:
            self.get('TxPostCursorLane2')
        return self._TxPostCursorLane2

    @property
    def TxPostCursorLane3(self):
        """
        get the value of property _TxPostCursorLane3
        """
        if self.force_auto_sync:
            self.get('TxPostCursorLane3')
        return self._TxPostCursorLane3

    @property
    def TxPreCursorLane0(self):
        """
        get the value of property _TxPreCursorLane0
        """
        if self.force_auto_sync:
            self.get('TxPreCursorLane0')
        return self._TxPreCursorLane0

    @property
    def TxPreCursorLane1(self):
        """
        get the value of property _TxPreCursorLane1
        """
        if self.force_auto_sync:
            self.get('TxPreCursorLane1')
        return self._TxPreCursorLane1

    @property
    def TxPreCursorLane2(self):
        """
        get the value of property _TxPreCursorLane2
        """
        if self.force_auto_sync:
            self.get('TxPreCursorLane2')
        return self._TxPreCursorLane2

    @property
    def TxPreCursorLane3(self):
        """
        get the value of property _TxPreCursorLane3
        """
        if self.force_auto_sync:
            self.get('TxPreCursorLane3')
        return self._TxPreCursorLane3

    @RemoteFault.setter
    def RemoteFault(self, value):
        self._RemoteFault = value
        self.edit(RemoteFault=value)

    @WanMode.setter
    def WanMode(self, value):
        self._WanMode = value
        self.edit(WanMode=value)

    @PhyMode.setter
    def PhyMode(self, value):
        self._PhyMode = value
        self.edit(PhyMode=value)

    @TxDiffCtrlLane0.setter
    def TxDiffCtrlLane0(self, value):
        self._TxDiffCtrlLane0 = value
        self.edit(TxDiffCtrlLane0=value)

    @TxDiffCtrlLane1.setter
    def TxDiffCtrlLane1(self, value):
        self._TxDiffCtrlLane1 = value
        self.edit(TxDiffCtrlLane1=value)

    @TxDiffCtrlLane2.setter
    def TxDiffCtrlLane2(self, value):
        self._TxDiffCtrlLane2 = value
        self.edit(TxDiffCtrlLane2=value)

    @TxDiffCtrlLane3.setter
    def TxDiffCtrlLane3(self, value):
        self._TxDiffCtrlLane3 = value
        self.edit(TxDiffCtrlLane3=value)

    @TxPostCursorLane0.setter
    def TxPostCursorLane0(self, value):
        self._TxPostCursorLane0 = value
        self.edit(TxPostCursorLane0=value)

    @TxPostCursorLane1.setter
    def TxPostCursorLane1(self, value):
        self._TxPostCursorLane1 = value
        self.edit(TxPostCursorLane1=value)

    @TxPostCursorLane2.setter
    def TxPostCursorLane2(self, value):
        self._TxPostCursorLane2 = value
        self.edit(TxPostCursorLane2=value)

    @TxPostCursorLane3.setter
    def TxPostCursorLane3(self, value):
        self._TxPostCursorLane3 = value
        self.edit(TxPostCursorLane3=value)

    @TxPreCursorLane0.setter
    def TxPreCursorLane0(self, value):
        self._TxPreCursorLane0 = value
        self.edit(TxPreCursorLane0=value)

    @TxPreCursorLane1.setter
    def TxPreCursorLane1(self, value):
        self._TxPreCursorLane1 = value
        self.edit(TxPreCursorLane1=value)

    @TxPreCursorLane2.setter
    def TxPreCursorLane2(self, value):
        self._TxPreCursorLane2 = value
        self.edit(TxPreCursorLane2=value)

    @TxPreCursorLane3.setter
    def TxPreCursorLane3(self, value):
        self._TxPreCursorLane3 = value
        self.edit(TxPreCursorLane3=value)

    def _set_remotefault_with_str(self, value):
        seperate = value.find(':')
        exec('self._RemoteFault = EnumRemoteFault.%s' % value[:seperate])

    def _set_wanmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._WanMode = EnumWanMode.%s' % value[:seperate])

    def _set_phymode_with_str(self, value):
        seperate = value.find(':')
        exec('self._PhyMode = EnumPhyMode.%s' % value[:seperate])

    def _set_txdiffctrllane0_with_str(self, value):
        try:
            self._TxDiffCtrlLane0 = int(value)
        except ValueError:
            self._TxDiffCtrlLane0 = hex(int(value, 16))

    def _set_txdiffctrllane1_with_str(self, value):
        try:
            self._TxDiffCtrlLane1 = int(value)
        except ValueError:
            self._TxDiffCtrlLane1 = hex(int(value, 16))

    def _set_txdiffctrllane2_with_str(self, value):
        try:
            self._TxDiffCtrlLane2 = int(value)
        except ValueError:
            self._TxDiffCtrlLane2 = hex(int(value, 16))

    def _set_txdiffctrllane3_with_str(self, value):
        try:
            self._TxDiffCtrlLane3 = int(value)
        except ValueError:
            self._TxDiffCtrlLane3 = hex(int(value, 16))

    def _set_txpostcursorlane0_with_str(self, value):
        try:
            self._TxPostCursorLane0 = int(value)
        except ValueError:
            self._TxPostCursorLane0 = hex(int(value, 16))

    def _set_txpostcursorlane1_with_str(self, value):
        try:
            self._TxPostCursorLane1 = int(value)
        except ValueError:
            self._TxPostCursorLane1 = hex(int(value, 16))

    def _set_txpostcursorlane2_with_str(self, value):
        try:
            self._TxPostCursorLane2 = int(value)
        except ValueError:
            self._TxPostCursorLane2 = hex(int(value, 16))

    def _set_txpostcursorlane3_with_str(self, value):
        try:
            self._TxPostCursorLane3 = int(value)
        except ValueError:
            self._TxPostCursorLane3 = hex(int(value, 16))

    def _set_txprecursorlane0_with_str(self, value):
        try:
            self._TxPreCursorLane0 = int(value)
        except ValueError:
            self._TxPreCursorLane0 = hex(int(value, 16))

    def _set_txprecursorlane1_with_str(self, value):
        try:
            self._TxPreCursorLane1 = int(value)
        except ValueError:
            self._TxPreCursorLane1 = hex(int(value, 16))

    def _set_txprecursorlane2_with_str(self, value):
        try:
            self._TxPreCursorLane2 = int(value)
        except ValueError:
            self._TxPreCursorLane2 = hex(int(value, 16))

    def _set_txprecursorlane3_with_str(self, value):
        try:
            self._TxPreCursorLane3 = int(value)
        except ValueError:
            self._TxPreCursorLane3 = hex(int(value, 16))

