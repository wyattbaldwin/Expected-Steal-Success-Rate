import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load the data
df1 = pd.read_csv('pitch_arsenals.csv')
df2 = pd.read_csv('poptime.csv')
df3 = pd.read_csv('running_splits.csv')

# Split the data into training and test sets
train_index <- createDataPartition(data$label, p = 0.8, list = FALSE)
train <- data[train_index,]
test <- data[-train_index,]

# Extract the features and labels
X_train <- train[,c('feature1', 'feature2', ...)]
y_train <- train$label
X_test <- test[,c('feature1', 'feature2', ...)]
y_test <- test$label

# Train a random forest model
model <- randomForest(y_train ~ ., data = train)

# Make predictions on the test data
y_pred <- predict(model, newdata = test)

# Evaluate the model's performance
confusion_matrix <- table(y_pred, y_test)
accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
precision <- confusion_matrix[1,1] / (confusion_matrix[1,1] + confusion_matrix[2,1])
recall <- confusion_matrix[1,1] / (confusion_matrix[1,1] + confusion_matrix[1,2])

print(confusion_matrix)
print(accuracy)
print(precision)
print(recall)
