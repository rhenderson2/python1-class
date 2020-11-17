# homework assignment section 7-10
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could go one place in the world,"
                     " where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"If {name.title()} could go anywhere in the world, {name.title()}"
          f" would like to go to {response.title()}.")