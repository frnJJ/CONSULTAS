
texto1 = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python.
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""


def retornar_titulo(oracion):
    if (len(oracion)-1 <= 10):
        titulo = "ok"
    else:
        titlo =  "not ok"
    return(titulo)

def retornar_oraciones(lista):
    cant = [[0,"facil"],[0,"aceptable"],[0,"dificil"],[0,"muy dificil"]]
    for i in range(1,len(lista)):
        aux = lista[i].split()
        longitud = len(aux)
        if (longitud < 12):
            cant[0][0] += 1
        elif (longitud < 18):
            cant[1][0] += 1
        elif (longitud < 25):
            cant[2][0] += 1
        else:
            cant[3][0] += 1
    return(cant)




texto1 = texto1.lower()
lista = tuple(texto1.split("."))
tit = lista[0].split()



titulo = retornar_titulo(tit)

cant = retornar_oraciones(lista)


print(f"El titulo esta {titulo}")
print(cant)










