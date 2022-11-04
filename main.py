from barcode_lookup import *
import os
import pandas as pd
from pathlib import Path # Required to create thumbnail directory
import glob

collection_exists = os.path.isfile('%s/book_collection.csv' % os.getcwd())
#
# if collection_exists == True:
# #     # If the library catalogue already exists, append to it
#     df_collection = pd.read_csv('book_collection.csv')
#
# #     # single_lookup(9780345806307,df_collection)
#     batch_lookup(df_collection)
# #
# else:
# #     # No library created yet so make a blank dataframe for the lookup function
# #     # to append to
#      df_collection = pd.DataFrame(columns = ['title','author','published','pages','genre'])
#      batch_lookup(df_collection)


thumbnails = glob.glob("%s/static/thumbnails/*" % os.getcwd())
thumbnails = sorted(thumbnails, key = lambda x: x.split('_')[0].split('.')[0])
def generate_image_link(thumbnail):
    surname = thumbnail.split('_')[0].split('/')[-1]
    isbn = thumbnail.split('_')[1]
    file = os.path.basename(thumbnail)

    string = "<a href = '/book/%s'> \
              <img src={{ url_for('static', filename='thumbnails/%s') }}/> \
              </a>" % (isbn,file)

    return string

for thumbnail in thumbnails:
    print(generate_image_link(thumbnail))
