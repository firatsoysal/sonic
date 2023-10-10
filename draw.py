import matplotlib.pyplot as plt
import pandas as pd

# Read data from the CSV file
df = pd.read_csv("time_and_speed.csv", names=["Datetime", "Value"])

# Convert the "Datetime" column to datetime objects
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df["Datetime"], df["Value"], marker='o', linestyle='-')
plt.title("Speed vs. Datetime")
plt.xlabel("Datetime")
plt.ylabel("Value")
plt.grid(True)

# Save the graph as an image file (e.g., PNG)
plt.savefig("speed_vs_datetime.png")

# Show the graph
plt.show()