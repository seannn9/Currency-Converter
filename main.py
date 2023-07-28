import requests

url = 'http://api.currencylayer.com/live?access_key=daa1d79c5619ce03799702b95a6beb8e'

def convert():
    response = requests.get(url)
    rate = response.json()
    print(rate)

convert()