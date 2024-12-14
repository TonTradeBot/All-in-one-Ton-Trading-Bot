import os
import datetime
import json

class Helpers:
    """
    Provides utility functions for common operations in the bot.
    """

    @staticmethod
    def create_directory(path):
        """
        Creates a directory if it doesn't already exist.
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Directory created: {path}")
            else:
                print(f"Directory already exists: {path}")
        except Exception as e:
            print(f"Error creating directory: {e}")

    @staticmethod
    def format_timestamp(timestamp=None):
        """
        Formats a timestamp as a human-readable string.
        """
        if not timestamp:
            timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def read_json(file_path):
        """
        Reads a JSON file and returns its content.
        """
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON format: {file_path}")
            return {}

    @staticmethod
    def write_json(file_path, data):
        """
        Writes a dictionary to a JSON file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
                print(f"Data written to {file_path}")
        except Exception as e:
            print(f"Error writing JSON to {file_path}: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        Helpers.create_directory("data/logs")
        print("Current Timestamp:", Helpers.format_timestamp())

        sample_data = {"key": "value", "list": [1, 2, 3]}
        Helpers.write_json("data/sample.json", sample_data)
        read_data = Helpers.read_json("data/sample.json")
        print("Read Data:", read_data)
    except Exception as e:
        print(f"Error: {e}")
