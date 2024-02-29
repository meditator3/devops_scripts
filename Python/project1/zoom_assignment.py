# write a dictionary named "user" which has
# keys: name, active, admin
# whihc can be false or true(active, admin)
# depending on the values, it prints:
# (ADMIN) followed by user name if user is the admin
# ACTIVE - followed by user name if indeed is active
# ACTIVE - (ADMIN) followed by user name if both are true
# print user name if all is false

user = {}
user["name"] = 'somebody'
user["admin"] = False
user["active"] = False

if user["admin"] and not user["active"]:
    print(f"(ADMIN) - {user['name']}")
elif user["active"] and not user["admin"]:
    print(f"ACTIVE - {user['name']}")
elif user["admin"] and user["active"]:
    print(f"ACTIVE- (ADMIN) {user['name']}")
else:
    print(user["name"])


