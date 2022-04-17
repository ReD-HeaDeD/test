import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    con = sqlite3.connect("coin.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from Coins")

    rows = cur.fetchall() #возвращает все строки в виде списка
    return render_template('index.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

