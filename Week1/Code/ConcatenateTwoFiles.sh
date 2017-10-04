#! /bin/bash
#Author: Katie Willis kw1016@imperial.ac.uk
#Script: ConcatenateTwoFiles.sh
#Desc: Merge two files
#Arguments: $1 -> first file
#           $2 -> second file
#Date Oct 2015

cat $1 > $3
cat $2 >> $3
echo "Merged File is"
cat $3
