#! /bin/bash
#Author: Katie Willis kw1016@imperial.ac.uk
#Script: MyExampleScript.sh
#Desc: count lines in input file
#Arguments: $1 -> file name
#Date Oct 2015

NumLines=`wc -l < $1`
echo "The file $1 has $NumLines lines"
echo
