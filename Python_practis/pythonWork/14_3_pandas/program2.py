"""
# importing pandas module 
import pandas as pd 
    
# making data frame 
df = pd.read_csv("/home/woc/Pravin/Trainee/pythonWork/14_3_pandas/nba.csv", index_col ="Name") 
  
df.head(10)
  
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999},
                                                            index =[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop = True)
print(df.head(5))
"""
"""
# importing pandas module
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv("/home/woc/Pravin/Trainee/pythonWork/14_3_pandas/nba.csv", index_col ="Name" )
print(data)
# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
                            "R.J. Hunter"], inplace = True)
  
# display
print(data)

"""

"""
# importing pandas package
import pandas as pd
  
# making data frame from csv file 
data = pd.read_csv("/home/woc/Pravin/Trainee/pythonWork/14_3_pandas/nba.csv")
  
# retrieving rows by loc method 
row1 = data.loc[3]
  
# retrieving rows by iloc method
row2 = data.iloc[3]
  
# checking if values are equal
print(row1 == row2)
# Name        True
# Team        True
# Number      True
# Position    True
# Age         True
# Height      True
# Weight      True
# College     True
# Salary      True
# Name: 3, dtype: bool

"""

"""
# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
  
df = pd.DataFrame(dict, index = [True, False, True, False])
  
print(df)
"""

"""
# importing pandas module
import pandas as pd
  
# Define a dictionary containing employee data
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
    
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data1)
  
print(df)

# using groupby function
# with one key
 
df.groupby('Name')
print(df.groupby('Name').groups)
"""

import pandas as pd
import numpy as np

def adder(ele1,ele2):
    return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,4)
print(df.apply(np.mean))
