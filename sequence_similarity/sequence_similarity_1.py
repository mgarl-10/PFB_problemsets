#!/usr/bin/env python3

import sys

file1=sys.argv[1]
aa_protein=sys.argv[2]
scoring_matrix=sys.argv[3]

field_names=['query_id', 'subject_id', '%_identity', 'alignment_length', 'mismatches', 'gap_opens', 'q_start', 'q_end', 's_start', 's_end', 'evalue',' bit_score']
    

this_data={}

with open(file1, 'r') as file2:
   for line in file2:
     line=line.rstrip()
     if '#' in line:
       print()
     else:
        new_lines=line.split("\t")
       for name in field_names:
         this_data[name]=[]
       for value in new_lines:
         value.append=this_data
       #   for line in new_lines:
        #   i this_data[name]=line
        #this_data=zip(field_names,new_line)
         
#print(new_line)
#field_names=['query id', 'subject id', '% identity', 'alignment length', 'mismatches', 'gap opens', 'q. start', 'q. end', 's. start', 's. end', 'evalue',' bit score']

#for line in new  
#this data = zip (field_names,



