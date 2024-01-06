from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('ders_programi.db')

@app.route('/api/hoca_dersleri')
def get_hoca_dersleri():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HocaDers')
    hoca_dersleri = cursor.fetchall()
    conn.close()
    return jsonify({'hoca_dersleri': hoca_dersleri})

@app.route('/api/kisitlar')
def get_kisitlar():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Kisitlar')
    kisitlar = cursor.fetchall()
    conn.close()
    return jsonify({'kisitlar': kisitlar})

if __name__ == '__main__':
    app.run(debug=True)
 