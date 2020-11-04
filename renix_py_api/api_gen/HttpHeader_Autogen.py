"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpHeader(ROMObject):
    def __init__(self, HeaderName=None, HeaderValue=None, **kwargs):
        self._HeaderName = HeaderName  # HeaderName
        self._HeaderValue = HeaderValue  # HeaderValue

        properties = kwargs.copy()
        if HeaderName is not None:
            properties['HeaderName'] = HeaderName
        if HeaderValue is not None:
            properties['HeaderValue'] = HeaderValue

        # call base class function, and it will send message to renix server to create a class.
        super(HttpHeader, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, HeaderName=None, HeaderValue=None, **kwargs):
        properties = kwargs.copy()
        if HeaderName is not None:
            self._HeaderName = HeaderName
            properties['HeaderName'] = HeaderName
        if HeaderValue is not None:
            self._HeaderValue = HeaderValue
            properties['HeaderValue'] = HeaderValue

        super(HttpHeader, self).edit(**properties)

    @property
    def HeaderName(self):
        """
        get the value of property _HeaderName
        """
        if self.force_auto_sync:
            self.get('HeaderName')
        return self._HeaderName

    @property
    def HeaderValue(self):
        """
        get the value of property _HeaderValue
        """
        if self.force_auto_sync:
            self.get('HeaderValue')
        return self._HeaderValue

    @HeaderName.setter
    def HeaderName(self, value):
        self._HeaderName = value
        self.edit(HeaderName=value)

    @HeaderValue.setter
    def HeaderValue(self, value):
        self._HeaderValue = value
        self.edit(HeaderValue=value)

    def _set_headername_with_str(self, value):
        self._HeaderName = value

    def _set_headervalue_with_str(self, value):
        self._HeaderValue = value

