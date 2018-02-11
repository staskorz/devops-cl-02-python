import requests


GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?address='
DARKSKY_API_URL = 'https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/'


def getJson(url):
    result = requests.get(url)
    statusCode = result.status_code
    if statusCode < 200 or statusCode > 299:
        raise requests.RequestException(f'GET Error: {statusCode}')
    return result.json()


address = input('Type address: ')


locationDataJson = getJson(f'{GOOGLE_MAPS_API_URL}{address}')

locationResults = locationDataJson['results']

if len(locationResults) == 0:
    raise RuntimeError('No results')

coordinates = locationResults[0]['geometry']['location']


weatherDataJson = getJson(f'{DARKSKY_API_URL}{coordinates["lat"]},{coordinates["lng"]}')
currentWeather = weatherDataJson['currently']
temperature = currentWeather['temperature']
humidity = currentWeather['humidity']

print(f'Temperature (f): {temperature}')
print(f'Humidity (%): {humidity * 100}')
