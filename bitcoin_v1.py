import requests
import json
import sys

try:
    n = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    rate = (o["bpi"]["USD"]["rate_float"])
    amount = n * rate
    print (f"${amount:,.4f}")


except (requests.RequestException, IndexError, ValueError):
    if sys.argv[1:] == []:
        sys.exit("Missing command-line argument")
    elif sys.argv[1:] != float:
        sys.exit("Command-line argument is not a number")
