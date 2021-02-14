'''
a = 32476
b = 74823
if a > b:
    print("A is greater than B")
elif a == b:
    print("A is equal with B")
else:
    print("A is smaller dan B")
'''

username = "razorgaming"
password = "RzRg3g3"
'''
if username == "razorgaming" and password == "RzRg3g3":
    print("Login Success")
else:
    print("Try Again")
'''
if username == "razorgaming" and password == "RzRg3g3":
    print("Login Success")
elif not username == "razorgaming":
    print("Wrong username, try again")
elif not password == "RzRg3g3":
    print("Wrong password, try again")
else:
    print("Wrong input, try again")