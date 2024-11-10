
#---- SETUP
require(kernlab)      # Contains the spam dataset and other machine learning tools
require(randomForest) # For Random Forest algorithm
require(dplyr)        # For data manipulation

rm(list = ls())


#---- DATA
data(spam)    # Loads the spam dataset from kernlab package
str(spam)     # Shows the structure of the dataset
print("Dataset dimensions:")
print(dim(spam))



#---- MODEL 1
mod.rf.1 <- randomForest(type~.,         # formula: predict 'type' using all other columns
                       data=spam,        # the dataset to use
                       ntree=500,        # number of trees to grow
                       mtry=7,           # number of variables to try at each split
                       importance=TRUE)  # calculate variable importance

importance(mod.rf.1) %>% View()
varImpPlot(mod.rf.1)


#---- MODEL 2

# Split data into training and testing sets
set.seed(123)  # for reproducibility

# Calculate total number of rows for percentage reference
n <- nrow(spam)


# First split: Separate test set (20% of total data)
train_index <- sample(1:n, 0.8 * n)
train_data <- spam[train_index, ]
test_data <- spam[-train_index, ]

# Second split: Split remaining data into train and validation (80% of train_data)
train_index_2 <- sample(1:nrow(train_data), 0.8 * nrow(train_data))
final_train_data <- train_data[train_index_2, ]
validation_data <- train_data[-train_index_2, ]

# Print the proportions of each dataset
cat("\nDataset proportions:\n")
cat("Training set:", round(nrow(final_train_data)/n * 100, 2), "%\n")
cat("Validation set:", round(nrow(validation_data)/n * 100, 2), "%\n")
cat("Test set:", round(nrow(test_data)/n * 100, 2), "%\n")

# Train Random Forest model
mod.rf <- randomForest(type ~ .,
                       data = final_train_data,
                       ntree = 500,
                       mtry = 7,
                       importance = TRUE)

importance(mod.rf.2)




# Initialize storage for results
n_iterations <- 10  # Number of iterations
accuracy_results <- data.frame(
  iteration = 1:n_iterations,
  train_acc = numeric(n_iterations),
  validation_acc = numeric(n_iterations),
  test_acc = numeric(n_iterations)
)
importance_matrix <- matrix(0, nrow = ncol(spam) - 1, ncol = n_iterations)
rownames(importance_matrix) <- names(spam)[-which(names(spam) == "type")]

# Start the loop
for(i in 1:n_iterations) {
  # First split: Separate test set (20% of total data)
  train_index <- sample(1:n, 0.8 * n)
  train_data <- spam[train_index, ]
  test_data <- spam[-train_index, ]
  
  # Second split: Split remaining data into train and validation
  train_index_2 <- sample(1:nrow(train_data), 0.8 * nrow(train_data))
  final_train_data <- train_data[train_index_2, ]
  validation_data <- train_data[-train_index_2, ]
  
  # Train Random Forest model
  mod.rf <- randomForest(type ~ .,
                         data = final_train_data,
                         ntree = 500,
                         mtry = 7,
                         importance = TRUE)
  
  # Calculate accuracies
  train_pred <- predict(mod.rf, final_train_data)
  validation_pred <- predict(mod.rf, validation_data)
  test_pred <- predict(mod.rf, test_data)
  
  accuracy_results$train_acc[i] <- mean(train_pred == final_train_data$type)
  accuracy_results$validation_acc[i] <- mean(validation_pred == validation_data$type)
  accuracy_results$test_acc[i] <- mean(test_pred == test_data$type)
  
  # Store variable importance
  importance_matrix[, i] <- importance(mod.rf)[, "MeanDecreaseGini"]
  
  # Print progress
  cat("Iteration", i, "completed\n")
}







# Print model summary
print(mod.rf.2)

# Calculate and view variable importance
importance_scores <- importance(mod.rf.2)
sorted_importance <- importance_scores[order(importance_scores[,3], decreasing=TRUE),]
print("Top 10 most important variables:")
print(head(sorted_importance, 10))

# Make predictions on test data
predictions <- predict(mod.rf.2, test_data)

# Calculate accuracy
accuracy <- mean(predictions == test_data$type)
print(paste("Model accuracy:", round(accuracy * 100, 2), "%"))

# Create confusion matrix
conf_matrix <- table(Predicted = predictions, Actual = test_data$type)
print("Confusion Matrix:")
print(conf_matrix)












