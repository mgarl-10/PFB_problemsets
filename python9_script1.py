#!/usr/bin/env python3
import re
import sys
file1=''
try:

 file1=sys.argv[1]
 print("User provided file name:",file1)
 if not file1.endswith(('.fa','.fasta','.nt')):
   raise ValueError("Not a FASTA file")
 if 
 FASTA=open(file1,"r")
 for line in FASTA:
   print(line)
except IndexError:
  print('Please provide a file name')
except IOError as ex:
  print("Can't find file:",file1,':',ex.strerror)

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
print(dictionary_counts)



