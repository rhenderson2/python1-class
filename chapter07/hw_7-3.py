# homework assignment section 7-3
multiple_ten = input("Please tell me a number: ")
multiple_ten = int(multiple_ten)
if multiple_ten % 10 == 0:
    print(f"{multiple_ten} is a multiple of 10.")
else:
    print(f"{multiple_ten} is mot a multiple of 10.")