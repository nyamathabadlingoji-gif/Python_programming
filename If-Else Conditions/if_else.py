# example of checking if a list is empty

users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


# example of checking for unique usernames
current_users = ["admin", "john", "eric", "sarah", "david"]

new_users = ["John", "Emma", "DAVID", "alex", "mary"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

# Check each new username
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"'{user}' is already taken. Please enter a new username.")
    else:
        print(f"'{user}' is available.")

# example of ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")