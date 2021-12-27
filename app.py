from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Home.html")


@app.route('/gal')
def index_Gal():
    return render_template("Galery.html")


def get_db_connection_B():
    connect = sqlite3.connect('database_Between.db')
    connect.row_factory = sqlite3.Row
    return connect


def get_db_connection():
    connect = sqlite3.connect('database.db')
    connect.row_factory = sqlite3.Row
    return connect


@app.route('/comment', methods=['POST', 'GET'])
def create():
    posts = Get_content()
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        connect = get_db_connection_B()

        connect.execute("INSERT INTO Com (name, comment) VALUES (?, ?)",
            (name, comment)
            )

        connect.commit()
        connect.close()

        posts = Get_content()

    return render_template("comment.html", posts=posts)


def Get_content():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM com').fetchall()
    conn.close()
    return posts


if __name__ == '__main__':
    app.run(debug=True)
