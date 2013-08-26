# -*- coding: utf-8 -*-

"""Definition of the DocLegis content type
"""

from zope.interface import implements

from DateTime.DateTime import DateTime

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.Archetypes.utils import Vocabulary

# -*- Message Factory Imported Here -*-
from apl.doclegis import doclegisMessageFactory as _

from apl.doclegis.interfaces import IDocLegis
from apl.doclegis.config import PROJECTNAME
from apl.doclegis.browser import vocabulary

DocLegisSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        'numero',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Numero ou ID"),
            description=_(u""),
        ),
    ),

    atapi.TextField(
        'text',
        storage=atapi.AnnotationStorage(),
        allowable_content_types=('text/html',),
        default_output_type='text/html',
        widget=atapi.RichWidget(
            label=_(u"Corps de texte"),
            description=_(u""),
        ),
    ),

    atapi.StringField(
        'document_type',
        vocabulary=vocabulary.TYPE,
        storage=atapi.AnnotationStorage(),
        widget=atapi.SelectionWidget(
            label=_(u"Type de document"),
            description=_(u""),
            format='select',
        ),
        required=True,
    ),

    atapi.DateTimeField(
        'date',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date"),
            description=_(u"jj/mm/aaaa"),
            show_hm=False,
            starting_year=1830,
        ),

        default_method='getDefaultTime',
        validators=('isValidDate'),
    ),


    atapi.DateTimeField(
        'datepublication',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date de publication au moniteur si connue"),
            description=_(u"jj/mm/aaaa"),
            show_hm=False,
            starting_year=1830,
        ),
        validators=('isValidDate'),
    ),

    atapi.StringField(
        'institution',
        vocabulary=vocabulary.INSTITUTIONS,
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Institution(s)"),
            description=_(u""),
            format='checkbox',
        ),
    ),


    atapi.StringField(
        'theme',
        vocabulary=vocabulary.THEMES,
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Theme(s)"),
            description=_(u""),
            format='checkbox',
        ),
    ),


    atapi.StringField(
        'commune',
        vocabulary=vocabulary.COMMUNES,
        storage=atapi.AnnotationStorage(),
        widget=atapi.MultiSelectionWidget(
            label=_(u"Commune (si applicable)"),
            description=_(u""),
            format='checkbox',
        ),
    ),


    atapi.StringField(
        'url',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Url ou se trouve le document"),
            description=_(u""),
        ),
        validators=('isURL'),
    ),

    atapi.FileField(
        'fichier',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Fichier a attacher"),
            description=_(u""),
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

DocLegisSchema['title'].storage = atapi.AnnotationStorage()
DocLegisSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(DocLegisSchema, moveDiscussion=False)


class DocLegis(base.ATCTContent):

    """Un document legislatif"""
    implements(IDocLegis)

    meta_type = "DocLegis"
    schema = DocLegisSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    institution = atapi.ATFieldProperty('institution')

    theme = atapi.ATFieldProperty('theme')

    commune = atapi.ATFieldProperty('commune')

    url = atapi.ATFieldProperty('url')

    fichier = atapi.ATFieldProperty('fichier')

    numero = atapi.ATFieldProperty('numero')

    date = atapi.ATFieldProperty('date')

    text = atapi.ATFieldProperty('text')

    document_type = atapi.ATFieldProperty('document_type')

    def getDefaultTime(self):  # function to return the current date and time
        return DateTime()

atapi.registerType(DocLegis, PROJECTNAME)
