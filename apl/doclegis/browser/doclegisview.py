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
                    formated_date = "{0}/{1}/{2}".format(date.day(), date.month(), date.year())
                    year = date.year()
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


class IDocLegisSimpleView(Interface):

    """
    DocLegis view interface
    """

    def get_doclegis():
        """ test method"""


class DocLegisSimpleView(BrowserView):

    """
    DocLegis browser view
    """
    implements(IDocLegisSimpleView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def get_date(self):
        date = self.context.getDate()
        formated_date = "{0}/{1}/{2}".format(date.day(), date.month(), date.year())
        return formated_date

    def get_datepublication(self):
        date = self.context.getDatepublication()
        if date:
            formated_date = "{0}/{1}/{2}".format(date.day(), date.month(), date.year())
            return formated_date
        else:
            return ''

    def get_documenttype(self):
        msgid = _(self.context.document_type)
        document_type = self.context.translate(msgid)
        return document_type

    def get_themes(self):
        trans_theme = []
        for theme in self.context.theme:
            msgid = _(theme)
            trans_theme.append(self.context.translate(msgid))
        return ", ".join(trans_theme)

    def get_inst(self):
        trans_institution = []
        for institution in self.context.institution:
            msgid = _(institution)
            trans_institution.append(self.context.translate(msgid))
        return ", ".join(trans_institution)

    def get_communes(self):
        trans_commune = []
        for commune in self.context.commune:
            msgid = _(commune)
            trans_commune.append(self.context.translate(msgid))
        return ", ".join(trans_commune)

    def get_fichier(self):
        html = []
        #file_size
        # download_url fieldname filename filename_encoded
        return " ".join(html)
