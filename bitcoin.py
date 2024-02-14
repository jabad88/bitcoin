import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = r.json()

print("Welcome to the Bitcoin Tracker", "\n")

def main():
    number_of_coins = float(input("How many bitcoin would you like to calculate? "))
    currency = input("What form of currency do you need? (USD/GBP/EUR) ").upper()
    
    symbol = get_currency(currency)
    bitcoin = rate(number_of_coins,symbol)
    
    print("\n")
    print(f"{symbol}{bitcoin:.2f}")


def get_currency(currency):
    if currency == "USD":
        return "$"
    elif currency == "GBP":
        return "£"
    elif currency == "EUR":
        return "€"
    
def rate(number_of_coins,symbol):
    if symbol == "$":
        rate = (o["bpi"]["USD"]["rate_float"]) * number_of_coins
        return rate
    elif symbol == "£":
        rate = (o["bpi"]["GBP"]["rate_float"]) * number_of_coins
        return rate
    elif symbol == "€":
        rate = (o["bpi"]["EUR"]["rate_float"]) * number_of_coins
        return rate


if __name__ == "__main__":
    main()