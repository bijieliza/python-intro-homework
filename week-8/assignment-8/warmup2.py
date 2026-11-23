def getnumbers(numerator,denominator):

    try:
        result = numerator / denominator
        print(numerator, "÷", denominator, "=", result)
    except ZeroDivisionError:
        print("Can't divide by zero — please try a non-zero denominator.")
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
getnumbers(numerator,denominator)