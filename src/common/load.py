import os
import json


# Load from a json file
def load(file_name: str):
    try:
        # Define the file path
        data_file_path = os.path.join(
            os.path.dirname(__file__), "..", "data", file_name
        )

        # Check if the file exists
        if not os.path.exists(data_file_path):
            raise FileNotFoundError(f"{file_name} does not exist.")

        # Read the data from the file
        with open(data_file_path, "r") as f:
            data = json.load(f)
        print(f"\nData successfully loaded from {file_name}")
        return data

    except Exception as e:
        print(f"\nAn error occurred while loading {file_name} data: {e}")
        return None
