import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
'''
d = st.date_input("Date")
st.write("Date:", d)
t = st.time_input("Time")
st.write("Time:", t)

'''
- pickup longitude
'''
pickup_longitude = st.text_input("pickup longitude", "-73.950655")
st.write("pickup longitude: ", pickup_longitude)

'''
- pickup latitude
'''
pickup_latitude = st.text_input("pickup latitude", "40.783282")
st.write("pickup longitude: ", pickup_latitude)

'''
- dropoff longitude
'''
dropoff_longitude = st.text_input("dropoff longitude", "-73.950655")
st.write("pickup longitude: ", dropoff_longitude)

'''
- dropoff latitude
'''
dropoff_latitude = st.text_input("dropoff latitude", "40.783282")
st.write("dropoff latitude: ", dropoff_latitude)


'''
- passenger count
'''
passenger_count = st.text_input("passenger count", "2")
st.write("passenger count: ", passenger_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-2mxzlh7rma-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
pickup_datetime = str(d)+" "+str(t)
pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_count)
}

'''
3. Let's call our API using the `requests` package...
'''

response = requests.get(url,params=params).json()


'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
st.write("This is the prediction: ", response)
