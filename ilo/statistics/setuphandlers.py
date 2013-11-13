from collective.grok import gs
from ilo.statistics import MessageFactory as _

@gs.importstep(
    name=u'ilo.statistics', 
    title=_('ilo.statistics import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ilo.statistics.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
