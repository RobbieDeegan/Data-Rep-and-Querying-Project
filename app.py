import flask as fl
import sqlite3

import string
import random
import json

DATABASE = 'data/passwordData.db'

app = fl.Flask(__name__)

###################################################

# Adapted from https://github.com/data-representation/example-sqlite
# Get information from database to be used in oldPassword
def getDataBase():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
        return db
    
################################################### 

#size = (fl.request.values["userinput"])
#size = request.GET["userinput"]

@app.route("/")
def root():
    return app.send_static_file('index.html')

# Code for generating randomly found from: http://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
@app.route("/password", methods=["GET", "POST"])
def passwordGen(size = 10, chars = string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

# Code to display all passwords saved to the database
# Adapted from https://github.com/data-representation/example-sqlite
@app.route("/oldPassword", methods=["GET", "POST"])
def previousPasswords():
    cur = getDataBase().cursor()
    cur.execute("SELECT password FROM passwordTable") 
    return str(cur.fetchall())

if __name__ == "__main__":
    app.run()