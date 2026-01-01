import math

# Function to greet the user
# def greeting(name):
#     print(f"Hello, {name}, have a nice day!")
    
# user_name = str(input("Enter your name: "))
# if user_name:
#     greeting(user_name)
# else:
#     print("No name provided.")  

# Function to calculate the hypotenuse of a right triangle
# def two_numbers(height, width):
#     return (height ** 2 + width ** 2) ** 0.5
  

# numbers = int(input("Enter first number: ")), int(input("Enter second number: "))
# result = int(two_numbers(*numbers))
# print(f"The hypotenuse of the right triangle with sides {numbers} is: {result}")


# Containers (tuples, lists, dictionaries)
tuple_example = (1, 2, 3, 4, 5, 'hello')
list_example = [10, 20, 30, 40, 50]

print("Tuple example:", tuple_example)
print("List example:", list_example)

print("Length of tuple:", len(tuple_example))
print("Length of list:", len(list_example))

# tuple_example.append(20)  # This will raise an AttributeError since tuples are immutable
list_example.append(60)   # This will work since lists are mutable

# Set example
set_example = {1, 2, 3, 4, 5}
set_example.add(6)  # Adding an element to the set
print("Set example after adding an element:", set_example)
set_example.remove(3)  # Removing an element from the set
print("Set example after removing an element:", set_example)

print(list(set_example))

