# homework assignment section 4-11
pizzas = ["sausage", "chicken", "hawaiian"]
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"\nI love {pizza} pizza.")
print(f"\nI love all of these pizzas!")
friend_pizzas = pizzas[:]
pizzas.append("cheese")
friend_pizzas.append("anchovie")
print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print(f"\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
