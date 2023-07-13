# logical operators (and,or,not) - used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if not(temp>=0 and temp<=30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp >30):
    print("The temperature is good today!")
    print("Go outside!")
#  not reverses the outcome of a conditional statement - (if it was true it will be false. if it was false it will
# become true
