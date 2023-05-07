import pandas as pd
import re


cols = []

##Ask user for file path
def get_file_path():
    global file_path
    file_path = input('Please input the file path. Example ' + r'C:\Users\Test.csv' + '\n')
    file_path = file_path.replace("\\", "/")

##function to list the column names, and ask the user which names and store it into array cols

def get_column_names():
    data_within_file = pd.read_csv(file_path, nrows=0)
    for index,col in enumerate(data_within_file.columns):
        print(index, col)
    chosen_cols = input('Please input the columns you would like. USE THE NUMBERS, seperate with spaces:')
    
    cols.extend(list(map(int, re.findall(r'\d+', chosen_cols))))

## store array cols into dataframe and create a csv based on file used.

def write_new_csv():
    data_within_file = pd.read_csv(file_path)
    created_dataframe = pd.DataFrame(data_within_file)
    new_info = created_dataframe[created_dataframe.columns[cols]]
    new_info.to_csv(file_path + '_revised.csv', index=False)
    print(file_path + '_revised.csv has been created!')


get_file_path()
get_column_names()
write_new_csv()
input("Press Enter to continue...")
