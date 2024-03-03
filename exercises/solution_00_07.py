import pandas as pd

df = pd.read_csv("ERP131433_df.tsv", sep="\t")

#verifica che ci sia la colonna DOI nel tuo df, unisci nello stesso comando i due metodi che conosci!
lista_colonne = df.columns.to_list()
print(lista_colonne)

#estrai la colonna DOI e seleziona i suoi valori unici
colonna_doi_unici = df["DOI"].unique()
print(colonna_doi_unici)
