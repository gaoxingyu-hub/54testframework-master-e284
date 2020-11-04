"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .HttpCommand_Autogen import HttpCommand


@rom_manager.rom
class HttpPutCommand(HttpCommand):
    def __init__(self, NameValueArgs=None, FileName=None, SendContentMD5=None, EnableChunk=None, ChunkSize=None, **kwargs):
        self._NameValueArgs = NameValueArgs  # NameValueArgs
        self._FileName = FileName  # Put File Name
        self._SendContentMD5 = SendContentMD5  # Send Content-MD5 header
        self._EnableChunk = EnableChunk  # Enable Chunk Encoding
        self._ChunkSize = ChunkSize  # Chunk Size (bytes)

        properties = kwargs.copy()
        if NameValueArgs is not None:
            properties['NameValueArgs'] = NameValueArgs
        if FileName is not None:
            properties['FileName'] = FileName
        if SendContentMD5 is not None:
            properties['SendContentMD5'] = SendContentMD5
        if EnableChunk is not None:
            properties['EnableChunk'] = EnableChunk
        if ChunkSize is not None:
            properties['ChunkSize'] = ChunkSize

        # call base class function, and it will send message to renix server to create a class.
        super(HttpPutCommand, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NameValueArgs=None, FileName=None, SendContentMD5=None, EnableChunk=None, ChunkSize=None, **kwargs):
        properties = kwargs.copy()
        if NameValueArgs is not None:
            self._NameValueArgs = NameValueArgs
            properties['NameValueArgs'] = NameValueArgs
        if FileName is not None:
            self._FileName = FileName
            properties['FileName'] = FileName
        if SendContentMD5 is not None:
            self._SendContentMD5 = SendContentMD5
            properties['SendContentMD5'] = SendContentMD5
        if EnableChunk is not None:
            self._EnableChunk = EnableChunk
            properties['EnableChunk'] = EnableChunk
        if ChunkSize is not None:
            self._ChunkSize = ChunkSize
            properties['ChunkSize'] = ChunkSize

        super(HttpPutCommand, self).edit(**properties)

    @property
    def NameValueArgs(self):
        """
        get the value of property _NameValueArgs
        """
        if self.force_auto_sync:
            self.get('NameValueArgs')
        return self._NameValueArgs

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        if self.force_auto_sync:
            self.get('FileName')
        return self._FileName

    @property
    def SendContentMD5(self):
        """
        get the value of property _SendContentMD5
        """
        if self.force_auto_sync:
            self.get('SendContentMD5')
        return self._SendContentMD5

    @property
    def EnableChunk(self):
        """
        get the value of property _EnableChunk
        """
        if self.force_auto_sync:
            self.get('EnableChunk')
        return self._EnableChunk

    @property
    def ChunkSize(self):
        """
        get the value of property _ChunkSize
        """
        if self.force_auto_sync:
            self.get('ChunkSize')
        return self._ChunkSize

    @NameValueArgs.setter
    def NameValueArgs(self, value):
        self._NameValueArgs = value
        self.edit(NameValueArgs=value)

    @FileName.setter
    def FileName(self, value):
        self._FileName = value
        self.edit(FileName=value)

    @SendContentMD5.setter
    def SendContentMD5(self, value):
        self._SendContentMD5 = value
        self.edit(SendContentMD5=value)

    @EnableChunk.setter
    def EnableChunk(self, value):
        self._EnableChunk = value
        self.edit(EnableChunk=value)

    @ChunkSize.setter
    def ChunkSize(self, value):
        self._ChunkSize = value
        self.edit(ChunkSize=value)

    def _set_namevalueargs_with_str(self, value):
        self._NameValueArgs = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_sendcontentmd5_with_str(self, value):
        self._SendContentMD5 = (value == 'True')

    def _set_enablechunk_with_str(self, value):
        self._EnableChunk = (value == 'True')

    def _set_chunksize_with_str(self, value):
        self._ChunkSize = value

