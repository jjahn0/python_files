#! user/jjahn/dev/repos

import csv

file = 'cereal.csv'

with open(file, 'r') as cereal_data:
    read_cereal = csv.reader(cereal_data)
    for box in read_cereal:
        if float(box[8]) >= 5:
            print (box[0])
