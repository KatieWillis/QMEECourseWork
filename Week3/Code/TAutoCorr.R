load("../Data/KeyWestAnnualMeanTemperature.RData")

x <- ats$Temp[1:(nrow(ats)-1)]
y <- ats$Temp[2:nrow(ats)]
correlation_score <- cor(x,y)

Sample_distribution <-  rep(NA, 10000)
for (i in 1:10000){
  x_rand <- sample(x, replace = FALSE)
  y_rand <- sample(y, replace = FALSE)
  Sample_distribution[i] <- cor(x_rand,y_rand)
}

P_value <- sum(Sample_distribution >= correlation_score)/10000
