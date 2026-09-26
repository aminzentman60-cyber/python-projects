import requests
import json
try:
    respond = requests.get("https://jsonplaceholder.typicode.com/users" ,
                           timeout = 7)
    print(respond.status_code)
    respond.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f" you got an error : {e}")
    
data = respond.json()
print(data)

with open("users.json" , "w") as file:
    json.dump(data,file)
    



