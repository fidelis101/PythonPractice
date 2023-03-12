import random

print("Hello World")
integer = 10
example_int = 2
example_string = "Test"

print(example_int)

name = input("What is your name? ")
package = input("What package do you want? A will ask for type, B will not")


def pick_random_num():
    test_int = random.randint(0, 10)
    return test_int


if package == "A":
    type_str = "Static"
elif package == "B":
    type_str = input("What type do you prefer")
else:
    type_str = "undefined"

rand_num = pick_random_num()

print("Base on the Package you selected, your type is "+type_str+" and your Random number is "+str(rand_num))
