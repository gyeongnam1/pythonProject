'''
ex14-4-csvReader2.py
'''

import csv
with open('회원명단.csv', 'r', newline='', encoding="UTF-8") as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_reader:
        print(line)