import os
import datetime

class Logger:
    """
    Logs messages and events for the bot's operations.
    """

    LOG_FILE_PATH = "data/trade_logs.txt"

    @staticmethod
    def log(message):
        """
        Logs a message to the console and to a log file with a timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        
        # Print to console
        print(formatted_message)
        
        # Append to log file
        try:
            with open(Logger.LOG_FILE_PATH, "a") as file:
                file.write(formatted_message + "\n")
        except Exception as e:
            print(f"Error writing to log file: {e}")

    @staticmethod
    def log_trade(transaction_id, trade_type, amount, price):
        """
        Logs trade details such as transaction ID, type, amount, and price.
        """
        message = f"Trade Executed - ID: {transaction_id}, Type: {trade_type}, Amount: {amount} SOL, Price: ${price:.2f}"
        Logger.log(message)

if __name__ == "__main__":
    # Example usage
    try:
        Logger.log("Bot initialized.")
        Logger.log_trade("txn_123456", "BUY", 10, 22.50)
        Logger.log_trade("txn_123457", "SELL", 5, 25.30)
    except Exception as e:
        print(f"Error: {e}")
