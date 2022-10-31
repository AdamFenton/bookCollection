from barcode_lookup import barcode_lookup
import os
import pandas as pd
from pathlib import Path # Required to create thumbnail directory


cwd = os.getcwd()

df_scans = pd.read_csv('isbn_scans.csv',header = 0)
df_collection = pd.DataFrame(columns = ['title','author','published','pages','genre'])

ISBNS = df_scans['Code data']

for isbn in ISBNS:
    new_entry = barcode_lookup(isbn)
    df_collection = pd.concat([df_collection, pd.DataFrame([new_entry])])
