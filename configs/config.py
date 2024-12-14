import json

CONFIG_FILE_PATH = "configs/config.json"

def load_config():
    """
    Loads the configuration file for the bot.
    """
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        raise Exception(f"Configuration file not found at {CONFIG_FILE_PATH}. Please ensure the file exists.")
    except json.JSONDecodeError:
        raise Exception("Configuration file is not in a valid JSON format.")

def save_config(new_config):
    """
    Saves new configuration settings to the config file.
    """
    try:
        with open(CONFIG_FILE_PATH, "w") as file:
            json.dump(new_config, file, indent=4)
    except Exception as e:
        raise Exception(f"Error saving configuration file: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        config = load_config()
        print("Loaded config:", config)
    except Exception as e:
        print(f"Error: {e}")
