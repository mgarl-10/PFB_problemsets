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

print(f"Original sequence 5'{dna} 3'\nComplement 3'{dna_replacing_C} 5'\nReverse complement 5'{dna_reverse} 3'")
