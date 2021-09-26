from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_bybeesh'
app.config['MYSQL_PASSWORD'] = '0595'
app.config['MYSQL_DB'] = 'cs340_bybeesh'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    cur = mysql.connection.cursor()
    cur.execute(query)
    results = cur.fetchall()

    return "<h1>MySQL Results:</h1>" + json.dumps(results[0])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4242))

    app.run(port=port)