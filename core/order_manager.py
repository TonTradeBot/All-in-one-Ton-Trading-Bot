import random
import time

class OrderManager:
    """
    Manages the creation, tracking, and cancellation of buy/sell orders.
    """

    def __init__(self, api_connector):
        self.api_connector = api_connector
        self.active_orders = {}

    def create_order(self, order_type, amount):
        """
        Creates a new buy/sell order and returns a transaction ID.
        """
        if order_type not in ["buy", "sell"]:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")

        transaction_id = self._generate_transaction_id()
        timestamp = time.time()
        self.active_orders[transaction_id] = {
            "type": order_type,
            "amount": amount,
            "timestamp": timestamp,
            "status": "pending"
        }

        print(f"Order created: {order_type.upper()} {amount} SOL (Transaction ID: {transaction_id})")
        return transaction_id

    def cancel_order(self, transaction_id):
        """
        Cancels an active order by its transaction ID.
        """
        if transaction_id in self.active_orders:
            self.active_orders[transaction_id]["status"] = "canceled"
            print(f"Order {transaction_id} has been canceled.")
        else:
            print(f"No active order found with Transaction ID: {transaction_id}")

    def get_order_status(self, transaction_id):
        """
        Returns the status of a specific order.
        """
        order = self.active_orders.get(transaction_id)
        if order:
            return order["status"]
        else:
            return "Order not found."

    def _generate_transaction_id(self):
        """
        Generates a random transaction ID.
        """
        return f"txn_{random.randint(100000, 999999)}"

if __name__ == "__main__":
    # Example usage
    try:
        from core.api_connector import APIConnector

        api_connector = APIConnector("dummy_api_key", "dummy_secret_key")
        order_manager = OrderManager(api_connector)

        # Create and manage orders
        txn_id = order_manager.create_order("buy", 10)
        time.sleep(1)
        print(f"Order Status: {order_manager.get_order_status(txn_id)}")
        order_manager.cancel_order(txn_id)
        print(f"Order Status After Cancellation: {order_manager.get_order_status(txn_id)}")
    except Exception as e:
        print(f"Error: {e}")

