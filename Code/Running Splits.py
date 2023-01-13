# Load necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load data from CSV files
running_splits = pd.read_csv("Database/running_splits_2022.csv")

# Extract the features and labels
X = running_splits[['time_at_000ft', 'time_at_005ft', 'time_at_010ft', 'time_at_015ft','time_at_020ft','time_at_025ft','time_at_030ft','time_at_035ft','time_at_040ft','time_at_045ft','time_at_050ft','time_at_055ft','time_at_060ft','time_at_065ft','time_at_070ft','time_at_075ft','time_at_080ft','time_at_085ft','time_at_090ft']]
y = running_splits['player_position_name']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a logistic regression model
logistic_regression_model = LogisticRegression()

# Train the model using the training data
logistic_regression_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = logistic_regression_model.predict(X_test)

# Evaluate the model's performance
confusion_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print('Confusion matrix:')
print(confusion_matrix)
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
