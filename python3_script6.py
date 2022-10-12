#!/usr/bin/env python3
import sys
dna = sys.argv[1]
dna_upper=dna.upper()
sub_dna=dna_upper[99:200]
GC_counts=sub_dna.count('G')

print(f"The substring is {sub_dna} and has {GC_counts} G's")

