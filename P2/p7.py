
import string


def retur_list (txt):
    lista = txt.split()
    return(lista)

def cant (lista,may,min):
    cant_nochar= 0
    cant_min= 0
    cant_may= 0
    for i in lista:
        if (i in may):
            cant_may+= 1
        elif(i in min):
            cant_min+= 1
        else:
            cant_nochar+= 1
    return(cant_min,cant_may,cant_nochar)

texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
 """

letters_may = string.ascii_uppercase
letters_min = string.ascii_lowercase
total = [0, 0, 0]


lista = retur_list(texto)
for i in range(0,len(lista)):
    dicc= cant(lista[i], letters_may, letters_min)
    total[0] += dicc[0]
    total[1] += dicc[1]
    total[2] += dicc[2]
   
print(total)

