import sys
import requests

if len(sys.argv) != 2 :
    sys.exit("Missing command-line argument")
else :
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    response = (requests
            .get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            .json()
            )
    money = float(response["bitcoin"]["usd"])
except requests.RequestException:
    sys.exit()



print(f"${money*n:,.4f}")