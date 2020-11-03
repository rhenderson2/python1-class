# homework assignment section 5-8
usernames = ['Rick', 'Bob', 'Bill', 'Admin', 'Joe']
for username in usernames:
    if username == 'Admin':
       print("Hellow Admin,"
             " would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging"
              f" in again.")

