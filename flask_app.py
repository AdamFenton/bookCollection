
from flask import Flask, render_template
import os
app = Flask(__name__)
cwd = os.getcwd()
import glob

thumbnails = glob.glob("%s/static/thumbnails/*" % os.getcwd())
thumbnails = sorted(thumbnails, key = lambda x: x.split('_')[0].split('.')[0])

@app.route('/')
def home():
   return render_template('grid.html')

@app.route('/book/<isbn>')
def show_book_page(isbn):

    filename = glob.glob('./static/thumbnails/*_%s.jpeg' % isbn)
    file = filename[0].split('/')[-2]+'/'+filename[0].split('/')[-1]

    return render_template('book_page.html',value=file)

if __name__ == '__main__':
   app.run()