# Modificati repository Explosion per l'introduzione della lingua latina

## **[spaCy](https://github.com/Miriam1998/spaCy/tree/spacyLatin):** 

- website -> meta -> [languages.json](https://github.com/Miriam1998/spaCy/blob/spacyLatin/website/meta/languages.json):

```bash
{
	            "code": "la",
	            "name": "Latin",
	            "example": "Quanti aestimas ista cognoscere, et rebus terminos ponere?",
	            "has_examples": true
	        },
```

- spacy -> lang -> [la](https://github.com/Miriam1998/spaCy/tree/spacyLatin/spacy/lang/la):

    -[tokenizer_exceptions.py](https://github.com/Miriam1998/spaCy/blob/spacyLatin/spacy/lang/la/tokenizer_exceptions.py)

    -[tag_map.py](https://github.com/Miriam1998/spaCy/blob/spacyLatin/spacy/lang/la/tag_map.py)
  
    -[stop_words.py](https://github.com/Miriam1998/spaCy/blob/spacyLatin/spacy/lang/la/stop_words.py)

#### Pacchetto installato con il seguente comando:

```bash
pip install git+https://github.com/Miriam1998/spaCy.git@spacyLatin#egg=spaCy
```

### **[spacy-lookups-data](https://github.com/Miriam1998/spacy-lookups-data/tree/lemmaLatin):** 

- spacy-lookups-data -> [setup.cfg](https://github.com/Miriam1998/spacy-lookups-data/blob/lemmaLatin/setup.cfg):

```bash
la = spacy_lookups_data:la
```

-	spacy-lookups-data -> spacy_lookups_data -> [_init_.py](https://github.com/Miriam1998/spacy-lookups-data/blob/lemmaLatin/spacy_lookups_data/__init__.py):

```bash
la = {"lemma_lookup": get_file("la_lemma_lookup.json")}
```

-	spacy-lookups-data -> spacy_lookups_data -> [data](https://github.com/Miriam1998/spacy-lookups-data/tree/lemmaLatin/spacy_lookups_data/data):

    [la_lemma_lookup.json (lemmazione)](https://github.com/Miriam1998/spacy-lookups-data/blob/lemmaLatin/spacy_lookups_data/data/la_lemma_lookup.json)
    
#### Pacchetto installato con il seguente comando:

```bash
pip install git+https://github.com/Miriam1998/spacy-lookups-data.git@lemmaLatin#egg=spacy-lookups-data
```


## Installazione da un branch 

- [How to install Python package from GitHub? [duplicate]](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github)
    
- [pip install from git repo branch](https://stackoverflow.com/questions/20101834/pip-install-from-git-repo-branch)
    
- [VCS Support](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support)

## Addestramento e comandi

### [Convert](https://spacy.io/api/cli#convert)
Converte file nel [formato JSON](https://spacy.io/api/annotation#json-input) di SpaCy

### [Debug-data](https://spacy.io/api/cli#debug-data):

Analizza, esegui il debug e convalida i dati di formazione e sviluppo. Ottieni statistiche utili e trova problemi come annotazioni di entità non valide, dipendenze cicliche, etichette con dati bassi e altro ancora.

### [Train](https://spacy.io/api/cli#train):

```bash
python -m spacy train [lang] [output_path] [train_path] [dev_path] [+altri argomenti]
```

Dettagli per [training da cli](https://spacy.io/usage/training#spacy-train-cli)

### Aggiornare un modello statistico preesistente tramite cli:

Esempio:

```bash
python -m spacy train la latin cbma_ann_train6.json cbma_ann_test6.json -b model-best -p ner -R -n 10
```

| Argomento utilizzato   |                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| la                     | Specifica della lingua, per il latino è "la".                                                                  |
| latin                  | Directory dove vengono salvati i modelli di ciascuna iterazione. "latin" nome della directory dell'esempio.    |
| cbma_ann_train6.json   | Training set.                                                                                                  |
| cbma_ann_test6.json    | Validation set.                                                                                                |
| -b model-best          | Modello di base da aggiornare. "model-best" nome della directory del modello scelto come esempio da aggiornare.|
| -p ner                 | Componenti della pipeline da addestrare. Nell'esempio solo 'ner'.                                              |
| -R                     | Sostituire i componenti dal modello base.                                                                      |
| -n 10                  | Numero di iterazioni (default: 30).                                                                            |

#### Issues utili:

- [Error when trying to train NER component with CLI starting from a base model](https://github.com/explosion/spaCy/issues/4902)

- [spacy CLI train - KeyError [E022] when training an additional NER entity type with --base-mode](https://github.com/explosion/spaCy/issues/4465)

### [Aggiornamento di modelli tramite script](https://spacy.io/usage/training#example-train-ner)

### [Creazione del package e installazione tramite cli](https://spacy.io/api/cli#package)



