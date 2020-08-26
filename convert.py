from docx import Document

from data import *
from utils import addtables, deletetables
from mappings import *

REPLACEORIGINALTABLE = True

DELETEUNUSEDTABLES = True

doc = Document('input.docx')

usedtableindexes = []
for p in mappings:
	if not p['enabled']: continue
	addtables(doc, p['tableindex'], p['list'], p['mappings'], replaceoriginaltable=REPLACEORIGINALTABLE)
	usedtableindexes.append(p['tableindex'])

if DELETEUNUSEDTABLES: deletetables(doc, usedtableindexes, 'Nessun elemento in questa categoria.')

doc.save('output.docx')
