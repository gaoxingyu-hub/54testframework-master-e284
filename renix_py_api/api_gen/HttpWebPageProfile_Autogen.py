"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpWebPageProfile(ROMObject):
    def __init__(self, SendContentMD5=None, EnableChunk=None, **kwargs):
        self._SendContentMD5 = SendContentMD5  # Send Content-MD5 header
        self._EnableChunk = EnableChunk  # Enable Chunk Encoding

        properties = kwargs.copy()
        if SendContentMD5 is not None:
            properties['SendContentMD5'] = SendContentMD5
        if EnableChunk is not None:
            properties['EnableChunk'] = EnableChunk

        # call base class function, and it will send message to renix server to create a class.
        super(HttpWebPageProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SendContentMD5=None, EnableChunk=None, **kwargs):
        properties = kwargs.copy()
        if SendContentMD5 is not None:
            self._SendContentMD5 = SendContentMD5
            properties['SendContentMD5'] = SendContentMD5
        if EnableChunk is not None:
            self._EnableChunk = EnableChunk
            properties['EnableChunk'] = EnableChunk

        super(HttpWebPageProfile, self).edit(**properties)

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

    @SendContentMD5.setter
    def SendContentMD5(self, value):
        self._SendContentMD5 = value
        self.edit(SendContentMD5=value)

    @EnableChunk.setter
    def EnableChunk(self, value):
        self._EnableChunk = value
        self.edit(EnableChunk=value)

    def _set_sendcontentmd5_with_str(self, value):
        self._SendContentMD5 = (value == 'True')

    def _set_enablechunk_with_str(self, value):
        self._EnableChunk = (value == 'True')

