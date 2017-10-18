#!/usr/bin/env python
"""Demonstration of using local vs global variables"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

## Try this first
_a_global = 10

def a_function():
    """Demonstration of a local and global function"""
    _a_global = 5
    _a_local = 4
    print "Inside the function, the value is ", _a_global
    print "Inside the function, the value is ", _a_local
    return None

a_function()
print "Outside the function, the value is ", _a_global

## Now try this

_a_global = 10

def a_function():
    """Demonstration of a local and global function"""
    global _a_global
    _a_global = 5
    _a_local = 4
    print "Inside the function, the value is ", _a_global
    print "Inside the function, the value is ", _a_local
    return None

a_function()
print "Outside the function, the value is", _a_global
