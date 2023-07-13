#  nested loop = having one loop inside of another - an inner loop finishes all of its stuff before the outer loop
#   makes one iteration


rows = int(input("How many rows would you like?: "))
columns = int(input("How many columns would you like?: "))
symbol = input("What symbol would you like to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print(symbol)