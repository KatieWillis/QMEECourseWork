#! /bin/bash
#Author: Katie Willis kw1016@imperial.ac.uk
#Script: variables.sh
#Desc: shows the use of variables
#Arguments: none
#Date Oct 2015

MyVar='some string'
echo 'the current value of the variable is' $MyVar

echo 'Please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar

#Multple values
echo 'Enter two numbers separated by space(s)'
read a b
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum
