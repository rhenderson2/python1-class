# homework assignment section 7-9
sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'egg salad', 'pastrami']
finished_sandwiches = []
print('We have run out of pastrami for the day.\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())