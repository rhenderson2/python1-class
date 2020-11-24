# homework assignment section 8-5
def describe_city(city, country= 'US'):
    if country == "US":
        print(f"{city.title()} is in the {country.title()}.")
    else:
        print(f"{city.title()} is in {country.title()}.")
describe_city("nashvill")
print("\n")
describe_city('columbus')
print("\n")
describe_city('london', 'england')