import requests

url = 'http://api.currencylayer.com/live?access_key=daa1d79c5619ce03799702b95a6beb8e'

def convert():
    response = requests.get(url)
    print(response.json())
    from_curr = input("From: ")
    to_curr = input("To: ")
    amount = int(input("Amount: "))
    rate = response.json()['quotes'][from_curr]
    print(rate)

convert()