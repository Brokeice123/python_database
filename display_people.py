from main import People

our_people = People.select()
for people in our_people:
    print(people.name, people.phone_number, people.email, people.country, people.gender, people.religion,
          people.password)
