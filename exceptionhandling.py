# exception - an event detected during execution that interrupts the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero!")
except ValueError as e:
    print(e)
    print("You must enter a number!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:
    print("This will always execute ;)")