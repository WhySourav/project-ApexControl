from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OPENF1_BASE = "https://api.openf1.org/v1"
SESSION_KEY = "bahrain2025"  # Fixed session key for Bahrain GP 2025

@app.route("/telemetry")
def get_telemetry():
    driver_number = request.args.get("driver_number", "1")
    url = f"{OPENF1_BASE}/car_data?session_key={SESSION_KEY}&driver_number={driver_number}"
    resp = requests.get(url)
    data = resp.json()
    return jsonify(data)

@app.route("/sync_data")
def sync_data():
    video_time = float(request.args.get("video_time", 0))
    api_start = request.args.get("api_start")
    video_offset = float(request.args.get("video_offset", 0))
    driver_number = request.args.get("driver_number", "1")

    api_start_dt = datetime.fromisoformat(api_start.replace("Z", "+00:00"))
    current_api_time = api_start_dt + timedelta(seconds=(video_time - video_offset))

    url = f"{OPENF1_BASE}/car_data?session_key={SESSION_KEY}&driver_number={driver_number}"
    resp = requests.get(url)
    data = resp.json()
    nearest = min(data, key=lambda t: abs(datetime.fromisoformat(t["date"].replace("Z", "+00:00")) - current_api_time))
    return jsonify(nearest)

if __name__ == "__main__":
    app.run(debug=True)
