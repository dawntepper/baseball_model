import sqlite3

def get_db_connection():
    conn = sqlite3.connect('baseball_data.db')
    return conn

def save_players(players_data):
    conn = get_db_connection()
    cur = conn.cursor()
   
    cur.executemany('INSERT INTO Players (Name, Team, Games, etc) VALUES (?, ?, ?, etc)', players_data)
    conn.commit()
    conn.close()

def save_teams(teams_data):
    conn = get_db_connection()
    cur = conn.cursor()

def save_pitchers(pitchers_data):
    conn = get_db_connection()
    cur = conn.cursor()
    # Create table if not exists and insert data; adapt fields as necessary
    cur.executemany('INSERT INTO Pitchers (Name, Team, Handedness) VALUES (?, ?, ?)', 
                    [(p['Name'], p['Team'], p['Handedness']) for p in pitchers_data])
  
    
    cur.executemany('INSERT INTO Teams (TeamName, Games, etc) VALUES (?, ?, etc)', teams_data)
    conn.commit()
    conn.close()
