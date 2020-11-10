# homework assignment section 6-10
favorite_numbers = {'John': [7, 3, 5],
                    'Mike': [4, 7],
                    'John L': 2,
                    'Niki': [8, 5, 6],
                    'Mary': 4}
for key,value in favorite_numbers.items():
    print(f"\nName: {key}")
    print(f"Favorite Number(s): {value}")