#include <WiFi.h>
#include <HTTPClient.h>
#include "EmonLib.h"

EnergyMonitor emon1;
const int ctPin = 34;

void setup() {
  Serial.begin(115200);
  emon1.current(ctPin, 30); // Pin, Calibration constant
  // WiFi provisioning logic from previous projects
}

void loop() {
  double Irms = emon1.calcIrms(1480); // Calculate RMS Current
  
  HTTPClient http;
  http.begin("http://your-grid-app.com/update");
  http.addHeader("Content-Type", "application/json");
  
  String json = "{\"current\":" + String(Irms) + "}";
  http.POST(json);
  http.end();
  
  delay(2000);
}
