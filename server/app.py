from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS
from baseball_scraper import get_probable_pitchers 

app = Flask(__name__)
CORS(app, resources={r"/api/pitchers/*": {"origins": "*"}})

def get_db_connection():
    conn = sqlite3.connect('baseball_data.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pitchers (
            pitcher TEXT,
            team TEXT,
            handedness TEXT,
            opponent_team TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/pitchers', methods=['GET'])
def get_pitchers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pitchers')
    pitchers = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([dict(ix) for ix in pitchers])

def insert_pitcher_data():
    # pitchers_data = get_probable_pitchers()
    pitchers_data = [
        {'pitcher': 'Max Scherzer', 'team': 'Mets', 'handedness': 'R', 'opponent_team': 'Yankees'},
        {'pitcher': 'Clayton Kershaw', 'team': 'Dodgers', 'handedness': 'L', 'opponent_team': 'Giants'}
    ]
    conn = get_db_connection()
    c = conn.cursor()
    c.executemany('''
        INSERT INTO pitchers (pitcher, team, handedness, opponent_team)
        VALUES (?, ?, ?, ?)
    ''', [(d['pitcher'], d['team'], d['handedness'], d['opponent_team']) for d in pitchers_data])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()  # Ensure the database and table are created
    insert_pitcher_data()  # Optionally, insert some initial data
    app.run(debug=True)
