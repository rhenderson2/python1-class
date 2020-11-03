# homework assignment section 5-2
print("Tests for equality and inequality with strings\n")
user = 'Bob'
if user == 'Bob':
    print(True)
user = 'Rick'
if user != 'Bob':
    print(False)
print("\nTests using the lower() method\n")
person = 'Bob'
if person.lower() == "bob":
    print(True)
person = 'Rick'
if person.lower() != 'bob':
    print(False)
print("\nNumerical tests involving equality"
      "and inequality,\ngreater than and "
      "less than, greater than or equal to,\n"
      "and less than or equal to\n")
print("set_one")
user = 21
if user == 21:
    print(True)
user = 19
if user != 21:
    print(False)
print("\nset two")
user = 21
if user >= 21:
    print(True)
user = 19
if user <= 21:
    print(False)
print("\nset three")
user = 22
if user > 21:
    print(True)
user = 19
if user < 21:
    print(False)
print("\nTests using the 'and' keyword and the 'or' keyword")
user_1 = 21
user_2 = 19
if user_1 >= 21 or user_2 >= 21:
    print(True)
else:
    print(False)
user_1 = 21
user_2 = 19
if user_1 < 21 and user_2 < 21:
    print(True)
else:
    print(False)
print("\nTest whether an item is in a list\n"
      "or not in a list\n")
primary_colors = ['red', 'blue', 'yellow']
print('red' in primary_colors)
print('green' in primary_colors)

