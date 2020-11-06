class IndiceMasaCorporal(object):

    def calcula_imc(kg, m2):
        imc = kg/(m2 * m2)
        return imc

    if __name__ == '__main__':
        print("Ejemplo de entrada para el pesos: 53.2")
        print("Ejemplo de entrada para la alturas: 1.67")

        print("\nEscribe el peso en kilogramos: ")
        kg = float(input())

        print("\nEscribe la altura en metros: ")
        m2 = float(input())

        imc = calcula_imc(kg, m2)

        print("\nTu IMC es: " + str(round(imc, 3)))
