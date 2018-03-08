#! user/jjahn/dev/repos

import csv

file = 'store_items.csv'

with open(file, 'r') as store_data:
    store_r = csv.reader(store_data)
    fieldnames = ['Item','Stock']
    with open('store_items2.csv','w',newline="") as store_data2:
            store_w = csv.DictWriter(store_data2, fieldnames = fieldnames)
            store_w.writeheader()
            for line in store_r:
                line2 = dict(zip(fieldnames,line))
                print (line2['Item'] +': '+ line2['Stock'])
                store_w.writerow(line2)

# with open('store_items2.csv', 'r') as new_store_data:
#     store_reader2 = csv.DictReader(store_data2)
#     # item = input("choose item from stock: ")
#     for item in store_reader2:
#         print (item)
        
