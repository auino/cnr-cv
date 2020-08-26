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

Aprire il file `data.py` e inserire i propri elementi del curriculum vitae, in formato JSON, raggruppati secondo le proprie preferenze (nell'esempio, si distingue tra contributi su rivista e contributi a conferenze di natura scientifica).
La struttura degli oggetti JSON non è fissata ed è aperta in base alle proprie preferenze, benché si mantenga la stessa struttura per tutti gli oggetti dello stesso tipo.

Dunque, aprire il file `mappings.py` ed impostare l'oggetto `mappings` in modo da configurare il match tra gli oggetti JSON memorizzati in `data.py` e il contenuto da riportare all'interno del file Word, come da template CNR (rappresentato dal file `input.docx`).
Per ogni oggetto:
* `enabled` identifica se la creazione degli oggetti per la voce corrente è abilitata o meno (se disabilitata, verrà ignorata e gli oggetti non verranno inclusi nel CV prodotto)
* `tableindex` identifica l'indice della tabella nel file `input.docx`, a partire da `0`
* `list` identifica la lista di oggetti da considerare per il "riempimento" della voce corrente, a partire dalla loro definizione all'interno del file `data.py`
* `mappings` identifica il match da considerare, come definito sopra

Fare in generale riferimento all'esempio fornito per comprendere al meglio la struttura considerata.

### Esecuzione ###

Per poter eseguire il programma, aprire il terminale e lanciare il seguente comando:
```
python convert.py
```

Verrà generato il file `output.docx` del proprio curriculum vitae.
Come operazione finale, controllare il risultato prodotto (nell'esempio fornito, è ad esempio importante ricordarsi di aggiungere i propri riferimenti nella prima pagina) e generare un eventuale file PDF definitivo.

### Contatti ###

I recapiti del sottoscritto sono reperibili al sito [CNR-IEIIT](http://ieiit.cnr.it).

Sono anche disponibile su Twitter come [@auino](https://twitter.com/auino).
