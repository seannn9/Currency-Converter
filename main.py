import requests

url = 'http://data.fixer.io/api/latest?access_key=aa29df5a1c0921db9f56b133f27476dc'

def main_func():
    response = requests.get(url)
    from_curr = input("From: ")
    to_curr = input("To: ")
    amount = int(input("Amount: "))
    rate = response.json()['rates'][from_curr]
    amount = amount/rate
    amount = amount * response.json()['rates'][to_curr]
    print(round(amount,2))
    again = input("Convert again? y/n: ").lower()
    if again == 'y':
        main_func()

if __name__ == '__main__':
    main_func()