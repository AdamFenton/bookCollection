import json
import os
import pandas as pd
from urllib.request import urlopen,urlretrieve
from pathlib import Path # Required to create thumbnail directory
from pretty_html_table import build_table
import fileinput
import shutil

def barcode_lookup(isbn):

    ''' Use google's API to lookup the ISBN of a book and return its
        title, author(s), publication date, page count and genre(s).
    '''

    Path("%s/static/thumbnails/" % os.getcwd()).mkdir(parents=True, exist_ok=True )
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    resp = urlopen(api + str(isbn))
    book_data = json.load(resp)

    try:
        volume_info = book_data["items"][0]["volumeInfo"]
        author = volume_info["authors"]
        prettify_author = author if len(author) > 1 else author[0]
        title = volume_info['title']
        published = volume_info['publishedDate']
        pages = volume_info['pageCount']
        surname = prettify_author.split(' ')[1].replace("'","")
        try:
            genre = volume_info['categories']
        except:
            genre = None
            print('No genre found for <%s>' % volume_info['title'])
        try:
            image = book_data['items'][0]["volumeInfo"]['imageLinks']['thumbnail']
            urlretrieve(image, "static/thumbnails/%s_%s.jpeg" % (surname,isbn))
        except:
            print('No image found for <%s>' % volume_info['title'] )
            shutil.copyfile('%s/unknownCover.jpg' % os.getcwd(), "static/thumbnails/%s_%s.jpeg" % (surname,isbn))

        new_entry = {'title':title, 'author':prettify_author, 'published':published,'pages':pages,'genre':genre}
        print('Completed Entry for <%s>' % volume_info['title'] )
        return new_entry

    except:
        print('No Entry found for this title')



def format_collection(collection):
    ''' Format the pandas dataframe to a html table and save it to a file
        static/ directory
    '''

    html_table_blue_light = build_table(collection, 'blue_light')
    with open('%s/templates/table.html' % os.getcwd(), 'w') as f:
        f.write(html_table_blue_light)


def batch_lookup(collection):

    ''' Load a dataframe of ISBN numbers produced by barcode scanner and pass
        each ISBN to the barcode_lookup function. A new dataframe is produced
        at the end of this function containing the information for all the
        books scanned.
    '''
    df_scans = pd.read_csv('isbn_scans.csv',header = 0)
    ISBNS = df_scans['Code data']
    for isbn in ISBNS:
        new_entry = barcode_lookup(isbn)
        collection = pd.concat([collection, pd.DataFrame([new_entry])])

    collection.to_csv('%s/book_collection.csv' % os.getcwd(),index=False)


def single_lookup(isbn,collection):

    ''' Take isbn of a single book as an argument and perform lookup with
        barcode_lookup function and append to the library csv file
    '''

    new_entry = barcode_lookup(isbn)
    collection = pd.concat([collection, pd.DataFrame([new_entry])])
    collection.to_csv('%s/book_collection.csv' % os.getcwd(),index=False)
