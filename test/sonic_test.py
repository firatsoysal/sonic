import speedtest
import csv
from datetime import datetime
import time as t
import matplotlib.pyplot as plt

time_list = []
download_list = []


def plot_graph(x_axis, y_axis, date):
    plt.plot(x_axis, y_axis, "--bo")
    plt.title("Speedtest")
    plt.xlabel("Date")
    plt.ylabel("Download(Mbit)")
    plt.savefig("speedtest_" + str(date) + ".png")
    plt.show()


def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)


try:
    while True:
        print("Started to test. Please do not interrupt!")
        time = datetime.now()

        download_list.append(speedtest.Speedtest().download()/1000000)
        time_list.append(time)
        print(download_list[-1])
        print("Test ended successfully")

        t.sleep(900)
except KeyboardInterrupt:
    plot_graph(time_list, download_list, time)

    csv_file = "time_and_speed.csv"
    zipped_data = list(zip(time_list, download_list))
    write_to_csv(zipped_data, csv_file)


