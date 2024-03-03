---
title: "Chapter 0: WORKSHOP'S FUNDAMENTALS'"
description:
  "In questo capitolo tratteremo tutti i comandi necessari per svolgere gli step del workshop"
prev: null
next: /chapter1
type: chapter
id: 0
---

<exercise id="1" title="PANDAS" type="slides">
<slides source="chapter0_01_pandas">
</slides>
</exercise>


<exercise id="2" title="DATAFRAME" type="slides">
<slides source="chapter0_02_dataframe">
</slides>
</exercise>


<exercise id="3" title="HANDS ON DATAFRAME">
È tempo di mettere le mani in pasta, cioè in Python!

POV: sei un partecipante del workshop Data Hunters e vuoi curare i metadati del progetto ERP131433. Il primo passaggio che devi fare è leggere il file ERP131433_df.tsv come DataFrame. Provaci!
<codeblock id="00_03">

* Ti sei ricordato di importare Pandas prima di utilizzare una sua funzione?
* Ricorda di indicare il nome del file e il separatore!
</codeblock>
</exercise>


<exercise id="4" title="DATAFRAME MANIPULATION" type="slides">
<slides source="chapter0_04_dataframe-columns">
</slides>
</exercise>


<exercise id="5" title="HANDS ON DATAFRAME">
È tempo di mettere in pratica quanto imparato!

POV: sei un partecipante del workshop Data Hunters e vuoi curare i metadati del progetto ERP131433. Ricordati di importare Pandas, leggere il dataframe, e prova a vedere da quali colonne è formato!
<codeblock id="00_05">

* Qui devi usare due metodi che hai imparato nelle slide precenti: qualcosa sulle colonne e sulla lista...
</codeblock>
```out
['study_accession', 'secondary_study_accession', 'sample_accession', 'secondary_sample_accession', 'experiment_accession', 'run_accession', 'submission_accession', 'tax_id', 'scientific_name_exp', 'instrument_platform', 'instrument_model', 'library_name', 'library_layout', 'library_strategy', 'library_source', 'library_selection', 'read_count', 'base_count', 'center_name_exp', 'first_public', 'last_updated', 'experiment_title', 'study_title', 'study_alias', 'experiment_alias', 'run_alias', 'fastq_bytes', 'fastq_md5', 'fastq_ftp', 'fastq_aspera', 'fastq_galaxy', 'sample_alias', 'sample_title', 'first_created', 'center_name_sam', 'PRIMARY_ID', 'EXTERNAL_ID', 'SUBMITTER_ID', 'TITLE', 'TAXON_ID', 'SCIENTIFIC_NAME', 'ENA-FASTQ-FILES', 'ENA-SUBMITTED-FILES', 'organism', 'ENA-FIRST-PUBLIC', 'ENA-LAST-UPDATE', 'DESCRIPTION', 'submitted_bytes', 'submitted_md5', 'submitted_ftp', 'submitted_aspera', 'submitted_galaxy', 'submitted_format', 'ENA-CHECKLIST', 'collection date', 'host sex', 'host subject id', 'nominal_length', 'geographic location (country and/or sea)', 'project name', 'environment (material)', 'geographic location (longitude)', 'geographic location (latitude)', 'investigation type', 'sequencing method', 'environment (biome)', 'environment (feature)', 'human skin environmental package', 'DOI', 'common name', 'host disease status', 'host body-mass index', 'host site']
```
</exercise>


<exercise id="6" title="DATAFRAME MANIPULATION" type="slides">
<slides source="chapter0_06_dataframe-columns-extraction">
</slides>
</exercise>


<exercise id="7" title="HANDS ON DATAFRAME">
Ottimo, ti va di mettere in pratica quello che hai imparato?

POV: sei un partecipante del workshop Data Hunters e vuoi curare i metadati del progetto ERP131433. Seleziona la colonna "DOI" e visualizza i suoi valori unici!
<codeblock id="00_07">

* Allora facciamo mente locale: abbiamo imparato i metodi per ricavare il nome delle colonne, per rendere una variabile una lista, e selezionare solo i valori unici di una colonna...
</codeblock>
```out
['study_accession', 'secondary_study_accession', 'sample_accession', 'secondary_sample_accession', 'experiment_accession', 'run_accession', 'submission_accession', 'tax_id', 'scientific_name_exp', 'instrument_platform', 'instrument_model', 'library_name', 'library_layout', 'library_strategy', 'library_source', 'library_selection', 'read_count', 'base_count', 'center_name_exp', 'first_public', 'last_updated', 'experiment_title', 'study_title', 'study_alias', 'experiment_alias', 'run_alias', 'fastq_bytes', 'fastq_md5', 'fastq_ftp', 'fastq_aspera', 'fastq_galaxy', 'sample_alias', 'sample_title', 'first_created', 'center_name_sam', 'PRIMARY_ID', 'EXTERNAL_ID', 'SUBMITTER_ID', 'TITLE', 'TAXON_ID', 'SCIENTIFIC_NAME', 'ENA-FASTQ-FILES', 'ENA-SUBMITTED-FILES', 'organism', 'ENA-FIRST-PUBLIC', 'ENA-LAST-UPDATE', 'DESCRIPTION', 'submitted_bytes', 'submitted_md5', 'submitted_ftp', 'submitted_aspera', 'submitted_galaxy', 'submitted_format', 'ENA-CHECKLIST', 'collection date', 'host sex', 'host subject id', 'nominal_length', 'geographic location (country and/or sea)', 'project name', 'environment (material)', 'geographic location (longitude)', 'geographic location (latitude)', 'investigation type', 'sequencing method', 'environment (biome)', 'environment (feature)', 'human skin environmental package', 'DOI', 'common name', 'host disease status', 'host body-mass index', 'host site']
```

```out
['https://doi.org/10.1038/s41598-022-19676-6']
```
</exercise>


<exercise id="8" title="DATAFRAME MANIPULATION" type="slides">
<slides source="chapter0_08_dataframe-manipulation-cols-presenti">
</slides>
</exercise>


<exercise id="9" title="HANDS ON DATAFRAME">
Eccoci: è la tua opportunità di testare tutto quello che hai imparato!

POV: sei un partecipante del workshop Data Hunters e vuoi curare i metadati del progetto ERP131433. Estrai il valore unico della colonna "library_strategy" e crea una nuova colonna con il valore corretto.
<codeblock id="00_09">

* Ti ricordi come creare una nuova colonna? Dai è simile a estrarre una colonna esistente!
</codeblock>
</exercise>


<exercise id="10" title="DATAFRAME MANIPULATION" type="slides">
<slides source="chapter0_10_dataframe-manipulation-cols-non-presenti">
</slides>
</exercise>


<exercise id="11" title="HANDS ON DATAFRAME">
Bene, mettiamo in pratica il for e l'if. Esercitiamoci un po' su questi due concetti prima di ritornare a curare i nostri metadati.

<codeblock id="00_11">

* Con il ciclo for, ogni elemento di una lista viene preso uno alla volta...
</codeblock>

<codeblock id="00_12">

* Con l'istruzione if, se la condizione è vera si esegue il blocco di comandi dopo l'if, altrimenti il blocco di comandi dopo l'else
</codeblock>
</exercise>


<exercise id="13" title="HANDS ON DATAFRAME">
A questo punto aggiungiamo i nuovi metodi imparati (.lower() e .append()) al for e all'if, prima di ritornare a curare i nostri metadati.

<codeblock id="00_13">

* Itera i diversi ingredienti della lista_spesa e verifica se l'ingrediente è uguale a "mascarpone". Come sarà scritto mascarpone nella tua lista? Rendi ogni ingrediente minuscolo!
</codeblock>

<codeblock id="00_14">

* Crea una lista vuota a cui appendere l'ingrediente mascarpone, qualora fosse presente nella lista_spesa!
</codeblock>

```out
mascarpone
```

</exercise>


<exercise id="15" title="DATAFRAME MANIPULATION" type="slides">
<slides source="chapter0_15_dataframe-manipulation-cols-non-presenti">
</slides>
</exercise>


<exercise id="16" title="HANDS ON DATAFRAME">
Vedo già il traguardo, siamo alle battute finali!

POV: sei un partecipante del workshop Data Hunters e vuoi curare i metadati del progetto ERP131433. Nel primo esercizio, verifica la correttezza del valore contenuto nella colonna onnipresente. Nel secondo esercizio,verifica la presenza di una delle 7 colonne non sempre presenti, ed eventualmente la correttezza dell'informazione contenuta!

<codeblock id="00_16">

* Sembra che il valore contenuto nella colonna sia sbagliato... crea una nuova colonna curata!
</codeblock>

<codeblock id="00_17">

* Crea una lista delle colonne dei metadati
* Crea una lista vuota per contenere il nome delle colonne che contengono "Italy"
* Se è stata trovata almeno una colonna che contiene "Italy" allora stampa il nome di questa colonna e i suoi valori unici, altrimenti stampa la frase "nessuna colonna trovata!"
* Crea la nuova colonna specifica per la nazionalità degli individui campionati
</codeblock>
</exercise>








<exercise id="10" title="to_csv" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>


<exercise id="11" title="CARICARE SU DATABASE" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>