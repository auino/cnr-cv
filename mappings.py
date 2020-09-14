from data_publications import *
from utils import reorder, setattribute, loadfromtxtfile, loadfromjsonfile

# loading the list of publications
PUBLICATIONS_JOURNALS = reorder(setattribute(PUBLICATIONS_JOURNALS, 'type', 'Articolo su rivista'), 'year')
PUBLICATIONS_CONFERENCES = reorder(setattribute(PUBLICATIONS_CONFERENCES, 'type', 'Conference Proceeding'), 'year')
#ALL_PUBLICATIONS = reorder(PUBLICATIONS_JOURNALS + PUBLICATIONS_CONFERENCES, 'year')
RESPONSIBILITIES_LAB = reorder(RESPONSIBILITIES_LAB, 'year')
MONOGRAFIES = reorder(loadfromtxtfile('data_monografies.txt'), 'year')
PATENTS = reorder(loadfromjsonfile('data_patents.json'), 'year')

# the separator used for muliple field mappings
separator = '\n\n'

# the list of paragraphs to remove from text
paragraphstoremove = [
	{
		'enabled':True,
		'paragraphsindex':6
	},
	{
		'enabled':True,
		'paragraphsindex':[27,28,29,30,31,32,33,34,35,36,37,38,39]
	}
]

# the list of headers replacements to do
headers_mappings = [
	{
		'enabled':True,
		'paragraphindex':9,
		'style':'bold',
		'text': 'CANDIDATO: ENRICO CAMBIASO'
	},
	{
		'enabled':True,
		'paragraphindex':11,
		'style':'bold',
		'text': 'MATRICOLA: 17440'
	},
	{
		'enabled':True,
		'paragraphindex':13,
		'style':'bold',
		'text': 'STRUTTURA DI APPARTENENZA: Istituto di Elettronica e di Ingegneria dell\'Informazione e delle Telecomunicazioni (IEIIT)'
	}
]

# the list of mappings
mappings = [
	{
		'enabled':True,
		'type':'mixed',
		'tableindex':0,
		'mappings': [
			{
				'enabled':True,
				'list':PUBLICATIONS_JOURNALS,
				'tableindex':0,
				'mappings':[
					{'row':0, 'text':'Nr. {COUNT}', 'style':'bold', 'marker':{'type':'index', 'name':'{COUNT}'}},
					{'row':1, 'text':'Tipologia prodotto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'type'}},
					{'row':2, 'text':'Titolo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'title'}},
					{'row':3, 'text':'Elenco autori: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'authors'}},
					{'row':4, 'text':'Ruolo svolto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'role'}},
					{'row':5, 'text':'Rivista: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'journal'}},
					{'row':6, 'text':'Codice identificativo (ISSN): {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'issn'}},
					{'row':7, 'text':'Anno di pubblicazione: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'year'}},
					{'row':8, 'text':'Impact Factor rivista: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'impactfactor'}},
					{'row':9, 'text':'Categoria della rivista secondo classificazione ANVUR: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'anvurcategory'}},
					{'row':10, 'text':'Numero citazioni: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'citation'}},
					{'row':11, 'text':'Altre informazioni: {V}', 'marker':{'type':'multiple','name':'{V}','separator':separator,'values':[{'text':'Riferimenti: {V}','marker':{'type':'field','name':'{V}','field':'reference'}},{'text':'DOI: {V}','marker':{'type':'field','name':'{V}','field':'doi'}}]}}
				]
			},
			{
				'enabled':True,
				'tableindex':1,
				'list':PUBLICATIONS_CONFERENCES,
				'mappings':[
					{'row':0, 'text':'Nr. {COUNT}', 'style':'bold', 'marker':{'type':'index', 'name':'{COUNT}'}},
					{'row':1, 'text':'Tipologia prodotto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'type'}},
					{'row':2, 'text':'Titolo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'title'}},
					{'row':3, 'text':'Nr. pagine libro: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'pages_book'}},
					{'row':4, 'text':'Nr. pagine: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'pages'}},
					{'row':5, 'text':'Elenco autori: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'authors'}},
					{'row':6, 'text':'Codice identificativo (ISBN o ISSN): {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'isbn'}},
					{'row':7, 'text':'Anno di pubblicazione: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'year'}},
					{'row':8, 'text':'Altre informazioni: {V}', 'marker':{'type':'multiple','name':'{V}','separator':separator,'values':[{'text':'Libro: {V}','marker':{'type':'field','name':'{V}','field':'book'}},{'text':'Conferenza: {V}','marker':{'type':'field','name':'{V}','field':'conference'}},{'text':'DOI: {V}','marker':{'type':'field','name':'{V}','field':'doi'}}]}}
				]
			},
			{
				'enabled':True,
				'tableindex':2,
				'list':MONOGRAFIES,
				'mappings':[
					{'row':0, 'text':'Nr. {COUNT}', 'style':'bold', 'marker':{'type':'index', 'name':'{COUNT}'}},
					{'row':1, 'text':'Tipologia prodotto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'type'}},
					{'row':2, 'text':'Titolo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'title'}},
					{'row':3, 'text':'Nr. pagine: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'pages'}},
					{'row':4, 'text':'Codice identificativo (ISBN): {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'isbn'}},
					{'row':5, 'text':'Anno di pubblicazione: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'year'}},
					{'row':6, 'text':'Altre informazioni: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'notes'}}
				]
			},
			{
				'enabled':True,
				'tableindex':3,
				'list':PATENTS,
				'mappings':[
					{'row':0, 'text':'Nr. {COUNT}', 'style':'bold', 'marker':{'type':'index', 'name':'{COUNT}'}},
					{'row':1, 'text':'Tipo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'type'}},
					{'row':2, 'text':'Titolo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'title'}},
					{'row':3, 'text':'Nr. brevetto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'number'}},
					{'row':4, 'text':'Elenco autori: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'authors'}},
					{'row':5, 'text':'Ruolo svolto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'role'}},
					{'row':6, 'text':'Anno di deposito/registrazione: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'year'}},
					{'row':7, 'text':'Contratti stipulati: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'contracts'}},
					{'row':8, 'text':'Livello di diffusione: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'diffusionlevel'}},
					{'row':9, 'text':'Altre informazioni: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'notes'}}
				]
			}
		]
	},
	{
		'enabled':True,
		'tableindex':7,
		'list':RESPONSIBILITIES_LAB,
		'mappings':[
			{'row':0, 'text':'Nr. {COUNT}', 'style':'bold', 'marker':{'type':'index', 'name':'{COUNT}'}},
			{'row':1, 'text':'Ruolo svolto: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'role'}},
			{'row':2, 'text':'Struttura: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'structure'}},
			{'row':3, 'text':'Riferimento o n. protocollo: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'protocol'}},
			{'row':4, 'text':'Periodi di attività: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'period'}},
			{'row':5, 'text':'Altre informazioni: {V}', 'marker':{'type':'field', 'name':'{V}', 'field':'notes'}}
		]
	}
]
