# 🌦️ Advanced Weather Data Pipeline System

## 📌 Project Overview
This project is an end-to-end ETL pipeline that extracts real-time weather data from OpenWeatherMap API, validates and processes it, stores it in a normalized SQLite database, and generates alerts and monitoring logs.

## 🏗️ Architecture
API → Extract → Validate → Transform → Load → Alerts → Monitoring → Scheduler

## ⚙️ Setup Instructions

1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt
3. Add your API key in config.py
4. Run pipeline:
   python src/etl_pipeline.py
5. Run scheduler:
   python src/scheduler.py

## 🗄️ Database Tables
- cities
- weather_data
- alerts
- pipeline_logs

## 🚨 Alert System
- Temperature > 30°C
- Humidity > 75%
- Wind Speed > 15 m/s

## 📊 Monitoring
Run:
python src/monitor.py

## 🧪 Technologies Used
- Python
- SQLite
- OpenWeatherMap API
- Schedule library
- Flask (optional dashboard)

## 📈 Future Improvements
- Email alerts
- Cloud deployment
- Docker support
- Power BI dashboard
