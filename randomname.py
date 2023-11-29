import random
input_names = input("Enter the name: ")
names = input_names.split(",")

names_list_len = len(names)

random_value = random.randint(0,names_list_len)

print(f"{names[random_value]} is going to buy the meal today!")

# print(names)
# print(random_value)
