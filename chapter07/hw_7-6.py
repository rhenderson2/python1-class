# homework assignment section 7-6

prompt = "Please enter the age of the guest."
prompt += "\nEnter '0' when all guest ages have bee inputed: "
movie_age = ""
while movie_age != "0":
    movie_age = input(prompt)
    movie_age = int(movie_age)
    if movie_age == 0:
        break
    elif movie_age < 3:
        print("This ticket is free.")
    elif movie_age < 13:
        print("This ticket is $10.")
    elif movie_age >= 12:
        print("This ticket is $15.")