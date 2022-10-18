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
    

sequences=seqs.values()
ids=seqs.keys()
res=[]

for sequence in sequences:
  start=0
  end=3 
  res.append([])
  while sequence[start:end]!="": 
    codons=sequence[start:end]
    res[-1].append(codons)
    start+=3
    end+=3
for index, it in enumerate(ids):
  print(f'{it}-frame-1-codons\n{res[index]}') 
