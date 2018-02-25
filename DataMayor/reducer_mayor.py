#!/usr/bin/python

import sys

solucion = 0

# Recorremos los datos de entrada linea a linea y nos quedamos con el valor mayor
for line in sys.stdin:

    maximo = float(line)

    if maximo >= solucion:
        solucion = maximo

print solucion
