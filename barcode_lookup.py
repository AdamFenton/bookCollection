import json
import os
import pandas as pd
from urllib.request import urlopen,urlretrieve
from pathlib import Path # Required to create thumbnail directory


def barcode_lookup(isbn):

    ''' Use google's API to lookup the ISBN of a book and return its
        title, author(s), publication date, page count and genre(s).
    '''

    Path("%s/thumbnails/" % os.getcwd()).mkdir(parents=True, exist_ok=True )
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    resp = urlopen(api + str(isbn))
    book_data = json.load(resp)

    volume_info = book_data["items"][0]["volumeInfo"]
    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]
    title = volume_info['title']
    published = volume_info['publishedDate']
    pages = volume_info['pageCount']

    try:
        genre = volume_info['categories']
    except:
        genre = None
        print('No genre found for <%s>' % volume_info['title'])
    try:
        image = book_data['items'][0]["volumeInfo"]['imageLinks']['thumbnail']
        urlretrieve(image, "thumbnails/%s.jpeg" % isbn)
    except:
        print('No image found for <%s>' % volume_info['title'] )

    new_entry = {'title':title, 'author':prettify_author, 'published':published,'pages':pages,'genre':genre}

    return new_entry



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
    new_entry = barcode_lookup(isbn)
    collection = pd.concat([collection, pd.DataFrame([new_entry])])
    collection.to_csv('%s/book_collection.csv' % os.getcwd(),index=False)
