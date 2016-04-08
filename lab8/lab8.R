
setwd('C:/Users/waclas/Documents/Y2_S2/open_source/lab8')
admissions = read.csv('binary.csv')


col_names <- names(admissions)
admissions[,col_names] <- lapply(admissions[,col_names], factor)

library(arules)

rules.all <-apriori(admissions, parameter = list(support=.008, confidence=.09) )

quality(rules) <- round(quality(rules), digits=3)
rules.sorted <- sort(rules, by="lift")

inspect(rules.all)

# find redundant rules
subset.matrix <- is.subset(rules.sorted, rules.sorted)
subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
redundant <- colSums(subset.matrix, na.rm=T) >= 1
which(redundant)


plot(rules.all)
plot(rules.all, method="grouped")
plot(rules.all, method="graph")