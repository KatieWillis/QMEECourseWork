#!/usr/bin/env python
"""Examples of list comprehensions and loops to extract information from list of tuples"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively.
latin_names = [species[0] for species in birds]
common_names = [species[1] for species in birds]
mean_body_mass = [species[2] for species in birds]

# (2) Now do the same using conventional loops (you can shoose to do this
# before 1 !).
latin_names = []                         #Initiate the empty set
for species in birds:                    #Iterates through list of species
          latin_names.append(species[0]) #Adds the first element of the tuple to the list

#Repeat the above structure for the other pieces of information
common_names = []
for species in birds:
          common_names.append(species[1])

mean_body_mass = []
for species in birds:
          mean_body_mass.append(species[2])


# ANNOTATE WHAT EVERY BLOCK OR, IF NECESSARY, LINE IS DOING!

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
