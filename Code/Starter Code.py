# Load necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV files
pitch_time = pd.read_csv("pitch_arsenals.csv")
pop_time = pd.read_csv("poptime.csv")
running_splits = pd.read_csv("running_splits.csv")

# Merge data into a single dataframe
data = pd.merge(pitch_time, pop_time, on="player_id")
data = pd.merge(data, running_splits, on="player_id")

# Generate summary statistics
print(data.describe())

# Visualize relationships between variables
plt.scatter(data["pitch_time"], data["pop_time"])
plt.xlabel("Average Pitch Time (seconds)")
plt.ylabel("Catcher Pop Time (seconds)")
plt.show()

# Check for missing values
print(data.isnull().sum())
