# homework assignment section 7-2
dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print(f"I am sorry, you will need to wait for a table.")
else:
    print("Your table is ready.")
