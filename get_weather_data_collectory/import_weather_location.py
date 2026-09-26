import json
import requests
with open("weather_location.json","r") as file:
    content = json.load(file)
    latitude = content["latitude"]
    longitude = content ["longitude"]
params ={"latitude":latitude,
         "longitude" : longitude,
         "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
         }
    
try:
    respond = requests.get("https://api.open-meteo.com/v1/forecast",
                       timeout=5,
                       params=params)

    print(respond.status_code)
except requests.exceptions.RequestException as e:
    print(f" you have an error the error is {e}")


data = respond.json()



temperature =  data["current"]["temperature_2m"]
relative_humidity = data["current"]["relative_humidity_2m"]
wind_speed = data ["current"]["wind_speed_10m"]

all_data = temperature,relative_humidity,wind_speed


print(f"the temperature is : {temperature}, and the relative_humidity is : { relative_humidity} , and the wind_speed is : {wind_speed}")



with open("weather_data.json" , "w",encoding="utf_8") as file:
    json.dump(all_data,file,indent=4)