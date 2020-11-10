def lee_fasta(archivo):
    dna_una_linea = ""

    for linea in archivo.readlines():
        if not linea.startswith('>'):
            # quitamos los espacios y saltos de linea y vamos concatenando las
            # secuencias de ADN.
            dna_una_linea = dna_una_linea + linea.strip()

    return dna_una_linea


print("\n ---------- Archivo: nomascus_leucogenys ---------- \n")
print(lee_fasta(open("./nomascus_leucogenys", "r")))
print("\n ---------- Archivo: homo_sapiens ---------- \n")
print(lee_fasta(open("./homo_sapiens", "r")))
