# homework assignment section 6-9
favorite_places = {
 'bob': ['london', 'boston', 'new york'],
 'sarah': ['san antonio', 'new york'],
 'joe': ['switzerland', 'woodland park', 'chicago']
  }

for name, places in favorite_places.items():
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
                print(f"\t{place.title()}")