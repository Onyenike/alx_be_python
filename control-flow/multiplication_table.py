number = int(input("Enter a number to see its multiplication table: "))

for X in range(1, 11):
        print(f"{number} * {X} = {number * X}", end = "\n")