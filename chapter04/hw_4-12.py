# homework assignment section 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods.append("chocolate")
print(f"My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print(f"\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)
