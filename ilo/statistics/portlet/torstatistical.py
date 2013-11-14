from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

# XXX: Uncomment for z3cform

from z3c.form import field

from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationList, RelationChoice

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ilo.statistics import MessageFactory as _
from plone import api

class ITORStatistical(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(ITORStatistical)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('TOR Statistical')

class Renderer(base.Renderer):


    render = ViewPageTemplateFile('templates/torstatistical.pt')

    @property
    def available(self):
        return True

    def total_tor(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        return len(catalog(portal_type='ploneun.tor.torfacilityform'))

    def get_data(self, key):
        catalog = api.portal.get_tool(name='portal_catalog')
        uniquevalue = catalog.uniqueValuesFor('%s' % key)
        data = catalog.searchResults({
            key: uniquevalue,
            'portal_type': "ploneun.tor.torfacilityform"
            })

        final_data = list()

        for i in data:
            final_data.extend(getattr(i, key))

        return list(set(final_data))

# XXX: z3cform
# class AddForm(z3cformhelper.AddForm):
class AddForm(base.AddForm):

#    XXX: z3cform
#    fields = field.Fields(ITORStatistical)

    form_fields = form.Fields(ITORStatistical)

    label = _(u"Add TOR Statistical")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

# XXX: z3cform
# class EditForm(z3cformhelper.EditForm):
class EditForm(base.EditForm):

#    XXX: z3cform
#    fields = field.Fields(ITORStatistical)

    form_fields = form.Fields(ITORStatistical)

    label = _(u"Edit TOR Statistical")
    description = _(u"")
