import sqlite3
from config import DATABASE_NAME

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT UNIQUE,
        country TEXT,
        latitude REAL,
        longitude REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        timestamp DATETIME,
        temperature_c REAL,
        humidity INTEGER,
        pressure_hpa REAL,
        wind_speed_mps REAL,
        weather_condition TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(city_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        alert_type TEXT,
        alert_message TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pipeline_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT,
        records_processed INTEGER,
        error_message TEXT
    )
    ''')

    conn.commit()
    conn.close()