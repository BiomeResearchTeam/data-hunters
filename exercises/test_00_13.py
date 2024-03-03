def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    for ingrediente in lista_spesa:
        if ingrediente.lower() == "mascarpone":
            mascarpone_presente = True

    assert mascarpone_presente, "Il mascarpone non è presente nella lista della spesa."


    __msg__.good("Well done!")
