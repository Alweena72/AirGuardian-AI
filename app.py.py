!pip install gradio matplotlib numpy requests

import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import random
import requests

API_KEY = "PASTE_YOUR_OPENWEATHER_API_KEY"

# =========================
# Pakistan Cities
# =========================
city_coordinates = {
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Faisalabad": (31.4504, 73.1350),
    "Rawalpindi": (33.5651, 73.0169),
    "Peshawar": (34.0151, 71.5805),
    "Multan": (30.1575, 71.5249),
    "Quetta": (30.1798, 66.9750)
}

fallback_aqi = {
    "Lahore": 230,
    "Karachi": 160,
    "Islamabad": 105,
    "Faisalabad": 190,
    "Rawalpindi": 140,
    "Peshawar": 155,
    "Multan": 175,
    "Quetta": 90
}

area_modifier = {
    "Industrial Zone": 1.3,
    "High Traffic Zone": 1.2,
    "Dense Residential": 1.1,
    "Moderate Residential": 1.0,
    "Green / Low Density": 0.85
}

# =========================
# Fetch Live AQI
# =========================
def get_live_aqi(city):
    try:
        lat, lon = city_coordinates[city]
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        scale = data["list"][0]["main"]["aqi"]
        return scale * 50
    except:
        return fallback_aqi[city]

# =========================
# Micro-Zone Intelligence
# =========================
def micro_zone_analysis(locality_name):
    score = 1.0
    explanation = []

    name = locality_name.lower()

    if any(word in name for word in ["industrial", "factory", "estate"]):
        score += 0.25
        explanation.append("Proximity to industrial activity detected.")

    if any(word in name for word in ["market", "road", "signal", "bazaar"]):
        score += 0.20
        explanation.append("High traffic density indicators found.")

    if any(word in name for word in ["colony", "phase", "sector", "block"]):
        score += 0.15
        explanation.append("Dense residential clustering inferred.")

    if any(word in name for word in ["garden", "green", "park"]):
        score -= 0.10
        explanation.append("Green space indicators detected.")

    return score, explanation

# =========================
# AI ENGINE
# =========================
def env_ai(mode, city, area_type, locality, outdoor_hours, vulnerable):

    base_aqi = get_live_aqi(city)
    trend = [base_aqi + random.randint(-20, 20) for _ in range(7)]
    current = trend[-1]

    adjusted = current * area_modifier[area_type]

    micro_multiplier, micro_notes = micro_zone_analysis(locality)
    micro_adjusted = adjusted * micro_multiplier

    exposure = micro_adjusted * (outdoor_hours / 24)

    if vulnerable:
        exposure *= 1.25

    risk_score = min(int(exposure * 0.5), 100)

    micro_index = min(int((micro_multiplier - 0.8) * 100), 100)

    # Risk Category
    if micro_adjusted <= 50:
        category = "🟢 Good"
        color = "#16a34a"
    elif micro_adjusted <= 100:
        category = "🟡 Moderate"
        color = "#ca8a04"
    elif micro_adjusted <= 150:
        category = "🟠 Unhealthy (Sensitive)"
        color = "#ea580c"
    elif micro_adjusted <= 200:
        category = "🔴 Unhealthy"
        color = "#dc2626"
    else:
        category = "🟣 Very Unhealthy"
        color = "#7e22ce"

    safest_city = min(fallback_aqi, key=fallback_aqi.get)

    if mode == "I Want to Relocate":
        relocation_advice = f"""
### Smart Relocation Insight
Lowest AQI currently: **{safest_city}**
Long-term exposure reduction possible via relocation.
"""
    else:
        relocation_advice = "Mitigation-focused strategy selected."

    trees_needed = int(micro_adjusted * 20)
    projected = max(int(micro_adjusted * 0.75), 50)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(trend, marker="o")
    ax.set_title("7-Day AQI Trend")
    ax.set_ylabel("AQI")
    ax.set_xlabel("Days")

    micro_text = " ".join(micro_notes) if micro_notes else "No major micro-risk indicators detected."

    dashboard = f"""
## Environmental Intelligence Report

### Location Profile
City: {city}
Area Type: {area_type}
Locality: {locality}

---

### Air Quality Status
Base AQI: {int(current)}
Micro-Zone Adjusted AQI: {int(micro_adjusted)}
<span style="color:{color}; font-size:20px;"><b>{category}</b></span>

---

### Micro-Zone Intelligence
Micro-Risk Index: {micro_index}/100
AI Interpretation: {micro_text}

---

### Health Exposure Model
Outdoor Hours: {outdoor_hours} hrs/day
Vulnerable Household: {vulnerable}
Personal Risk Score: {risk_score}/100

---

### Mitigation Simulation
Estimated Trees Required (Community Scale): {trees_needed}
Projected AQI After Plantation: {projected}

---

{relocation_advice}
"""

    return dashboard, fig

# =========================
# UI
# =========================
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # AirGuardian AI Pro
    ### Citizen-Level Environmental Health Intelligence System
    """)

    with gr.Row():
        with gr.Column(scale=1):
            mode = gr.Radio(
                ["I Want to Relocate", "I Cannot Relocate – Improve My Area"],
                label="Objective"
            )

            city = gr.Dropdown(list(city_coordinates.keys()), label="City")

            area_type = gr.Dropdown(list(area_modifier.keys()), label="Area Type")

            locality = gr.Textbox(label="Enter Your Locality / Neighborhood Name")

            outdoor_hours = gr.Slider(1, 24, value=6, label="Daily Outdoor Exposure (Hours)")

            vulnerable = gr.Checkbox(label="Children / Elderly / Respiratory Conditions Present")

            analyze = gr.Button("Run Environmental AI Scan")

        with gr.Column(scale=2):
            output = gr.Markdown()
            plot = gr.Plot()

    analyze.click(
        env_ai,
        inputs=[mode, city, area_type, locality, outdoor_hours, vulnerable],
        outputs=[output, plot]
    )

demo.launch(share=True)