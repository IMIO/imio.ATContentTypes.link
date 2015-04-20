from Products.Archetypes.public import BooleanField
from Products.ATContentTypes.interface import IATLink
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implements


class _ExtensionBooleanField(ExtensionField, BooleanField):
    pass


class LinkTargetExtender(object):
    adapts(IATLink)
    implements(ISchemaExtender)

    fields = [
        _ExtensionBooleanField(
            name="openInNewTab",
            widget=BooleanField._properties['widget'](
                label=u"Open in a new tab (true/false)",
                description=u"Open link in a new tab (true/false)",
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
