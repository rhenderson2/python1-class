# homework assignment section 8-4
def make_shirt(size= 'Large', text= 'I love Python.'):
    print(f"You have ordered a {size} shirt with a"
          f" message that reads: \n\t'{text}'")
make_shirt()
print("\n")
make_shirt(size= 'Medium')
print("\n")
make_shirt(size= 'Small', text= 'Different Message')
