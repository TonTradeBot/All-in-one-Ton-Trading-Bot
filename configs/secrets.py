import os

class Secrets:
    """
    """

    @staticmethod
    def ConncectPhantom():
        """
        """
        api_key = os.getenv("SOLANA_API_KEY")
        if not api_key:
            raise Exception("Phantom Wallet not found.")
        return api_key


if __name__ == "__main__":
    try:
        print("API :", Secrets.ConncectPhantom())
    except Exception as e:
        print(f"Error: {e}")
