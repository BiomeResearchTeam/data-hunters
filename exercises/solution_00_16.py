import pandas as pd

df = pd.read_csv("ERP131433_df.tsv", sep="\t")

#verifica la correttezza dell'informazione contenuta nella colonna "instrument_model"
modello = df["instrument_model"].unique()
print(modello)

#non è corretto
["VALORE SBAGLIATO"]

#crea una nuova colonna con l'informazione corretta
df["SKIOME_instrument_model"] = "Illumina MiSeq"
