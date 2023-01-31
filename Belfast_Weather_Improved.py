import requests


def get_weather_desc_and_temp():
    api_key = "dd9cd8720e580964029f385138b11193"
    city = "Belfast"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description,
            "temp_min": temp_min,
            "temp_max": temp_max}


weather_dict = get_weather_desc_and_temp()

print("Today's forecast in Belfast is", weather_dict.get("description"))
print("Lowest temp", weather_dict.get("temp_min"), "C", "highest temp ", weather_dict.get("temp_max"), "C")
