class AreaTriangulo(object):

    def calcula_area(b, h):
        area = (b * h)/2
        return area

    if __name__ == '__main__':
        print("\nEscribe la longitud de la base: ")
        b = float(input())

        print("\nEscribe la longitud de la altura: ")
        h = float(input())

        area = calcula_area(b, h)

        print("\nEl área es: " + str(round(area, 2)))
