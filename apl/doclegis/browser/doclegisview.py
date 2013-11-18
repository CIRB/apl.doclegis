# -*- coding: utf-8 -*-
from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from apl.doclegis import doclegisMessageFactory as _
from plone.app.form.widgets.datecomponents import DateComponents


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
        results = []
        catalog = self.portal_catalog
        path = '/'.join(self.context.getPhysicalPath())
        brains = catalog.searchResults({'portal_type': 'DocLegis',
                                        'review_state': 'published'},
                                        path={'query': path, 'depth': 1},
                                        )
        for brain in brains:
            doclegis = brain.getObject()
            date = doclegis.date
            formated_date = ''
            year = ''
            if date:
                formated_date = "{0}/{1}/{2}".format(date.day(),
                                                     date.month(),
                                                     date.year())
                year = date.year()
            #publication_date = doclegis.getDatepublication()
            #if publication_date:
            #    year = publication_date.year()
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


class DateComponentsDocLegis(DateComponents):

    def result(self, date=None,
               use_ampm=False,
               starting_year=None,
               ending_year=None,
               future_years=None,
               minute_step=5):
        """Returns a dict with date information.
        """
        res = super(DateComponentsDocLegis, self).result(date=date,
                use_ampm=use_ampm,
                starting_year=starting_year,
                ending_year=ending_year,
                future_years=future_years,
                minute_step=minute_step)
        years = res['years']
        years.reverse()
        first = years.pop()
        years.insert(0, first)
        #res['years'] = years
        return res

