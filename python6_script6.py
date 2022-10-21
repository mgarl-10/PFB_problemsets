#!/usr/bin/env python3
import sys
file1=sys.argv[1]
genes={}
with open(file1,"r") as seq_read:
  for line in seq_read:
    line=line.rstrip()
    line.find('>')
    gene_id,seq = line.split('>')
    genes[gene_id]= seq
print(genes)




