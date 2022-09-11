import csv
import json

csvfile = open('test.csv','r')
jsonfile = open('test.json','w')

reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile,indent=0)


