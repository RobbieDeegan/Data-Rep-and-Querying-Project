# A Random Password Generator

### Project for Third Year Data Representation and Querying 2016. The task is to create a single page web application in Python.

This webapp will generate a password with a random amount of characters between 6 and 20 which will include numbers, letters(upper and lower case) and other ascii characters. It will also save all passwords generated to a database and display them all in the web app.

### How to run the application
The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

The [sqlite3](https://docs.python.org/2/library/sqlite3.html) package was used for the database side of the project and must be installed.
No further configuration our setup is required it is all included in the 

When you have the above installed, you must setup the database to hold the passwords. This is will be made in the data folder. Then
run the app and view the webapp locally at http://127.0.0.1:5000/ in your browser 
```bash
$ python dbsetup.py
$ python app.py
```