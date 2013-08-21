# -*- coding: utf-8 -*-
from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from apl.doclegis import doclegisMessageFactory as _


class IDocLegis(Interface):

    """Un document legislatif"""

    # -*- schema definition goes here -*-
    numero = schema.TextLine(
        title=_(u"Numéro ou ID"),
        required=False,
        description=_(u"Field description"),
    )
#
    date = schema.Date(
        title=_(u"Date"),
        required=False,
        description=_(u"Field description"),
    )
#
    text = schema.TextLine(
        title=_(u"Corps de texte"),
        required=False,
        description=_(u"Field description"),
    )
#
    document_type = schema.TextLine(
        title=_(u"Type de document"),
        required=True,
        description=_(u"Field description"),
    )
#
    administration = schema.TextLine(
        title=_(u"Administration(s)"),
        required=False,
        description=_(u"Field description"),
    )
#
    theme = schema.TextLine(
        title=_(u"Theme(s)"),
        required=False,
        description=_(u"Field description"),
    )
#
    commune = schema.TextLine(
        title=_(u"Commune (si applicable)"),
        required=False,
        description=_(u"Field description"),
    )
#
    url = schema.TextLine(
        title=_(u"Url ou se trouve le document"),
        required=False,
        description=_(u"Field description"),
    )
#
    # fichier = schema.TextLine(
    #     title=_(u"Fichier a attacher"),
    #     required=False,
    #     description=_(u"Field description"),
    # )
