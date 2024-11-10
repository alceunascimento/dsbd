# PRINCIPAL COMPONENT ANALYSIS - PCA

#---- DATA
data <- read.table("/home/espinf/aenascimento/dsbd/sklearn-env/data/wine/wine.data", sep=",")
str(data)

# data info

# 0) class = categorica alvo (1,2,3)

# The attributes are (dontated by Riccardo Leardi, riclea@anchem.unige.it )
# 1) Alcohol
# 2) Malic acid
# 3) Ash
# 4) Alcalinity of ash  
# 5) Magnesium
# 6) Total phenols
# 7) Flavanoids
# 8) Nonflavanoid phenols
# 9) Proanthocyanins
# 10)Color intensity
# 11)Hue
# 12)OD280/OD315 of diluted wines
# 13)Proline 



# analisar a variavel tipo
tipo <- data$V1
table(tipo)

# criar um subset sem o TIPO
VARS <- data[ ,-1]


apply(VARS,2,sd)

pairs(VARS, col=tipo)
pairs(VARS[,1:3], col=tipo, cex=2)

require(rgl)
plot3d(VARS[,1:3], col=tipo)

ACP <- prcomp(VARS, scale = TRUE)
ACP

nrow(ACP$x)
nrow(VARS)

prop <- round((ACP$sdev[1:2]^2)/sum(ACP$sdev^2),4)*100
plot(ACP$x[,1],ACP$x[,2],col=tipo, cex=2, pch=19)

#3rd
prop <- round((ACP$sdev[1:3]^2)/sum(ACP$sdev^2),4)*100
plot3d(ACP$x[,1],
       ACP$x[,2],
       ACP$x[,3],
       col=tipo, 
       size=10, 
       xlab=prop[1],
       ylab=prop[2],
       zlab=prop[3])


# check quais são em modulo maior que 0.3
# \a| > 0.3
# Get the rotation matrix
rotation <- ACP$rotation[,1:3]

# Create a function to filter values > |0.3|
filter_loadings <- function(x) {
  ifelse(abs(x) > 0.3, x, NA)
}

# Apply the filter to the rotation matrix
significant_loadings <- apply(rotation, 2, filter_loadings)

# Convert to data frame and add variable names
loadings_df <- as.data.frame(significant_loadings)
rownames(loadings_df) <- paste0("V", 2:14)

# Remove columns with all NAs if any exist
loadings_df <- loadings_df[, colSums(!is.na(loadings_df)) > 0]

# Print the result
print(loadings_df, na.print="")

