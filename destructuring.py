people = [("Bob", 42, "Mechanic"),("James", 24, "Artist"),("harry", 32, "Lecturer")]
print(type(people))

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
