from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from apl.doclegis import doclegisMessageFactory as _


class IDocLegisView(Interface):

    """
    DocLegis view interface
    """

    def test():
        """ test method"""


class DocLegisView(BrowserView):

    """
    DocLegis browser view
    """
    implements(IDocLegisView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')
        return {'dummy': dummy}

    def get_doclegis(self):
        # XXX check if content is DocLegis
        return self.context.contentValues()
