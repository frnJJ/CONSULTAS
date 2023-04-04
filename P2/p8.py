
def heterograma (palabra):
    ok = True
    palabra = palabra.split()
    for i in palabra:
        print(i)
        if (not (palabra.count(i) == 1)):
            ok = False
    return ok

palabra = ""           
while (palabra != "fin" ):
    palabra = input('ingrese la palabra a verificar')
    print(["Es heterograma" if heterograma(palabra) else "No es heterograma"])
