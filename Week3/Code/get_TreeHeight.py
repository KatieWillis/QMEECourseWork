import csv
import math
import sys

#Calculate the distance
def TreeHeight(degrees, distance):
    """Find x to the power of 0.5."""
    radians = degrees*math.pi/180.0
    distance * math.tan(radians)
    height = distance * math.tan(radians)
    return (height)


#get command line arguments
inputfile = sys.argv[1]
outputfile = inputfile.replace('.csv', '')
outputfile = outputfile.replace('../Data/', '')
outputfile = "../Results/" + outputfile + "_treeheights_python.csv"

#Read in file
f = open(inputfile,'rb')
csvread = csv.reader(f)
header = next(csvread)


#prepare write file
g = open(outputfile,'wb')
csvwrite = csv.writer(g)

#calculate height and write output to file
csvwrite.writerow(header + ["Tree.Height.m"])
for row in csvread:
    tree_height = TreeHeight(float(row[2]),float(row[1]))
    csvwrite.writerow(row + [str(tree_height)])

f.close()
g.close()
