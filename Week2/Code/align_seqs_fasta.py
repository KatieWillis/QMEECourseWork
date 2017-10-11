#!/usr/bin/env python
"""Aligns the two sequences input as fasta files"""
__author__ = 'Katie Willis (kw1016@imperial.ac.uk)'

import sys

def extract_seq(input_fasta_file):
    f = open(input_fasta_file, 'r')
    data = f.readlines()
    f.close()

    data = [line.rstrip() for line in data]
    data = "".join(data[1:])

    return data

def calculate_score(s1, s2, l1, l2, startpoint):
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


def main(filename = "", file1 = "../Data/407228326.fasta", file2 = "../Data/407228412.fasta"):
    seq1 = extract_seq(file1)
    seq2 = extract_seq(file2)

    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths

    # function that computes a score
    # by returning the number of matches
    # starting from arbitrary startpoint

    #Find the alignment with the highest score
    my_best_align = None
    my_best_start_position = None
    my_best_score = -1
    my_match = None

    for i in range(l1):
        output = calculate_score(s1, s2, l1, l2, i)
        z = output[0]
        if z > my_best_score:
            my_best_align = "." * i + s2
            my_best_start_position = i
            my_best_score = z
            my_match = output[1]


    # build some formatted output and write to file
    o = open('../Data/aligned_input_sequences.txt', 'w')

    line1 = "." * my_best_start_position + my_match
    line2 = "." * my_best_start_position + s2
    line3 = s1

    o.write("Best score: " + str(my_best_score) + "\n")
    o.write("" + "\n")

    for i in range(l1/80):
        o.write(line1[i*80:80*(i+1)] + "\n")
        o.write(line2[i*80:80*(i+1)] + "\n")
        o.write(line3[i*80:80*(i+1)] + "\n")

        o.write(""+ "\n")

    o.close()

if (__name__ == "__main__"): #makes sure the "main" function is called from commandline
    status = main(sys.argv)
    sys.exit(status)
