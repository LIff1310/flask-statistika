import statistics
import sqlite3
import os
from flask import current_app

def hitung_statistik(data):
    return {
        "rata_rata": statistics.mean(data),
        "median": statistics.median(data),
        "modus": statistics.mode(data),
        "simpangan_baku": statistics.stdev(data) if len(data) > 1 else 0.0
    }

def simpan_data(data_input, hasil):
    db_path = os.path.join(os.getcwd(), current_app.config["DATABASE"])
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS hasil (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_input TEXT,
                    rata_rata REAL,
                    median REAL,
                    modus REAL,
                    simpangan_baku REAL
                )''')
    c.execute('''INSERT INTO hasil (data_input, rata_rata, median, modus, simpangan_baku)
                 VALUES (?, ?, ?, ?, ?)''',
              (data_input, hasil["rata_rata"], hasil["median"], hasil["modus"], hasil["simpangan_baku"]))
    conn.commit()
    conn.close()
