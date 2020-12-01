# homework assignment section 9-14
from random import choice
lottery = ('A', 'D', 'G', 'I', 'Z', 3, 18, 9, 26, 58, 72, 41, 7, 42, 98)

print(f"Any ticket with the following numbers and letters will win a prize.")
st1 = choice(lottery)
st2 = choice(lottery)
st3 = choice(lottery)
st4 = choice(lottery)
print(st1, st2, st3, st4)

