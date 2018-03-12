#! user/jjahn/dev/repos

import csv

def revenue_calculate (file):
    months = 0
    hi = 0
    low = 0
    total_revenue = 0
    
    with open (file, 'r') as budget_file:
        budget_reader = csv.DictReader(budget_file)

        for line in budget_reader:
            months = months + 1
            index_revenue = int(line['Revenue'])
            total_revenue = total_revenue + index_revenue
        
        # find greatest revenue gains and lowest revenue losses

            if index_revenue > hi:
                hi = index_revenue
                hi_date = line['Date']
            elif index_revenue < low:
                low = index_revenue
                low_date = line['Date']
    
        avg_change = int(total_revenue / months)

        fieldnames = [  'months',
                        'total_revenue',
                        'average_change',
                        'highest date',
                        'highest_revenue',
                        'lowest date',
                        'lowest_revenue']

        data_entry = [months, total_revenue, avg_change, hi_date, hi, low_date, low]

        # writes to file
        row_data = dict(zip(fieldnames, data_entry))
        new_budget_writer.writerow(row_data)

        # print out results of data set in legible format
        print ('------------------------------------------------')
        print ("months:\t\t\t  " + str(months))
        print ("total revenue:\t\t$ {:14,.2f}".format(total_revenue))
        print ("avg.change:\t\t$ {:14,.2f}".format(avg_change))
        print ("highest increase: \t{} (${:14,.2f})".format(hi_date, hi))
        print ("lowest drop:\t\t{} (${:14,.2f})".format(low_date, low))
        print ('------------------------------------------------')
        
# field names and list of budget data files.  any additiona data goes to 'data_bank' list
fieldnames = [  'months',
                'total_revenue',
                'average_change',
                'highest date',
                'highest_revenue',
                'lowest date',
                'lowest_revenue']

bank_data=['budget_data1.csv','budget_data2.csv']

# reads though each dataset indicated.  method will print and write to file as needed.
with open('budget_data_calulated.csv', 'w', newline='') as new_budget_file:
    new_budget_writer = csv.DictWriter(new_budget_file, fieldnames = fieldnames)
    new_budget_writer.writeheader()
    for budgets in bank_data:
        revenue_calculate(budgets)

