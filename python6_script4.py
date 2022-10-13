#!/usr/bin/env python3
import sys
file1=sys.argv[1]
genes={}
with open(file1,"r") as seq_read:
  for line in seq_read:
    line=line.rstrip()
    gene_id,seq = line.split('\t')
    genes[gene_id]= seq
print(genes)


for gene in genes:
  gene_ids=gene
  print(gene_ids)
  seq=genes[gene]
  print(seq)
  dna_lower=seq.lower()
  dna_replacing_A=dna_lower.replace("a","T") 
  dna_replacing_T=dna_replacing_A.replace("t","A")
  dna_replacing_G=dna_replacing_T.replace("g","C")
  dna_replacing_C=dna_replacing_G.replace("c","G") 
  dna_reverse=dna_replacing_C[::-1]
  print(f"This is the complementary sequence\n{dna_replacing_C}")
  print(f"This is the reverse complement sequence\n{dna_reverse}")


