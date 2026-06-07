import streamlit as st
import joblib
import pandas as pd

model = joblib.load("airline_satisfaction_model.pkl")
# Page Configuration
st.set_page_config(
    page_title="Airline Satisfaction Prediction",
    page_icon="✈️",
    layout="centered"
)

# Title
st.title("✈️ Airline Passenger Satisfaction Prediction")

st.write("Enter Passenger Details Below")

# Inputs

passenger_id = st.number_input(
    "Passenger ID",
    min_value=1,
    value=1
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

flight_distance = st.number_input(
    "Flight Distance",
    min_value=0,
    value=1000
)

inflight_wifi_service = st.slider(
    "Inflight Wifi Service",
    0, 5, 3
)

online_boarding = st.slider(
    "Online Boarding",
    0, 5, 3
)

seat_comfort = st.slider(
    "Seat Comfort",
    0, 5, 3
)

inflight_entertainment = st.slider(
    "Inflight Entertainment",
    0, 5, 3
)

leg_room_service = st.slider(
    "Leg Room Service",
    0, 5, 3
)

travel_type = st.selectbox(
    "Travel Type",
    ["Business Travel", "Personal Travel"]
)

travel_encoded = 1 if travel_type == "Personal Travel" else 0

travel_class = st.selectbox(
    "Class",
    ["Business", "Eco"]
)

class_encoded = 1 if travel_class == "Eco" else 0

# Prediction Button

if st.button("Predict"):

    input_data = pd.DataFrame({
        'id': [passenger_id],
        'age': [age],
        'flight_distance': [flight_distance],
        'inflight_wifi_service': [inflight_wifi_service],
        'online_boarding': [online_boarding],
        'seat_comfort': [seat_comfort],
        'inflight_entertainment': [inflight_entertainment],
        'leg_room_service': [leg_room_service],
        'type_of_travel_Personal Travel': [travel_encoded],
        'class_Eco': [class_encoded]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Satisfied Passenger")
    else:
        st.error("❌ Neutral / Dissatisfied Passenger")