def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert set(colonna_doi_unici) == set(df["DOI"]), "I valori unici della colonna 'DOI' non corrispondono ai valori effettivi."

    __msg__.good("Well done!")
