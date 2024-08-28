import streamlit as st
import requests

st.title("Know thy wather")
st.write("Enter the city name to get the current weather information.")

city_name = st.text_input("City Name", "")
api_key=st.secrets['api_key']

def get_weather(city_name, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        st.error("City not found, please try again.")
        return None
    else:
        st.error("An error occurred while fetching the data.")
        return None

 # Replace with your actual API key

if city_name:
    data = get_weather(city_name, api_key)
    if data:
        st.write(f"### Weather in {city_name}")
        st.write(f"Temperature: {data['current']['temp_c']} °C")
        st.write(f"Condition: {data['current']['condition']['text']}")
        st.write(f"Humidity: {data['current']['humidity']}%")
        st.write(f"Wind Speed: {data['current']['wind_kph']} kph")
