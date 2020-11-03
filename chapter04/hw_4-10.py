# homework assignment section 4-10
long_noses = ["anteater", "toucan", "elephant", "elephant shrew", "tapir", "rhinoceros"]
for long_nose in long_noses:
    print(long_nose)
for long_nose in long_noses:
    print(f"A {long_nose} has a long nose.")
print(f"\nAll of these animals have a long nose!")
print(f"\nThe first three items in the list are:\n{long_noses[:3]}.")
print(f"\nThree items from the middle of the list are:\n{long_noses[1:4]}")
print(f"\nThe last three items in the list are:\n{long_noses[3:]}.")