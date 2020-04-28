# Helper functions

import pandas as pd
import os


def proc_row(str_series):
    out = str_series.str.lower()
    return out


def xls_kwd_search(wb,kwd):
    
    # read in xlsx or xls
    xls = pd.ExcelFile(path)

    # list of sheets
    sheets = xls.sheet_names
    
    for sheet in sheets:
        df = pd.read_excel(xls,sheet)
        if kwd in str(df.columns).lower():
            # return a boolean --> store filename or not
            return True
            break
        else:
            
            col_search = df.apply(lambda row: proc_row(row).str.contains(kwd).any(), axis=1)
            
            # boolean, True if any instance of kwd
            if any(col_search):
                return True
            else:
                return False


def csv_kwd_search(csv,kwd):
    
    with open(csv) as f:
        
        encoding = f.encoding
        
    
    df = pd.read_csv(csv,encoding = encoding)
    
    if 'isolate' in str(df.columns).lower():

        return True
    else:
        
        col_search = df.apply(lambda row: proc_row(row).str.contains(kwd).any(), axis=1)
            
        # boolean, True if any instance of kwd
        if any(col_search):
            return True
        else:
            return False



    
def get_all_files(directory):
    # output a list
    f = []
    # walk through all subdirectories
    for (dirpath, dirnames, filenames) in os.walk(directory):
        
        for file in filenames:
            # only keep workbooks and csv's
            if '.csv' in file or '.xls' in file:
                path_bad = os.path.join(dirpath,file)
                path_good = path_bad.replace('\\','/')
                f.append(path_good)
    return f


'''
final function:
    inputs:  
        kwd:  keyword to be searched
        Directory:  directory (and all subdirectories) to be searched in
    
    output:
        dataframe:  a df of all filenames in the directry

    * beware of using kwd as a parameter multiple times
'''

def kwd_search(kwd,directory):
    
    all_files = get_all_files(directory)
    
    out_list = []
    
    for file in all_files:
        
        if 'csv' in file:
            
            if csv_kwd_search(file,kwd):
                
                out_list.append(file)
                
        else:
            
            if xls_kwd_search(file,kwd):
                
                out_list.append(file)
                
    out_df = pd.DataFrame(out_list, columns = ['files'])
    
    return out_df