import pandas as pd

df = pd.read_csv("ERP131433_df.tsv", sep="\t")

colonne = df.columns.to_list()
colonne_trovate = []

#cerca il valore Italy per capire se esiste una colonna "individuals_nationality"
for colonna in colonne:
    if "Italy".lower() in colonna.lower():
        colonne_trovate.append(colonna)
    else:
        pass

if len(colonne_trovate)>0:
    for colonna in colonne_trovate:
        print(colonna, df[colonna].unique())
else:
    print("nessuna colonna trovata!")

#supponiamo che non è stata trovata nessuna colonna contente "Italy": crea la colonna "SKIOME_individuals_nationality"
df["SKIOME_individuals_nationality"] = "Italy"

