import speedtest
import csv
from datetime import datetime
import time as t

def write_to_csv(data):
    with open("time_and_speed.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


while True:
    print("Started to test. Please do not interrupt!")

    dl_speed = speedtest.Speedtest(secure=True).download()/1000000
    test_time = datetime.now()
    data_to_write = [test_time, dl_speed]
    write_to_csv(data_to_write)
    print(dl_speed)
    print("Test ended successfully")

    t.sleep(30)


