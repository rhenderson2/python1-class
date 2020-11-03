# homework assignment section 5-10
current_users = ['rick', 'bob', 'bill', 'scott', 'joe']
new_users = ['George', 'Travis', 'Bill', 'BOB', 'Mary']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry {new_user},\n\tyou will need to use"
             " a different\n\tusername as that username\n\t"
          "has already been taken.")
    else:
        print(f"{new_user}, \n\tThat username is available.")