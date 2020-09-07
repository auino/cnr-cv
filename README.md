# cnr-cv

*This software is intended to be mainly used from Italian persons. This document is therefore written in Italian language. Nevertheless, code and included comments are in English language.*

### Introduzione ###

Questo programma permette la creazione di un curriculum vitae strutturato nel formato richiesto per i concorsi [CNR](http://www.cnr.it).
A partire dal template fornito dal CNR ed un file JSON costruito contenente tutte le voci del proprio curriculum vitae, viene generato il curriculum vitae definitivo.

L'idea alla base del progetto è quella di poter utilizzare un file JSON comune ad esempio con altre versioni del curriculum, oppure integrato con un sito web di istituto o personale, dunque, senza necessità di alterarlo, generare il curriculum vitae strutturato, nel formato richiesto per i concorsi CNR.

### Installazione ###

1. Assicurarsi che `python` versione `3` e `pip` siano installati:
```
python -V
```
2. Clonare il repository:
```
git clone https://github.com/auino/cnr-cv.git
```
3. Accedere alla directory del repository:
```
cd cnr-cv
```
4. Installare le dipendenze:
```
pip install -r requirements.txt
```
5. Sostituire il file `input.docx` con il file del template del curriculum vitae strutturato fornito dal CNR

### Configurazione ###

Aprire il file `mappings.py` ed impostare l'oggetto `mappings` in modo da configurare il match tra gli oggetti JSON memorizzati in `data.py` e il contenuto da riportare all'interno del file Word, come da template CNR (rappresentato dal file `input.docx`).
Per ogni oggetto:
* `enabled` identifica se la creazione degli oggetti per la voce corrente è abilitata o meno (se disabilitata, verrà ignorata e gli oggetti non verranno inclusi nel CV prodotto)
* `tableindex` identifica l'indice della tabella nel file `input.docx`, a partire da `0`
* `list` identifica la lista di oggetti da considerare per il "riempimento" della voce corrente, a partire dalla loro definizione all'interno del file `data.py`
* `mappings` identifica il match da considerare, come definito sopra

In modo analogo, all'interno del file `mappings.py`, impostare l'oggetto `headers_mappings` in base alle proprie necessità.

Fare in generale riferimento all'esempio fornito per comprendere al meglio la struttura considerata.

#### Tipologia di input ####

Per ogni tipologia di input, è stato fornito un esempio.
Inserire i propri elementi del curriculum vitae, secondo il formato preferito, raggruppati secondo le proprie preferenze (ad esempio, distinguendo tra contributi su rivista e contributi a conferenze di natura scientifica, monografie e brevetti).
La struttura degli oggetti non è fissata ed è aperta in base alle proprie preferenze, benché si mantenga la stessa struttura per tutti gli oggetti dello stesso tipo.

Sono disponibili tre tipologie di input:
* **Formato TXT:** (fare riferimento al file `data_monografies.txt`): in questo caso, all'interno di un file TXT, inserire gli elementi, separandoli tra loro con due caratteri newline; per ogni elemento, una riga coinciderà con un attributo, e chiave e valore considerati verranno separati dal carattere `:` (ad esempio: `title:My title` assegnerà alla chiave `title` il valore `My title`). In questo caso, come riportato all'interno del file `mappings.py` (che si suggerisce di consultare), è possibile caricare il file di input tramite il metodo (presente in `utils.py`) `loadfromtxtfile(<filename>)`
* **Formato JSON per ogni tipologia di elemento:** (fare riferimento al file `data_patents.json`): in questo caso, all'interno di un file JSON, inserire l'oggetto JSON che rappresenta la lista di elementi da inserire all'interno del curriculum vitae, per la voce/il raggruppamento corrente (es. tutte le pubblicazioni su rivista internazionale). In questo caso, come riportato all'interno del file `mappings.py` (che si suggerisce di consultare), è possibile caricare il file di input tramite il metodo (presente in `utils.py`) `loadfromjsonfile(<filename>)`
* **Formato JSON con più elementi:** (fare riferimento al file `data_publications.py`): in questo caso, all'interno di un file Python, inserire le variabili desiderate, con contenuto espresso in formato JSON. In questo caso, come riportato all'interno del file `mappings.py` (che si suggerisce di consultare), è possibile caricare il file di input tramite una semplice importazione Python quale ad esempio `from <filename> import *`

### Esecuzione ###

Per poter eseguire il programma, aprire il terminale e lanciare il seguente comando:
```
python convert.py
```

Verrà generato il file `output.docx` del proprio curriculum vitae.
Come operazione finale, controllare il risultato prodotto e generare un eventuale file PDF definitivo.

### TODO ###

* Migliorare la leggibilità del codice
* Descrivere i metodi supportati

### Contatti ###

I recapiti del sottoscritto sono reperibili al sito [CNR-IEIIT](http://ieiit.cnr.it).

Sono anche disponibile su Twitter come [@auino](https://twitter.com/auino).
