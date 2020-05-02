'''

inputs:  keyword:  list?
         Full directory path:  string

outputs:  csv's containing all files with instances of keyword

'''

import helpers
import pandas as pd

# keyword is a list?
keyword = input('Enter keyword list: ')
dir_path = input('Enter directory (full-path):  ')




df = helpers.kwd_search(keyword,dir_path)
out_name = 'kwd_' + keyword + '.csv'
df.to_csv(out_name)
