from flask import Flask, render_template
import os
app = Flask(__name__)
cwd = os.getcwd()
@app.route('/')
def home():
   return render_template('grid.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
   app.run()
