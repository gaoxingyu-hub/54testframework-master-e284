"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DynamicProperty(ROMObject):
    def __init__(self, PropertyCategory=None, PropertyDisplay=None, PropertyDescription=None, IsPrivate=None, IsAggregate=None, PropertyDefault=None, RefProperties=None, ReplaceByRef=None, Expression=None, **kwargs):
        self._PropertyCategory = PropertyCategory  # Property Category
        self._PropertyDisplay = PropertyDisplay  # Property Display
        self._PropertyDescription = PropertyDescription  # Property Description
        self._IsPrivate = IsPrivate  # Private
        self._IsAggregate = IsAggregate  # Aggregate
        self._PropertyDefault = PropertyDefault  # Property Default Value
        self._RefProperties = RefProperties  # Property Reference
        self._ReplaceByRef = ReplaceByRef  # Replace by Property Reference
        self._Expression = Expression  # Property Expression

        properties = kwargs.copy()
        if PropertyCategory is not None:
            properties['PropertyCategory'] = PropertyCategory
        if PropertyDisplay is not None:
            properties['PropertyDisplay'] = PropertyDisplay
        if PropertyDescription is not None:
            properties['PropertyDescription'] = PropertyDescription
        if IsPrivate is not None:
            properties['IsPrivate'] = IsPrivate
        if IsAggregate is not None:
            properties['IsAggregate'] = IsAggregate
        if PropertyDefault is not None:
            properties['PropertyDefault'] = PropertyDefault
        if RefProperties is not None:
            properties['RefProperties'] = RefProperties
        if ReplaceByRef is not None:
            properties['ReplaceByRef'] = ReplaceByRef
        if Expression is not None:
            properties['Expression'] = Expression

        # call base class function, and it will send message to renix server to create a class.
        super(DynamicProperty, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PropertyCategory=None, PropertyDisplay=None, PropertyDescription=None, IsPrivate=None, IsAggregate=None, PropertyDefault=None, RefProperties=None, ReplaceByRef=None, Expression=None, **kwargs):
        properties = kwargs.copy()
        if PropertyCategory is not None:
            self._PropertyCategory = PropertyCategory
            properties['PropertyCategory'] = PropertyCategory
        if PropertyDisplay is not None:
            self._PropertyDisplay = PropertyDisplay
            properties['PropertyDisplay'] = PropertyDisplay
        if PropertyDescription is not None:
            self._PropertyDescription = PropertyDescription
            properties['PropertyDescription'] = PropertyDescription
        if IsPrivate is not None:
            self._IsPrivate = IsPrivate
            properties['IsPrivate'] = IsPrivate
        if IsAggregate is not None:
            self._IsAggregate = IsAggregate
            properties['IsAggregate'] = IsAggregate
        if PropertyDefault is not None:
            self._PropertyDefault = PropertyDefault
            properties['PropertyDefault'] = PropertyDefault
        if RefProperties is not None:
            self._RefProperties = RefProperties
            properties['RefProperties'] = RefProperties
        if ReplaceByRef is not None:
            self._ReplaceByRef = ReplaceByRef
            properties['ReplaceByRef'] = ReplaceByRef
        if Expression is not None:
            self._Expression = Expression
            properties['Expression'] = Expression

        super(DynamicProperty, self).edit(**properties)

    @property
    def PropertyCategory(self):
        """
        get the value of property _PropertyCategory
        """
        if self.force_auto_sync:
            self.get('PropertyCategory')
        return self._PropertyCategory

    @property
    def PropertyDisplay(self):
        """
        get the value of property _PropertyDisplay
        """
        if self.force_auto_sync:
            self.get('PropertyDisplay')
        return self._PropertyDisplay

    @property
    def PropertyDescription(self):
        """
        get the value of property _PropertyDescription
        """
        if self.force_auto_sync:
            self.get('PropertyDescription')
        return self._PropertyDescription

    @property
    def IsPrivate(self):
        """
        get the value of property _IsPrivate
        """
        if self.force_auto_sync:
            self.get('IsPrivate')
        return self._IsPrivate

    @property
    def IsAggregate(self):
        """
        get the value of property _IsAggregate
        """
        if self.force_auto_sync:
            self.get('IsAggregate')
        return self._IsAggregate

    @property
    def PropertyDefault(self):
        """
        get the value of property _PropertyDefault
        """
        if self.force_auto_sync:
            self.get('PropertyDefault')
        return self._PropertyDefault

    @property
    def RefProperties(self):
        """
        get the value of property _RefProperties
        """
        if self.force_auto_sync:
            self.get('RefProperties')
        return self._RefProperties

    @property
    def ReplaceByRef(self):
        """
        get the value of property _ReplaceByRef
        """
        if self.force_auto_sync:
            self.get('ReplaceByRef')
        return self._ReplaceByRef

    @property
    def Expression(self):
        """
        get the value of property _Expression
        """
        if self.force_auto_sync:
            self.get('Expression')
        return self._Expression

    @PropertyCategory.setter
    def PropertyCategory(self, value):
        self._PropertyCategory = value
        self.edit(PropertyCategory=value)

    @PropertyDisplay.setter
    def PropertyDisplay(self, value):
        self._PropertyDisplay = value
        self.edit(PropertyDisplay=value)

    @PropertyDescription.setter
    def PropertyDescription(self, value):
        self._PropertyDescription = value
        self.edit(PropertyDescription=value)

    @IsPrivate.setter
    def IsPrivate(self, value):
        self._IsPrivate = value
        self.edit(IsPrivate=value)

    @IsAggregate.setter
    def IsAggregate(self, value):
        self._IsAggregate = value
        self.edit(IsAggregate=value)

    @PropertyDefault.setter
    def PropertyDefault(self, value):
        self._PropertyDefault = value
        self.edit(PropertyDefault=value)

    @RefProperties.setter
    def RefProperties(self, value):
        self._RefProperties = value
        self.edit(RefProperties=value)

    @ReplaceByRef.setter
    def ReplaceByRef(self, value):
        self._ReplaceByRef = value
        self.edit(ReplaceByRef=value)

    @Expression.setter
    def Expression(self, value):
        self._Expression = value
        self.edit(Expression=value)

    def _set_propertycategory_with_str(self, value):
        self._PropertyCategory = value

    def _set_propertydisplay_with_str(self, value):
        self._PropertyDisplay = value

    def _set_propertydescription_with_str(self, value):
        self._PropertyDescription = value

    def _set_isprivate_with_str(self, value):
        self._IsPrivate = (value == 'True')

    def _set_isaggregate_with_str(self, value):
        self._IsAggregate = (value == 'True')

    def _set_propertydefault_with_str(self, value):
        self._PropertyDefault = value

    def _set_refproperties_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RefProperties = tmp_value.split()

    def _set_replacebyref_with_str(self, value):
        self._ReplaceByRef = (value == 'True')

    def _set_expression_with_str(self, value):
        self._Expression = value

