# Pie chart:

import matplotlib.pyplot as plt

df_dist = pd.read_csv("Trips_by_Distance.csv")

# Sum total trips per distance category
total_trips_by_category = df_dist[trip_cols].sum()

# Pie chart with separate legend and better spacing
plt.figure(figsize=(10,8))

# Plot pie without labels directly on slices
wedges, texts, autotexts = plt.pie(
    total_trips_by_category,
    autopct='%1.1f%%',
    startangle=140,
    labeldistance=1.1,
    textprops={'fontsize': 10}
)

# Add legend
plt.legend(wedges, trip_cols, title="Distance Ranges", loc="center left", bbox_to_anchor=(1, 0.5))

# Add title
plt.title('Proportion of Total Trips by Distance')
plt.tight_layout()
plt.show()

###############################################
# Stackplot:

# Convert 'Date' to datetime
df_dist['Date'] = pd.to_datetime(df_dist['Date'])

# Plot only for selected distance categories (to avoid clutter)
selected_cols = [
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]

# Area plot
plt.figure(figsize=(14,7))
plt.stackplot(df_dist['Date'], [df_dist[col] for col in selected_cols], labels=selected_cols, alpha=0.8)
plt.title('Travel Volume Over Time by Distance')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
