#!/usr/bin/env python3
import sys
dna = sys.argv[1]
dna_upper=dna.upper()
count_Aa=dna_upper.count('A')
count_Tt=dna_upper.count('T')
count_Cc=dna_upper.count('C')
count_Gg=dna_upper.count('G')

print(f"This sequence has {count_Aa} A's, {count_Tt} T's, {count_Cc} C's, and {count_Gg} G's.")
