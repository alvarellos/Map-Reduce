#!/usr/bin/env python

from operator import itemgetter
import sys

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 16:
        # Algo ha pasado, nos saltamos esta linea
        continue

    # parseamos la entrada que hemos obtenido del mapper.py
    idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, maximo, minimo, media = data_mapped

    # pasamos los valores de string a float

    try:
	Float_gsm19023 = float(gsm19023)
	Float_gsd19024 = float(gsd19024)
	Float_gsd19025 = float(gsd19025)
	Float_gsd19026 = float(gsd19026)

    except ValueError:
        # si alguno no es un numero, descartamos la linea
        continue

    maximo = max(Float_gsm19023, Float_gsd19024, Float_gsd19025, Float_gsd19026)
    minimo = min(Float_gsm19023, Float_gsd19024, Float_gsd19025, Float_gsd19026)
    media = (Float_gsm19023 + Float_gsd19024 + Float_gsd19025 + Float_gsd19026) / 4.0

    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}".format(idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, maximo, minimo, media)

