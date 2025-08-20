import sysconfig
#print(sysconfig.get_paths()["stdlib"])

#import os
#print(os.__file__)
#print(os.__doc__)

#import random
#print(random.__doc__)
#print(random.__file__)

#import math
#print(math.__doc__)   # Zeigt die interne Dokumentation an
# print(math.__file__)  # Gibt einen Fehler aus – es ist ein eingebautes Modul und in C geschrieben



import sys
print(sys.builtin_module_names)


"""
Manche Module wie math oder sys sind tief im Python-Interpreter integriert und haben keine .py-Datei 
– man nennt sie eingebaute C-Module.

Interner Quellcode des Moduls math :
https://github.com/python/cpython/blob/main/Modules/mathmodule.c

Andere wie random oder os gehören zwar auch zur Standardbibliothek, sind aber in Python geschrieben 
und liegen als .py-Dateien im Lib/-Ordner.

"""


