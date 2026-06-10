# 🌱 Smart Agriculture Monitoring System

An IoT-based Smart Agriculture Monitoring System built using **ESP32**, **DHT22 Sensor**, **Soil Moisture Monitoring**, **Automated Pump Control**, **ThingSpeak Cloud Integration**, and **Python-Based Analytics**.

The system continuously monitors environmental parameters such as temperature, humidity, and soil moisture. Based on soil conditions, it automatically controls irrigation through a pump simulation (LED), uploads data to ThingSpeak Cloud, logs sensor readings, and generates analytical graphs for monitoring crop conditions.

This project demonstrates practical concepts of IoT, Embedded Systems, Sensor Integration, Cloud Connectivity, Automation, Data Logging, and Data Analytics.

---

# 📖 Project Overview

Agriculture traditionally relies on manual monitoring and fixed irrigation schedules, often leading to:

- Excessive water usage
- Delayed irrigation
- Reduced crop productivity
- Increased labor effort
- Lack of real-time visibility

This project provides an intelligent IoT solution that automatically monitors field conditions and controls irrigation based on soil moisture levels.

The entire system can be implemented using physical hardware or simulated using Wokwi, making it ideal for students and IoT learners.

---

# 🎯 Objectives

- Monitor temperature and humidity using DHT22.
- Monitor soil moisture levels.
- Automatically control irrigation.
- Simulate water pump operation using LED.
- Upload sensor data to ThingSpeak Cloud.
- Generate alerts based on threshold conditions.
- Store sensor data for analytics.
- Visualize environmental trends using Python.

---

# 🚀 Key Features

### Environmental Monitoring

- Temperature Monitoring
- Humidity Monitoring
- Soil Moisture Monitoring

### Automation

- Automatic Pump Control
- Moisture-Based Irrigation
- Threshold-Based Decision Making

### Cloud Integration

- ThingSpeak Cloud Monitoring
- Remote Data Access
- Historical Data Storage

### Data Management

- CSV Data Logging
- Sensor History Tracking
- Environmental Trend Analysis

### Visualization

- Serial Monitor Output
- ThingSpeak Dashboard
- Soil Moisture Graphs
- Temperature Graphs
- Humidity Graphs

### Simulation

- Fully Simulated Using Wokwi
- No Physical Hardware Required

---

# 🏗 System Architecture

## High-Level Architecture

```text
+----------------------+
|      DHT22 Sensor    |
| Temperature/Humidity |
+----------+-----------+
           |
           |
           v
+----------------------+
| Soil Moisture Sensor |
| (Potentiometer Sim.) |
+----------+-----------+
           |
           |
           v
+----------------------+
|        ESP32         |
| Data Acquisition     |
+----------+-----------+
           |
           |
           v
+----------------------+
| Threshold Logic      |
| Pump Decision Engine |
+----------+-----------+
           |
    +------+------+
    |             |
    v             v
+--------+   +-----------+
|  LED   |   |  Serial   |
| Pump   |   |  Monitor  |
+--------+   +-----------+
                  |
                  |
                  v
         +------------------+
         |   ThingSpeak     |
         | Cloud Dashboard  |
         +------------------+
                  |
                  |
                  v
         +------------------+
         | CSV Data Logging |
         +------------------+
                  |
                  |
                  v
         +------------------+
         | Python Analytics |
         | & Graphs         |
         +------------------+
```

---

# 🔄 Workflow

```text
Sensor Data
     │
     ▼
ESP32 Reads Values
     │
     ▼
Threshold Comparison
     │
     ▼
Pump Decision Logic
     │
 ┌───┴────┐
 │        │
 ▼        ▼
Pump ON  Pump OFF
 │
 ▼
ThingSpeak Upload
 │
 ▼
CSV Logging
 │
 ▼
Analytics & Graphs
```

---

# 🔧 Hardware Components Used

| Component | Purpose |
|------------|------------|
| ESP32 Dev Module | Main Controller |
| DHT22 Sensor | Temperature & Humidity Monitoring |
| Soil Moisture Sensor / Potentiometer | Soil Moisture Monitoring |
| LED | Pump Simulation |
| Jumper Wires | Wiring |
| USB Cable | ESP32 Programming |
| Wokwi Simulator | Virtual Simulation |

---

# 💻 Software & Cloud Technologies Used

| Technology | Purpose |
|------------|------------|
| Arduino IDE | ESP32 Programming |
| ESP32 Board Package | ESP32 Development |
| Python 3.x | Data Processing |
| Pandas | Data Analytics |
| Matplotlib | Data Visualization |
| ThingSpeak | Cloud Data Logging |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📁 Repository Structure

```text
Smart-Agriculture-Monitoring-System/
│
├── arduino_code/
│   └── smart_agriculture.ino
│
├── python_simulation/
│   ├── data_logger.py
│   └── analytics.py
│
├── data/
│   └── sensor_log.csv
│
├── outputs/
│   ├── soil_moisture_graph.png
│   ├── temperature_graph.png
│   └── humidity_graph.png
│
├── images/
│   ├── circuit_diagram.png
│   ├── simulation_running.png
│   ├── serial_monitor.png
│   ├── pump_on.png
│   ├── pump_off.png
│   └── analytics_output.png
│
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔌 Circuit Overview

## DHT22 Sensor

| DHT22 Pin | ESP32 Pin |
|------------|------------|
| VCC | 3.3V |
| GND | GND |
| DATA | GPIO 4 |

---

## Soil Moisture Sensor

| Sensor Pin | ESP32 Pin |
|------------|------------|
| VCC | 3.3V |
| GND | GND |
| AO | GPIO 34 |

---

## Pump Simulation (LED)

| LED Pin | ESP32 Pin |
|------------|------------|
| Anode (+) | GPIO 25 |
| Cathode (-) | GND |

---

# ⚙ How the System Works

### Step 1

ESP32 reads:

- Temperature
- Humidity
- Soil Moisture

### Step 2

Sensor values are compared with predefined thresholds.

### Step 3

If soil moisture falls below the threshold:

```text
Pump ON
```

Otherwise:

```text
Pump OFF
```

### Step 4

Sensor readings are displayed on the Serial Monitor.

### Step 5

Sensor values are uploaded to ThingSpeak Cloud.

### Step 6

Sensor data is stored in CSV format.

### Step 7

Python scripts generate analytical graphs.

---

# ☁ ThingSpeak Integration

The project uses ThingSpeak for cloud-based monitoring and storage.

### Monitored Parameters

| Field | Parameter |
|---------|---------|
| Field 1 | Temperature |
| Field 2 | Humidity |
| Field 3 | Soil Moisture |
| Field 4 | Pump Status |

### Benefits

- Real-time cloud monitoring
- Historical data visualization
- Remote access
- IoT dashboard capabilities

### API Configuration

```cpp
String apiKey = "YOUR_THINGSPEAK_WRITE_API_KEY";
```

Never upload actual API keys to GitHub.

Use placeholders or environment variables.

Example:

```env
WIFI_SSID=YOUR_WIFI_NAME
WIFI_PASSWORD=YOUR_WIFI_PASSWORD

THINGSPEAK_API_KEY=YOUR_THINGSPEAK_WRITE_API_KEY
```

---

# 🛠 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Agriculture-Monitoring-System.git

cd Smart-Agriculture-Monitoring-System
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Python Simulation

Generate sample sensor data:

```bash
python main.py
```

Run logger:

```bash
python python_simulation/data_logger.py
```

---

# 📊 Generate Analytics Graphs

Run:

```bash
python python_simulation/analytics.py
```

Graphs are automatically generated inside:

```text
outputs/
```

Generated files:

- soil_moisture_graph.png
- temperature_graph.png
- humidity_graph.png

---

# 🔥 Upload & Run ESP32 Code

### Step 1

Open Arduino IDE.

### Step 2

Install ESP32 Board Package.

### Step 3

Select Board:

```text
ESP32 Dev Module
```

### Step 4

Open:

```text
arduino_code/smart_agriculture.ino
```

### Step 5

Update WiFi and ThingSpeak credentials.

### Step 6

Upload code to ESP32.

### Step 7

Open Serial Monitor.

Baud Rate:

```text
115200
```

---

# 📈 Sample Output

### Dry Soil

```text
Temperature: 29°C
Humidity: 58%

Soil Moisture: 288

ALERT: Dry Soil Detected
Pump Status: ON

Uploading to ThingSpeak...
```

---

### Wet Soil

```text
Temperature: 29°C
Humidity: 58%

Soil Moisture: 3034

Soil Moisture Normal
Pump Status: OFF

Uploading to ThingSpeak...
```

---

### 📸Screenshots

- ![Circuit Diagram](<images/circuit diagram.png>)
- ![Wokwi Simulation Running](<images/Simulation Running.png>)
- ![Serial Monitor Output](<images/Serial Monitor.png>)
- ![Pump ON State](<images/Pump On.png>)
- ![Pump OFF State](<images/Pump Off.png>)
- ![Analytics Graph Output](<images/Dashboard Output Graph.png>)


```text
images/
├── circuit_diagram.png
├── simulation_running.png
├── serial_monitor.png
├── pump_on.png
├── pump_off.png
├── thingspeak_dashboard.png
└──analytics_output.png
```

---

# 📚 Concepts Demonstrated

- Internet of Things (IoT)
- Embedded Systems
- Sensor Interfacing
- Cloud Computing
- ThingSpeak Integration
- Automation Logic
- Threshold-Based Control
- Data Logging
- Data Analytics
- Data Visualization

---

# 🌍 Real-World Applications

- Smart Irrigation Systems
- Precision Agriculture
- Greenhouse Monitoring
- Nursery Automation
- Water Conservation Projects
- Agricultural Research

---

# 🔮 Future Improvements

- MQTT Communication
- Node-RED Dashboard
- Blynk Mobile Monitoring
- Water Level Monitoring
- Weather API Integration
- LoRa Connectivity
- AI-Based Irrigation Prediction
- Smart Fertilizer Recommendation

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- ESP32 Programming
- Sensor Integration
- IoT System Design
- ThingSpeak Cloud Connectivity
- Automation Systems
- Data Logging Techniques
- Python Analytics
- Data Visualization
- GitHub Documentation

---

# 👩‍💻 Author

**Shravani Hande**

Aspiring IoT Engineer | Embedded Systems Enthusiast | Smart Agriculture Developer

---

# 📄 License

This project is developed for educational and learning purposes.

MIT License

Copyright (c) 2026

