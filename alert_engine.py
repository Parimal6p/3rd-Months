from config import TEMP_ALERT_THRESHOLD, HUMIDITY_ALERT_THRESHOLD, WIND_ALERT_THRESHOLD

def check_alerts(data):
    alerts = []

    if data["temp"] > TEMP_ALERT_THRESHOLD:
        alerts.append("High Temperature")

    if data["humidity"] > HUMIDITY_ALERT_THRESHOLD:
        alerts.append("High Humidity")

    if data["wind"] > WIND_ALERT_THRESHOLD:
        alerts.append("Strong Wind")

    return alerts