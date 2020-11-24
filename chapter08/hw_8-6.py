# homework assignment section 8-6
def city_country(city, country= 'US'):
    full_city_country = f'"{city}, {country}."'
    return full_city_country.title()

city01 = city_country("nashvill")
print(city01)
city02 = city_country('columbus')
print(city02)
city03 = city_country('london', 'england')
print(city03)