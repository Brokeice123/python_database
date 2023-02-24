from main import User

our_users = User.select()
for user in our_users:
    print(user.name, user.email, user.password)