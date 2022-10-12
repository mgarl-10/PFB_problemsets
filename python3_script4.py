#!/usr/bin/env python3
import sys
dna = sys.argv[1]
dna_upper=dna.upper()
dna_replaced=dna_upper.replace('T','U')

print(f"The new sequence is {dna_replaced}.")
