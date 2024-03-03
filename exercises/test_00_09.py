def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert df["SKIOME_library_strategy"].unique() == ["AMPLICON"], "Il valore della nuova colonna non è corretto."

    __msg__.good("Well done!")
