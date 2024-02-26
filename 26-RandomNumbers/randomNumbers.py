import random # random module

x = random.randint(1, 6)
print(x)

y = random.random()
print(y)
print("===================")

my_list = ["rock", "paper", "scissors"]
z = random.choice(my_list)
print(z)
print("===================")

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(card)
print(card)