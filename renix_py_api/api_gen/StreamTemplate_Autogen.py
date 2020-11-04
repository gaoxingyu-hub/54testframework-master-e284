"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamTemplate(ROMObject):
    def __init__(self, HostsMesh=None, RepeatCount=None, EnableSignature=None, FrameLengthType=None, RandomLengthSeed=None, FixedLength=None, MinLength=None, MaxLength=None, StepLength=None, PayloadType=None, PayloadValue=None, TemplateString=None, **kwargs):
        self._HostsMesh = HostsMesh  # Hosts Mesh
        self._State = EnumState.NOTREADY  # Stream State, not editable
        self._RepeatCount = RepeatCount  # Repeat Count
        self._EnableSignature = EnableSignature  # Enable Signature
        self._FrameLengthType = FrameLengthType  # Frame Length Type
        self._RandomLengthSeed = RandomLengthSeed  # Seed
        self._FixedLength = FixedLength  # Fixed Length
        self._MinLength = MinLength  # Min Length
        self._MaxLength = MaxLength  # Max Length
        self._StepLength = StepLength  # Step Length
        self._PayloadType = PayloadType  # Payload Type
        self._PayloadValue = PayloadValue  # Payload Value
        self._TemplateString = TemplateString  # Template String
        self._GeneratedFrom = 'RawStream'  # Generated From, not editable

        properties = kwargs.copy()
        if HostsMesh is not None:
            properties['HostsMesh'] = HostsMesh
        if RepeatCount is not None:
            properties['RepeatCount'] = RepeatCount
        if EnableSignature is not None:
            properties['EnableSignature'] = EnableSignature
        if FrameLengthType is not None:
            properties['FrameLengthType'] = FrameLengthType
        if RandomLengthSeed is not None:
            properties['RandomLengthSeed'] = RandomLengthSeed
        if FixedLength is not None:
            properties['FixedLength'] = FixedLength
        if MinLength is not None:
            properties['MinLength'] = MinLength
        if MaxLength is not None:
            properties['MaxLength'] = MaxLength
        if StepLength is not None:
            properties['StepLength'] = StepLength
        if PayloadType is not None:
            properties['PayloadType'] = PayloadType
        if PayloadValue is not None:
            properties['PayloadValue'] = PayloadValue
        if TemplateString is not None:
            properties['TemplateString'] = TemplateString

        # call base class function, and it will send message to renix server to create a class.
        super(StreamTemplate, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HostsMesh=None, RepeatCount=None, EnableSignature=None, FrameLengthType=None, RandomLengthSeed=None, FixedLength=None, MinLength=None, MaxLength=None, StepLength=None, PayloadType=None, PayloadValue=None, TemplateString=None, **kwargs):
        properties = kwargs.copy()
        if HostsMesh is not None:
            self._HostsMesh = HostsMesh
            properties['HostsMesh'] = HostsMesh
        if RepeatCount is not None:
            self._RepeatCount = RepeatCount
            properties['RepeatCount'] = RepeatCount
        if EnableSignature is not None:
            self._EnableSignature = EnableSignature
            properties['EnableSignature'] = EnableSignature
        if FrameLengthType is not None:
            self._FrameLengthType = FrameLengthType
            properties['FrameLengthType'] = FrameLengthType
        if RandomLengthSeed is not None:
            self._RandomLengthSeed = RandomLengthSeed
            properties['RandomLengthSeed'] = RandomLengthSeed
        if FixedLength is not None:
            self._FixedLength = FixedLength
            properties['FixedLength'] = FixedLength
        if MinLength is not None:
            self._MinLength = MinLength
            properties['MinLength'] = MinLength
        if MaxLength is not None:
            self._MaxLength = MaxLength
            properties['MaxLength'] = MaxLength
        if StepLength is not None:
            self._StepLength = StepLength
            properties['StepLength'] = StepLength
        if PayloadType is not None:
            self._PayloadType = PayloadType
            properties['PayloadType'] = PayloadType
        if PayloadValue is not None:
            self._PayloadValue = PayloadValue
            properties['PayloadValue'] = PayloadValue
        if TemplateString is not None:
            self._TemplateString = TemplateString
            properties['TemplateString'] = TemplateString

        super(StreamTemplate, self).edit(**properties)

    @property
    def HostsMesh(self):
        """
        get the value of property _HostsMesh
        """
        if self.force_auto_sync:
            self.get('HostsMesh')
        return self._HostsMesh

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def RepeatCount(self):
        """
        get the value of property _RepeatCount
        """
        if self.force_auto_sync:
            self.get('RepeatCount')
        return self._RepeatCount

    @property
    def EnableSignature(self):
        """
        get the value of property _EnableSignature
        """
        if self.force_auto_sync:
            self.get('EnableSignature')
        return self._EnableSignature

    @property
    def FrameLengthType(self):
        """
        get the value of property _FrameLengthType
        """
        if self.force_auto_sync:
            self.get('FrameLengthType')
        return self._FrameLengthType

    @property
    def RandomLengthSeed(self):
        """
        get the value of property _RandomLengthSeed
        """
        if self.force_auto_sync:
            self.get('RandomLengthSeed')
        return self._RandomLengthSeed

    @property
    def FixedLength(self):
        """
        get the value of property _FixedLength
        """
        if self.force_auto_sync:
            self.get('FixedLength')
        return self._FixedLength

    @property
    def MinLength(self):
        """
        get the value of property _MinLength
        """
        if self.force_auto_sync:
            self.get('MinLength')
        return self._MinLength

    @property
    def MaxLength(self):
        """
        get the value of property _MaxLength
        """
        if self.force_auto_sync:
            self.get('MaxLength')
        return self._MaxLength

    @property
    def StepLength(self):
        """
        get the value of property _StepLength
        """
        if self.force_auto_sync:
            self.get('StepLength')
        return self._StepLength

    @property
    def PayloadType(self):
        """
        get the value of property _PayloadType
        """
        if self.force_auto_sync:
            self.get('PayloadType')
        return self._PayloadType

    @property
    def PayloadValue(self):
        """
        get the value of property _PayloadValue
        """
        if self.force_auto_sync:
            self.get('PayloadValue')
        return self._PayloadValue

    @property
    def TemplateString(self):
        """
        get the value of property _TemplateString
        """
        if self.force_auto_sync:
            self.get('TemplateString')
        return self._TemplateString

    @property
    def GeneratedFrom(self):
        """
        get the value of property _GeneratedFrom
        """
        if self.force_auto_sync:
            self.get('GeneratedFrom')
        return self._GeneratedFrom

    @HostsMesh.setter
    def HostsMesh(self, value):
        self._HostsMesh = value
        self.edit(HostsMesh=value)

    @RepeatCount.setter
    def RepeatCount(self, value):
        self._RepeatCount = value
        self.edit(RepeatCount=value)

    @EnableSignature.setter
    def EnableSignature(self, value):
        self._EnableSignature = value
        self.edit(EnableSignature=value)

    @FrameLengthType.setter
    def FrameLengthType(self, value):
        self._FrameLengthType = value
        self.edit(FrameLengthType=value)

    @RandomLengthSeed.setter
    def RandomLengthSeed(self, value):
        self._RandomLengthSeed = value
        self.edit(RandomLengthSeed=value)

    @FixedLength.setter
    def FixedLength(self, value):
        self._FixedLength = value
        self.edit(FixedLength=value)

    @MinLength.setter
    def MinLength(self, value):
        self._MinLength = value
        self.edit(MinLength=value)

    @MaxLength.setter
    def MaxLength(self, value):
        self._MaxLength = value
        self.edit(MaxLength=value)

    @StepLength.setter
    def StepLength(self, value):
        self._StepLength = value
        self.edit(StepLength=value)

    @PayloadType.setter
    def PayloadType(self, value):
        self._PayloadType = value
        self.edit(PayloadType=value)

    @PayloadValue.setter
    def PayloadValue(self, value):
        self._PayloadValue = value
        self.edit(PayloadValue=value)

    @TemplateString.setter
    def TemplateString(self, value):
        self._TemplateString = value
        self.edit(TemplateString=value)

    def _set_hostsmesh_with_str(self, value):
        seperate = value.find(':')
        exec('self._HostsMesh = EnumEndpointMapping.%s' % value[:seperate])

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumState.%s' % value[:seperate])

    def _set_repeatcount_with_str(self, value):
        try:
            self._RepeatCount = int(value)
        except ValueError:
            self._RepeatCount = hex(int(value, 16))

    def _set_enablesignature_with_str(self, value):
        self._EnableSignature = (value == 'True')

    def _set_framelengthtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FrameLengthType = EnumFrameLengthType.%s' % value[:seperate])

    def _set_randomlengthseed_with_str(self, value):
        try:
            self._RandomLengthSeed = int(value)
        except ValueError:
            self._RandomLengthSeed = hex(int(value, 16))

    def _set_fixedlength_with_str(self, value):
        try:
            self._FixedLength = int(value)
        except ValueError:
            self._FixedLength = hex(int(value, 16))

    def _set_minlength_with_str(self, value):
        try:
            self._MinLength = int(value)
        except ValueError:
            self._MinLength = hex(int(value, 16))

    def _set_maxlength_with_str(self, value):
        try:
            self._MaxLength = int(value)
        except ValueError:
            self._MaxLength = hex(int(value, 16))

    def _set_steplength_with_str(self, value):
        try:
            self._StepLength = int(value)
        except ValueError:
            self._StepLength = hex(int(value, 16))

    def _set_payloadtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._PayloadType = EnumPayloadType.%s' % value[:seperate])

    def _set_payloadvalue_with_str(self, value):
        try:
            self._PayloadValue = int(value)
        except ValueError:
            self._PayloadValue = hex(int(value, 16))

    def _set_templatestring_with_str(self, value):
        self._TemplateString = value

    def _set_generatedfrom_with_str(self, value):
        self._GeneratedFrom = value

