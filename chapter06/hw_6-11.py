# homework assignment section 6-11
cities = {'london': {'country': 'england',
                     'population': '9 million',
                     'fun fact': 'Over 300 languages are spoken here.'
                     },
          'new york': {'country': 'united states',
                        'population': '8.4 million',
                        'fun fact': 'The oldest building dates to about 1642.'
                        },
           'chicago': {'country': 'united states',
                        'population': '2.7 million',
                        'fun fact': 'Spray paint was invented here.'
                        }}
for city,facts in cities.items():
    print(f"\n{city.title()}")
    for key,value in facts.items():
        print(f"\t{key.title()}: {value.title()}")

