from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from apl.doclegis import doclegisMessageFactory as _


class IDocLegisView(Interface):

    """
    DocLegis view interface
    """

    def get_doclegis():
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

    def get_doclegis(self):
        # XXX check if content is DocLegis
        results = []
        for doclegis in self.context.contentValues():
            if doclegis.getPortalTypeName() == "DocLegis":
                date = doclegis.date
                formated_date = ''
                year = ''
                if date:
                    formated_date = date.strftime('%d/%m/%Y')
                    year = date.strftime('%Y')
                msgid = _(doclegis.document_type)
                document_type = self.context.translate(msgid)

                trans_theme = []
                trans_institution = []
                trans_commune = []

                for theme in doclegis.theme:
                    msgid = _(theme)
                    trans_theme.append(self.context.translate(msgid))

                for institution in doclegis.institution:
                    msgid = _(institution)
                    trans_institution.append(self.context.translate(msgid))

                for commune in doclegis.commune:
                    msgid = _(commune)
                    trans_commune.append(self.context.translate(msgid))

                results.append({
                    'title': doclegis.title,
                    'document_type': document_type,
                    'date': formated_date,
                    'annee': year,
                    'theme': ", ".join(trans_theme),
                    'institution': ", ".join(trans_institution),
                    'commune': ", ".join(trans_commune),
                    'absolute_url': doclegis.absolute_url,
                })
        return results
