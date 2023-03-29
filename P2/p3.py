from collections import Counter
import string


jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

letras = string.ascii_letters

x = input('ingrese un caracter a buscar')
jupyter_info = jupyter_info.lower()

lista = jupyter_info.split()

if (not (x in letras)):
    print('ERROR: Var Modulo String')
else: 
    print([i for i in lista if i.startswith(x)])




