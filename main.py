def main():
    entries = []
    n = int(input("Enter how many entries would you like to make? "))

    i = 0
    while i < n:
        num = int(input("Enter a number: "))
        entries.append(num)
        i += 1

    print(entries)

if __name__ == "__main__":
    main()