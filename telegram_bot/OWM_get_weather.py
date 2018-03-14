import requests
import misc
from pprint import pprint


def get_weather(city_name='Tokii'):
    url = r'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name,'units': 'metric', 'appid': misc.OWM_token}
    response = requests.get(url, params=params).json()
    if response['cod'] == 200:
        res = 'City: {}\nTemp: {}\nWeather: {}'.format(response['name'], response['main']['temp'], response['weather'][0]['description'])
    else:
        res = response['message']
    return res

    #price = response['ticker']['last']
    # return str(price) + ' usd' 


def main():
    print(get_weather())


if __name__ == '__main__':
    main()