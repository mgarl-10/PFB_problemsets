#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
seqs={}


with open(file1,"r") as file2:
  for line in file2:
    line=line.rstrip()
    if re.search(r'^>',line):
      genes_id=line
      seqs[genes_id]=""
    else:
      seq=line
      seqs[genes_id] += seq 
    
dictionary_counts={}
for it in seqs:
  seq=seqs[it]
  dictionary_counts[it]={'nt_comp':{},'seq':seq}
  unique=set(seq)
  for nt in unique:
    dictionary_counts[it]['nt_comp'][nt]=seq.count(nt)



