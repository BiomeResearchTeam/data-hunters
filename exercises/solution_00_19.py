#per questa ultima volta ti abbuono tutti i passaggi precedenti...
#supponiamo di avere curato le 9 colonne del DataFrame df e ora vogliamo salvarlo con il nome "SKIOME_ERP131433_df.tsv"

df.to_csv("SKIOME_ERP131433_df.tsv", sep = "\t", index=False)