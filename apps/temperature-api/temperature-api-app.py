from flask import Flask, request, jsonify
import random

app = Flask(__name__)

sensors = {
    "1": "kitchen",
    "2": "living_room",
    "3": "bedroom",
    "4": "bathroom"    
}

@app.route('/temperature')
def temperature():
    sensor_id = request.args.get('sensorId')
    if not sensor_id:
        return jsonify({"error": "sensorId is required"}), 400

    location = "unknown"
    if sensor_id in sensors:
        location = sensors[sensor_id]
    
    # Сгенерировать случайную температуру от 10 до 30 °C 
    temp = round(random.uniform(10, 30), 1)
    return jsonify({
        "sensorId": sensor_id,
        "location": location,
        "temperature": temp
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)