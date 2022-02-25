import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import pytz
'''
# TaxiFareModel front
'''
### Input your Passenger Numbers:
st.select_slider('Slide to select', options=[1,2,3,4,5,6,7,8])


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

'''
2. Let's build a dictionary containing the parameters for our API...
'''
pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
eastern = pytz.timezone("US/Eastern")
localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")

params_dict = {
"key": '2013-07-06 17:18:00.000000119',
"pickup_datetime": formatted_pickup_datetime,
"pickup_longitude": pickup_longitude,
"pickup_latitude": pickup_latitude,
"dropoff_longitude": dropoff_longitude,
"dropoff_latitude": dropoff_latitude,
"passenger_count": passenger_count
}

'''
3. Let's call our API using the `requests` package...
'''
response = requests.get(url,params=params_dict).json()

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

print(response)

if __name__ == '__main__':
    pickup_datetime='2012-10-06 12:10:20'
    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
    params_dict = dict(
    pickup_datetime='2012-10-06 12:10:20',
    pickup_longitude=40.7614327,
    pickup_latitude=-73.9798156,
    dropoff_longitude=40.6413111,
    dropoff_latitude=-73.9797156,
    passenger_count=1
    )
    response = requests.get(url,params=params_dict).json()
    print(response)
