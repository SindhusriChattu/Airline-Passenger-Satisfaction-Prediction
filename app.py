import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Airline Satisfaction Prediction",
    page_icon="✈️"
)

st.title("✈️ Airline Satisfaction Prediction")

# Passenger Details
age = st.number_input("Age", 1, 100, 30)
flight_distance = st.number_input("Flight Distance", 0, 10000, 1000)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

customer_type = st.selectbox(
    "Customer Type",
    ["Loyal Customer", "disloyal Customer"]
)

travel_type = st.selectbox(
    "Type of Travel",
    ["Business Travel", "Personal Travel"]
)

travel_class = st.selectbox(
    "Class",
    ["Business", "Eco", "Eco Plus"]
)

# Service Ratings
wifi = st.slider("Inflight Wifi Service", 0, 5, 3)
time_conv = st.slider("Departure/Arrival Time Convenient", 0, 5, 3)
online_booking = st.slider("Ease of Online Booking", 0, 5, 3)
gate_location = st.slider("Gate Location", 0, 5, 3)
food_drink = st.slider("Food and Drink", 0, 5, 3)
online_boarding = st.slider("Online Boarding", 0, 5, 3)
seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
onboard_service = st.slider("On-board Service", 0, 5, 3)
leg_room = st.slider("Leg Room Service", 0, 5, 3)
baggage = st.slider("Baggage Handling", 0, 5, 3)
checkin = st.slider("Check-in Service", 0, 5, 3)
inflight_service = st.slider("Inflight Service", 0, 5, 3)
cleanliness = st.slider("Cleanliness", 0, 5, 3)

dep_delay = st.number_input(
    "Departure Delay in Minutes",
    0,
    2000,
    0
)

arr_delay = st.number_input(
    "Arrival Delay in Minutes",
    0,
    2000,
    0
)

if st.button("Predict Satisfaction"):

    data = pd.DataFrame({
        "Age": [age],
        "Flight Distance": [flight_distance],
        "Inflight wifi service": [wifi],
        "Departure/Arrival time convenient": [time_conv],
        "Ease of Online booking": [online_booking],
        "Gate location": [gate_location],
        "Food and drink": [food_drink],
        "Online boarding": [online_boarding],
        "Seat comfort": [seat_comfort],
        "Inflight entertainment": [entertainment],
        "On-board service": [onboard_service],
        "Leg room service": [leg_room],
        "Baggage handling": [baggage],
        "Checkin service": [checkin],
        "Inflight service": [inflight_service],
        "Cleanliness": [cleanliness],
        "Departure Delay in Minutes": [dep_delay],
        "Arrival Delay in Minutes": [arr_delay],
        "Gender_Male": [1 if gender == "Male" else 0],
        "Customer Type_disloyal Customer": [1 if customer_type == "disloyal Customer" else 0],
        "Type of Travel_Personal Travel": [1 if travel_type == "Personal Travel" else 0],
        "Class_Eco": [1 if travel_class == "Eco" else 0],
        "Class_Eco Plus": [1 if travel_class == "Eco Plus" else 0]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Satisfied Passenger")
    else:
        st.error("❌ Neutral or Dissatisfied Passenger")

