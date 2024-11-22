# MULTIDIMENSIONAL SCALLING - MDS 

#---- SETUP

# Clear environment and load required package
require(smacof)
rm(list = ls())

# Read and prepare the Wine dataset
data <- read.table("/home/espinf/aenascimento/dsbd/sklearn-env/data/wine/wine.data", sep=",")

# Store class labels separately and normalize variables
wine_class <- data[,1]  # Store class labels
VARS <- scale(data[,-1])  # Scale the variables, excluding class
VARS


VARS <- data[ ,-1]
VARS

tipo <- data$V1
table(tipo)


# Create distance matrix
D <- dist(VARS, method = "euclidean")

# Perform MDS
mds <- smacof::mds(D, 
                   ndim = 2,
                   verbose = TRUE)

# Create visualization
plot(mds$conf, 
     col = wine_class,  # Color points by wine class
     pch = 19,         # Solid circles
     main = "MDS of Wine Dataset",
     xlab = "First Dimension",
     ylab = "Second Dimension") 
     legend("topright", 
       legend = unique(wine_class),
       col = unique(wine_class),
       pch = 19,
       title = "Wine Class")

# mds <- smacof::mds(D,
#            ndim=2,
#            verbose=TRUE)

mds$stress


plot(mds$conf,
     col=tipo,
     cex=2,
     pch=19)




#---- CLAUDE examples

rm(list = ls())

# Load required libraries
library(MASS)
library(stats)
library(ggplot2)
library(cluster)

# Load the data dataset
data <- read.table("/home/espinf/aenascimento/dsbd/sklearn-env/data/wine/wine.data", sep=",")
str(data)

# Create a distance matrix using the numeric variables
data_dist <- dist(data[, 1:4], method = "euclidean")

# Add small constant to distance matrix to avoid zero distances
data_dist_adj <- as.dist(as.matrix(data_dist) + 1e-10)

# Perform Classical (Metric) MDS
mds_result <- cmdscale(data_dist_adj, k = 2, eig = TRUE)

# Convert the MDS results into a data frame for plotting
mds_df <- data.frame(
  MDS1 = mds_result$points[,1],
  MDS2 = mds_result$points[,2],
  Species = data$V1
)

# Calculate the proportion of variance explained
eigenvalues <- mds_result$eig
var_explained <- eigenvalues^2 / sum(eigenvalues^2)
var_explained_pct <- round(var_explained[1:2] * 100, 2)

# Create the MDS plot
mds_plot <- ggplot(mds_df, aes(x = MDS1, y = MDS2, color = Species)) +
  geom_point(size = 3, alpha = 0.6) +
  theme_minimal() +
  labs(
    title = "MDS Plot of data Dataset",
    x = paste0("First Dimension (", var_explained_pct[1], "% variance explained)"),
    y = paste0("Second Dimension (", var_explained_pct[2], "% variance explained)"),
    color = "Species"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 14),
    legend.position = "right"
  )

# Display the plot
print(mds_plot)

# Print stress value (goodness of fit)
stress <- sum((dist(mds_result$points) - data_dist_adj)^2) / sum(data_dist_adj^2)
cat("\nStress value:", round(stress, 4))

# Perform non-metric MDS with adjusted distance matrix
nmds_result <- isoMDS(data_dist_adj, k = 2)

# Convert non-metric MDS results to data frame
nmds_df <- data.frame(
  NMDS1 = nmds_result$points[,1],
  NMDS2 = nmds_result$points[,2],
  Species = data$Species
)

# Create the non-metric MDS plot
nmds_plot <- ggplot(nmds_df, aes(x = NMDS1, y = NMDS2, color = Species)) +
  geom_point(size = 3, alpha = 0.6) +
  theme_minimal() +
  labs(
    title = "Non-metric MDS Plot of data Dataset",
    x = "First Dimension",
    y = "Second Dimension",
    color = "Species"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 14),
    legend.position = "right"
  )

# Display the non-metric MDS plot
print(nmds_plot)

# Print non-metric MDS stress value
cat("\nNon-metric MDS stress value:", round(nmds_result$stress, 4))

# Create Shepard diagram
shepard_test <- Shepard(data_dist_adj, cmdscale(data_dist_adj, k = 2))
plot(shepard_test$x, shepard_test$y,
     xlab = "Original Distances",
     ylab = "MDS Distances",
     main = "Shepard Diagram",
     pch = 20)
lines(shepard_test$x, shepard_test$yf, type = "l", col = "red")

