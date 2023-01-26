import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import random

# Load data from spreadsheet
data = pd.read_csv("Database/running_splits_2022.csv")

# Define the features and target
X = data[['player_age']]
y = data[['time_at_00ft', 'time_at_5ft', 'time_at_10ft', 'time_at_15ft', 'time_at_20ft', 'time_at_25ft', 'time_at_30ft', 'time_at_35ft', 'time_at_40ft', 'time_at_45ft', 'time_at_50ft', 'time_at_55ft', 'time_at_60ft', 'time_at_65ft', 'time_at_70ft', 'time_at_75ft', 'time_at_80ft', 'time_at_85ft', 'time_at_90ft']]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print("Mean squared error:", mean_squared_error(y_test, y_pred))

# Use the model to predict the time at an unknown distance
player_age = 27
distance = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
player_data = [[player_age]]
predicted_time = model.predict(player_data)[0][distance//5]
print(f"The estimated time for player with age {player_age} to reach {distance}ft is {predicted_time} seconds.")
