import os
import time
import requests
import hmac
import hashlib
from typing import Dict, Any

class TonSwapClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.tonswap.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from TonSwap: {resp.text}")

    def buy_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "buy"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}

    def sell_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "sell"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}


class StonfiClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.stonfi.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Stonfi: {resp.text}")

    def buy_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "buy"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}

    def sell_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "sell"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}


class DeDustClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.dedust.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from DeDust: {resp.text}")

    def buy_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "buy"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}

    def sell_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "sell"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}


class MegatonClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.megaton.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Megaton: {resp.text}")

    def buy_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "buy"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}

    def sell_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "sell"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}


class TegroClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.tegro.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Tegro: {resp.text}")

    def buy_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "buy"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}

    def sell_token(self, base: str, quote: str, amount: float) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/order"
        payload = {
            "base": base,
            "quote": quote,
            "amount": amount,
            "side": "sell"
        }
        headers = self._sign_request(payload)
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=5)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": "error", "detail": resp.text}


def main_loop():
    # API credentials should be properly secured and not hardcoded.
    # Here they are referenced from environment variables as placeholders.
    tonswap = TonSwapClient(api_key=os.getenv("TONSWAP_API_KEY", "YOUR_TONSWAP_API_KEY"),
                            secret_key=os.getenv("TONSWAP_SECRET_KEY", "YOUR_TONSWAP_SECRET"))
    stonfi = StonfiClient(api_key=os.getenv("STONFI_API_KEY", "YOUR_STONFI_API_KEY"),
                          secret_key=os.getenv("STONFI_SECRET_KEY", "YOUR_STONFI_SECRET"))
    dedust = DeDustClient(api_key=os.getenv("DEDUST_API_KEY", "YOUR_DEDUST_API_KEY"),
                          secret_key=os.getenv("DEDUST_SECRET_KEY", "YOUR_DEDUST_SECRET"))
    megaton = MegatonClient(api_key=os.getenv("MEGATON_API_KEY", "YOUR_MEGATON_API_KEY"),
                            secret_key=os.getenv("MEGATON_SECRET_KEY", "YOUR_MEGATON_SECRET"))
    tegro = TegroClient(api_key=os.getenv("TEGRO_API_KEY", "YOUR_TEGRO_API_KEY"),
                        secret_key=os.getenv("TEGRO_SECRET_KEY", "YOUR_TEGRO_SECRET"))

    base = "TON"
    quote = "USDT"
    amount = 10.0

    while True:
        try:
            prices = [
                ("TonSwap", tonswap, tonswap.get_price(base, quote)),
                ("Stonfi", stonfi, stonfi.get_price(base, quote)),
                ("DeDust", dedust, dedust.get_price(base, quote)),
                ("Megaton", megaton, megaton.get_price(base, quote)),
                ("Tegro", tegro, tegro.get_price(base, quote))
            ]

            cheapest = min(prices, key=lambda x: x[2])
            priciest = max(prices, key=lambda x: x[2])

            profit_threshold = 0.05
            if priciest[2] - cheapest[2] > profit_threshold:
                buy_res = cheapest[1].buy_token(base, quote, amount)
                if buy_res.get("status") == "success":
                    sell_res = priciest[1].sell_token(base, quote, amount)
                    if sell_res.get("status") == "success":
                        print("Arbitrage trade executed successfully.")
                    else:
                        print(f"Sell order failed: {sell_res}")
                else:
                    print(f"Buy order failed: {buy_res}")
            else:
                print("No profitable opportunity detected.")

            time.sleep(10)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main_loop()
