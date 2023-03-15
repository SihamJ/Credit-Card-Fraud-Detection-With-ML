
import pandas as pd
import sys

"""
How to run this program:

python concatenate_datasets.py "root_directory" "file_1" ... "file_n" "output_file"

"""

root = sys.argv[1]
nb = len(sys.argv) - 1
filenames = sys.argv[2:nb]
final_name = sys.argv[nb]
datasets = []

print("\nConcatenating datasets...\n")

for n in filenames:
    df = pd.read_excel(root + n)
    datasets.append(df)

final_dataset = pd.concat(datasets)

print("\nSaving new dataset...\n")

final_dataset.to_excel(root + final_name, index=False)