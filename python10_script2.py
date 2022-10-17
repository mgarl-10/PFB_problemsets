#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
width=sys.argv[2]
#start=int(0)
#end=int(60)
def new_lines(dna,widt):
 list_dna=list(dna)
 start=int(0)
 end=int(widt)
 res=[]
 for line in dna:
  res.append(line.replace("\n",""))
 while dna[start:end]!='':
  print(dna[start:end])  
  start+=int(widt)
  end+=int(widt)
print(new_lines(file1,width))

def GC_content(dna):
  c_counts=dna.count('C')
  g_counts=dna.count('G')
  dna_len=len(dna)
  gc_content=(c_counts+g_counts)/dna_len
  return(f'{gc_content:.2%}')

def reverse_complement(dna):
    dna_lower=dna.lower()
    dna_replacing_A=dna_lower.replace("a","T") 
    dna_replacing_T=dna_replacing_A.replace("t","A")
    dna_replacing_G=dna_replacing_T.replace("g","C")
    dna_replacing_C=dna_replacing_G.replace("c","G") 
    dna_reverse=dna_replacing_C[::-1]
    return(dna_reverse)

print('The GC content of this sequence is:',GC_content(file1))
print('Reverse sequence:'+ '\n'+ reverse_complement(file1))
