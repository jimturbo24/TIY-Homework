apiKey = 'e7e45d431a67a77ffb8f40994fa4668f'

import requests


# testUrl = 'http://api.openweathermap.org/data/2.5/weather?id=4726206&APPID=' + apiKey
# resp = requests.get(testUrl)
# if resp.status_code in [200, 201]:
#     weatherData = resp.json()
#     print("The weather in {} is {}.".format(weatherData['name'],
#                                             weatherData['weather'][0]['description']))
# else:
#     print("ERROR: " + str(resp.status_code))



# testUrl = 'http://api.openweathermap.org/data/2.5/weather?id=2643741&APPID=' + apiKey
# resp = requests.get(testUrl)
# if resp.status_code in [200, 201]:
#     weatherData = resp.json()
#     print("The weather in {} is {}.".format(weatherData['name'],
#                                             weatherData['weather'][0]['description']))
# else:
#     print("ERROR: " + str(resp.status_code))


testUrl = 'http://api.openweathermap.org/data/2.5/forecast?id=2643741&APPID=' + apiKey
resp = requests.get(testUrl)
if resp.status_code in [200, 201]:
    forcastData = resp.json()
    print("The weather in {} is {}.".format(forcastData['name'],
                                            forcastData['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))

forcastData = resp.json()
