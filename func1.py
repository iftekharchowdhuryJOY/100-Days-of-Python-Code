users = [
    (0, "Bob", "password"),
(1, "adam", "12password"),
(2, "adm", "pa23e43ssword"),
]


username_mapping = {user[1]: user for user in users}
print(username_mapping['Bob'])
# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")
#
# _, username, password = username_mapping[username_input]
#
#
# if password_input == password:
#     print ("your details are correct")
#
# else:
#     print("your details are not")