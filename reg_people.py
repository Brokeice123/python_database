from main import People

try:
    people_name = input("Enter your name \n")
    people_phone_number = input("Enter your phonenumber \n")
    people_email = input("Enter your email \n")
    people_country = input("Enter your country \n")
    people_gender = input("Enter your gender \n")
    people_religion = input("Enter your religion \n")
    people_password = input("Enter your password \n")

    People.create(name=people_name, phone_number=people_phone_number, email=people_email, country=people_country,
                  gender=people_gender, religion=people_religion, password=people_password)
    print("Registration successful")

except:
    print("Registration failed. Try using a different email")
