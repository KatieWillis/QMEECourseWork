#!/usr/bin/env python
"""Aligns the the two DNA sequences in the file sequences.csv"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

import sys

def calculate_score(s1, s2, l1, l2, startpoint):
    """function that computes a score by returning the number of matches starting from arbitrary startpoint"""
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
    return [score, matched] #edit to return score and matched pattern rather print

def main():
    """Reads in sequences and writes a file displaying the best alignment"""
    #save elements of list as 2 separate variables
    f = open('../Data/sequences.csv', 'r')
    data = f.read()
    f.close()
    data = data.rstrip()
    data = data.split(',')

    seq1 = data[0]
    seq2 = data[1]

    #Find the length of each sequence
    l1 = len(seq1)
    l2 = len(seq2)

    #Identify the longest length and label as #1 (s1 and l1)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths

    #Initiate best score as less than any possible value
    my_best_score = -1
    #Find the alignment with the highest score and save kay information in 4 variables
    for i in range(l1):
        output = calculate_score(s1, s2, l1, l2, i)
        z = output[0]
        if z > my_best_score:
            my_best_align = "." * i + s2
            my_best_start_position = i
            my_best_score = z
            my_match = output[1]

    # build some formatted output and write to file
    o = open('../Results/aligned_sequences.txt', 'w')
    o.write("Best score: " + str(my_best_score) + "\n")
    o.write("." * my_best_start_position + my_match+ "\n")
    o.write("." * my_best_start_position + s2+ "\n")
    o.write(s1+ "\n")
    o.close()

if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
    status = main()
    sys.exit(status)
