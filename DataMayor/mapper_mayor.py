#!/usr/bin/python
 
import sys
 
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) == 16:
	    idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, maximo, minimo, media = data


    if 100.0 <= float(gsm19023) <= 1000.0:
    	print media
