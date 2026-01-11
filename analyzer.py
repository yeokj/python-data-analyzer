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

def print_report(numbers, results):
    print("\nAnalysis Report")
    print("------------------")
    
    print("Numbers Entered:")
    for num in numbers:
        print(num, end=" ")

    print()
    print("\nStatistics")
    
    print("Count:", results.get("count"))
    print("Minimum:", results.get("minimum"))
    print("Maximum:", results.get("maximum"))
    print("Sum:", results.get("sum"))
    print("Average:", results.get("average"))