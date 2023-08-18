import requests
s1 = input("Enter the place\n")
key="03574280618349c5b02203004231808"
aqi="yes"
url =f"https://api.weatherapi.com/v1/current.json?key={key}&q={s1}&aqi={aqi}"
response = requests.get(url)
data = response.json()

if 'error' in data:
    print("Error:", data['error']['message'])
else:
    location = data['location']['name']
    temperature_c = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Weather in {location}:")
    print(f"Temperature: {temperature_c}°C")
    print(f"Condition: {condition}")

