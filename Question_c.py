import dask
# Disable the new arrow-based string conversion in Dask
dask.config.set({"dataframe.convert-string": False})

import time
import pandas as pd
import dask.dataframe as dd

# Load dataset using Pandas
df_dist = pd.read_csv("Trips_by_Distance.csv")

n_processors = [10, 20, 40]
n_processors_time = {}

# Example: forcing numeric columns to float64
df_dist["Number of Trips 10-25"] = pd.to_numeric(df_dist["Number of Trips 10-25"], errors="coerce")
df_dist["Number of Trips 50-100"] = pd.to_numeric(df_dist["Number of Trips 50-100"], errors="coerce")

dask_df = dd.from_pandas(df_dist, npartitions=4)


for processor in n_processors:
    print(f"\n=== (Simulating) Processing with {processor} 'logical cores' ===")
    # Using perf_counter for more precise timing
    start_time = time.perf_counter()

    # (a) Filter "Number of Trips 10-25" > 10 million
    trips_10_25 = dask_df[dask_df["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]]
    trips_10_25 = trips_10_25.compute()

    # (b) Filter "Number of Trips 50-100" > 10 million
    trips_50_100 = dask_df[dask_df["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]]
    trips_50_100 = trips_50_100.compute()

    # Record time
    dask_time = time.perf_counter() - start_time
    n_processors_time[processor] = dask_time

    # Print results
    print(f"10-25 Trips (>10M): {len(trips_10_25)} rows")
    print(f"50-100 Trips (>10M): {len(trips_50_100)} rows")
    print(f"Time taken: {dask_time:.4f} seconds")

print("\n=== Summary of times by (intended) number of processors ===")
for proc, t in n_processors_time.items():
    print(f"{proc} processors: {t:.4f} seconds")
