import requests


def kelvin_to_far(tempKelv):
    return round(((tempKelv - 273.15)*1.8 + 32))

# 1.
apiKey = 'e7e45d431a67a77ffb8f40994fa4668f'

testUrl = 'http://api.openweathermap.org/data/2.5/weather?id=4726206&APPID=' + apiKey
resp = requests.get(testUrl)
if resp.status_code in [200, 201]:
    weatherData = resp.json()
    print("It is {0} in {1} and {2}.".format(kelvin_to_far(weatherData['main']['temp']),
                                             weatherData['name'],
                                             weatherData['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))

# 2.
testUrl = 'http://api.openweathermap.org/data/2.5/forecast?id=2643741&APPID=' + apiKey
resp = requests.get(testUrl)
forcastData = resp.json()
forcastList = forcastData['list']
timeList = ['06:00', '12:00', '15:00', '21:00']
for item in forcastList:
    for t in timeList:
        if t in item['dt_txt'] and t == '06:00':
            print('London temperatures for {0}'.format(item['dt_txt'][0:10]))
            print('{0} and {1} at {2} hours.'.format(kelvin_to_far(item['main']['temp_max']),
                                                     item['weather'][0]['main'], t))
        elif t in item['dt_txt']:
            print('{0} and {1} at {2} hours.'.format(kelvin_to_far(item['main']['temp_max']),
                                                     item['weather'][0]['main'], t))

# Output
# It is 64 in San Antonio and clear sky.
# London temperatures for 2016-05-05
# 48 and Clear at 06:00 hours.
# 69 and Clear at 12:00 hours.
# 69 and Clouds at 15:00 hours.
# 60 and Clouds at 21:00 hours.
# London temperatures for 2016-05-06
# 53 and Clear at 06:00 hours.
# 70 and Clouds at 12:00 hours.
# 74 and Clouds at 15:00 hours.
# 62 and Clouds at 21:00 hours.
# London temperatures for 2016-05-07
# 58 and Clouds at 06:00 hours.
# 70 and Clouds at 12:00 hours.
# 70 and Clouds at 15:00 hours.
# 64 and Clouds at 21:00 hours.
# London temperatures for 2016-05-08
# 57 and Clouds at 06:00 hours.
# 70 and Clouds at 12:00 hours.
# 71 and Clouds at 15:00 hours.
# 64 and Clouds at 21:00 hours.
# London temperatures for 2016-05-09
# 59 and Clouds at 06:00 hours.
# 69 and Rain at 12:00 hours.
# 70 and Rain at 15:00 hours.
# 62 and Rain at 21:00 hours.
