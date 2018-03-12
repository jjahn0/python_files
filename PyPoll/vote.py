#!/user/jjahn/dev/repo

from collections import Counter
import csv

v_tally = list()
total_votes = 0
file_list = ['election_data_1.csv', 'election_data_2.csv']

def tally_votes (csv_file):
    with open (csv_file, 'r') as election_file:
        election_reader = csv.DictReader(election_file)

        # tally total votes

        for line in election_reader:
            v_tally.append(line['Candidate'])

def drawline ():
    for index in range (25):
        print('-', end='')
    print('')

for file_num in file_list:
    tally_votes(file_num)

drawline()
print('ELECTION RESULTS')
drawline()

total_votes = len(v_tally)
print('Total Votes: {:,}'.format(total_votes))

c_tally = Counter(v_tally) # tallies all votes per candidate
c_tally.most_common() # reorders vote tally from highest to lowest

result_ls = list(c_tally.most_common()) #cast to list
d_out = 'election_result_Data.csv'

# calculate winner and percentages, prints and exports tally to file

with open(d_out, 'w', newline='') as vote_results:
    vote_writer = csv.writer(vote_results)
    header = ['candidate', 'percentage', 'votes']
    vote_writer.writerow(header)
    for i in range(len(result_ls)-1):
        v = result_ls[i][1]
        p = (result_ls[i][1]/total_votes)*100
        c = result_ls[i][0]
        print('{}: {:5.1f}% ({:,})'.format(c,p,v))
        d_entry = [c,p,v]
        vote_writer.writerow(d_entry)

drawline()

winner = result_ls[0][0]
print('Winner: {}'.format(winner))

drawline()
