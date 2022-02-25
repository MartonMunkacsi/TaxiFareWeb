import streamlit as st
import requests
import time
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
date = st.date_input("Please select date")
st.write('Pick-up date', date)

times = st.time_input("Please select a time")
st.write('Pick-up time', times)
passenger_count = st.number_input('Insert a number', min_value=1, step=1)
st.write('The current number is ', passenger_count)
# location
pickup_longitude = st.number_input('Insert pickup longitude')
pickup_latitude = st.number_input('Insert pickup latitude')
dropoff_longitude = st.number_input('Insert dropoff longitude')
dropoff_latitude = st.number_input('Insert dropoff latitude')


# -----------------------------------------------------------
url = 'https://taxifare.lewagon.ai/predict'
params = {
        "pickup_datetime": str(date) + " " + str(times),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

if url == 'https://taxifare.lewagon.ai/predict':


    if st.button('Predict'):
        response = requests.get(url, params=params).json()
        prediction = response.get("fare", "no prediction")
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        st.write(f'${round(prediction,2)}')

# make sure to add your HEROKU_EMAIL to secrets on github repo and change setup.sh email to f${HEROKU_EMAIL}
