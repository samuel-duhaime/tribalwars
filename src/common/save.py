import os
import json


# Save to a json file
def save(data, file_name: str):
    try:
        # Ensure the directory exists
        os.makedirs("../../data", exist_ok=True)

        # Define the file path
        data_file_path = os.path.join(
            os.path.dirname(__file__), "..", "data", file_name
        )

        # Write the data to the file
        with open(data_file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nData successfully saved to {file_name}")

    except Exception as e:
        print(f"\nAn error occurred while saving {file_name} data: {e}")
