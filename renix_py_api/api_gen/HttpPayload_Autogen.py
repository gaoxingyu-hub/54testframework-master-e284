"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpPayload(ROMObject):
    def __init__(self, OffsetType=None, Offset=None, Repeat=None, TextType=None, Text=None, **kwargs):
        self._OffsetType = OffsetType  # Payload Offset Type
        self._Offset = Offset  # Offset
        self._Repeat = Repeat  # Repeat
        self._TextType = TextType  # Text Type
        self._Text = Text  # Text

        properties = kwargs.copy()
        if OffsetType is not None:
            properties['OffsetType'] = OffsetType
        if Offset is not None:
            properties['Offset'] = Offset
        if Repeat is not None:
            properties['Repeat'] = Repeat
        if TextType is not None:
            properties['TextType'] = TextType
        if Text is not None:
            properties['Text'] = Text

        # call base class function, and it will send message to renix server to create a class.
        super(HttpPayload, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OffsetType=None, Offset=None, Repeat=None, TextType=None, Text=None, **kwargs):
        properties = kwargs.copy()
        if OffsetType is not None:
            self._OffsetType = OffsetType
            properties['OffsetType'] = OffsetType
        if Offset is not None:
            self._Offset = Offset
            properties['Offset'] = Offset
        if Repeat is not None:
            self._Repeat = Repeat
            properties['Repeat'] = Repeat
        if TextType is not None:
            self._TextType = TextType
            properties['TextType'] = TextType
        if Text is not None:
            self._Text = Text
            properties['Text'] = Text

        super(HttpPayload, self).edit(**properties)

    @property
    def OffsetType(self):
        """
        get the value of property _OffsetType
        """
        if self.force_auto_sync:
            self.get('OffsetType')
        return self._OffsetType

    @property
    def Offset(self):
        """
        get the value of property _Offset
        """
        if self.force_auto_sync:
            self.get('Offset')
        return self._Offset

    @property
    def Repeat(self):
        """
        get the value of property _Repeat
        """
        if self.force_auto_sync:
            self.get('Repeat')
        return self._Repeat

    @property
    def TextType(self):
        """
        get the value of property _TextType
        """
        if self.force_auto_sync:
            self.get('TextType')
        return self._TextType

    @property
    def Text(self):
        """
        get the value of property _Text
        """
        if self.force_auto_sync:
            self.get('Text')
        return self._Text

    @OffsetType.setter
    def OffsetType(self, value):
        self._OffsetType = value
        self.edit(OffsetType=value)

    @Offset.setter
    def Offset(self, value):
        self._Offset = value
        self.edit(Offset=value)

    @Repeat.setter
    def Repeat(self, value):
        self._Repeat = value
        self.edit(Repeat=value)

    @TextType.setter
    def TextType(self, value):
        self._TextType = value
        self.edit(TextType=value)

    @Text.setter
    def Text(self, value):
        self._Text = value
        self.edit(Text=value)

    def _set_offsettype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OffsetType = EnumPayloadOffsetType.%s' % value[:seperate])

    def _set_offset_with_str(self, value):
        try:
            self._Offset = int(value)
        except ValueError:
            self._Offset = hex(int(value, 16))

    def _set_repeat_with_str(self, value):
        self._Repeat = (value == 'True')

    def _set_texttype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TextType = EnumPayloadTextType.%s' % value[:seperate])

    def _set_text_with_str(self, value):
        self._Text = value

