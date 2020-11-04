"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HttpResponse(ROMObject):
    def __init__(self, Code=None, Reason=None, Mime=None, TimeZone=None, DateType=None, DateTime=None, DateIncr=None, DateIncrSec=None, DateIncrPage=None, ModifyType=None, ModifyTime=None, ModifyIncr=None, ModifyIncrSec=None, ModifyIncrPage=None, ExpireType=None, ExpireTime=None, ExpireIncr=None, ExpireIncrSec=None, ExpireIncrPage=None, **kwargs):
        self._Code = Code  # Code
        self._Reason = Reason  # Reason
        self._Mime = Mime  # MIME Type
        self._TimeZone = TimeZone  # Time Zone
        self._DateType = DateType  # Date Type
        self._DateTime = DateTime  # Date Date/Time
        self._DateIncr = DateIncr  # Increment
        self._DateIncrSec = DateIncrSec  # Date Incr By (sec)
        self._DateIncrPage = DateIncrPage  # Date Incr For(Page Ref.)
        self._ModifyType = ModifyType  # Modify Type
        self._ModifyTime = ModifyTime  # Modify Date/Time
        self._ModifyIncr = ModifyIncr  # Modify Increment
        self._ModifyIncrSec = ModifyIncrSec  # Modify Incr By (sec)
        self._ModifyIncrPage = ModifyIncrPage  # Modify Incr For(Page Ref.)
        self._ExpireType = ExpireType  # Expire Type
        self._ExpireTime = ExpireTime  # Expire Date/Time
        self._ExpireIncr = ExpireIncr  # Expire Increment
        self._ExpireIncrSec = ExpireIncrSec  # Expire Incr By (sec)
        self._ExpireIncrPage = ExpireIncrPage  # Expire Incr For(Page Ref.)

        properties = kwargs.copy()
        if Code is not None:
            properties['Code'] = Code
        if Reason is not None:
            properties['Reason'] = Reason
        if Mime is not None:
            properties['Mime'] = Mime
        if TimeZone is not None:
            properties['TimeZone'] = TimeZone
        if DateType is not None:
            properties['DateType'] = DateType
        if DateTime is not None:
            properties['DateTime'] = DateTime
        if DateIncr is not None:
            properties['DateIncr'] = DateIncr
        if DateIncrSec is not None:
            properties['DateIncrSec'] = DateIncrSec
        if DateIncrPage is not None:
            properties['DateIncrPage'] = DateIncrPage
        if ModifyType is not None:
            properties['ModifyType'] = ModifyType
        if ModifyTime is not None:
            properties['ModifyTime'] = ModifyTime
        if ModifyIncr is not None:
            properties['ModifyIncr'] = ModifyIncr
        if ModifyIncrSec is not None:
            properties['ModifyIncrSec'] = ModifyIncrSec
        if ModifyIncrPage is not None:
            properties['ModifyIncrPage'] = ModifyIncrPage
        if ExpireType is not None:
            properties['ExpireType'] = ExpireType
        if ExpireTime is not None:
            properties['ExpireTime'] = ExpireTime
        if ExpireIncr is not None:
            properties['ExpireIncr'] = ExpireIncr
        if ExpireIncrSec is not None:
            properties['ExpireIncrSec'] = ExpireIncrSec
        if ExpireIncrPage is not None:
            properties['ExpireIncrPage'] = ExpireIncrPage

        # call base class function, and it will send message to renix server to create a class.
        super(HttpResponse, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Code=None, Reason=None, Mime=None, TimeZone=None, DateType=None, DateTime=None, DateIncr=None, DateIncrSec=None, DateIncrPage=None, ModifyType=None, ModifyTime=None, ModifyIncr=None, ModifyIncrSec=None, ModifyIncrPage=None, ExpireType=None, ExpireTime=None, ExpireIncr=None, ExpireIncrSec=None, ExpireIncrPage=None, **kwargs):
        properties = kwargs.copy()
        if Code is not None:
            self._Code = Code
            properties['Code'] = Code
        if Reason is not None:
            self._Reason = Reason
            properties['Reason'] = Reason
        if Mime is not None:
            self._Mime = Mime
            properties['Mime'] = Mime
        if TimeZone is not None:
            self._TimeZone = TimeZone
            properties['TimeZone'] = TimeZone
        if DateType is not None:
            self._DateType = DateType
            properties['DateType'] = DateType
        if DateTime is not None:
            self._DateTime = DateTime
            properties['DateTime'] = DateTime
        if DateIncr is not None:
            self._DateIncr = DateIncr
            properties['DateIncr'] = DateIncr
        if DateIncrSec is not None:
            self._DateIncrSec = DateIncrSec
            properties['DateIncrSec'] = DateIncrSec
        if DateIncrPage is not None:
            self._DateIncrPage = DateIncrPage
            properties['DateIncrPage'] = DateIncrPage
        if ModifyType is not None:
            self._ModifyType = ModifyType
            properties['ModifyType'] = ModifyType
        if ModifyTime is not None:
            self._ModifyTime = ModifyTime
            properties['ModifyTime'] = ModifyTime
        if ModifyIncr is not None:
            self._ModifyIncr = ModifyIncr
            properties['ModifyIncr'] = ModifyIncr
        if ModifyIncrSec is not None:
            self._ModifyIncrSec = ModifyIncrSec
            properties['ModifyIncrSec'] = ModifyIncrSec
        if ModifyIncrPage is not None:
            self._ModifyIncrPage = ModifyIncrPage
            properties['ModifyIncrPage'] = ModifyIncrPage
        if ExpireType is not None:
            self._ExpireType = ExpireType
            properties['ExpireType'] = ExpireType
        if ExpireTime is not None:
            self._ExpireTime = ExpireTime
            properties['ExpireTime'] = ExpireTime
        if ExpireIncr is not None:
            self._ExpireIncr = ExpireIncr
            properties['ExpireIncr'] = ExpireIncr
        if ExpireIncrSec is not None:
            self._ExpireIncrSec = ExpireIncrSec
            properties['ExpireIncrSec'] = ExpireIncrSec
        if ExpireIncrPage is not None:
            self._ExpireIncrPage = ExpireIncrPage
            properties['ExpireIncrPage'] = ExpireIncrPage

        super(HttpResponse, self).edit(**properties)

    @property
    def Code(self):
        """
        get the value of property _Code
        """
        if self.force_auto_sync:
            self.get('Code')
        return self._Code

    @property
    def Reason(self):
        """
        get the value of property _Reason
        """
        if self.force_auto_sync:
            self.get('Reason')
        return self._Reason

    @property
    def Mime(self):
        """
        get the value of property _Mime
        """
        if self.force_auto_sync:
            self.get('Mime')
        return self._Mime

    @property
    def TimeZone(self):
        """
        get the value of property _TimeZone
        """
        if self.force_auto_sync:
            self.get('TimeZone')
        return self._TimeZone

    @property
    def DateType(self):
        """
        get the value of property _DateType
        """
        if self.force_auto_sync:
            self.get('DateType')
        return self._DateType

    @property
    def DateTime(self):
        """
        get the value of property _DateTime
        """
        if self.force_auto_sync:
            self.get('DateTime')
        return self._DateTime

    @property
    def DateIncr(self):
        """
        get the value of property _DateIncr
        """
        if self.force_auto_sync:
            self.get('DateIncr')
        return self._DateIncr

    @property
    def DateIncrSec(self):
        """
        get the value of property _DateIncrSec
        """
        if self.force_auto_sync:
            self.get('DateIncrSec')
        return self._DateIncrSec

    @property
    def DateIncrPage(self):
        """
        get the value of property _DateIncrPage
        """
        if self.force_auto_sync:
            self.get('DateIncrPage')
        return self._DateIncrPage

    @property
    def ModifyType(self):
        """
        get the value of property _ModifyType
        """
        if self.force_auto_sync:
            self.get('ModifyType')
        return self._ModifyType

    @property
    def ModifyTime(self):
        """
        get the value of property _ModifyTime
        """
        if self.force_auto_sync:
            self.get('ModifyTime')
        return self._ModifyTime

    @property
    def ModifyIncr(self):
        """
        get the value of property _ModifyIncr
        """
        if self.force_auto_sync:
            self.get('ModifyIncr')
        return self._ModifyIncr

    @property
    def ModifyIncrSec(self):
        """
        get the value of property _ModifyIncrSec
        """
        if self.force_auto_sync:
            self.get('ModifyIncrSec')
        return self._ModifyIncrSec

    @property
    def ModifyIncrPage(self):
        """
        get the value of property _ModifyIncrPage
        """
        if self.force_auto_sync:
            self.get('ModifyIncrPage')
        return self._ModifyIncrPage

    @property
    def ExpireType(self):
        """
        get the value of property _ExpireType
        """
        if self.force_auto_sync:
            self.get('ExpireType')
        return self._ExpireType

    @property
    def ExpireTime(self):
        """
        get the value of property _ExpireTime
        """
        if self.force_auto_sync:
            self.get('ExpireTime')
        return self._ExpireTime

    @property
    def ExpireIncr(self):
        """
        get the value of property _ExpireIncr
        """
        if self.force_auto_sync:
            self.get('ExpireIncr')
        return self._ExpireIncr

    @property
    def ExpireIncrSec(self):
        """
        get the value of property _ExpireIncrSec
        """
        if self.force_auto_sync:
            self.get('ExpireIncrSec')
        return self._ExpireIncrSec

    @property
    def ExpireIncrPage(self):
        """
        get the value of property _ExpireIncrPage
        """
        if self.force_auto_sync:
            self.get('ExpireIncrPage')
        return self._ExpireIncrPage

    @Code.setter
    def Code(self, value):
        self._Code = value
        self.edit(Code=value)

    @Reason.setter
    def Reason(self, value):
        self._Reason = value
        self.edit(Reason=value)

    @Mime.setter
    def Mime(self, value):
        self._Mime = value
        self.edit(Mime=value)

    @TimeZone.setter
    def TimeZone(self, value):
        self._TimeZone = value
        self.edit(TimeZone=value)

    @DateType.setter
    def DateType(self, value):
        self._DateType = value
        self.edit(DateType=value)

    @DateTime.setter
    def DateTime(self, value):
        self._DateTime = value
        self.edit(DateTime=value)

    @DateIncr.setter
    def DateIncr(self, value):
        self._DateIncr = value
        self.edit(DateIncr=value)

    @DateIncrSec.setter
    def DateIncrSec(self, value):
        self._DateIncrSec = value
        self.edit(DateIncrSec=value)

    @DateIncrPage.setter
    def DateIncrPage(self, value):
        self._DateIncrPage = value
        self.edit(DateIncrPage=value)

    @ModifyType.setter
    def ModifyType(self, value):
        self._ModifyType = value
        self.edit(ModifyType=value)

    @ModifyTime.setter
    def ModifyTime(self, value):
        self._ModifyTime = value
        self.edit(ModifyTime=value)

    @ModifyIncr.setter
    def ModifyIncr(self, value):
        self._ModifyIncr = value
        self.edit(ModifyIncr=value)

    @ModifyIncrSec.setter
    def ModifyIncrSec(self, value):
        self._ModifyIncrSec = value
        self.edit(ModifyIncrSec=value)

    @ModifyIncrPage.setter
    def ModifyIncrPage(self, value):
        self._ModifyIncrPage = value
        self.edit(ModifyIncrPage=value)

    @ExpireType.setter
    def ExpireType(self, value):
        self._ExpireType = value
        self.edit(ExpireType=value)

    @ExpireTime.setter
    def ExpireTime(self, value):
        self._ExpireTime = value
        self.edit(ExpireTime=value)

    @ExpireIncr.setter
    def ExpireIncr(self, value):
        self._ExpireIncr = value
        self.edit(ExpireIncr=value)

    @ExpireIncrSec.setter
    def ExpireIncrSec(self, value):
        self._ExpireIncrSec = value
        self.edit(ExpireIncrSec=value)

    @ExpireIncrPage.setter
    def ExpireIncrPage(self, value):
        self._ExpireIncrPage = value
        self.edit(ExpireIncrPage=value)

    def _set_code_with_str(self, value):
        self._Code = value

    def _set_reason_with_str(self, value):
        self._Reason = value

    def _set_mime_with_str(self, value):
        self._Mime = value

    def _set_timezone_with_str(self, value):
        self._TimeZone = value

    def _set_datetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._DateType = EnumDateType.%s' % value[:seperate])

    def _set_datetime_with_str(self, value):
        self._DateTime = value

    def _set_dateincr_with_str(self, value):
        self._DateIncr = (value == 'True')

    def _set_dateincrsec_with_str(self, value):
        try:
            self._DateIncrSec = int(value)
        except ValueError:
            self._DateIncrSec = hex(int(value, 16))

    def _set_dateincrpage_with_str(self, value):
        try:
            self._DateIncrPage = int(value)
        except ValueError:
            self._DateIncrPage = hex(int(value, 16))

    def _set_modifytype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ModifyType = EnumModifyType.%s' % value[:seperate])

    def _set_modifytime_with_str(self, value):
        self._ModifyTime = value

    def _set_modifyincr_with_str(self, value):
        self._ModifyIncr = (value == 'True')

    def _set_modifyincrsec_with_str(self, value):
        try:
            self._ModifyIncrSec = int(value)
        except ValueError:
            self._ModifyIncrSec = hex(int(value, 16))

    def _set_modifyincrpage_with_str(self, value):
        try:
            self._ModifyIncrPage = int(value)
        except ValueError:
            self._ModifyIncrPage = hex(int(value, 16))

    def _set_expiretype_with_str(self, value):
        seperate = value.find(':')
        exec('self._ExpireType = EnumExpireType.%s' % value[:seperate])

    def _set_expiretime_with_str(self, value):
        self._ExpireTime = value

    def _set_expireincr_with_str(self, value):
        self._ExpireIncr = (value == 'True')

    def _set_expireincrsec_with_str(self, value):
        try:
            self._ExpireIncrSec = int(value)
        except ValueError:
            self._ExpireIncrSec = hex(int(value, 16))

    def _set_expireincrpage_with_str(self, value):
        try:
            self._ExpireIncrPage = int(value)
        except ValueError:
            self._ExpireIncrPage = hex(int(value, 16))

