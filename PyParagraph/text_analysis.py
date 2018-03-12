#! users/jjahn/dev/repos

import csv
import re

#file = 'paragraph_1.txt'
file_list = ['paragraph_1.txt', 'paragraph_2.txt']

def text_analyze(file):
    with open (file, 'r') as text_file:
        letters = 0
        text_reader = text_file.read()
        s = re.split('[.!?]\s+', text_reader)
        w = re.split('\s+', text_reader)
        for i in w:
            l = len(i)
            letters = letters + l

    words = len(w)
    sentences = len(s)
    avg_letters = (letters - 1)/ words
    s_lengths = words / sentences

    print('-----------------------------------')  
    print('{} analysis complete'.format(file))
    print('-----------------------------------')
    print('words: \t\t\t{}'.format(words))
    print('sentences: \t\t{}'.format(sentences))
    print('letters per word: \t{:.1f}'.format(avg_letters))
    print('words per sentence: \t{:.1f}'.format(s_lengths))
    print('-----------------------------------')

for text in file_list:
    text_analyze(text)