print("------ Para deterner presiona < Ctrl + c > ------")

while True:
    print("\nEscriba el costo de la compra: ")

    costo = float(input())

    if costo > 100:
        descuento = .10
        nuevo_costo = costo - (costo * descuento)
        print("\nSu total con decuento aplicado es: $" + str(nuevo_costo))
    else:
        print("\nSu compra no supera los $100, su total es $" + str(costo))
