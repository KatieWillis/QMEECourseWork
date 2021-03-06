#!/usr/bin/env python
"""Print information in a tuple of tuples on separate lines"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )



# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line for each species
# Hints: use the "print" command! You can use list comprehensions!

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING!

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

for bird in birds:              #Iterates through list of tuples containing individual bird information
          for data in bird:     #Iterates through the tuple for each bird
                    print data  #Prints information on a new line
