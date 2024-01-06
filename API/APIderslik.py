from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('ders_programi.db')

@app.route('/api/ders_programi/<sinif>')
def get_ders_programi(sinif):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Kisitlar WHERE Sinif = ?', (sinif,))
    ders_programi = cursor.fetchall()
    conn.close()

    if not ders_programi:
        return jsonify({'message': f'Ders programı bulunamadı for {sinif}'}), 404

    return jsonify({'ders_programi': ders_programi})

if __name__ == '__main__':
    app.run(debug=True)
