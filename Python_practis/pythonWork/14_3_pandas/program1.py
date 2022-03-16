"""
pandas install and use pandas and numpy

# import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g','e','e','k','s'])
 
ser = pd.Series(data)
print(ser)
"""
"""
import pandas as pd

# a simple list
list = ['g', 'e', 'e', 'k', 's']
  
# create series form a list
ser = pd.Series(list)
print(ser)
"""
"""
# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
  
  
# accessing a element using index element
print(ser[10])
"""

"""# importing pandas module  
import pandas as pd  
     
# making data frame  
df = pd.read_csv("nba.csv")  
   
ser = pd.Series(df['Name']) 
data = ser.head(10)
data """

"""# importing pandas module  
import pandas as pd  
 
# creating a series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
 
# creating a series
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
 
print(data, "\n\n", data1)

"""
"""

import pandas as pd
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])
ser = pd.Series(array)
print(ser)

"""


"""
import pandas as pd
   
# Calling DataFrame constructor
df = pd.DataFrame()
print(df)
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
   
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

"""
"""
# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df)

"""


# importing pandas as pd
import pandas as pd
""" 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# using dropna() function  
print(df.dropna())
"""
"""
# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()
"""


"""
# importing pandas module
import pandas as pd
  
# making data frame
data = pd.read_csv("/home/woc/Pravin/Trainee/pythonWork/14_3_pandas/nba.csv")
n=9
# calling head() method 
# storing in new variable
data_top = data.head(n=n)
  
# display
print(data_top)
"""

# importing pandas module 
import pandas as pd 
    
# making data frame 
df = pd.read_csv("/home/woc/Pravin/Trainee/pythonWork/14_3_pandas/nba.csv", index_col ="Name") 
  
print(df.head(10))
  
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,'Position':'PG', 'Age':33, 'Height':'6-2','Weight':189, 'College':'MIT', 'Salary':99999},index =[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop = True)
print(df.head())