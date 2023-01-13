import pandas as pd

# Load data from spreadsheet
data = pd.read_csv("Database/running_splits_2022.csv")

# Define the function to calculate the time at an unknown distance
def interpolate_time(player_name, distance):
    # Filter the data for the player
    player_data = data[data["last_name"] == player_name]
    
    # Find the two known distances in feet that surround the unknown distance
    distances = [col for col in player_data.columns if "time_at" in col]
    distances = [float(d.replace("time_at_", "").replace("ft", "")) for d in distances]
    distances.sort()
    idx = min([i for i in range(len(distances)) if distances[i]>=distance])
    lower_distance = distances[idx-1]
    upper_distance = distances[idx]


    
    # Use the corresponding known times to calculate the time at the unknown distance
    lower_time = player_data[f"time_at_{str(lower_distance).zfill(3)}ft"].values[0]
    upper_time = player_data[f"time_at_{str(upper_distance).zfill(3)}ft"].values[0]
    interpolated_time = lower_time + (upper_time - lower_time) * (distance - lower_distance) / (upper_distance - lower_distance)
    
    return interpolated_time

# Test the function
player_name = "Abreu"
distance = 27
time = interpolate_time(player_name, distance)
print(f"The estimated time for player {player_name} to reach {distance}ft is {time} seconds.")
