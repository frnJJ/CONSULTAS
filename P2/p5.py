


def generar_lista ():
    frase = input('ingrese una frase')

    frase = frase.lower()

    lista = tuple(frase.split())

    return(lista)


def cant_palabras (lista, x):
    cant = 0
    for i in lista:
        if (x in i):
            cant+= 1
    return(cant)

lista = generar_lista()

print(lista)

x = input('ingrese la palabra a buscar')

cant = cant_palabras(lista, x)


print(f"la cantidad de palabras con la letra {x} son {cant}")
    

