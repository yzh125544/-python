import sys
import requests

def main():
    """
    Calculates the current cost of a specified number of Bitcoins.
    """
    # 1. Get the number of Bitcoins from the command-line argument.
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")

        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 2. Query the CoinCap API for the current Bitcoin price.
    try:
        # NOTE: Replace 'YOUR_API_KEY_HERE' with your actual CoinCap API key.
        api_key = "YOUR_API_KEY_HERE"
        if api_key == "YOUR_API_KEY_HERE":
             print("Warning: Please replace 'YOUR_API_KEY_HERE' with your actual CoinCap API key.", file=sys.stderr)

        url = f"https://api.coincap.io/v2/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)

        data = response.json()

        # Extract the price from the JSON response
        bitcoin_price_usd_str = data['data']['priceUsd']
        bitcoin_price_usd = float(bitcoin_price_usd_str)

    except requests.RequestException:
        sys.exit("Error fetching data from the API. Check your network connection or API endpoint.")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing the API response.")

    # 3. Calculate the total cost.
    total_cost = num_bitcoins * bitcoin_price_usd

    # 4. Output the result formatted to four decimal places with a thousands separator.
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
