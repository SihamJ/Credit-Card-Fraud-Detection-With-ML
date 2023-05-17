import pandas as pd
import numpy as np
from utils import *
from rules import make_fraud
import sys, os
from termcolor import colored as cl # text customization

"""
How to run this program:

python generate_dataset.py "root_directory" "original_dataset_name"

"""

print(cl('\nReading file...'))

root = sys.argv[1]
df = pd.read_excel(root + sys.argv[2], dtype = str)

distinct_names = df['CLASS'].unique()
df.loc[df['CLASS'].isin(distinct_names[1:]) , 'CLASS'] = 1
df['CLASS']=df['CLASS'].astype(int)

cases = len(df)
nonfraud_count = len(df[df.CLASS == 0])
fraud_count = len(df[df.CLASS == 1])
fraud_percentage = round(fraud_count/nonfraud_count*100, 2)

print(cl('CASE COUNT', attrs = ['bold']))
print(cl('--------------------------------------------', attrs = ['bold']))
print(cl('Total number of cases are {}'.format(cases), attrs = ['bold']))
print(cl('Number of Non-fraud cases are {}'.format(nonfraud_count), attrs = ['bold']))
print(cl('Number of fraud cases are {}'.format(fraud_count), attrs = ['bold']))
print(cl('Percentage of fraud cases is {}%'.format(fraud_percentage), attrs = ['bold']))
print(cl('--------------------------------------------', attrs = ['bold']))

print('\n')

print(cl('\nSplitting Dataset...'))
split_count = nonfraud_count-fraud_count
df_fraud = df[df.CLASS == 1]
df_non_fraud = df[df.CLASS == 0]
df_to_update = pd.DataFrame.copy(df_non_fraud[:(split_count)])

df_fraud = pd.concat([df_fraud, df_to_update])


print(cl('\nSaving non fraud file separately...'))
df_non_fraud.to_excel(root + 'non_fraud_data.xlsx', index=False)

## temporary
print(cl('\nTreating fraud dataset...'))
df_fraud.to_excel(root + 'temp.xlsx', index=False)

## Re-reading the file is necessary to avoid some bugs
df_fraud = pd.read_excel(root + 'temp.xlsx', dtype=str)

print(cl('\nGenerating fraud instances...'))
df['V10'] = df['V10'].astype(float)
max_V10 = get_max_values(df)['V10']
final_fraud = make_fraud(df_fraud, max_V10)
final_df = pd.concat([df_non_fraud, final_fraud])


print(cl('\nSaving results...'))
final_fraud.to_excel(root + "final_fraud.xlsx", index=False)
final_df.to_excel(root + "final.xlsx", index=False)
os.remove(root + 'temp.xlsx')