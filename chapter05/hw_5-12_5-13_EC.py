# homework assignment section 5-12, 5-13 / EC
# Reviewed coding a lot during course of assignments.
# Doing Extra Credit from email in lieu of 5-13 below.
print("*** Prime numbers from 1 - 100. ***\n")

temporary_list = []
current_number = 1
key = 1
while current_number < 100:
    current_number += 1
    if current_number % key == 0:
        temporary_list.append(current_number)
        key += 1
        continue

        print(set(temporary_list))







