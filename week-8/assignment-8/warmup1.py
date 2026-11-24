def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")

number = get_number()
print("You entered:", number)