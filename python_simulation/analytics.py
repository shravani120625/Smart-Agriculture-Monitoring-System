import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/sensor_log.csv")

# Soil Moisture Graph
plt.figure(figsize=(8,4))
plt.plot(df["soil_moisture"])
plt.title("Soil Moisture Trend")
plt.xlabel("Reading")
plt.ylabel("Soil Moisture")
plt.grid(True)
plt.savefig("outputs/soil_moisture_graph.png")
plt.close()

# Temperature Graph
plt.figure(figsize=(8,4))
plt.plot(df["temperature"])
plt.title("Temperature Trend")
plt.xlabel("Reading")
plt.ylabel("Temperature")
plt.grid(True)
plt.savefig("outputs/temperature_graph.png")
plt.close()

# Humidity Graph
plt.figure(figsize=(8,4))
plt.plot(df["humidity"])
plt.title("Humidity Trend")
plt.xlabel("Reading")
plt.ylabel("Humidity")
plt.grid(True)
plt.savefig("outputs/humidity_graph.png")
plt.close()

print("Graphs Generated Successfully")