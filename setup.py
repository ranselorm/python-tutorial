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

# Dictionary example
dict_example = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary example:", dict_example)
print("Keys in dictionary:", dict_example.keys())
print("Values in dictionary:", dict_example.values())
dict_example['age'] = 31  # Modifying a value in the dictionary
print("Dictionary after modification:", dict_example)


# Looping through a list
for item in list_example:
    print("List item:", item)

# Looping through a dictionary
for key, value in dict_example.items():
    print(f"Key: {key}, Value: {value}")

# Slicing examples
print("Sliced tuple (first 3 elements):", tuple_example[:3])
print("Sliced list (last 2 elements):", list_example[-2:])



# Exercise: Create a list and perform various operations
numbers = range(1, 11)  # Create a range of numbers from 1 to 10
print("Numbers from 1 to 10:", list(numbers))
num_list = list(numbers)  # Convert range to list

new_list = num_list[7:0:-2]  # Slice the list from index 7 to 0 with a step of -2
print("Sliced list (from index 7 to 0 with step -2):", new_list)