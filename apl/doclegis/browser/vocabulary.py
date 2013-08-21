# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary
import zope.interface
from z3c.form import interfaces
from apl.doclegis import doclegisMessageFactory as _
from Products.Archetypes.utils import DisplayList


TYPE = DisplayList([
    ('loi', _(u'Loi')),
    ('ordonnance', _(u'Ordonnance')),
    ('arreteroyal', _(u'Arrêté royal')),
    ('arretegouvernement', _(u'Arrêté gouvernement')),
    ('circulaire', _(u'Circulaire')),
    ('reglement', _(u'Règlement')),
])

ADMINISTRATIONS = DisplayList([
    ('communes', _(u'Communes')),
    ('cpas', _(u'CPAS')),
    ('cultesetlaicite', _(u'Cultes et laïcité')),
    ('intercommunales', _(u'Intercommunales')),
    ('rescommunales', _(u'rés communales')),
    ('zonesdepolice', _(u'Zones de police')),
    ('lemontdepiete', _(u'Le Mont-de-Piété')),
    ('lesassociationschapitrexii',
        _(u'Les associations Chapitre XII')),
    ('lereseauhospitalieriris',
        _(u'Le réseau hospitalier IRIS')),
])

THEMES = DisplayList([
    ('cultesetlaicite', _(u'Cultes et laïcité')),
    ('elections', _(u'Elections')),
    (' fiscalite', _(u' Fiscalité')),
    ('marchespublics', _(u'Marchés publics')),
    ('soutienfinancier', _(u'Soutien financier')),
    ('egalitedeschancesetdiversite', _(u'Egalité des chances et diversité')),
    ('finances', _(u'Finances')),
    ('international', _(u'International')),
    ('personnel', _(u'Personnel')),
])

COMMUNES = DisplayList([
    ('anderlecht', _(u'Anderlecht')),
    ('auderghem', _(u'Auderghem')),
    ('berchemsainteagathe', _(u'Berchem-Sainte-Agathe')),
    ('bruxellesville', _(u'Bruxelles-Ville')),
    ('etterbeek', _(u'Etterbeek')),
    ('evere', _(u'Evere')),
    ('forest', _(u'Forest')),
    ('ganshoren', _(u'Ganshoren')),
    ('ixelles', _(u'Ixelles')),
    ('jette', _(u'Jette')),
    ('koekelberg', _(u'Koekelberg')),
    ('molenbeeksaintjean', _(u'Molenbeek-Saint-Jean')),
    ('saintgilles', _(u'Saint-Gilles')),
    ('saintjossetennoode', _(u'Saint-Josse-ten-Noode')),
    ('schaerbeek', _(u'Schaerbeek')),
    ('uccle', _(u'Uccle')),
    ('watermaelboitsfort', _(u'Watermael-Boitsfort')),
    ('woluwesaintlambert', _(u'Woluwe-Saint-Lambert')),
    ('woluwesaintpierre', _(u'Woluwe-Saint-Pierre')),
])
