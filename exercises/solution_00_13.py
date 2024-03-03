lista_spesa = ["SavOIArdi", "maScaRpOne", "caFFè", "cAcAO"]

#supponi che la lista della spesa è stata scritta dal tuo cuginetto che va in seconda elementare. 
#le lettere sono state scritte randomicamente un po' maiuscole e un po' minuscole.
#inoltre immagina che tu sia di frettissima e non sia riuscito a leggerla in anticipo,
#quindi ti trovi al banco frigo del supermercato, e l'unica cosa che ti interessa sapere a questo punto è:
#c'è il mascarpone nella lista della spesa?

#usa un ciclo for per indagare ogni ingrediente della lista_spesa
for ingrediente in lista_spesa:

    #non sapendo come il tuo cuginetto ha scritto mascarpone, forse ti conviene trasformare ogni ingrediente in minuscolo, no?
    if ingrediente.lower() == "mascarpone":
        print("Sì, nella lista della spesa c'è il mascarpone")
    else:
        print("No, niente mascarpone")

#digita l'output:
No, niente mascarpone
Sì, nella lista della spesa c'è il mascarpone
No, niente mascarpone
No, niente mascarpone