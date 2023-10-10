import speedtest
import csv
from datetime import datetime
import time as t

def write_to_csv(data):
    with open("time_and_speed.csv", 'a', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)


while True:
    print("Started to test. Please do not interrupt!")

    dl_speed = speedtest.Speedtest().download()/1000000
    test_time = datetime.now()
    zipped_data = list(zip(time_list, download_list))
    write_to_csv(zipped_data)
    print(dl_speed)
    print("Test ended successfully")

    t.sleep(30)


