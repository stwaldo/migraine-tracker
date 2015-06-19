import json import load
from urllib2 import urlopen, URLError

# pulls local weather information from wunderground.com and returns conditions

def weather(api, zipcode):
    site = 'http://api.wunderground.com/api/' + api + '/conditions/q/'
    url = site + zipcode + '.json'
    try:
        response = urlopen(url)
    except URLError as e:
        return e
    f = response.read()
    data = load(f)
    response.close()
    temp_f = data['current_observation']['temp_f']
    humidity = data['current_observation']['relative_humidity']
    pressure = data['current_observation']['pressure_mb']
    p_url = 'http://www.claritin.com/weatherpollenservice/weatherpollenservice.svc/getforecast/' + zipcode
    try:
        response = urlopen(url)
    except URLError as e:
        return e
    f = response.read()
    data = load(f)
    response.close
    
