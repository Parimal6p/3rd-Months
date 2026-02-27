def validate(data):
    if not (-50 <= data["temp"] <= 60):
        return False
    if not (0 <= data["humidity"] <= 100):
        return False
    if data["wind"] < 0:
        return False
    return True