# homework assignment section 3-10
mountains = ["Yale", "Princeton", "Harvard", "Oxford", "Evans"]
print(mountains)
print(mountains[-1])
print(mountains[0])
message = f"{mountains[0]} is the first mountain in my list\nof mountains in Colorado."
print(message)
mountains[0] = "Ebert"
print(mountains)
mountains.append("Yale")
print(mountains)
mountains = []
mountains.append("Yale")
mountains.append("Ebert")
mountains.append("Princeton")
mountains.append("Harvard")
print(mountains)
del mountains[0]
print(mountains)
del mountains[1]
print(mountains)
mountains = ["Yale", "Princeton", "Harvard", "Oxford", "Evans"]
print(mountains)
print(mountains.pop())
print(mountains)
pop_second = mountains.pop(1)
print(f"The second item in the list,\n{pop_second}, I just removed from the list.")
print(mountains)
test = "Harvard"
mountains.remove("Harvard")
print(mountains)
print(f"I removed {test} as a test case.")
mountains = ["Yale", "Princeton", "Harvard", "Oxford", "Evans"]
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
mountains = ["Yale", "Princeton", "Harvard", "Oxford", "Evans"]
print("\nOriginal list:")
print(mountains)
print("\nsorted list:")
print(sorted(mountains))
print("\nOriginal list again:")
print(mountains)
print("\nreverse sorted list:")
print(sorted(mountains,reverse=True))
print("\nOriginal list again, again:")
print(mountains)
mountains.reverse()
print("\nreverse sorted list using reverse method:")
print(mountains)
print(len(mountains))

