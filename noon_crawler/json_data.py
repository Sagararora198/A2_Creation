import csv
from urllib.request import urlopen
import json
file = open('noon_spider/items.csv','r')
reader = csv.reader(file)
i = 0
for row in reader:
    response = urlopen(row[0])
    data_json = json.loads(response.read())

