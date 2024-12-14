import requests

class PriceFetcher:
    """
    Fetches the latest Solana price data from an external API.
    """

    def __init__(self, api_connector):
        self.api_connector = api_connector
        self.price_api_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_solana_price(self):
        """
        Retrieves the current price of Solana (SOL) in USD.
        """
        params = {
            "ids": "solana",
            "vs_currencies": "usd"
        }
        try:
            response = requests.get(self.price_api_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return data["solana"]["usd"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching Solana price: {e}")

    def get_historical_prices(self, days=7):
        """
        Retrieves historical price data for Solana over a given number of days.
        """
        historical_api_url = "https://api.coingecko.com/api/v3/coins/solana/market_chart"
        params = {
            "vs_currency": "usd",
            "days": days,
            "interval": "daily"
        }
        try:
            response = requests.get(historical_api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("prices", [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching historical prices: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        fetcher = PriceFetcher(None)  # Pass None because we are not using api_connector here
        current_price = fetcher.get_solana_price()
        print(f"Current Solana Price: ${current_price}")
        historical_prices = fetcher.get_historical_prices()
        print(f"Historical Prices: {historical_prices[:5]}")  # Print the first 5 entries
    except Exception as e:
        print(f"Error: {e}")
