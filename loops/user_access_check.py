usernames = ["admin", "guest", "root", "user123"]

for user in usernames:
    if user == "admin" or user == "root":
        print(user, "- High privilege account")
    else:
        print(user, "- Standard account")
