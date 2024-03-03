#importa pandas e leggi il file come DataFrame
import pandas as pd
df = pd.read_csv("ERP131433_df.tsv", sep="\t")

#estrai il valore unico della colonna library_strategy e stampala
#il valore contenuto è sbagliato
strategia = df["library_strategy"].unique()
print(strategia)
["VALORE SBAGLIATO"]

#crea una nuova colonna chiamata "SKIOME_library_strategy" con il valore corretto
df["SKIOME_library_strategy"] = "AMPLICON"