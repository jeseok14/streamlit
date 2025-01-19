import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write(f"I'm {age} years old.")

st.subheader("Range slider")

range = st.slider('Select a range of values', 0.0, 100.0, (25.00, 75.00))
st.write(f"Values:{range}")

st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value = (time(11,30), time(12,45))
)
st.write(f"You're cheduled for : {appointment}")

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1, 1, 9, 30),
    format = "MM/DD/YY - hh:mm"
)
st.write(f"Start time : {start_time}")


st.header('st.select_slider')

st.subheader('select one thing')

color = st.select_slider(
    "Select a color of the rainbow",
    options = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
)
st.write(f"My favorite color is {color}")

st.subheader('select two things')

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value = ('orange', 'blue')
)
st.write(f"You selected wavelengths between {start_color} and {end_color}")