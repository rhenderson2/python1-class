# homework assignment section 6-6
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
take_poll = ['ted', 'jen', 'bill', 'bob', 'mary', 'sarah']

for name in take_poll:
 if name in favorite_languages.keys():
   print(f"\nThanks {name.title()}, I see you took my poll!")
 else:
  print(f"\nHello {name.title()}, Can you please take my poll?")



