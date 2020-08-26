from data import *
from utils import reorder, setattribute

PUBLICATIONS_JOURNALS = reorder(setattribute(PUBLICATIONS_JOURNALS, 'type', 'Articolo su rivista'), 'year')
PUBLICATIONS_CONFERENCES = reorder(setattribute(PUBLICATIONS_CONFERENCES, 'type', 'Conference Proceeding'), 'year')
#ALL_PUBLICATIONS = reorder(PUBLICATIONS_JOURNALS + PUBLICATIONS_CONFERENCES, 'year')

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

mappings = [
	{
		'enabled':True,
		'tableindex':0,
		'list':PUBLICATIONS_JOURNALS,
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
			{'row':11, 'text':'Altre informazioni: {V}', 'marker':{'type':'multiple','name':'{V}','separator':'. ','values':[{'text':'Riferimenti: {V}','marker':{'type':'field','name':'{V}','field':'reference'}},{'text':'DOI: {V}','marker':{'type':'field','name':'{V}','field':'doi'}}]}}
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
			{'row':8, 'text':'Altre informazioni: {V}', 'marker':{'type':'multiple','name':'{V}','separator':'. ','values':[{'text':'Libro: {V}','marker':{'type':'field','name':'{V}','field':'book'}},{'text':'Conferenza: {V}','marker':{'type':'field','name':'{V}','field':'conference'}},{'text':'DOI: {V}','marker':{'type':'field','name':'{V}','field':'doi'}}]}}
		]
	}
]
