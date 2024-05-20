from config import geo_url
import requests

def geo_location():
    response = requests.get(geo_url)
    return response.json('[]')

if __name__ == '__main__':
    print(geo_location())