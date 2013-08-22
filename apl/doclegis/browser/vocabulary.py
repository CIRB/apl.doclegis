# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary
import zope.interface
from z3c.form import interfaces
from apl.doclegis import doclegisMessageFactory as _
from Products.Archetypes.utils import DisplayList


def create_dl(elems):
    dl = DisplayList()
    for elem in elems:
        dl.add(key=elem[0], value=elem[1], msgid=elem[1])
    return dl


TYPE = create_dl([
    ('loi', _(u'loi')),
    ('ordonnance', _(u'ordonnance')),
    ('arreteroyal', _(u'arreteroyal')),
    ('arretegouvernement', _(u'arretegouvernement')),
    ('circulaire', _(u'circulaire')),
    ('reglement', _(u'reglement')),
])

INSTITUTIONS = create_dl([
    ('communes', _(u'communes')),
    ('cpas', _(u'cpas')),
    ('cultesetlaicite', _(u'cultesetlaicite')),
    ('intercommunales', _(u'intercommunales')),
    ('regiescommunales', _(u'regiescommunales')),
    ('zonesdepolice', _(u'zonesdepolice')),
    ('lemontdepiete', _(u'lemontdepiete')),
    ('lesassociationschapitrexii',
        _(u'lesassociationschapitrexii')),
    ('lereseauhospitalieriris',
        _(u'lereseauhospitalieriris')),
])

THEMES = create_dl([
    ('cultesetlaicite', _(u'cultesetlaicite')),
    ('elections', _(u'elections')),
    ('fiscalite', _(u'fiscalite')),
    ('marchespublics', _(u'marchespublics')),
    ('soutienfinancier', _(u'soutienfinancier')),
    ('egalitedeschancesetdiversite', _(u'egalitedeschancesetdiversite')),
    ('finances', _(u'finances')),
    ('international', _(u'international')),
    ('personnel', _(u'personnel')),
])

COMMUNES = create_dl([
    ('anderlecht', _(u'anderlecht')),
    ('auderghem', _(u'auderghem')),
    ('berchemsainteagathe', _(u'berchemsainteagathe')),
    ('bruxellesville', _(u'bruxellesville')),
    ('etterbeek', _(u'etterbeek')),
    ('evere', _(u'evere')),
    ('forest', _(u'forest')),
    ('ganshoren', _(u'ganshoren')),
    ('ixelles', _(u'ixelles')),
    ('jette', _(u'jette')),
    ('koekelberg', _(u'koekelberg')),
    ('molenbeeksaintjean', _(u'molenbeeksaintjean')),
    ('saintgilles', _(u'saintgilles')),
    ('saintjossetennoode', _(u'saintjossetennoode')),
    ('schaerbeek', _(u'schaerbeek')),
    ('uccle', _(u'uccle')),
    ('watermaelboitsfort', _(u'watermaelboitsfort')),
    ('woluwesaintlambert', _(u'woluwesaintlambert')),
    ('woluwesaintpierre', _(u'woluwesaintpierre')),
])
