from sklearn.cluster import KMeans
import pandas as pd

# Load the data
df1 = pd.read_csv('pitch_arsenals.csv')
df2 = pd.read_csv('poptime.csv')
df3 = pd.read_csv('running_splits.csv')

# Merge the dataframes
df = pd.concat([df1, df2, df3], ignore_index=True)

# Select the features to use for clustering
X = df[['pitch_type', 'zone', 'count', 'pitch_number', 'release_speed', 'release_pos_x', 'release_pos_z', 'player_name', 'split_time', 'distance', 'acceleration', 'top_speed']]

# Create and fit the model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predict the clusters for each data point
predictions = kmeans.predict(X)