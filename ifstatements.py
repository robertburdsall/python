#  if statement = a block of code that executes only if it's condition is true

age = int(input("How old are you?"))

if age == 100:
    print("You are a century old!")
elif age < 0:
    print("You haven't been born yet!")
elif age >=18:
    print("You are an adult!")
else:
    print("You are a child!")