from barcode_lookup import *
import os
import pandas as pd
from pathlib import Path # Required to create thumbnail directory

collection_exists = os.path.isfile('%s/book_collection.csv' % os.getcwd())

if collection_exists == True:
    # If the library catalogue already exists, append to it
    df_collection = pd.read_csv('book_collection.csv')
    single_lookup(9780345806307,df_collection)
#     batch_lookup(df_collection)

else:
    # No library created yet so make a blank dataframe for the lookup function
    # to append to
    df_collection = pd.DataFrame(columns = ['title','author','published','pages','genre'])
    batch_lookup(df_collection)
