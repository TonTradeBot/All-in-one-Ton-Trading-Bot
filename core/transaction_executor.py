import time
import random

class TransactionExecutor:
    """
    Executes buy/sell transactions for Solana (SOL) on the connected exchange.
    """

    def __init__(self, order_manager):
        self.order_manager = order_manager

    def execute_buy(self, amount):
        """
        Simulates a buy order for a specified amount of Solana (SOL).
        """
        transaction_id = self.order_manager.create_order("buy", amount)
        if transaction_id:
            self._simulate_network_latency()
            print(f"Buy order executed successfully! Transaction ID: {transaction_id}")
        else:
            raise Exception("Failed to execute buy order.")

    def execute_sell(self, amount):
        """
        Simulates a sell order for a specified amount of Solana (SOL).
        """
        transaction_id = self.order_manager.create_order("sell", amount)
        if transaction_id:
            self._simulate_network_latency()
            print(f"Sell order executed successfully! Transaction ID: {transaction_id}")
        else:
            raise Exception("Failed to execute sell order.")

    def _simulate_network_latency(self):
        """
        Simulates network latency for added realism.
        """
        time.sleep(random.uniform(0.5, 2.0))  # Latency between 0.5 to 2 seconds

if __name__ == "__main__":
    class MockOrderManager:
        """
        A mock order manager for testing purposes.
        """
        def create_order(self, order_type, amount):
            print(f"Creating a {order_type} order for {amount} SOL...")
            return f"mock_txn_{random.randint(1000, 9999)}"

    # Example usage
    try:
        mock_order_manager = MockOrderManager()
        executor = TransactionExecutor(mock_order_manager)
        
        executor.execute_buy(5)  # Simulate buying 5 SOL
        executor.execute_sell(3)  # Simulate selling 3 SOL
    except Exception as e:
        print(f"Error: {e}")
