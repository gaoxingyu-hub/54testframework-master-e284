"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L47File(ROMObject):
    def __init__(self, FileName=None, DummyFile=None, FilePath=None, FileSize=None, **kwargs):
        self._FileName = FileName  # File Name
        self._DummyFile = DummyFile  # Dummy File
        self._FilePath = FilePath  # File Path
        self._FileSize = FileSize  # File Size

        properties = kwargs.copy()
        if FileName is not None:
            properties['FileName'] = FileName
        if DummyFile is not None:
            properties['DummyFile'] = DummyFile
        if FilePath is not None:
            properties['FilePath'] = FilePath
        if FileSize is not None:
            properties['FileSize'] = FileSize

        # call base class function, and it will send message to renix server to create a class.
        super(L47File, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FileName=None, DummyFile=None, FilePath=None, FileSize=None, **kwargs):
        properties = kwargs.copy()
        if FileName is not None:
            self._FileName = FileName
            properties['FileName'] = FileName
        if DummyFile is not None:
            self._DummyFile = DummyFile
            properties['DummyFile'] = DummyFile
        if FilePath is not None:
            self._FilePath = FilePath
            properties['FilePath'] = FilePath
        if FileSize is not None:
            self._FileSize = FileSize
            properties['FileSize'] = FileSize

        super(L47File, self).edit(**properties)

    @property
    def FileName(self):
        """
        get the value of property _FileName
        """
        if self.force_auto_sync:
            self.get('FileName')
        return self._FileName

    @property
    def DummyFile(self):
        """
        get the value of property _DummyFile
        """
        if self.force_auto_sync:
            self.get('DummyFile')
        return self._DummyFile

    @property
    def FilePath(self):
        """
        get the value of property _FilePath
        """
        if self.force_auto_sync:
            self.get('FilePath')
        return self._FilePath

    @property
    def FileSize(self):
        """
        get the value of property _FileSize
        """
        if self.force_auto_sync:
            self.get('FileSize')
        return self._FileSize

    @FileName.setter
    def FileName(self, value):
        self._FileName = value
        self.edit(FileName=value)

    @DummyFile.setter
    def DummyFile(self, value):
        self._DummyFile = value
        self.edit(DummyFile=value)

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value
        self.edit(FilePath=value)

    @FileSize.setter
    def FileSize(self, value):
        self._FileSize = value
        self.edit(FileSize=value)

    def _set_filename_with_str(self, value):
        self._FileName = value

    def _set_dummyfile_with_str(self, value):
        self._DummyFile = (value == 'True')

    def _set_filepath_with_str(self, value):
        self._FilePath = value

    def _set_filesize_with_str(self, value):
        try:
            self._FileSize = int(value)
        except ValueError:
            self._FileSize = hex(int(value, 16))

