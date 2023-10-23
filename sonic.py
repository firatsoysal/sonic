import speedtest
import csv
from datetime import datetime
import time as t


def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


while True:
    speedtest_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        print("Started to speed test. Please do not interrupt!")

        dl_speed = speedtest.Speedtest(secure=True).download()/1000000
        write_to_csv([speedtest_time, dl_speed], "time_and_speed.csv")
        print(dl_speed)
        print("Speed test ended successfully")
        t.sleep(900)
    except Exception as e:
        write_to_csv([speedtest_time, e], "speed_errors.csv")
        t.sleep(60)
        continue
