import speedtest
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


def write_data(arr, file_name):
    with open(file_name + ".txt", "w") as file:
        for value in arr:
            file.write(str(value) + "\n")


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
    write_data(download_list, "download_values")
    write_data(time_list, "times")
    plot_graph(time_list, download_list, time)



