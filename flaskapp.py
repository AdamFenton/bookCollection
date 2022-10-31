from flask import Flask, render_template
import os
app = Flask(__name__)
cwd = os.getcwd()
@app.route('/')
def home():
   return render_template('table.html')
if __name__ == '__main__':
   app.run()
