import random

x = random.randint(1, 6)  # random ints
y = random.random()  # random float between 0 and 1

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)  # chooses a random choice in a list

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)  # shuffles a list

print(cards)
print(x)
print(y)
print(z)
