def analyze_numbers(numbers):
    if len(numbers) == 0:
        return None
    
    count = len(numbers)
    low_value = min(numbers)
    high_value = max(numbers)
    total = sum(numbers)
    average = total / count
    
    analysis = {
        "count": count,
        "minimum": low_value,
        "maximum": high_value,
        "sum": total,
        "average": average
    }

    return analysis

def main():
    entries = []
    n = int(input("Enter how many entries would you like to make? "))

    for _ in range(n):
        num = int(input("Enter a number: "))
        entries.append(num)

    print()
    print(entries)

    print("\nStatistics")
    
    report = analyze_numbers(entries)
    if report:
        print("count:", report.get("count"))
        print("Minimum:", report.get("minimum"))
        print("Maximum:", report.get("maximum"))
        print("Sum:", report.get("sum"))
        print("Average:", report.get("average"))

# def tba():
#     print("Python program running...")

#     print("\nMenu:")
#     print("1) Collect and analyze numbers")
#     print("2) Exit the program")

#     user_choice = int(input("Enter your choice: "))

#     match user_choice:
#         case 1:
#             collect_numbers()
#         case 2:
#             print("Exiting program... Goodbye")
#         case _:
#             print("Invalid option, try again.")

if __name__ == "__main__":
    main()