import os
import requests
import geocoder

# both apidata.mos.ru API key and GOOGLE_API_KEY
# should be accessible in current environment
MOS_API_KEY = os.environ['MOS_API_KEY']

src_dic = {
    '60788': 'Wi-Fi в библиотеках',
    '60789': 'Wi-Fi в кинотеатрах',
    '60790': 'Wi-Fi в культурных центрах',
    '861':   'Wi-Fi в парках'
}


def get_long(wifi_point):
    return wifi_point['geometry']['coordinates'][0]


def get_lat(wifi_point):
    return wifi_point['geometry']['coordinates'][1]


api_url_tpl = 'https://apidata.mos.ru/v1/mapfeatures/{dataset_id}?api_key={api_key}'

wifi_points_list = []
for wifi_source in src_dic.keys():
    api_url = api_url_tpl.format(dataset_id=wifi_source, api_key=mos_api_key)
    data = requests.get(api_url).json()
    wifi_points_list_new = data['features']
    wifi_points_list.extend(wifi_points_list_new)

street_list = [geocoder.google([get_lat(wifi_point), get_long(wifi_point)], method='reverse').street
               for wifi_point in wifi_points_list]

counted_wifi_by_street = sorted([(x, street_list.count(x)) for x in set(street_list) if x is not None
                                 and x != 'Unnamed Road'], key=lambda i: -i[1])

for w in counted_wifi_by_street[0:5]:
    result = '{num} WiFi APs on the {street}'.format(num=w[1], street=w[0])
    print(result)

# Geocoding API Policies
# https://developers.google.com/maps/documentation/geocoding/policies
print(' ')
print('-----------------')
print('powered by Google')
