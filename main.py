from barcode_lookup import *
import os
import pandas as pd
from pathlib import Path # Required to create thumbnail directory
import easygui as g
#

#
collection_exists = os.path.isfile('%s/book_collection.csv' % os.getcwd())

if collection_exists == True:
    df_collection = pd.read_csv('book_collection.csv')
    # batch_lookup(df_collection)
    # format_collection(df_collection)

else:
    title = 'Select CSV file containing ISBN scans'
    filename = g.fileopenbox(title)
    df_collection = pd.DataFrame(columns = ['Title','Author','Date Published','Pages','Genre'])
    batch_lookup(df_collection,filename)

format_collection(df_collection)
