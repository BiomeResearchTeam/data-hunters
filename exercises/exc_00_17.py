import pandas as pd

df = pd.read_csv("ERP131433_df.tsv", sep="\t")

colonne = df.___.___()
colonne_trovate = ___

#cerca il valore "Italy" per capire se esiste una colonna "individuals_nationality"
for colonna in ___:
    if ___.lower() in colonna.___():
        ___.append(___)
    else:
        pass

if ___(___)>0:
    for colonna in colonne_trovate:
        print(colonna, ___.unique())
else:
    print("nessuna colonna trovata!")

#supponiamo che non è stata trovata nessuna colonna contente "Italy": crea la colonna "SKIOME_individuals_nationality"
df___ = "Italy"
