# import stuff!
import logging
from controller import RouteBuilder
from mysqlconnection import MySQLConnector
from flask import Flask, render_template, g

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='mostsecret',
    USERNAME='root',
    PASSWORD='root',
))

# db connection business
# Connection to db
def connect_db():
    """Connects to a specified database"""
    mysql = MySQLConnector(app, 'wall1')
    return mysql

def get_db():
    """Establishes a connection to a database in the global context"""
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = connect_db()
    return g.mysql_db

def init_db():
    "method that allows us to initialize a db connection"
    get_db()

RouteBuilder(app)




if __name__ == "__main__":
    app.run(debug=False)