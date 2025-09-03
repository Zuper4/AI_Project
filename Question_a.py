# Using Pandas for data acquisition
import pandas as pd

# Load dataset using Pandas
df_dist = pd.read_csv("Trips_by_Distance.csv")

# Only refering to the National level rows
avg_stay_home = int(df_dist[df_dist["Level"] == "National"]["Population Staying at Home"].mean().round())

print(f"The average number of people staying at home is: {avg_stay_home}")

# Use average distance for each trip range
df_dist['Total Distance'] = (
    df_dist['Number of Trips <1'] * 0.5 +
    df_dist['Number of Trips 1-3'] * 2 +
    df_dist['Number of Trips 3-5'] * 4 +
    df_dist['Number of Trips 5-10'] * 7.5 +
    df_dist['Number of Trips 10-25'] * 17.5 +
    df_dist['Number of Trips 25-50'] * 37.5 +
    df_dist['Number of Trips 50-100'] * 75 +
    df_dist['Number of Trips 100-250'] * 175 +
    df_dist['Number of Trips 250-500'] * 375 +
    df_dist['Number of Trips >=500'] * 600
)

# Calculate average distance per person who left home
df_dist['Avg Distance Per Person'] = df_dist['Total Distance'].sum() / df_dist['Population Not Staying at Home'].sum()

average = df_dist["Avg Distance Per Person"].mean().round()

print(f"The average distance per person who left home is: {average} km")
