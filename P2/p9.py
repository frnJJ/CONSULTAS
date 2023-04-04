
uno = {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"}
dos = {"D", "G"}
tres = {"B", "C", "M", "P"}
cuatro = {"F", "H", "V", "W", "Y"}
cinco = {"K"}
ocho = {"X", "J"}
diez = {"Q", "Z"}



def puntos (palabra):
    punt = 0
    for i in palabra:
        if (i in uno):
            punt+= 1
        elif (i in dos):
            punt+= 2
        elif (i in tres):
            punt+= 3
        elif (i in cuatro):
            punt+= 4
        elif (i in cinco):
            punt+= 5
        elif (i in ocho):
            punt+= 8
        elif (i in diez):
            punt+= 10
    return punt

pal = " a "
while (pal != 'fin'):
    pal = input('ingrese la palabra')
    pal = pal.upper()
    print(puntos(pal))
