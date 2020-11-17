# homework assignment section 7-4
prompt = "Please tell me what topping you would like on your pizza."
prompt += "\nEnter 'q' for quit when you are done: "
while True:
    pizza_toppings = input(prompt)
    if pizza_toppings == 'q':
        break
    else:
        print(f"We are adding {pizza_toppings} to your pizza.")

