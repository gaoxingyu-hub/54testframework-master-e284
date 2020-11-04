"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpWebPage(ROMObject):
    def __init__(self, PageName=None, PayloadType=None, PageSize=None, FileName=None, ChunkSize=None, **kwargs):
        self._PageName = PageName  # Page Name
        self._PayloadType = PayloadType  # Payload Type
        self._PageSize = PageSize  # Page Size(From-To Bytes)
        self._FileName = FileName  # File Name
        self._ChunkSize = ChunkSize  # Chunk Size(From-To Bytes)

        properties = kwargs.copy()
        if PageName is not None:
            properties['PageName'] = PageName
        if PayloadType is not None:
            properties['PayloadType'] = PayloadType
        if PageSize is not None:
            properties['PageSize'] = PageSize
        if FileName is not None:
            properties['FileName'] = FileName
        if ChunkSize is not None:
            properties['ChunkSize'] = ChunkSize

        # call base class function, and it will send message to renix server to create a class.
        super(HttpWebPage, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PageName=None, PayloadType=None, PageSize=None, FileName=None, ChunkSize=None, **kwargs):
        properties = kwargs.copy()
        if PageName is not None:
            self._PageName = PageName
            properties['PageName'] = PageName
        if PayloadType is not None:
            self._PayloadType = PayloadType
            properties['PayloadType'] = PayloadType
        if PageSize is not None:
            self._PageSize = PageSize
            properties['PageSize'] = PageSize
        if FileName is not None:
            self._FileName = FileName
            properties['FileName'] = FileName
        if ChunkSize is not None:
            self._ChunkSize = ChunkSize
            properties['ChunkSize'] = ChunkSize

        super(HttpWebPage, self).edit(**properties)

    @property
    def PageName(self):
        """
        get the value of property _PageName
        """
        if self.force_auto_sync:
            self.get('PageName')
        return self._PageName

    @property
    def PayloadType(self):
        """
        get the value of property _PayloadType
        """
        if self.force_auto_sync:
            self.get('PayloadType')
        return self._PayloadType

    @property
    def PageSize(self):
        """
        get the value of property _PageSize
        """
        if self.force_auto_sync:
            self.get('PageSize')
        return self._PageSize

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        if self.force_auto_sync:
            self.get('FileName')
        return self._FileName

    @property
    def ChunkSize(self):
        """
        get the value of property _ChunkSize
        """
        if self.force_auto_sync:
            self.get('ChunkSize')
        return self._ChunkSize

    @PageName.setter
    def PageName(self, value):
        self._PageName = value
        self.edit(PageName=value)

    @PayloadType.setter
    def PayloadType(self, value):
        self._PayloadType = value
        self.edit(PayloadType=value)

    @PageSize.setter
    def PageSize(self, value):
        self._PageSize = value
        self.edit(PageSize=value)

    @FileName.setter
    def FileName(self, value):
        self._FileName = value
        self.edit(FileName=value)

    @ChunkSize.setter
    def ChunkSize(self, value):
        self._ChunkSize = value
        self.edit(ChunkSize=value)

    def _set_pagename_with_str(self, value):
        self._PageName = value

    def _set_payloadtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._PayloadType = EnumHttpPayloadType.%s' % value[:seperate])

    def _set_pagesize_with_str(self, value):
        self._PageSize = value

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_chunksize_with_str(self, value):
        self._ChunkSize = value

