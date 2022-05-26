import csv
import sys
from datetime import datetime
from pytz import timezone
import datetime
import time

def jmetertoCVS(j1):
    with open(j1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if (row[4] != 'OK'):
                timestamp_r = float(row[0])/1000.0
                date_time = datetime.datetime.fromtimestamp(timestamp_r)
                date = date_time.astimezone(timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S')
                #date = datetime.datetime.fromtimestamp(row[0])
                print(date +' PST',row[2], ',', row[3],',', row[4], row[8])
            


jmetertoCVS('Jmeter_log1.jtl')
jmetertoCVS('Jmeter_log2.jtl')