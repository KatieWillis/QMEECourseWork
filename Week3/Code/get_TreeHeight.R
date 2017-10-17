#This function calculates heights of trees from the angle of
#elevation and the distance from the base using the trigonometric
#formula height = distance * tan(radians)

#ARGUMENTS:
#degrees The angle of elevation
#distance The distance from base

#OUTPUT:
#The height of the tree, same units as "distance"

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  #print(paste("Tree height is:", height))
  return (height)
}

#Loads csv file from command line argument
infile <- commandArgs(trailingOnly = TRUE)[1]
MyData <- read.csv(infile, header = TRUE) # import with headers

#Calculate heights
Tree.Height.m <- TreeHeight(MyData$Angle.degrees, MyData$Distance.m)
Output <- cbind(MyData,Tree.Height.m)


#Writes csv file with label from command line argument
outfile <- gsub(".csv","",infile)
outfile <- gsub("../Data/","",outfile)
outfile <- paste("../Results/",outfile,"_treeheights.csv",sep="")
write.csv(Output, outfile, row.names=FALSE,quote = FALSE)
