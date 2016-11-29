# A Random Password Generator

### Project for Third Year Data Representation and Querying 2016. The task is to create a single page web application in Python.

### The Idea behind the app
Passwords are one of the most important aspects of modern life and having a secure password in essential. Everyday people are making better password cracking algorithms and getting information for accounts across the internet. 600,000 Facebook accounts are hacked everyday and 75% of Americans have been victim of online crime die to their accounts being hacked. 75% of people use the same password for multiple accounts which can lead to mulitple attacks. Popular passwords include pets names, siginifcant dates, family members names and shockingly, the word password.
An 8-character password with letters (upper & lower case) and includes numbers and symbols has 6,095,689,385,410,816 possible combinations. So in other words, it'll be tough to crack as most password cracking algorithms use dictionarys to guess the words included. So random characters is defintely the way to go.

This webapp will generate a password with a random amount of characters between 6 and 20 which will include numbers, letters(upper and lower case) and other ascii characters. It will also save all passwords generated to a database and display them all in the web app.

### How to run the application
Clone the files or download the zip file to your machine.

The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

The [sqlite3](https://docs.python.org/2/library/sqlite3.html) package was used for the database side of the project and must be installed. I found SQLite3 easier to use over couchDB or MongoDB.
No further configuration or setup is required it is all included in the imports in the python code.

When you have the above installed, you must setup the database to hold the passwords. This is will be made in the data folder. Then
run the app and view the webapp locally at http://127.0.0.1:5000/ in your browser 
```bash
$ python dbsetup.py
$ python app.py
```
### Reflections
Overall I found this project to be tricky. Bringing all the different packages and frameworks together was a struggle at times, but in the end I think its all come together well. I would have liked to have the user input the desired amount of characters for the passwords, but after struggling to get it to work for a few days I decided to have it randomly choose a number of characters. 

Overall I think this project has imporved my understanding of Python and Flask as well as my ability to use Git and manage my work on GitHub. 