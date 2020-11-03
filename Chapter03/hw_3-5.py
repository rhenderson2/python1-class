# homework assignment section 3-5
guest_list = ["Abraham Lincoln", "President Trump", "C.S.Lewis"]
print(f"Hello {guest_list[0]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[1]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[-1]},\nYou are invited to dinner at my house.")
print(f"\n{guest_list[1]} said he can't make it.\n")
guest_list[1] = "Andrew Wommack"
print(f"Hello {guest_list[0]},\nYou are still invited to dinner at my house.\n")
print(f"Hello {guest_list[1]},\nYou are invited to dinner at my house.\n")
print(f"Hello {guest_list[-1]},\nYou are still invited to dinner at my house.")