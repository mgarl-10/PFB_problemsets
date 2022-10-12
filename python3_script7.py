#!/usr/bin/env python3
import sys
dna = sys.argv[1]
dna_upper=dna.upper()
dna_lower=dna_upper.lower()
dna_replacing_A=dna_lower.replace("a","T") 
dna_replacing_T=dna_replacing_A.replace("t","A")
dna_replacing_G=dna_replacing_T.replace("g","C")
dna_replacing_C=dna_replacing_G.replace("c","G") 
dna_reverse=dna_replacing_C[::-1]

print(f"The reverse complement of {dna} is {dna_reverse}")

