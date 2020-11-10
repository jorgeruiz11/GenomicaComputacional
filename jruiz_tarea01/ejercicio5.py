import re

promotores = open("./promotores.txt", "r")
salida = open("./t1-5.txt", "w")

expr = re.compile("(AGATAG|TGATAG|AGATAA|TGATAA)")
instancias_por_secuencia = list()

archivo = promotores.readlines()

for linea in archivo:
    # Como queremos contar las apariciones entonces necesitamos buscar
    # cualquiera de las 4 expresiones en las cadenas del archivo promotores.txt
    # y después ver el tamaño.
    c = str(len(expr.findall(linea)))
    instancias_por_secuencia.append(c)
    # salida.write(c)


# La forma de escribirlos en el archivo será: [3,4,1,2,1,2,...] como se pide en
# el pdf de la tarea
salida.write("[")

for contados in instancias_por_secuencia:
    salida.write(contados + ", ")

salida.write("]")


promotores.close()
salida.close()
