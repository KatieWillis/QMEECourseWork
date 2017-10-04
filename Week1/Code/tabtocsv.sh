#! /bin/bash
#Author: Katie Willis kw1016@imperial.ac.uk
#Script: tabtocsv.sh
#Desc: substitute the tabs in the file with commas
#      saves output to a .csv file
#Arguments: $1 -> tab delimited file
#Date Oct 2015

echo "Creating a comma delimited version of $1 ..."

cat $1 | tr -s "\t" "," >> $1.csv

echo "Done!"

exit
