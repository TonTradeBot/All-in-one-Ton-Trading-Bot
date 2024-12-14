import requests

class APIConnector:
    """
    Handles communication with the Solana API.
    """

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = "https://api.solana.com"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def send_request(self, endpoint, payload):
        """
        Sends a POST request to the Solana API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error in API request: {e}")

    def get_account_balance(self, wallet_address):
        """
        Retrieves the balance of a given Solana wallet address.
        """
        payload = {
            "method": "getBalance",
            "params": [wallet_address],
            "jsonrpc": "2.0",
            "id": 1
        }
        response = self.send_request("v1/account", payload)
        return response.get("result", {}).get("value", 0)

if __name__ == "__main__":
    # Example usage
    try:
        balance=0
        print(f"Wallet Balance: {balance} SOL")
    except Exception as e:
        print(f"Error: {e}")
