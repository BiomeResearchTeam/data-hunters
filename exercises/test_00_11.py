def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    lista_spesa = ["savoiardi", "mascarpone", "caffè", "cacao"]
    risultato_effettivo = [ingrediente for ingrediente in lista_spesa]
    assert risultato_effettivo == lista_spesa, "Il ciclo for non produce l'output atteso."

    __msg__.good("Well done!")
