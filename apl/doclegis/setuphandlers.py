from zope.interface import alsoProvides
from apl.doclegis.browser.doclegisview import IDocLegisView


def testSetup(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('apl_doclegis_test.txt') is None:
        return

    site = context.getSite()
    portal_workflow = site.portal_workflow
    folder_id = site.invokeFactory('Folder',
                                   'Documents',
                                   language='fr')
    folder_fr = getattr(site, folder_id)
    portal_workflow.doActionFor(folder_fr, 'publish')
    folder_fr.setLayout('doclegis_view')
    alsoProvides(folder_fr, IDocLegisView)
    folder_id = site.invokeFactory('Folder',
                                   'Documenten',
                                   language='nl')
    folder_nl = getattr(site, folder_id)
    folder_nl.setLayout('doclegis_view')
    portal_workflow.doActionFor(folder_nl, 'publish')
    folder_nl.addTranslationReference(folder_fr)

    for i in range(15):
        doclegis_fr = create_doclegis(folder_fr, i, 'fr')
        portal_workflow.doActionFor(doclegis_fr, 'publish')

        doclegis_nl = create_doclegis(folder_nl, i, 'nl')
        portal_workflow.doActionFor(doclegis_nl, 'publish')
        doclegis_nl.addTranslationReference(doclegis_fr)


def create_doclegis(folder, num, lang):
    doclegis_id = folder.invokeFactory(
        'DocLegis',
        'DocumentLeg-{}-{}'.format(lang, num),
        language=lang)
    doclegis = getattr(folder, doclegis_id)
    doclegis.setTitle('DocumentLeg-{}-{}'.format(lang, num))
    doclegis.setText('Corps de texte {} {}'.format(lang, num))
    docum_type = ['loi', 'ordonnance', 'circulaire']
    doclegis.setDocument_type(docum_type[num % len(docum_type)])
    doclegis.setAdministration('communes')
    doclegis.setCommune('uccle')
    return doclegis
