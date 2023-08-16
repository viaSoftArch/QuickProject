import requests
import datetime as dt 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY =  "" # Add api key here

def KtoC(kelvin):
    celcius = kelvin - 273
    farenheit = celcius * (9/5) + 32

    return celcius, farenheit


def main ():

    if API_KEY == "":
        print("Edit the api key global variable in program")
        exit()

    print("Enter a city(spaces allowed)...")
    CITY = input()
    
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()
    tempK = response['main']['temp']
    tempC,tempF = KtoC(tempK)

    feelsLikeTempK = response['main']['feels_like']
    fTempC,fTempF = KtoC(feelsLikeTempK)

    windSpeed = int(response['wind']['speed']) * 2.23694 # meter/sec to miles/hours

    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset  = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    print(f"Temperature in {CITY}: {tempK:.2f}*K , {tempC:.2f}*C or {tempF:.2f}*F") 
    print(f"Temperature in {CITY} feels like: {feelsLikeTempK:.2f}*K , {fTempC:.2f}*C or {fTempF:.2f}*F") 
    print(f"Humidity in {CITY}: {humidity}%") 
    print(f"Wind Speed in {CITY}: {windSpeed:.2f} mph") 
    print(f"Weather Description in {CITY}: {description}")

    print(f"Sunrise in {CITY}: {sunrise} am")
    print(f"Sunset in {CITY}: {sunset} pm")

main()
