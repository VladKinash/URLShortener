from flask import Flask, g, render_template, request, redirect, url_for, abort
import sqlite3
from db import insert_url, get_url_by_short_code, list_all_urls, increment_clicks

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
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    short_code = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            short_code = insert_url(original_url)
    return render_template('index.html', short_code=short_code)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = get_url_by_short_code(short_code)
    if url:
        increment_clicks(short_code)
        return redirect(url)
    else:
        abort(404)

@app.route('/all')
def all_urls():
    urls = list_all_urls()
    return render_template('all_urls.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
