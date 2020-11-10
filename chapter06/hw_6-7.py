# homework assignment section 6-7
friend = {'first_name': 'john', 'last_name': 'wendler', 'city': 'colorado springs'}
wife = {'first_name': 'niki', 'last_name': 'henderson', 'city': 'fort wayne'}
child = {'first_name': 'carrissa', 'last_name': 'griffith', 'city': 'london'}

people = [friend, wife, child]

for person in people:
    print('\n')
    for key,value in person.items():
        print(f"{value.title()}")


