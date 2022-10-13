#!/usr/bin/env python3
import sys
dna=sys.argv[1]
nt_count={}

unique=set(dna)
print('unique nt:',unique)
for nt in unique:
  count=dna.count(nt)

  nt_count[nt]=count
print('nt_count:', nt_count)
total_A=nt_count['A']
total_C=nt_count['C']
total_G=nt_count['G']
total_T=nt_count['T']
lenght_dna=len(dna)
GC_counts=total_C + total_G
GC_content=(GC_counts/lenght_dna)*100
print(f"The GC content of this sequence is {GC_content:.2f}%")
