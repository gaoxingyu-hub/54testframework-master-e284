"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class CaptureEvent(ROMObject):
    def __init__(self, LogicRelation=None, FcsError=None, Ipv4ChecksumError=None, PayloadError=None, **kwargs):
        self._EventType = EnumEventType.QUALIFY  # Capture Event Type, not editable
        self._LogicRelation = LogicRelation  # Logic Relation
        self._FcsError = FcsError  # FCS Error
        self._Ipv4ChecksumError = Ipv4ChecksumError  # IPv4 Checksum Error
        self._PayloadError = PayloadError  # Payload Error

        properties = kwargs.copy()
        if LogicRelation is not None:
            properties['LogicRelation'] = LogicRelation
        if FcsError is not None:
            properties['FcsError'] = FcsError
        if Ipv4ChecksumError is not None:
            properties['Ipv4ChecksumError'] = Ipv4ChecksumError
        if PayloadError is not None:
            properties['PayloadError'] = PayloadError

        # call base class function, and it will send message to renix server to create a class.
        super(CaptureEvent, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, LogicRelation=None, FcsError=None, Ipv4ChecksumError=None, PayloadError=None, **kwargs):
        properties = kwargs.copy()
        if LogicRelation is not None:
            self._LogicRelation = LogicRelation
            properties['LogicRelation'] = LogicRelation
        if FcsError is not None:
            self._FcsError = FcsError
            properties['FcsError'] = FcsError
        if Ipv4ChecksumError is not None:
            self._Ipv4ChecksumError = Ipv4ChecksumError
            properties['Ipv4ChecksumError'] = Ipv4ChecksumError
        if PayloadError is not None:
            self._PayloadError = PayloadError
            properties['PayloadError'] = PayloadError

        super(CaptureEvent, self).edit(**properties)

    @property
    def EventType(self):
        """
        get the value of property _EventType
        """
        if self.force_auto_sync:
            self.get('EventType')
        return self._EventType

    @property
    def LogicRelation(self):
        """
        get the value of property _LogicRelation
        """
        if self.force_auto_sync:
            self.get('LogicRelation')
        return self._LogicRelation

    @property
    def FcsError(self):
        """
        get the value of property _FcsError
        """
        if self.force_auto_sync:
            self.get('FcsError')
        return self._FcsError

    @property
    def Ipv4ChecksumError(self):
        """
        get the value of property _Ipv4ChecksumError
        """
        if self.force_auto_sync:
            self.get('Ipv4ChecksumError')
        return self._Ipv4ChecksumError

    @property
    def PayloadError(self):
        """
        get the value of property _PayloadError
        """
        if self.force_auto_sync:
            self.get('PayloadError')
        return self._PayloadError

    @LogicRelation.setter
    def LogicRelation(self, value):
        self._LogicRelation = value
        self.edit(LogicRelation=value)

    @FcsError.setter
    def FcsError(self, value):
        self._FcsError = value
        self.edit(FcsError=value)

    @Ipv4ChecksumError.setter
    def Ipv4ChecksumError(self, value):
        self._Ipv4ChecksumError = value
        self.edit(Ipv4ChecksumError=value)

    @PayloadError.setter
    def PayloadError(self, value):
        self._PayloadError = value
        self.edit(PayloadError=value)

    def _set_eventtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._EventType = EnumEventType.%s' % value[:seperate])

    def _set_logicrelation_with_str(self, value):
        seperate = value.find(':')
        exec('self._LogicRelation = EnumCaptureOptionLogicRelation.%s' % value[:seperate])

    def _set_fcserror_with_str(self, value):
        seperate = value.find(':')
        exec('self._FcsError = EnumCaptureOptionType.%s' % value[:seperate])

    def _set_ipv4checksumerror_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4ChecksumError = EnumCaptureOptionType.%s' % value[:seperate])

    def _set_payloaderror_with_str(self, value):
        seperate = value.find(':')
        exec('self._PayloadError = EnumCaptureOptionType.%s' % value[:seperate])

