import pandas as pd
from datetime import datetime
import random

data = {
    "timestamp": datetime.now(),
    "temperature": random.randint(20, 40),
    "humidity": random.randint(40, 90),
    "soil_moisture": random.randint(200, 3500),
    "pump_status": random.choice([0, 1])
}

df = pd.DataFrame([data])

try:
    old = pd.read_csv("data/sensor_log.csv")
    df = pd.concat([old, df], ignore_index=True)
except:
    pass

df.to_csv("data/sensor_log.csv", index=False)

print("Data Logged Successfully")