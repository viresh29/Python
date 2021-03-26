import pytz
import datetime
import time


def convert_UTC_to_epoch(timestamp):
    tz_UTC = pytz.timezone('UTC')
    time_format = "%Y-%m-%d %H:%M:%S"
    naive_timestamp = datetime.datetime.strptime(timestamp, time_format)
    print(naive_timestamp)
    aware_timestamp = tz_UTC.localize(naive_timestamp)
    print(aware_timestamp)
    epoch = aware_timestamp.strftime("%s")
    return (int)(epoch)


print(convert_UTC_to_epoch("2020-02-23 00:00:00"))


print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1585253991049)))
print(datetime.datetime.fromtimestamp(
    1585253991049).strftime('%Y-%m-%d %H:%M:%S'))
