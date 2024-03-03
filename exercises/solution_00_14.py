#beh scritto così, il comando di prima non è utilissimo... per ben 3 volte ti ha detto che il mascarpone
#non era nella lista perché l'ingrediente preso in considerazione non era il mascarpone...
#proviamo a creare una lista vuota che andremo a riempire solo se il mascarpone è presente!

lista_spesa = ["SavOIArdi", "maScaRpOne", "caFFè", "cAcAO"]
lista_mascarpone = []

for ingrediente in lista_spesa:
    if ingrediente.lower() == "mascarpone":
        lista_mascarpone.append(ingrediente)
    else:
        pass

print(lista_mascarpone)