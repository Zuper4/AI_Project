# Using Pandas for data acquisition
import pandas as pd

# Load dataset using Pandas
df_dist = pd.read_csv("Trips_by_Distance.csv")

# Setting the condition to be over 10 million
# Using set() to remove duplicates
first = set(df_dist[df_dist['Number of Trips 10-25'] > 10000000]['Date'])
second = set(df_dist[df_dist['Number of Trips 50-100'] > 10000000]['Date'])

print(f"The number of dates where the number of trips between 10 and 25 miles is above 10 million is {len(first)}")
print(f"The number of dates where the number of trips between 50 and 100 miles is above 10 million is {len(second)}")
