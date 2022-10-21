#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
seqs={}


with open(file1,"r") as file2, open("Python_08.codons-3frames.nt","w") as seq_write:
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
#with open(file1,"r") as file2, open("Python_08.codons-3frames.nt","w") as seq_write:
#for index, it in enumerate(ids):
  #for codon in res:
for i in range(len(res)):
  res[i]=res[i].lower()
  A_replace=res[i].replace('a','A')
  T_replace=A_replace.replace('t','T')
  C_replace=T_replace.replace('c','C')
  G_replace=C_replace.replace('g','G')
  reverse_complement=G_replace[::-1]
  

print(reverse_complement)

   


# print(it+'-frame-1-codons\n'+str(res[index]))
    


