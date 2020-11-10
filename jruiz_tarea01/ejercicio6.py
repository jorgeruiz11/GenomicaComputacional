def complemento_inverso(cadena):
    cad_comp = ""

    for caracter in cadena:
        if caracter == 'A':
            cad_comp = cad_comp + 'T'
        elif caracter == 'T':
            cad_comp = cad_comp + 'A'
        elif caracter == 'C':
            cad_comp = cad_comp + 'G'
        else:
            cad_comp = cad_comp + 'C'

    # cad_comp[::-1] lo que hace es concatenar la cadena desde el final hasta
    # el inicio
    return cad_comp[::-1]


print(complemento_inverso("GATTACAAGT"))
