# homework assignment section 5-9
usernames = []
if usernames:
    for username in usernames:
        if username == 'Admin':
            print("Hellow Admin,"
             " would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging"
              f" in again.")
else:
    print("We need to get some more users!")



