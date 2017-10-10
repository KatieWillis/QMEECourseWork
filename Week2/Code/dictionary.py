#!/usr/bin/env python
"""Produces a dictionary of taxa:list of species from the data provided"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic
# derived from  taxa so that it maps order names to sets of taxa.
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc.

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING!

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:
taxa_dic = {} #Initiate an empty dictionary
for species in taxa:
         if species[1] in taxa_dic.keys(): #Check if the key exists
                  taxa_dic[species[1]].add(species[0]) #add the species to the set associated with the key
         else:
                  taxa_dic[species[1]] = set([species[0]]) #Add a new key with the first species used to initate the set
