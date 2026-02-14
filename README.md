# ⚡ Smart Grid Energy Meter

A non-invasive IoT energy monitoring system that provides real-time visibility into household or industrial power consumption and predicts monthly utility expenses.

## 🚀 Features
- **Non-Invasive Sensing:** Uses a Clip-on CT sensor (SCT-013) to measure current without cutting wires.
- **Cost Prediction:** Real-time calculation of electricity costs based on current load.
- **Monthly Forecasting:** Predicts total monthly consumption using historical averages.
- **Overload Alerts:** Notifies users via the dashboard when power exceeds a safe limit.

## ⚙️ Engineering Logic
- **Hardware:** ESP32 samples the analog signal from the CT sensor at high frequency.
- **Software:** Python calculates RMS Current and Real Power ($P = V \times I \times \cos \phi$) to visualize energy usage patterns.
