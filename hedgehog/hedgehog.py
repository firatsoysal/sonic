import subprocess
import speedtest
import csv
from datetime import datetime
import time as t

def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

count = 0
while True:
    speedtest_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        print("Started to speed test. Please do not interrupt!")

        dl_speed = speedtest.Speedtest(secure=True).download()/1000000
        write_to_csv([speedtest_time, dl_speed], "time_and_speed.csv")
        print(dl_speed)
        print("Speed test ended successfully")
    except Exception as e:
        write_to_csv([speedtest_time, e], "speed_errors.csv")
        continue

    for i in range(3):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            subprocess.run(["sudo", "systemctl", "stop", "dhcpcd"])
            t.sleep(5)

curl http://ipv4.download.thinkbroadband.com/20MB.zip> 20MB.zip
            subprocess.run(["curl", "http://ipv4.download.thinkbroadband.com/20MB.zip", ">", "20MB.zip"])

            subprocess.run(["rm", "20MB.zip"])

            count += 1

            write_to_csv([current_date, count], "counts.csv")

            t.sleep(1)

        except Exception as e:
            write_to_csv([current_date, e], "disconnect_errors.csv")
            continue
