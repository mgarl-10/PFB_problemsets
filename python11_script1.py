#!/usr/bin/env python3
import re
import sys
seq=sys.argv[1]
g_name=sys.argv[2]
s_name=sys.argv[3]

class DNARecord(object):
  def __init__(self,sequence,gene_name,species_name):
    self.sequence=sequence
    self.gene_name=gene_name
    self.species_name=species_name
    self.seq_len=len(sequence)

dna_rec_obj_1=DNARecord(seq,g_name,s_name)
for d in[dna_rec_obj_1]:
  print('name:',d.gene_name,' ','seq:',d.sequence,' ','species:',d.species_name,'sequence length:',d.seq_len)
