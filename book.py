import json
import os
import pandas as pd
from urllib.request import urlopen,urlretrieve

cwd = os.getcwd()

df = pd.read_csv('bookCollection.csv',header = 0)

ISBNS = df['Code data']

for isbn in ISBNS:
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    resp = urlopen(api + str(isbn))
    book_data = json.load(resp)
    volume_info = book_data["items"][0]["volumeInfo"]


    author = volume_info["authors"]
    prettify_author = author if len(author) > 1 else author[0]
    try:
        image = book_data['items'][0]["volumeInfo"]['imageLinks']['thumbnail']
        image_file = urlretrieve(image,'%s/%s.png' % (cwd,volume_info['title']))
    except:
        print('No image found for %s' % volume_info['title'] )
    # print(f"\nTitle: {volume_info['title']}")
    # print(f"Author: {prettify_author}")
    # print(f"Page Count: {volume_info['pageCount']}")
    # print(f"Publication Date: {volume_info['publishedDate']}")
    # print("\n***\n")
