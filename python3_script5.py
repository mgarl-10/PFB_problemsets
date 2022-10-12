#!/usr/bin/env python3
import sys
dna=sys.argv[1]

AT_counts=dna.count("A") + dna.count ("T")
length=len(dna)
AT_content= (AT_counts/length)*100
AT_content_2='{:.2f}'.format(AT_content)
GC_counts=dna.count("G") + dna.count ("C")
GC_content=(GC_counts/length)*100
GC_content_2='{:.2f}'.format(GC_content)

print(f"This sequence has an AT content of {AT_content_2}% and a GC content of {GC_content_2}%")
