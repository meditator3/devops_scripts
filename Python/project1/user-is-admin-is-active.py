# create dict of user with key pairs admin- boolean, active-boolean, and name of user
# print (ADMIN) and foolwed by user name
#print (ACTIVE) and foolwed by user name
# print (ADMIN - ACTIVE) foolwed by user name
# print only user if not admin and not active


user = {'admin': True, 'active': True, 'name': 'ariel'}

if user['admin']:

    if user['active']:
        print(f"ACTIVE - (ADMIN): {user['name']}")
    else:
        print(f"ADMIN :{user['name']}  ")
else:
    if user['active']:
        print(f"ACTIVE : {user['name']}")
    else:
        print(user['name'])

