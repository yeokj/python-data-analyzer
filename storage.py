# storage.py
# Create a function save_numbers(numbers, filename="data.json")
# It should save the list of numbers to a JSON file as a dictionary: {"numbers": numbers}
# Use indent=2 for readable formatting
# Overwrite the file if it exists
# Do not print anything in this function
import json

def save_number(numbers, filename="data.json"):
    with open(filename, "w") as f:
        json.dump({"numbers" : numbers}, f, indent=2)
