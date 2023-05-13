from flask import *
from pandas import *
from sqlite3 import *
app=Flask(__name__)
@app.route('/1')
def main():
    return "This is a test";
app.run(host="dovuq.github.io/test1")
