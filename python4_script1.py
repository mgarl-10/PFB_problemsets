#!/usr/bin/env python3
taxa="sapiens,erectus,neanderthalensis"
print(taxa)
print(taxa[1])
type(taxa)
species=taxa.split(',')
print(species)
print(species[1])
type(species)
sorted(species)
sorted(species,key=len)

