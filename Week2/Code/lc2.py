#!/usr/bin/env python
"""Examples of list comprehensions and loops to extract information from list of tuples"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
rain_morethan_100 = [month for month in rainfall if month[1] > 100.0]

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm.
rain_lessthan_50 = [month[0] for month in rainfall if month[1] < 50]

# (3) Now do (1) and (2) using conventional loops (you can choose to do
# this before 1 and 2 !).
rain_morethan_100 = []
for month in rainfall:
            if month[1] > 100:
                        rain_morethan_100.append(month)

rain_lessthan_50 = []
for month in rainfall:
            if month[1] < 50:
                        rain_lessthan_50.append(month[0])

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING!

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
