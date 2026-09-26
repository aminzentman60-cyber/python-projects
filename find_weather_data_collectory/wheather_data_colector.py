import requests
import json
city = input("enter the city please : ")
url = "https://geocoding-api.open-meteo.com/v1/search"
p = {
    "name" : city ,
    "count": 1,
    "language": "en",
    "format": "json"
}
try:
    respond = requests.get(url , 
                           params=p,
                           timeout = 1000)
    print(respond.status_code)
    
    respond.raise_for_status()

except requests.exceptions.RequestException as error:
    print(f"you have an error the error is {error}")
    
data = respond.json()
print(data)



name = data["results"][0]["name"]
latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

location_data = {"name" : name,
                 "latitude":latitude,
                 "longitude":longitude}

print(location_data)


with open("weather_location.json" , "a") as file:
    json.dump(location_data,file)
    
    

        
    
    
    
    
    
