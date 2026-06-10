#include <WiFi.h>
#include "DHT.h"
#include "ThingSpeak.h"

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Wokwi-GUEST";
const char* password = "";

WiFiClient client;

unsigned long channelID = 3404714;
const char* writeAPIKey = "NIK2WVQVX50V58H4";

int soilPin = 34;
int pumpPin = 25;

void setup() {

  Serial.begin(115200);

  pinMode(pumpPin, OUTPUT);

  WiFi.begin(ssid, password);

  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi Connected");

  ThingSpeak.begin(client);

  dht.begin();
}

void loop() {

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  int soil = analogRead(soilPin);

  int pumpStatus = 0;

  if(soil < 1660){
      digitalWrite(pumpPin, HIGH);
      pumpStatus = 1;
  }
  else{
      digitalWrite(pumpPin, LOW);
      pumpStatus = 0;
  }

  ThingSpeak.setField(1,temp);
  ThingSpeak.setField(2,hum);
  ThingSpeak.setField(3,soil);
  ThingSpeak.setField(4,pumpStatus);

  int response = ThingSpeak.writeFields(channelID,writeAPIKey);

  Serial.print("ThingSpeak Response: ");
  Serial.println(response);

  delay(20000);
}