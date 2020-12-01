# homework assignment section 9-15
from random import choice
lottery = ('A', 'D', 'G', 'I', 'Z', 3, 18, 9, 26, 58, 72, 41, 7, 42, 98)
my_ticket = ['A', 'I', '18', 'Z']
winning = {'st1':'A', 'st2':'I', 'st3':'18', 'st4':'Z'}
current_number = 0
while my_ticket != winning:
    st1 = choice(lottery)
    st2 = choice(lottery)
    st3 = choice(lottery)
    st4 = choice(lottery)
    current_number += 1
    continue

print(f"It took {current_number} times to get this winning ticket.")
print(st1, st2, st3, st4)

