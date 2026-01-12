from storage import save_number, load_numbers, save_report
from analyzer import analyze_numbers, print_report

def collect_numbers():
    # Ask the user how many numbers to enter
    # Loop to collect inputs
    # Validate each input is a number
    # Store numbers in a list
    # Print the list
    numbers = []

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
                numbers.append(num)
                break
            except ValueError:
                print("Not an integer — try again.")

    print()
    print(numbers)

    return numbers
   

def main():
    numbers = []
    last_results = None
    while True:
        print("\nMenu:")
        print("1) Collect numbers")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Analyze numbers")
        print("5) Save analysis to report.txt file")
        print("6) Exit the program")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option, try again.")
            continue

        if user_choice == 1:
            # call the collector to get a list of numbers
            numbers = collect_numbers()
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
            # Analyze numbers and print a report
            if not numbers:
                print("No numbers available. Please collect or load numbers first.")
                continue
            try:
                results = analyze_numbers(numbers)
                if results is None:
                    print("No numbers to analyze.")
                    continue
                last_results = results
                print_report(numbers, results)
            except Exception as e:
                print(f"Failed to analyze numbers: {e}")
        elif user_choice == 5:
            # Save the last analysis to report.txt
            if not numbers:
                print("No numbers available to save. Collect or load numbers first.")
                continue
            if not last_results:
                print("No analysis available. Run option 4 to analyze numbers first.")
                continue
            try:
                save_report(numbers, last_results, filename="report.txt")
                print("Analysis report saved to report.txt")
            except Exception as e:
                print(f"Failed to save analysis report: {e}")
        elif user_choice == 6:
            print("Exiting program... Goodbye")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()