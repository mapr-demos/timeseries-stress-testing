import time
import os
import json
import sys
import csv

#Open the file
with open("2Simoutput.csv") as f:
  reader = csv.DictReader(f)
  outputfile = open("2Simoutput.json", "w+")
  for row in reader:

    print(json.dumps(dict(row)))
    outputfile.write(json.dumps(dict(row)))
  outputfile.close()

issue = datetime.datetime.strptime(msg['nwws']['issue'], "%Y-%m-%dT%H:%M:%SZ")
 _id: UTIME
  convert date to UTIME

  https://docs.python.org/3.5/library/datetime.html

  https://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python#9637908