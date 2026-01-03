double_value = lambda num: num * 2
print("Double of 5 is:", double_value(5))

# Function to calculate the hypotenuse of a right triangle

random_list  = [('Anna', 40, 6), ('Erica', 32, 12), ('Rita', 18, 3), ('John', 25, 4)] 

sorted_list_by_name = sorted(random_list)
sorted_list_by_age = sorted(random_list, key = lambda user_tuple: user_tuple[1])
sorted_list_by_r = sorted(random_list, key = lambda user_tuple: user_tuple[2])

print("Sorted list by name:", sorted_list_by_name)
print("Sorted list by age:", sorted_list_by_age)
print("Sorted list by r:", sorted_list_by_r)