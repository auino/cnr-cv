from docx import Document

from utils import addtables, deletetables
from mappings import *

# should the original table be deleted/replaced with content or kept as reference?
REPLACEORIGINALTABLE = True

# should unused tables be deleted or not?
DELETEUNUSEDTABLES = True
# replacement text when unused tables are deleted
DELETEUNUSEDTABLES_TEXT = 'Nessun elemento in questa categoria.'

# loading the template document
doc = Document('input.docx')

# updating headers
for h in headers_mappings:
	if not h['enabled']: continue
	doc.paragraphs[h['paragraphindex']].text = h['text']
	try:
		if h['style'] == 'bold': doc.paragraphs[h['paragraphindex']].runs[0].font.bold = True
	except: pass

# updating content
usedtableindexes = []
for p in mappings:
	if not p['enabled']: continue
	addtables(doc, p['tableindex'], p['list'], p['mappings'], replaceoriginaltable=REPLACEORIGINALTABLE)
	usedtableindexes.append(p['tableindex'])

# deleting unused tables, if needed
if DELETEUNUSEDTABLES: deletetables(doc, usedtableindexes, DELETEUNUSEDTABLES_TEXT)

# saving the output document
doc.save('output.docx')
