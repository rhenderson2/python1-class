# homework assignment section 6-12
# I modified assignment 6-7 to family
# and used a dictionary in a dictionary to provide
# more key terms, better formatting and sequence number.
family =    {'1. wife': {'first_name': 'niki', 'last_name': 'henderson', 'city': 'fort wayne'},
            '2. child_1': {'first_name': 'carrissa', 'last_name': 'griffith', 'city': 'london'},
            '3. child_2': {'first_name': 'ailsa', 'last_name': 'henderson', 'city': 'fort wayne'},
            '4. child_3': {'first_name': 'jaida', 'last_name': 'henderson', 'city': 'fort wayne'},
            '5. child_4': {'first_name': 'ayin', 'last_name': 'henderson', 'city': 'fort wayne'},
            '6. child_5': {'first_name': 'tymon', 'last_name': 'henderson', 'city': 'fort wayne'},
            '7. child_6': {'first_name': 'skylar', 'last_name': 'henderson', 'city': 'fort wayne'},
            '8. child_7': {'first_name': 'ayriana', 'last_name': 'henderson', 'city': 'fort wayne'},
            }

for person, facts in family.items():
    full_name = f"{facts['first_name']} {facts['last_name']}"
    location = facts['city']

    print(f"\n{person.title()}: {full_name.title()}")
    print(f'\t{location.title()}')