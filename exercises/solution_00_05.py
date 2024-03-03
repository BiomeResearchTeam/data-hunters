import pandas as pd 

df = pd.read_csv("ERP131433_df.tsv", sep = "\t")

colonne = df.columns
lista_colonne = colonne.to_list()
print(lista_colonne)
