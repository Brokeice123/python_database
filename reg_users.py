from main import User

try:
    user_name = input("Enter Name \n")
    user_email = input("Enter Email \n")
    user_password = input("Enter Password \n")

    User.create(name=user_name, email=user_email, password=user_password)
    print("User Created Successfully")


except:
    print("Failed to create user, Use a different email")
