# storage.py
# Create a function save_numbers(numbers, filename="data.json")
# It should save the list of numbers to a JSON file as a dictionary: {"numbers": numbers}
# Use indent=2 for readable formatting
# Overwrite the file if it exists
# Do not print anything in this function
import json


def save_number(numbers, filename="data.json"):
    # write JSON using a fixed encoding for portability
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"numbers": numbers}, f, indent=2)

# Create a function load_numbers(filename="data.json")
# It should load the JSON file and return the list under the "numbers" key
# If the file does not exist, return an empty list
# Do not print anything in this function

def load_numbers(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            nums = data.get("numbers", []) if isinstance(data, dict) else []
            # ensure the stored value is a list of numbers
            if not isinstance(nums, list):
                return []
            if not all(isinstance(x, (int, float)) for x in nums):
                raise ValueError("Loaded 'numbers' contains non-numeric items")
            return nums
    except (FileNotFoundError, json.JSONDecodeError):
        return []