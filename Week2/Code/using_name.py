#!/usr/bin/python
"""Examples of how to differentiate between running from the CL and importing modules"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

# Filename: using_name.py
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
