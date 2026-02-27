from database import setup_database, get_connection
from api_client import fetch_weather
from validators import validate
from alert_engine import check_alerts
from config import CITIES

def run_pipeline():
    setup_database()
    conn = get_connection()
    cursor = conn.cursor()

    processed = 0

    try:
        for city in CITIES:
            data = fetch_weather(city)

            if not validate(data):
                continue

            cursor.execute("INSERT OR IGNORE INTO cities (city_name, country, latitude, longitude) VALUES (?, ?, ?, ?)",
                           (data["city"], data["country"], data["lat"], data["lon"]))

            cursor.execute("SELECT city_id FROM cities WHERE city_name = ?", (data["city"],))
            city_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO weather_data 
                (city_id, timestamp, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (city_id, data["timestamp"], data["temp"], data["humidity"],
                  data["pressure"], data["wind"], data["condition"]))

            alerts = check_alerts(data)
            for alert in alerts:
                cursor.execute("INSERT INTO alerts (city_id, alert_type, alert_message) VALUES (?, ?, ?)",
                               (city_id, alert, f"{alert} detected in {data['city']}"))

            processed += 1

        cursor.execute("INSERT INTO pipeline_logs (status, records_processed) VALUES (?, ?)",
                       ("SUCCESS", processed))

        conn.commit()

    except Exception as e:
        cursor.execute("INSERT INTO pipeline_logs (status, records_processed, error_message) VALUES (?, ?, ?)",
                       ("FAILED", processed, str(e)))
        conn.commit()

    finally:
        conn.close()

if __name__ == "__main__":
    run_pipeline()
