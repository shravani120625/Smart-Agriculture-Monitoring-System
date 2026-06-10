import pandas as pd
import random
from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

data = {
    "timestamp": datetime.now(),
    "temperature": random.randint(20, 40),
    "humidity": random.randint(40, 90),
    "soil_moisture": random.randint(200, 3500),
    "water_level": random.randint(20, 100)
}

df = pd.DataFrame([data])

file_path = "data/sensor_log.csv"

if os.path.exists(file_path):
    old = pd.read_csv(file_path)
    df = pd.concat([old, df], ignore_index=True)

df.to_csv(file_path, index=False)

print("Sensor data saved.")