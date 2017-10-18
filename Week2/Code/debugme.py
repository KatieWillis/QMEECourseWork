#!/usr/bin/env python
"""A toy function to explore using a debugger"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

def createabug(x):
    y = x**4
    z = 0.
    y = y/z
    return y

createabug(25)
