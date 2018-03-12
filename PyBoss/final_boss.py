#! user/jjahn/dev/repos

import csv
import us
import pandas as pd
from datetime import date


file_list = ['employee_data1.csv','employee_data2.csv']
fieldnames = ['Emp_ID','First_Name','Last_Name','DOB','SSN','State']

def format_employee_data (file):
        with open(file, 'r') as employee_data:
            employee_reader = csv.DictReader(employee_data)
            e = list()
            e = []
            for index in employee_reader:
                # store employee ID
                emp_id = index['Emp ID']
                e.append(emp_id)

                # splits Name into First Name and Last Name
                name = index['Name']
                split_name = name.split(' ')

                first_name = split_name[0]
                last_name = split_name[1]
                e.append(first_name)
                e.append(last_name)

                # reformat date to M/D/Y
                dob = index['DOB']
                d = pd.to_datetime(dob)             # use datetime module
                new_dob = d.strftime('%m/%d/%y')    # format date
                e.append(new_dob)

                #censor SSN
                SSN = index['SSN']
                split_SSN = list(SSN)
                for num in range(6):
                    if str.isdigit(split_SSN[num]):
                        split_SSN[num] = '*'
                new_SSN =''.join(split_SSN)
                e.append(new_SSN)

                #simplify State
                read_state = index['State']
                state_list = us.states.mapping('abbr','name')
                for abb, state in state_list.items():
                    if state == read_state:
                        state_abb = abb
                e.append(state_abb)
        
                # write reformatted employee data to new file
                # print (e)
                employee_writer.writerow(e)
                e = []          # clear employee data for new data entry
                e = list()

data_out_file = 'employee_data_formatted.csv'

with open(data_out_file, 'w', newline='') as new_employee_data:
        employee_writer = csv.writer(new_employee_data)
        employee_writer.writerow(fieldnames)
        for data_file_index in file_list:
            format_employee_data(data_file_index)

print ('** data reformatted -> {} **'.format(data_out_file))
