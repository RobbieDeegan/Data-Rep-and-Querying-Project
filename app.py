import flask as fl

app = fl.Flask(__name__)

import string
import random
import json

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/password", methods=["GET", "POST"])

# Code for generating randomlly found from: http://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
def passwordGen(size = 10, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    app.run()