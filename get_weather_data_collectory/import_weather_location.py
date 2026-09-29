import json
import requests
city = input("enter the city please:  ")
with open("weather_location.json","r") as file:
    content = json.load(file)
    for i in content:
        if i["name"] == city:
                city = i["name"]
                latitude = i["latitude"]
                longitude = i ["longitude"]
            
    
params ={ 
         "latitude":latitude,
         "longitude" : longitude,
         "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
         }
    
try:
    respond = requests.get("https://api.open-meteo.com/v1/forecast",
                       timeout=1000,
                       params=params)

    print(respond.status_code)
except requests.exceptions.RequestException as e:
    print(f" you have an error the error is {e}")


data = respond.json()
print(data)



temperature =  data["current"]["temperature_2m"]
relative_humidity = data["current"]["relative_humidity_2m"]
wind_speed = data ["current"]["wind_speed_10m"]

all_data = {"name" : city,
            "temperature": temperature , 
            "relative_humidity":  relative_humidity , "wind_speed": wind_speed }


print(f" the name is {city},the temperature is : {temperature} , and the relative_humidity is : { relative_humidity}  , and the wind_speed is : {wind_speed}")



with open("weather_data.json" , "a",encoding="utf_8") as file:
    json.dump(all_data,file,indent=4)
    
    
    
    
