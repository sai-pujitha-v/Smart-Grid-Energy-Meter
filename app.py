import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Smart Grid Dashboard", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .metric-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-top: 5px solid #f1c40f; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Smart Grid Utility Monitor")

cost_per_unit = st.sidebar.number_input("Cost per kWh (INR)", value=8.0)
voltage = 230 # Standard AC Voltage

if 'energy_history' not in st.session_state:
    st.session_state.energy_history = pd.DataFrame(columns=['Time', 'Current_A', 'Power_W'])

placeholder = st.empty()

for _ in range(100):
    curr_a = round(np.random.uniform(0.5, 10.0), 2)
    power_w = round(curr_a * voltage, 1)
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), curr_a, power_w]], 
                            columns=st.session_state.energy_history.columns)
    st.session_state.energy_history = pd.concat([st.session_state.energy_history, new_data]).tail(20)

    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.metric("Live Current", f"{curr_a} A")
        c2.metric("Active Power", f"{power_w} W")
        
        # Predictive Logic
        daily_kwh = (power_w * 24) / 1000
        monthly_bill = daily_kwh * 30 * cost_per_unit
        c3.metric("Projected Bill", f"₹{round(monthly_bill, 2)}", delta="Estimated")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.energy_history['Time'], 
                                 y=st.session_state.energy_history['Power_W'], 
                                 fill='tozeroy', line_color='#f1c40f'))
        fig.update_layout(title="Real-time Power Load (Watts)", template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(2)
