from flask import Flask, render_template
from mysqlconnection import MySQLConnection
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)




app = Flask(__name__)

mysql = MySQLConnection(app,'sakila')

@app.route('/')
def main():
    logging.debug("Application is up and going!")
    return render_template("index.html")


app.run(debug=True)