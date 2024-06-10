import random
# Make sure each name is separeted by a comma to avoid confusion 

names_string = input(f"Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# Longer Method for the code

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to pay for the meal today.")

# Shoter way to write the code

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to pay for the meal today.")
