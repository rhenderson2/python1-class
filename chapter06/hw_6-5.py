# homework assignment section 6-5
rivers = {
    'mississippi': 'united states',
    'amazon': 'peru',
    'huang he': 'china',
    }
exception = ['united states']
for river, name in rivers.items():
    if name in exception:
        print(f"\nThe {river.title()} runs through the {name.title()}.")
    else:
        print(f"\nThe {river.title()} runs through {name.title()}.")
print("\nRivers:")
for river, name in rivers.items():
    print(f"\t{river.title()}")
print("\nCountries:")
for river, name in rivers.items():
    print(f"\t{name.title()}")