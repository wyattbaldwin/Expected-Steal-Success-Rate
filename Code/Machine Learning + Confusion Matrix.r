#The script is loading and merging three datasets from .csv files, pre-processing them and then training a machine learning model using a method called glm.
#The script is using the trained model to make predictions on a test set, and then evaluating the performance of the model by calculating a confusion matrix and accuracy score.


# Install necessary libraries
#install.packages("tidyverse")
#install.packages("caret")

# Load necessary libraries
library(tidyverse)
library(caret)

# Load data from .csv files
setwd("C:\\Users\\Wyatt Baldwin\\Music\\Stealing Bases")
pitch_arsenals <- read_csv("pitch_arsenals.csv")
poptime <- read_csv("poptime.csv")
running_splits <- read_csv("running_splits.csv")

# Merge the three datasets into a single dataset
base_stealing_data <- merge(pitch_arsenals, poptime, by = "player_id") %>%
  merge(running_splits, by = "player_id")

# Pre-process the data
base_stealing_data <- base_stealing_data %>%
  select(-player_id, -player_name) %>%
  na.omit()

# Split the data into a training set and a test set
set.seed(123)
split_index <- createDataPartition(base_stealing_data$success, p = 0.8, list = FALSE)
train <- base_stealing_data[split_index, ]
test <- base_stealing_data[-split_index, ]

# Train a machine learning model using the training data
model <- train(success ~ ., data = train, method = "glm")

# Make predictions on the test data using the trained model
predictions <- predict(model, test)

# Calculate the confusion matrix and accuracy score
confusion_matrix <- confusionMatrix(predictions, test$success)
accuracy_score <- confusion_matrix$overall[1]

# Print the confusion matrix and accuracy score
print(confusion_matrix)
print(accuracy_score)
