#!/usr/bin/env python3
import sys
dna = sys.argv[1]
site = sys.argv[2]
dna_upper=dna.upper()
find_start=dna_upper.find(site)
length_site=len(site)
length_site_exact=int(length_site) - 1
find_end=find_start+length_site_exact
print(f"The start position of the EcoRI site is {find_start} and the end position is {find_end}")
