# homework assignment section 3-7
guest_list = ["Abraham Lincoln", "President Trump", "C.S.Lewis"]
guest_list[1] = "Andrew Wommack"
print(f"Hello {guest_list[0]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[1]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[-1]},\nYou are still invited to dinner at my house.\n")
print(f"{guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, I just found a bigger table for our dinner.\n")
guest_list.insert(0, 'John F Kennedy')
guest_list.insert(2, 'Jack Welch')
guest_list.append('Duane Sherrif')
print(f"Hello {guest_list[0]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[1]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[2]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[3]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[4]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[5]},\nYou are invited to dinner at my house.\n")
print(f"Uh Oh, My new dinner table won't arrive in time for our dinner\nand now I can only invite two guests.\n")
popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list},\nI can no longer invite you the the dinner since\nmy table will not arrive in time.\n")
popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list},\nI can no longer invite you the the dinner since\nmy table will not arrive in time.\n")
popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list},\nI can no longer invite you the the dinner since\nmy table will not arrive in time.\n")
popped_guest_list = guest_list.pop()
print(f"Sorry {popped_guest_list},\nI can no longer invite you the the dinner since\nmy table will not arrive in time.\n")
print(f"Hello {guest_list[0]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[1]},\nYou are still invited to dinner at my house.\n")
del guest_list[0]
del guest_list[1]
print(guest_list)

