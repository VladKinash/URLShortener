from flask import Flask, g, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close

@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/hello')
def oneplusone():
    return str(1+1)

@app.route('/template')
def show_food():
    food = {'name': 'greek yogurt', 'vegan': False}


if __name__ == '__main__':
    app.run(debug=True)