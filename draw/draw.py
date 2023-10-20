import matplotlib.pyplot as plt
import csv

date_times = []
values = []

with open("time_and_speed.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        date_times.append(row[0])  # First element as datetime
        values.append(int(row[1]))

plt.figure(figsize=(10, 6))
plt.plot(date_times, values, marker='o', linestyle='-')
plt.title("Speed vs. Datetime")
plt.xlabel("Datetime")
plt.ylabel("Value")
plt.grid(True)

# Save the graph as an image file (e.g., PNG)
plt.savefig("speed_vs_datetime.png")

# Show the graph
plt.show()