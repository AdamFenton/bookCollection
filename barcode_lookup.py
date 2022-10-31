import json
import os
import pandas as pd
from urllib.request import urlopen,urlretrieve
from pathlib import Path # Required to create thumbnail directory

Path("%s/thumbnails/" % os.getcwd()).mkdir(parents=True, exist_ok=True )

cwd = os.getcwd()

df_scans = pd.read_csv('isbn_scans.csv',header = 0)
df_collection = pd.DataFrame(columns = ['title','author','published','pages','genre'])

ISBNS = df_scans['Code data']


for isbn in ISBNS:
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
        image_file = urlretrieve(image,'%s/thumbnails/thumbnail_%s.png' % (cwd,isbn))
    except:

        print('No image found for <%s>' % volume_info['title'] )

    new_entry = {'title':title, 'author':prettify_author, 'published':published,'pages':pages,'genre':genre}
    df_collection= pd.concat([df_collection, pd.DataFrame([new_entry])])
print(df_collection)
