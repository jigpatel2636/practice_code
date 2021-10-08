import csv

file_handle = open('weather.csv', encoding='utf-8')
csv_reader = csv.DictReader(file_handle)

for row in csv_reader:
    print(row)

file_handle.close()