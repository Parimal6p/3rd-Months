from database import get_connection

def show_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM weather_data")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM pipeline_logs ORDER BY log_id DESC LIMIT 1")
    last_run = cursor.fetchone()

    print("WEATHER PIPELINE STATUS")
    print("-----------------------")
    print("Total Records:", total)
    print("Last Run:", last_run)

    conn.close()

if __name__ == "__main__":
    show_status()