import requests
import datetime as dt 

BASE_URL = "http://api.openweathermap.org/data/2.5/"
API_KEY =  "" # Add api key here

def KtoC(kelvin):
    celcius = kelvin - 273
    farenheit = celcius * (9/5) + 32

    return celcius, farenheit


def currentWeather(city):

        
    url = BASE_URL + "weather?"+ "appid=" + API_KEY + "&q=" + city

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

    print(f"Temperature in {city}: {tempK:.2f}*K , {tempC:.2f}*C or {tempF:.2f}*F") 
    print(f"Temperature in {city} feels like: {feelsLikeTempK:.2f}*K , {fTempC:.2f}*C or {fTempF:.2f}*F") 
    print(f"Humidity in {city}: {humidity}%") 
    print(f"Wind Speed in {city}: {windSpeed:.2f} mph") 
    print(f"Weather Description in {city}: {description}")

    print(f"Sunrise in {city}: {sunrise}")
    print(f"Sunset in {city}: {sunset}")

def forcast(city):

    url = BASE_URL + "forecast?"+ "appid=" + API_KEY + "&q=" + city 

    response = requests.get(url).json()

    for predicts in response['list']:
    
        time = predicts['dt_txt']
        tempK = predicts['main']['temp']
        tempC,tempF = KtoC(tempK)

        windSpeed = int(predicts['wind']['speed']) * 2.23694 # meter/sec to miles/hours

        humidity = predicts['main']['humidity']
        description = predicts['weather'][0]['description']
        
        print(f"Time in {city}: {time}")
        print(f"Weather Description in {city}: {description}")
        print(f"Temperature in {city}: {tempK:.2f}*K , {tempC:.2f}*C or {tempF:.2f}*F") 
        print(f"Humidity in {city}: {humidity}%") 
        print(f"Wind Speed in {city}: {windSpeed:.2f} mph", 2*"\n") 



            







def main():

    if API_KEY == "":
        print("Edit the api key global variable in program")
        exit()

    print("Enter a city(spaces allowed)...")
    city = input()
    
    print("Current Weather(C) or 5 Day Forecast(F)")
    
    fork = input().lower()
    if fork == "c":
        currentWeather(city)
    elif fork == "f":
        forcast(city)

main()
