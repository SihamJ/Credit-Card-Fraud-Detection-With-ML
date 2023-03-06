import numpy as np
import string
import random 

"""
get max values of each column in the dataset
"""
def get_max_values(df):
    columns_num = df.select_dtypes(include=np.number).columns.tolist()
    max_values = {}

    for v in columns_num:
        max_values[v] = df[v].max()

    return max_values

"""
Return a random number not in the list
"""
def random_not_in(l, max):
    res = l[0]
    while(res in l):
        res = np.random.randint(0, max)
    return res

"""
Generate a random string not in the list
"""
def random_string_not_in(l):
    res = l[0]
    S = len(l[0])
    while(res in l):
        res = ''.join(random.choices(string.digits, k = S))    
    return res