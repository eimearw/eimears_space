import requests
api_key = "dd9cd8720e580964029f385138b11193"
city = "Belfast"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"
requests = requests.get(url)
json = requests.json()
description = json.get("weather") [0].get("description")
print("Today's forecast in Belfast is", description)
temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")
print("The temperature today is a low of", temp_min, "Degrees Celsius ", "with a high of ", temp_max, "Degrees Celsius")