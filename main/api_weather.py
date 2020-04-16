import requests

def make_request_lat_long(lat, long):
    # returns the json file for current weather using lat and long
    api_url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + \
              "&lon=" + long + "&appid=f83336df5edd981133fe2ac091157719&units=metric"
    r = requests.get(api_url).json()
    return r

def make_request_name(city_name):
    # returns the json file for current weather using city name
    api_url = 'http://openweathermap.org/data/2.5/weather?q=' + city_name + \
              '&appid=b6907d289e10d714a6e88b30761fae22'
    r = requests.get(api_url).json()
    return r

def make_request_hourly_city_id(city_id):
    api_url = 'http://openweathermap.org/data/2.5/forecast/hourly?id=' + str(city_id) +\
              '&appid=b6907d289e10d714a6e88b30761fae22'
    r = requests.get(api_url).json()
    r_list_24_hours = r['list'][:8]
    return r_list_24_hours

def make_request_query_set(query_set):
    hometown = ''
    list_city_details = []
    for i in query_set:
        api_url = 'http://openweathermap.org/data/2.5/weather?q=' + i.cities + \
                    '&appid=b6907d289e10d714a6e88b30761fae22'
        r = requests.get(api_url).json()
        if i.hometown == True:
            hometown = {'id' : i.id, 'set' : r}
            print('-------',hometown,'-------')
        else:
            list_city_details.append({'id' : i.id, 'set' : r})
    return hometown, list_city_details

def detect_location():
    current_location_lat_long_list = []
    text = ''
    current_location_details = requests.get('https://ipinfo.io/').json()
    current_location_lat_long = current_location_details['loc']
    for i in (current_location_lat_long + ','):
        if i != ',':
            text = text + i
        elif i == ',':
            current_location_lat_long_list.append(text)
            text = ''
    return current_location_lat_long_list

if __name__ == '__main__':
    pass

