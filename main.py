from datetime import datetime
from storage import save_number, load_numbers

# Define analyze_numbers(numbers)
def analyze_numbers(numbers):
    if not numbers:
        return None
    
    count = len(numbers)
    low_value = min(numbers)
    high_value = max(numbers)
    total = sum(numbers)
    average = round(total / count, 2)
    
    analysis = {
        "count": count,
        "minimum": low_value,
        "maximum": high_value,
        "sum": total,
        "average": average
    }

    # Return count, min, max, sum, average in a dictionary
    return analysis

def collect_and_analyze():
    # Ask the user how many numbers to enter
    # Loop to collect inputs
    # Validate each input is a number
    # Store numbers in a list
    # Print the list
    entries = []

    # Validate number of entries (n)
    while True:
        s = input("Enter how many entries would you like to make: ").strip()
        try:
            n = int(s)
            if n <= 0:
                print("Please enter an integer greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Collect exactly n integer entries, re-prompt on invalid input
    for _ in range(n):
        while True:
            s = input("Enter an integer: ").strip()
            try:
                num = int(s)
                entries.append(num)
                break
            except ValueError:
                print("Not an integer — try again.")

    print()
    print(entries)

    print("\nStatistics")

    report = analyze_numbers(entries)
    if report:
        print("Count:", report.get("count"))
        print("Minimum:", report.get("minimum"))
        print("Maximum:", report.get("maximum"))
        print("Sum:", report.get("sum"))
        print("Average:", report.get("average"))
        # Save the analysis report to a file named report.txt
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            with open("report.txt", "w") as f:
                f.write(f"Analysis Report - {timestamp}\n")
                f.write("Numbers Entered:\n")
                for entry in entries:
                    f.write(f"{entry}\n")
                f.write("\nStatistics\n")
                f.write(f"Count: {report.get('count')}\n")
                f.write(f"Minimum: {report.get('minimum')}\n")
                f.write(f"Maximum: {report.get('maximum')}\n")
                f.write(f"Sum: {report.get('sum')}\n")
                f.write(f"Average: {report.get('average')}\n")
            print("\nAnalysis report saved to report.txt")
        except OSError as e:
            print(f"Failed to write report.txt: {e}")
        return entries
    else:
        print("No numbers to analyze.")
        return None

def main():
    # Show menu options
    # 1) Enter numbers and analyze
    # 2) Exit the program
    # Ask user for menu choice
    # If choice is 1:
    # collect numbers
    # analyze numbers
    # print formatted report
    # If choice is 2:
    # break out of the loop
    numbers = []
    while True:
        print("\nMenu:")
        print("1) Collect and analyze numbers")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Exit the program")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option, try again.")
            continue

        if user_choice == 1:
            # call the collector to get a list of numbers
            numbers = collect_and_analyze()
            # continue to menu so the user can choose to save or exit
        elif user_choice == 2:
            # Prevent saving when there are no collected numbers or when numbers
            # is in an unexpected state.
            if not numbers:
                print("No numbers available. Please collect numbers first (option 1).")
                continue
            try:
                save_number(numbers)
                print("Numbers saved to data.json")
            except (TypeError, OSError) as e:
                print(f"Failed to save numbers: {e}")
        elif user_choice == 3:
            # Load numbers from disk regardless of current in-memory state
            try:
                loaded = load_numbers()
                if not loaded:
                    print("No numbers found in data.json")
                    continue
                numbers = loaded
                print("Numbers loaded from data.json")
            except Exception as e:
                # catch ValueError from invalid content and other I/O issues
                print(f"Failed to load numbers: {e}")
        elif user_choice == 4:
            print("Exiting program... Goodbye")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()