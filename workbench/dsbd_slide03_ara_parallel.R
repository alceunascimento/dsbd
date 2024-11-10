
#---- SETUP
require(kernlab)
require(randomForest)
require(dplyr)
require(doParallel)
require(foreach)

rm(list = ls())

#---- DATA
data(spam)
n <- nrow(spam)


#---- MODELS

# Set up parallel processing
num_cores <- detectCores() - 1  # Leave one core free for system processes
cl <- makeCluster(num_cores)
registerDoParallel(cl)

# Set seed for reproducibility
set.seed(123)

# Number of iterations
n_iterations <- 50

# Start total timing
total_start_time <- Sys.time()

# Create a progress log file
log_file <- "rf_progress_log.txt"
cat("Starting Random Forest Parallel Processing\n", file=log_file)

# Initialize progress tracking
cat(sprintf("\nStarting parallel processing with %d iterations on %d cores\n", 
            n_iterations, num_cores))

# Parallel execution of the loop with progress tracking
results <- foreach(i = 1:n_iterations,
                   .packages = c("randomForest", "kernlab"),
                   .combine = 'rbind') %dopar% {
                     
                     # Start timing for this iteration
                     iter_start_time <- Sys.time()
                     
                     # Log start of iteration
                     msg <- sprintf("\nIteration %d/%d started at %s", 
                                    i, n_iterations, format(iter_start_time, "%H:%M:%S"))
                     cat(msg, file=log_file, append=TRUE)
                     
                     # First split: Separate test set (20% of total data)
                     train_index <- sample(1:n, 0.8 * n)
                     train_data <- spam[train_index, ]
                     test_data <- spam[-train_index, ]
                     
                     # Log data split information
                     msg <- sprintf("\n  Data split complete - Training: %d, Test: %d", 
                                    nrow(train_data), nrow(test_data))
                     cat(msg, file=log_file, append=TRUE)
                     
                     # Second split: Split remaining data into train and validation
                     train_index_2 <- sample(1:nrow(train_data), 0.8 * nrow(train_data))
                     final_train_data <- train_data[train_index_2, ]
                     validation_data <- train_data[-train_index_2, ]
                     
                     # Log second split information
                     msg <- sprintf("\n  Second split complete - Final Training: %d, Validation: %d", 
                                    nrow(final_train_data), nrow(validation_data))
                     cat(msg, file=log_file, append=TRUE)
                     
                     # Train Random Forest model
                     model_start_time <- Sys.time()
                     cat("\n  Starting Random Forest training...", file=log_file, append=TRUE)
                     
                     mod.rf <- randomForest(type ~ .,
                                            data = final_train_data,
                                            ntree = 500,
                                            mtry = 7,
                                            importance = TRUE)
                     
                     model_end_time <- Sys.time()
                     model_duration <- difftime(model_end_time, model_start_time, units="secs")
                     msg <- sprintf("\n  Random Forest training complete - Duration: %.2f seconds", 
                                    as.numeric(model_duration))
                     cat(msg, file=log_file, append=TRUE)
                     
                     # Calculate accuracies
                     train_pred <- predict(mod.rf, final_train_data)
                     validation_pred <- predict(mod.rf, validation_data)
                     test_pred <- predict(mod.rf, test_data)
                     
                     # Calculate and log accuracies
                     train_acc <- mean(train_pred == final_train_data$type)
                     validation_acc <- mean(validation_pred == validation_data$type)
                     test_acc <- mean(test_pred == test_data$type)
                     
                     msg <- sprintf("\n  Accuracies - Train: %.3f, Validation: %.3f, Test: %.3f",
                                    train_acc, validation_acc, test_acc)
                     cat(msg, file=log_file, append=TRUE)
                     
                     # Store variable importance
                     imp <- importance(mod.rf)[, "MeanDecreaseAccuracy"]
                     
                     # Calculate iteration duration
                     iter_end_time <- Sys.time()
                     iter_duration <- difftime(iter_end_time, iter_start_time, units="mins")
                     msg <- sprintf("\nIteration %d completed - Duration: %.2f minutes\n",
                                    i, as.numeric(iter_duration))
                     cat(msg, file=log_file, append=TRUE)
                     
                     # Return a data frame row
                     data.frame(
                       iteration = i,
                       train_acc = train_acc,
                       validation_acc = validation_acc,
                       test_acc = test_acc,
                       duration_mins = as.numeric(iter_duration),
                       # Add importance as additional columns
                       t(imp)
                     )
                   }

# Calculate and log total execution time
total_end_time <- Sys.time()
total_duration <- difftime(total_end_time, total_start_time, units="mins")
msg <- sprintf("\nTotal execution time: %.2f minutes\n", as.numeric(total_duration))
cat(msg, file=log_file, append=TRUE)
cat(msg)  # Also print to console

# Stop the cluster
stopCluster(cl)


# Extract accuracy results
accuracy_results <- results[, c("iteration", "train_acc", "validation_acc", "test_acc")]

# Extract importance matrix
importance_cols <- setdiff(names(results), c("iteration", "train_acc", "validation_acc", "test_acc"))
importance_matrix <- as.matrix(results[, importance_cols])
rownames(importance_matrix) <- 1:nrow(importance_matrix)
colnames(importance_matrix) <- importance_cols

# Calculate summary statistics
accuracy_summary <- data.frame(
  Dataset = c("Training", "Validation", "Test"),
  Mean = c(mean(accuracy_results$train_acc),
           mean(accuracy_results$validation_acc),
           mean(accuracy_results$test_acc)),
  SD = c(sd(accuracy_results$train_acc),
         sd(accuracy_results$validation_acc),
         sd(accuracy_results$test_acc))
)

# Calculate mean importance across all iterations
mean_importance <- colMeans(importance_matrix)
importance_sd <- apply(importance_matrix, 2, sd)
final_importance <- data.frame(
  Variable = names(mean_importance),
  Mean_Importance = mean_importance,
  SD_Importance = importance_sd
)
final_importance <- final_importance[order(final_importance$Mean_Importance, decreasing = TRUE), ]

# Print results
cat("\nAccuracy Summary:\n")
print(round(accuracy_summary * 100, 2))

cat("\nTop 10 Most Important Variables (averaged across iterations):\n")
print(head(final_importance, 10))

# Create visualizations
par(mfrow = c(2, 1))

# Boxplot of accuracies
boxplot(accuracy_results[, c("train_acc", "validation_acc", "test_acc")] * 100,
        names = c("Training", "Validation", "Test"),
        main = "Model Performance Across Iterations",
        ylab = "Accuracy (%)",
        col = c("lightblue", "lightgreen", "lightpink"))

# Plot variable importance (top 10)
top_10_vars <- head(final_importance$Variable, 10)
barplot(final_importance$Mean_Importance[1:10],
        names.arg = top_10_vars,
        main = "Top 10 Variable Importance",
        las = 2,
        ylab = "Mean Decrease in Accuracy")

# Reset plot parameters
par(mfrow = c(1, 1))

