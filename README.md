# 🌍 AirGuardian AI  
### Citizen-Level Environmental Health Intelligence System

---

## 🚨 Problem Statement

Air pollution is one of the most severe environmental threats affecting urban populations. While Air Quality Index (AQI) data is publicly available, existing platforms only present numerical values without translating them into:

- Personalized health risk
- Locality-level environmental intelligence
- Actionable mitigation strategies
- Decision support for relocation vs. improvement

Citizens are given data — but not guidance.

AirGuardian AI addresses this gap by transforming environmental data into meaningful, decision-oriented intelligence.

---

## 💡 Solution Overview

AirGuardian AI is an environmental decision-support platform that converts AQI data into personalized exposure analysis and mitigation insights.

Instead of acting as a static AQI dashboard, the system:

- Converts AQI into a Personal Health Risk Score
- Analyzes locality-level micro-zone indicators
- Simulates environmental mitigation via tree-based modeling
- Provides relocation vs. improvement intelligence
- Visualizes short-term AQI trends for contextual awareness

The system focuses on enabling informed environmental decision-making at the citizen level.

---

## 🧠 Core Features

### 1️⃣ Live AQI Integration
- Fetches real-time air pollution data using OpenWeather Air Pollution API
- Provides up-to-date air quality context

### 2️⃣ Micro-Zone Intelligence Engine
Locality names are analyzed for environmental risk indicators such as:
- Industrial proximity
- Traffic density
- Residential clustering
- Green area presence

These signals dynamically adjust exposure risk using a structured multiplier model.

### 3️⃣ Personal Exposure Modeling
Risk score calculation is based on:
- Adjusted AQI
- Daily outdoor exposure hours
- Vulnerable household factor (children, elderly, respiratory conditions)

Output: Normalized Personal Health Risk Score (0–100).

### 4️⃣ Mitigation Simulation Engine
The system estimates:
- Approximate number of trees required for measurable AQI improvement
- Projected AQI after mitigation

This demonstrates community-level environmental improvement potential.

### 5️⃣ Decision Intelligence Layer
Users receive guidance on:
- Whether relocation is advisable
- Whether mitigation strategies are viable
- Relative environmental risk across monitored cities

---

## 🏗 Technical Architecture

**Backend:**  
- Python

**Frontend:**  
- Gradio UI Framework

**Data Integration:**  
- OpenWeather Air Pollution API

**Visualization:**  
- Matplotlib

**Custom Modules:**  
- Micro-Zone Risk Inference Engine  
- Personal Exposure Model  
- Tree-Based Mitigation Simulation Logic  

The architecture is modular and designed for scalability.

---

## 🌱 Environmental Impact

AirGuardian AI improves environmental decision-making by:

- Translating pollution data into health-centered intelligence
- Enabling safer housing and relocation decisions
- Encouraging urban tree-based mitigation strategies
- Supporting localized environmental planning awareness

The system shifts environmental tools from passive reporting to active guidance.

---

## 🚀 Future Scope

Future development may include:

- Satellite-based pollution mapping integration
- Machine learning models for micro-block AQI forecasting
- Real-time traffic emission data integration
- Municipal urban planning dashboards
- Community-level environmental impact tracking

This project demonstrates a scalable prototype of a citizen-focused environmental intelligence engine.

---

## 🛠 Installation & Setup

1. Install required libraries:

```
pip install gradio matplotlib numpy requests
```

2. Add your OpenWeather API key in `app.py`:

```
API_KEY = "YOUR_API_KEY_HERE"
```

3. Run the application:

```
python app.py
```

---

## ⚠️ Disclaimer

This project is a functional prototype developed for environmental innovation purposes. Real-world deployment would require validated environmental datasets, expanded geographic coverage, and collaboration with urban planning authorities.
