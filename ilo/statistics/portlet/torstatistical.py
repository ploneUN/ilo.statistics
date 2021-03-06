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
from operator import itemgetter
from heapq import nlargest


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

    def get_mostcommon_for(self, index, limit=5):
        catalog = api.portal.get_tool(name='portal_catalog')
        uniquevalue = catalog.uniqueValuesFor(index)
        data = catalog.searchResults({
            index: uniquevalue,
            'portal_type': "ploneun.tor.torfacilityform"
            })

        final_data = list()

        for i in data:
            final_data.extend(getattr(i, key))

        return self.mostcommon(final_data, limit)

    def mostcommon(self, iterable, n=None):
        """Return a sorted list of the most common to
        least common elements andtheir counts.  If n is specified,
        return only the n most common elements.

        """
        #http://code.activestate.com/recipes/347615/

        bag = {}
        bag_get = bag.get
        for elem in iterable:
            bag[elem] = bag_get(elem, 0) + 1
        if n is None:
            return sorted(bag.iteritems(), key=itemgetter(1), reverse=True)
        it = enumerate(bag.iteritems())
        nl = nlargest(n, ((cnt, i, elem) for (i, (elem, cnt)) in it))
        return [(elem, cnt) for cnt, i, elem in nl]

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
