#!/usr/bin/env python
"""Examples of using sys for command line argument inputs"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

import sys
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)
