#!/usr/bin/env python3
import sys
nucleotides=sys.argv[1]
dna_seq='GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if nucleotides in dna_seq:
  print('found '+ nucleotides + ' in your dna sequence')
else:
  print('did not find ' + nucleotides + ' in your dna sequence')
