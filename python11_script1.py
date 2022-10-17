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

  #def calc_len(self):
  #  seq_len=len(self.sequence)
   # return seq_len

  def a_count(self):
    a_counts=self.sequence.count('A')
    return a_counts
  def t_count(self):
    t_counts=self.sequence.count('T')
    return t_counts
  def c_count(self):
    c_counts=self.sequence.count('C')
    return c_counts
  def g_count(self):
    g_counts=self.sequence.count('G')
    return g_counts
  
  def get_GC(self):
    GC_content=(self.g_count() + self.c_count())/self.seq_len
    return (f'{GC_content:.2%}')

  def fasta_format(self):
    fasta_ids='>' + self.gene_name
    return fasta_ids + '\n'+ self.sequence

dna_rec_obj_1=DNARecord(seq,g_name,s_name)

for d in[dna_rec_obj_1]:
  print('name:',d.gene_name,' ','seq:',d.sequence,' ','species:',d.species_name,'sequence length:',d.seq_len)
  print('A counts:',d.a_count(),'T counts:',d.t_count(),'C counts:',d.c_count(),'G counts:',d.g_count())
  print('GC content:',d.get_GC())
  print(d.fasta_format())
