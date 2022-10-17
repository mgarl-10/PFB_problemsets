#!/usr/bin/env python3
from Bio import SeqIO
import re
import sys
file1=sys.argv[1]

for seq_record in SeqIO.parse(file1,"fasta"):
  print('ID', seq_record.id)
  print('Sequence','\n'+seq_record.seq)
  print('Description',seq_record.description)

id_dict=SeqIO.to_dict(SeqIO.parse(file1,'fasta'))

counts=0
for seq in id_dict:
  seq.count('id')
  counts+=1

print("Sequence count:",counts)
